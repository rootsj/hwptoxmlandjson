import struct

def GetDword(buf, off):
    return struct.unpack('<L', buf[off:off+4])[0]


fp = open('static/00n-S190106-example.hwp', 'rb')
buf = fp.read()
fp.close()

if buf[0:4] == b'\xd0\xcf\x11\xe0':
    print('OLE')
else:
    print('no ole')

# BBD
num_bbd = GetDword(buf, 0x2C)

bbd = ''
for i in range(num_bbd):
    block_no = GetDword(buf, 0x4c + (i*4))
    print(hex(block_no))
    off = (block_no + 1) * 0x200
    # off = (block_no + 1) << 9
    # print(off)
    # bbd += buf[off:off+0x200].decode('utf-8')

# print(bbd)