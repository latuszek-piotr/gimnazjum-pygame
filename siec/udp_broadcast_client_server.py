import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.settimeout(0.1)
MAX = 65535
PORT = 50004
if len(sys.argv) == 2 and sys.argv[1] == 'server':
    s.bind(('', PORT))
    print 'Listening for broadcasts at', s.getsockname()
    while True:
        data, address = s.recvfrom(MAX)
        print 'The client at %r says: %r' % (address, data)
        s.sendto('Hi, here is server! Answer to: {} time is: {}'.format(str(address), repr(time.time())), address)

elif len(sys.argv) == 2 and sys.argv[1] == 'client':
    s.sendto('Broadcast message ---! time is: {}'.format(repr(time.time())), ('<broadcast>', PORT))
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
