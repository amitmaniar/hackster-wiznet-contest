import socket
import struct
import requests

from constants import *
from commons import *


# get Modbus Request command.
mb_req = mb_rtu_make_request( 1, 3, READ_OFFSET, READ_COUNT * 2)

# sock is connecting Wiznet. Here, Wiznet configured as TCP Server.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((WIZNET_HOST, WIZNET_PORT))
    sock.send(mb_req)

    # Look for the response
    amount_received = 0
    amount_expected = (READ_COUNT * 4) + 5

    final_string = ''
    while amount_received < amount_expected:
        data = sock.recv(16)
        final_string = final_string + data
        amount_received += len(data)
    # print 'received', len(final_string), ' bytes'
    # print [elem.encode("hex") for elem in final_string]
    patam_dict = {}
    for param in range(0, READ_COUNT):
        start_char = (param *4) + 3
        byte_str = final_string[start_char+2:start_char+4] + final_string[start_char:start_char+2]
        val = struct.unpack('>f', byte_str)[0]
        patam_dict[str(param+1)] = val
        data = 'reading,key='+str(param+1)+' value=' + str(val)
        res = requests.post(url=TELEGRAF_URL, data=data, headers={'Content-Type': 'application/octet-stream'})
    print 'Posted:', patam_dict
finally:
    sock.close()