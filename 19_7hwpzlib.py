from binascii import hexlify
from logging import StreamHandler
from os import strerror # hex를 string으로 표혅
from struct import unpack

import codecs
import zlib

fname = 'static\\test1.hwp'

magicid = '' # Magic ID
num_BBAT_depot = '' # Number of BBAT Depot
startblock_property = '' # Start block of Property
startblock_SBAT = '' # Start block of SBAT
num_SBAT_depot = '' # Number of Small Block Allocation Table Depot
array_BBAT_depot_members = '' # Array of BBAT Depot members

def bin2hex(fp, offset, size):
    fp.seek(offset)
    buf = fp.read(size)
    return buf
    
def hex2int(buf):
    return unpack('I', buf)[0]

with open(fname, 'rb') as fp:
        
    header = bin2hex(fp, 20480, 22)
    stream1 = bin2hex(fp, 20502, 2729)
    #23231

    if __name__ == '__main__':
        print('header : ', header)
        print('id.decode("ISO-8859-1") : ', header.decode("ISO-8859-1"))
        # print(stream1)
        # print(stream1)
        # print(stream1.decode('utf-16le'))
        with open('stream1.dmp', 'wb') as fp:
            fp.write(stream1)

        # print(stream1.hex())
        output = zlib.decompress(stream1, -15) 
        # print(output)