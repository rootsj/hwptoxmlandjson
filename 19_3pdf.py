import struct
import io

import ole
import zlib

with open('static/00n-S190106-example.pdf', 'rb') as fp:
    buf = fp.read()
    test = io.BytesIO(fp.read())
    test2 = ole.Read(fp, -1)

# buf = zlib.decompress(buf)
# print(buf)

print(test2)

# print(test)
# print(test.getbuffer())

# with open('C:/Users/rootsj/Desktop/hiconsy/static/pdf2text.txt', 'wb') as f:
#     f.write(buf)

# with open('C:/Users/rootsj/Desktop/hiconsy/static/pdf2text.pdf', 'wb') as f:
#     f.write(buf)