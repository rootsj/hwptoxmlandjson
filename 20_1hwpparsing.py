import struct

def GetDword(buf, off):
    return struct.unpack('<L', buf[off:off+4])[0]


with open('static/00n-S190106-example.hwp', 'rb') as fp:
    buf = fp.read()


# if buf[0:4] == b'\xd0\xcf\x11\xe0': #OLE File 구분하는 용도, 모두 동일
#     print('OLE')
# else:
#     print('no ole')



# BBD (Big Block Depot)
num_bbd = GetDword(buf, 0x2C)
# Big Block Depot을 구성하는 블럭의 개수
# print(hex(num_bbd))


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

# bbd 파일로 저장
# with open('bbd.dmp', 'wb') as fp:
#     fp.write(bbd)


#root entry #Start block of property, 스토리지와 스트림의 구조의 정보를 담고 있는 프로퍼티 영역.
start_root = GetDword(buf, 0x30)
# print(hex(start_root))

i = start_root

root = b''
while True:
    if i == 0xfffffffe:
        break
    print(hex(i))
    off = (i+1) << 9
    root += buf[off:off+0x200]
    i = GetDword(bbd, i*4)

# print(root)

with open('root.dmp', 'wb') as fp:
    fp.write(root)


# SBD(Smal Block)
# 크기 - 64byte(0x40)
# sbd_startblock - 0x3c
# num_of_sbd_blocks 0x40
sbd_block = GetDword(buf, 0x40)
print('sbd_blocks = ' + hex(sbd_block) + '개')
start_sbd = GetDword(buf, 0x3c)
print('start_sbd = ' + hex(start_sbd) + '번')
# bbd의 7번 블럭을 보면 링크 정보가 있다.

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


# PPS (property storage)
num_pps = int(len(root) / 0x80)
# 전체 길이에서 8줄마다 파일이 있으니 체크

# 2바이트 체크
def GetWord(buf, off):
    return struct.unpack('<H', buf[off:off+2])[0]

for i in range(num_pps):
    off = i * 0x80
    ppsl = root[off:off+0x80]

    size_name = GetWord(ppsl, 0x40)

    name = ppsl[0:size_name-2:2]
    if name[0] == 0:
        break

    if ppsl[0x42] == 5:
        pps_type = 'ROOT'
    elif ppsl[0x42] == 1:
        pps_type = 'Storage'
    elif ppsl[0x42] == 2:
        pps_type = 'Stream'
    else:
        pps_type = 'Unknown'

    start = GetDword(ppsl, 0x74)
    size = GetDword(ppsl, 0x78)

    print('%s [%s] size- %d start - (%d)' %(name, pps_type, size, start))