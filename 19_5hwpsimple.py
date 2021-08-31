import struct

def GetDword(buf, off):
    return struct.unpack('<L', buf[off:off+4])[0]
    #'<L' 거꾸로 표현

with open('simple.hwp', 'rb') as fp:
    buf = fp.read()

print(buf[1025:1536])
# BBD
num_bbd = GetDword(buf, 0x2C)
print(num_bbd)

print(GetDword(buf, 0x200))
print(GetDword(buf, 0x201))
print(GetDword(buf, 0x202))
print(GetDword(buf, 0x60E))
# bbd = ''
# for i in range(num_bbd):
#     block_no = GetDword(buf, 0x4c + (i*4))
#     print(hex(block_no))
#     off = (block_no + 1) * 0x200
#     off = (block_no + 1) << 9
#     print(off)
#     bbd += buf[off:off+0x200].decode('utf-8')

# print(bbd)