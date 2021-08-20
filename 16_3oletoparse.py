import olefile

with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/test.hwp') as ole:
    for entry in ole.listdir():
        # if entry[0] == 'PrvImage':
        #     continue
        # print(entry.data())
        # if len(entry) ==1:
        #     print(ole.openstream(entry).read())
        # else:
        #     print(ole.openstream(entry).read())
        print(entry)