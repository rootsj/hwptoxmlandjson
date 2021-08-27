import olefile

import zlib

with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/00n-S190106-example.hwp') as ole:
    test = ole.openstream('BodyText/Section0')

    print(test.read())
    # data = test.read()
    # tempd = data[22:69]
    # print(type(tempd))
    # print(tempd)


    # dec = zlib.decompressobj(32 + zlib.MAX_WBITS)  # offset 32 to skip the header
    # for chunk in stream:
    #     rv = dec.decompress(chunk)
    #     if rv:
    #         yield rv