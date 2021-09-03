from binascii import hexlify # hex를 string으로 표혅
from struct import unpack

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
    
def split2(string):
    ret = ''
    while string:
        ret += string[:2] + ' '
        string = string[2:]
    return ret.upper()
    
def hex2int(buf):
    return unpack('I', buf)[0]

with open(fname, 'rb') as fp:
        
    magicid = bin2hex(fp, 0, 8)
    num_BBAT_depot = hex2int(bin2hex(fp, 44, 4))
    startblock_property = hex2int(bin2hex(fp, 48, 4))
    startblock_SBAT = hex2int(bin2hex(fp, 60, 4))
    num_SBAT_depot = hex2int(bin2hex(fp, 64, 4))
    tmp = bin2hex(fp, 76, num_BBAT_depot * 4)
    array_BBAT_depot_members = unpack('I'*num_BBAT_depot, tmp)


    if __name__ == '__main__':
        print('hexlift(id) : ', hexlify(magicid))
        print('hexlift(id).hex() : ', hexlify(magicid).hex())
        print('type(hexlify(id) : ', type(hexlify(magicid)))
        print('bytearray.fromhex(hexlify(id).hex()).decode() : ', bytearray.fromhex(hexlify(magicid).hex()).decode())
        print('---------')
        print('id : ', magicid)
        print('id.hex() : ', magicid.hex())
        print('id.hex().encode("utf-8") : ', magicid.hex().encode('utf-8'))
        print('id.hex().encode("utf-16") : ', magicid.hex().encode('utf-16'))
        print('type(id) : ', type(magicid))
        print('---------')
        print('id.decode("ISO-8859-1") : ', magicid.decode("ISO-8859-1"))
        print('id.decode("utf-16") : ', magicid.decode("utf-16"))
        print('---------')


        # test = hexlify(magicid).hex()

        # import base64
        # data = base64.b16decode(test).decode('utf-16')
        # print(data)

        # print('Number of BBAT Depot : ', num_BBAT_depot)
        # print('Start block of Property : ', startblock_property)
        # print('Start block of SBAT : ', startblock_SBAT)
        # print('Number of SBAT Depot : ', num_SBAT_depot)
        # print('Array of BBAT Depot members : ', array_BBAT_depot_members)