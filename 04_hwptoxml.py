import win32com.client as win32 

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

hwp.Open("C:/Users/rootsj/Desktop/hiconcy/static/test.hwp")
xml = hwp.GetTextFile("HWPML2X", "")

# 인코딩 해결해야함
f = open("C:/Users/rootsj/Desktop/hiconcy/static/test1.xml", 'w')
f.write(xml)
f.close

hwp.Quit()