import olefile


with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/00n-S190106-example.hwp') as ole:
    # with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/test.hwp') as ole # ole.close() 생략 가능

    # print(ole.listdir())
    # [['\x05HwpSummaryInformation'], ['BodyText', 'Section0'], ['DocInfo'], ['DocOptions', '_LinkDoc'], ['FileHeader'], ['PrvImage'], ['PrvText'], ['Scripts', 'DefaultJScript'], ['Scripts', 'JScriptVersion']]
    # print(ole.listdir(streams=True, storages=True))

    # print(type(ole))
    #<class 'olefile.olefile.OleFileIO'>

    # meta = ole.get_metadata()
    # print(meta.keywords('BodyText'))
    # print(meta)

    # test = ole.openstream('FileHeader')
    # data = test.read()
    # print(data)
    # print(data.decode('utf-8'))

    test = ole.openstream('BodyText/Section0')
    data = test.read()
    # print(data[:100])
    tempd = data[22:69]
    print(type(tempd))
    print(tempd)
    print(tempd.decode("ISO-8859-1"))



    # props = ole.getproperties('\x05HwpSummaryInformation')
    # print(props)


