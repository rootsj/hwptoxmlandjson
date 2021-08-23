import olefile


with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/test.hwp') as ole:
    # with olefile.OleFileIO('C:/Users/rootsj/Desktop/hiconsy/static/test.hwp') as ole # ole.close() 생략 가능

    # print(ole.listdir())
    #[['\x05HwpSummaryInformation'], ['BodyText', 'Section0'], ['DocInfo'], ['DocOptions', '_LinkDoc'], ['FileHeader'], ['PrvImage'], ['PrvText'], ['Scripts', 'DefaultJScript'], ['Scripts', 'JScriptVersion']]
    # print(ole.listdir(streams=True, storages=True))

    # print(type(ole))
    #<class 'olefile.olefile.OleFileIO'>

    # meta = ole.get_metadata()
    # print(meta.keywords('BodyText'))
    # print(meta)

    # test = ole.openstream('\x05HwpSummaryInformation')
    # data = test.read()
    # print(data)

    # props = ole.getproperties('\x05HwpSummaryInformation')
    # print(props)

    print(ole)

    ole.close()
