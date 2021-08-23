from os import makedirs
import zipfile
import tempfile
import os, glob

def addFolderToZip(myZipFile,folder):
    for file in glob.glob(folder+"\\*"):
            if os.path.isfile(file):
                myZipFile.write(file, os.path.basename(file), compress_type=zipfile.ZIP_DEFLATED)
            elif os.path.isdir(file):
                for f in glob.glob(file+"\\*"):
                    if os.path.isfile(f):
                        myZipFile.write(f, os.path.basename(file) +'\\' + os.path.basename(f), compress_type=zipfile.ZIP_DEFLATED)


with zipfile.ZipFile("static/testhwpx.hwpx") as doc:

    doclist = doc.infolist()
    
    newfile = []
    with tempfile.TemporaryDirectory() as tempDir:
        # if os.path.exists(tempDir):
        # print(os.listdir(tempDir))

        for i in doclist:

            if i.orig_filename == 'Preview/PrvImage.png':
                data = doc.read(i.orig_filename)
            else:
                data = doc.read(i.orig_filename).decode('utf-8')


            if '/' in i.orig_filename:
                a = i.orig_filename.split('/')

                if not os.path.exists(tempDir + '\\' + a[0]):
                    makedirs(tempDir + '\\' + a[0])

                if i.orig_filename == 'Preview/PrvImage.png':
                    with open(tempDir + '\\'+'Preview\\PrvImage.png', 'wb') as f:
                        f.write(data) 
                else:
                    with open(tempDir+'\\'+i.orig_filename.replace('/','\\'),'w', encoding='utf-8') as temp:
                        temp.write(data)
            else:
                with open(tempDir+'\\'+i.orig_filename,'w', encoding='utf-8') as temp:
                        temp.write(data)

        with zipfile.ZipFile('test17.hwpx', 'w') as new_hwpx:
            addFolderToZip(new_hwpx, tempDir)