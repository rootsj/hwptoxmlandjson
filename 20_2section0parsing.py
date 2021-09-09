import struct

def GetDword(buf, off):
    return struct.unpack('<L', buf[off:off+4])[0]


with open('static/00n-S190106-example.hwp', 'rb') as fp:
    buf = fp.read()


# BBD (Big Block Depot)
num_bbd = GetDword(buf, 0x2C)

bbd = b''
for i in range(num_bbd):
    block_no = GetDword(buf, 0x4c + (i*4))
    off = (block_no + 1) << 9
    bbd += buf[off:off+0x200]


start_root = GetDword(buf, 0x30)
i = start_root

root = b''
while True:
    if i == 0xfffffffe:
        break
    off = (i+1) << 9
    root += buf[off:off+0x200]
    i = GetDword(bbd, i*4)


# SBD(Smal Block)
sbd_block = GetDword(buf, 0x40)
start_sbd = GetDword(buf, 0x3c)

i = start_sbd

sbd = b''
while True:
    if i == 0xfffffffe:
        break
    off = (i+1) << 9
    sbd += buf[off:off+0x200]
    i = GetDword(bbd, i*4)

num_pps = int(len(root) / 0x80)

def GetWord(buf, off):
    return struct.unpack('<H', buf[off:off+2])[0]

for i in range(num_pps):
    off = i * 0x80
    ppsl = root[off:off+0x80]

    size_name = GetWord(ppsl, 0x40)

    name = ppsl[0:size_name-2:2]
    if name[0] == 0:
        break
    
    if name == b'Section0':
        start_sec = GetDword(root, off + 0x74)


print(start_sec)

# section0 = b''
# while True:
#     if start_sec == 0xfffffffe:
#         break
#     off = (start_sec+1) << 9
#     print(off)
#     section0 += buf[off:off+0x200]
#     start_sec = GetDword(bbd, start_sec*4)

# print(section0)

section0 = b''
while True:
    if start_sec == 0xfffffffe:
        break
    off = (start_sec+1) << 9
    print(off)
    section0 += buf[off:off+0x40]
    start_sec = GetDword(sbd, start_sec*4)

print(section0)