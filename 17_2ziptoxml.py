import zipfile

doc = zipfile.ZipFile("static/testhwpx.hwpx")

# print(doc.infolist())
doclist = doc.infolist()

# for i in doclist:
    # print(i)
    # print(i.orig_filename)
    # print(i.orig_filename, i.date_time, i.filename, i.file_size, i.compress_size)

for i in doclist:
    # if i.orig_filename == 'META-INF/manifest.xml':
    #     xmlstring = doc.read(i.orig_filename).decode('utf-8')
        # print(xmlstring)

        # with open("C:/Users/rootsj/Desktop/hiconsy/static/hwpxxml.xml", 'w', encoding="UTF-8") as f:
        #    f.write(xmlstring)

    # if i.orig_filename == 'Preview/PrvText.txt':
    #     xmlstring = doc.read(i.orig_filename).decode('utf-8')
    #     print(xmlstring)

    # if i.orig_filename == 'META-INF/container.rdf':
    #     xmlstring = doc.read(i.orig_filename).decode('utf-8')
    #     print(xmlstring)

    # if i.orig_filename == 'Contents/content.hpf':
    #     xmlstring = doc.read(i.orig_filename).decode('utf-8')
    #     print(xmlstring)

    # if i.orig_filename == 'Preview/PrvImage.png':
    #     data = doc.read(i.orig_filename)
    #     with open('img2.bmp', 'wb') as f:
    #             f.write(data) 

    # if i.orig_filename == 'mimetype':
    #     xmlstring = doc.read(i.orig_filename).decode('utf-8')
    #     print(xmlstring)