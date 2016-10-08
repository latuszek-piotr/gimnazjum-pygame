import socket
import sys
import time
import subprocess
import ipaddress

MAX = 65535
PORT = 50004

def get_host_ip():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1.connect(('10.255.255.255', 0))
    ip_string = s1.getsockname()[0]
    print 'HOST IP addr == ', ip_string
    s1.close()
    return ip_string

def get_mask(ip_string):
    proc = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
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


def get_broadcast_ip(ip_string, mask_string):
    """Broadcast IP is IP bitwise ORed with Bit-negated mask"""
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

host_ip = get_host_ip()
# ip_mask = get_mask(host_ip)
h_ip = ipaddress.IPv4Interface(socket.inet_aton(host_ip))
print h_ip
ip_mask = h_ip.network.hostmask
# broadcast_ip = get_broadcast_ip(host_ip, ip_mask)
broadcast_ip = h_ip.network.broadcast_address

print "HOST IP      = %s" % host_ip
print "IP MASK      = %s" % ip_mask
print "BROADCAST IP = %s" % broadcast_ip

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

if len(sys.argv) == 2 and sys.argv[1] == 'server':
    s.bind(('', PORT))
    print 'Listening for broadcasts at', s.getsockname()
    while True:
        data, address = s.recvfrom(MAX)
        print 'The client at %r says: %r' % (address, data)
        s.sendto('Hi, here is server! Answer to: {} time is: {}'.format(str(address), repr(time.time())), address)

elif len(sys.argv) == 2 and sys.argv[1] == 'client':
    s.settimeout(0.1)
    s.sendto('Broadcast message ---! time is: {}'.format(repr(time.time())), (broadcast_ip, PORT))
    try:
        data, address = s.recvfrom(MAX)
        print 'The server at %r says: %r' % (address, data)
    except socket.timeout:
        pass
    try:
        data, address = s.recvfrom(MAX)
        print 'The server at %r says: %r' % (address, data)
    except socket.timeout:
        pass
