import win32com.client as win32 

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

hwp.Open("C:/Users/rootsj/Desktop/hiconcy/static/test.hwp")
xml = hwp.GetTextFile("HWPML2X", "")

f = open("C:/Users/rootsj/Desktop/hiconcy/static/test.xml", 'w', encoding="UTF-8")

f.write(xml)

f.close

hwp.Quit()