import struct
import io
import olefile

import zlib

# with open('static/00n-S190106-example.hwp', 'rb') as fp:
#     buf = fp.read()
#     # test = io.BytesIO(fp.read())

# print(buf)

with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/00n-S190106-example.hwp') as ole:
    test = ole.openstream('BodyText/Section0')
    data = test.read()

# wbits = zlib.MAX_WBITS

# zlib_compress = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS)

# text = '''test'''

# zlib_data = zlib_compress.compress(text) + zlib_compress.flush()


# zlib.decompress(zlib_data)
# zlib.decompress(data)
# zlib.decompress(str(data, 'ascii'), zlib.MAX_WBITS|32)
# 'test'


#  zlib.decompress(zlib_data, zlib.MAX_WBITS|32)
# 'test'

output = zlib.decompress(data, -15)
# print(output)
print(output.decode("cp949"))

