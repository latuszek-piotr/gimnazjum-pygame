import socket
import sys
import time
import subprocess
import platform
import re


class CantFindIpMask(Exception): pass
class CantGetBroadcastIp(Exception): pass


def get_host_ip():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1.connect(('10.255.255.255', 0))
    ip_string = s1.getsockname()[0]
    print 'HOST IP addr == ', ip_string
    s1.close()
    return ip_string


def get_mask(ip_string):
    if platform.system() == 'Windows':
        return get_mask_from_ipconfig(ip_string)
    if platform.system() == 'Linux':
        return get_broadcast_ip_from_ip_addr(ip_string)
    return "255.255.255.0"


def get_broadcast_ip_from_ip_addr(ip_string):
    proc = subprocess.Popen(['ip', 'addr'], stdout=subprocess.PIPE)
    line = proc.stdout.readline()
    while line:
        line = proc.stdout.readline()
        # print line
        match = re.search(r"inet\s+(\S+)\s+brd\s+(\S+)", line)
        if match:
            ip_addr = match.group(1)
            broadcast_addr = match.group(2)
            # print ip_string, ip_addr, broadcast_addr
            if ip_string in ip_addr:
                return broadcast_addr
    return "255.255.255.0"


def get_mask_from_ipconfig(ip_string):
    proc = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:
            raise CantFindIpMask()
        ip_encoded = ip_string.encode()
        if ip_encoded in line:
            # print line, ip_encoded
            break
    next_line = proc.stdout.readline()
    # print next_line
    mask_str = next_line.rstrip().split(b':')[-1]
    mask = mask_str.replace(b' ',b'').decode()
    # print 'mask = %s' % mask
    return mask


def get_broadcast_ip(ip_string):
    if platform.system() == 'Windows':
        return get_broadcast_ip_from_ifconfig(ip_string)
    if platform.system() == 'Linux':
        return get_broadcast_ip_from_ip_addr(ip_string)
    parts = ip_string.split('.')
    parts[-1]='255'
    return ".".join(parts)


def get_broadcast_ip_from_ifconfig(ip_string):
    """Broadcast IP is IP bitwise ORed with Bit-negated mask"""
    try:
        mask_string = get_mask_from_ipconfig(ip_string)
    except CantFindIpMask:
        raise CantGetBroadcastIp
    mask_int_parts = [(~int(part) & 0xFF) for part in mask_string.split('.')]
    # print "inverted_mask %s" % mask_int_parts
    ip_int_parts = [(int(part) & 0xFF) for part in ip_string.split('.')]
    # print ip_int_parts
    # print zip(ip_int_parts, mask_int_parts)
    broadcast_str_parts = [str(ip|mask) for (ip,mask) in zip(ip_int_parts, mask_int_parts)]
    # print broadcast_str_parts
    broadcast_ip = '.'.join(broadcast_str_parts)
    # print broadcast_ip
    return broadcast_ip


class NetworkConnection(object):
    def __init__(self, port=50004, broadcast_ip=None, use_server=True):
        self.port = port
        self.max_buffsize = 65535
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.connection.settimeout(0.001)
        self.last_data = ''
        self.last_sender_address = None
        self.broadcast_ip = broadcast_ip
        self.broadcast_delay = 0.1
        self._last_broadcast_time = time.time()
        if use_server:
            self.start_server()
        self.start_client()

    def start_server(self):
        self.connection.bind(('', self.port))
        print 'Oczekuje na pozycje graczy pod adresem: {}'.format(self.connection.getsockname())

    def start_client(self):
        try:
            if self.broadcast_ip is None:
                host_ip = get_host_ip()
                self.broadcast_ip = get_broadcast_ip(host_ip)
            self.broadcast_address = (self.broadcast_ip, self.port)
            # print 'Rozglaszam swoja pozycje gracza na adres: {}'.format(str(self.broadcast_address))
        except CantGetBroadcastIp:
            print 'Brak sieci - gra sieciowa niemozliwa'
            self.broadcast_address = None

    def shutdown(self):
        self.connection.close()

    def receive(self):
        try:
            self.last_data, self.last_sender_address = self.connection.recvfrom(self.max_buffsize)
            # print 'Dostalem "%s" od: %s' % (self.last_data, self.last_sender_address)
            return self.last_data
        except socket.timeout:
            return None

    def send_to_last_sender(self, data):
        if self.last_sender_address is not None:
            # print 'Sending "%s" to: %s' % (data, self.last_sender_address)
            self.connection.sendto(data, self.last_sender_address)

    def broadcast(self, data):
        if self.broadcast_address is None:
            return
        now = time.time()
        delay_from_last_broadcast = now - self._last_broadcast_time
        if delay_from_last_broadcast > self.broadcast_delay:
            # print 'Sending "%s" to: %s' % (data, self.broadcast_address)
            self.connection.sendto(data, self.broadcast_address)
            self._last_broadcast_time = now


if __name__ == '__main__':
    broadcast_ip = None
    if len(sys.argv) == 3:
        broadcast_ip = sys.argv[2]

    if sys.argv[1] == 'client':
        net_connection = NetworkConnection(broadcast_ip=broadcast_ip, use_server=False)
    else:
        net_connection = NetworkConnection(broadcast_ip=broadcast_ip)

    if len(sys.argv) == 2 and sys.argv[1] == 'server':
        while True:
            data = net_connection.receive()
            if data:
                answer = 'Hi, here is server! My time is: {}'.format(repr(time.time()))
                net_connection.send_to_last_sender(data=answer)

    elif len(sys.argv) >= 2 and sys.argv[1] == 'client':
        msg = 'Broadcast message ---! time is: {}'.format(repr(time.time()))
        net_connection.broadcast(data=msg)
        net_connection.receive()
        net_connection.receive()
