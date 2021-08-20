import zipfile
import tempfile
import shutil
import os

with zipfile.ZipFile("static/testhwpx.hwpx") as doc:

    doclist = doc.infolist()

    newfile = []
    with tempfile.TemporaryDirectory() as tpd:
        print(os.listdir(tpd))
    # for i in doclist:
    #     data = doc.read(i.orig_filename).decode('utf-8')

    #     tp.write('data')
    #     newfile.append(tp)
    #     tp.close

        # newfile.append(data)

        # result = bytes(my_string, 'utf-8')

    # with zipfile.ZipFile("test_zip.zip", 'w') as my_zip:
    #     for i in newfile:
    #         my_zip.write(i)
    #     my_zip.close()
