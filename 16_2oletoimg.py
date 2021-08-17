import olefile

import cv2

with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/test.hwp') as ole:

    for entry in ole.listdir():
        # print(entry[0])
        # print(ole.openstream(entry))

        if entry[0] == "PrvImage":
            prvimg = ole.openstream(entry)
            data = prvimg.read()

            with open('img.bmp', 'wb') as f:
                f.write(data)     
        # 이후 섬네일 이미지는 opencv로 진행하면 됨