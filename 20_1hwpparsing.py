import struct

def GetDword(buf, off):
    print(struct.unpack('<L', buf[off:off+4]))
    return struct.unpack('<L', buf[off:off+4])[0]


with open('static/00n-S190106-example.hwp', 'rb') as fp:
    buf = fp.read()


if buf[0:4] == b'\xd0\xcf\x11\xe0': #OLE File 구분하는 용도, 모두 동일
    print('OLE')
else:
    print('no ole')



# BBD (Big Block Depot)
num_bbd = GetDword(buf, 0x2C)
# Big Block Depot을 구성하는 블럭의 개수
print(hex(num_bbd))


bbd = b''
for i in range(num_bbd):
    block_no = GetDword(buf, 0x4c + (i*4))
    # print(hex(block_no))
    # 4c 이후에 block 의 위치 출력됨
    off = (block_no + 1) << 9
    # off = (block_no + 1) * 0x200 # 512
    # 1블럭당 512바이트 수 읽어 오기
    bbd += buf[off:off+0x200]

# print(bbd)

# 완성한 bbd 파일로 저장
# with open('bbd.dmp', 'wb') as fp:
#     fp.write(bbd)


'''
#root entry
start_root = GetDword(buf, 0x30)
# print(hex(start_root))

i = start_root

root = b''
while True:
    if i == 0xfffffffe:
        break
    # print(hex(i))
    off = (i+1) << 9
    root += buf[off:off+0x200]
    i = GetDword(bbd, i*4)

with open('root.dmp', 'wb') as fp:
    fp.write(root)


# SBD(Smal Block)
start_sbd = GetDword(buf, 0x3c)
# print(hex(start_sbd))

i = start_sbd

sbd = b''
while True:
    if i == 0xfffffffe:
        break
    # print(hex(i))
    off = (i+1) << 9
    sbd += buf[off:off+0x200]
    i = GetDword(bbd, i*4)

with open('sbd.dmp', 'wb') as fp:
    fp.write(sbd)
'''