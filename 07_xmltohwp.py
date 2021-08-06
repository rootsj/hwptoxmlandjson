import os 
import win32com.client as win32 

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

#test1, HWP -> XML -> HWP
with open("C:/Users/rootsj/Desktop/hiconcy/static/test1.xml",'r') as f:
    xml1 = f.read()

# test2, HWP -> XML -> JSON -> XML -> HWP
with open("C:/Users/rootsj/Desktop/hiconcy/static/json_to_xml.xml",'r') as f:
    xml2 = f.read()

# test3, HWP -> Str -> HWP
hwp.Open("C:/Users/rootsj/Desktop/hiconcy/static/test.hwp")
xml3 = hwp.GetTextFile("HWPML2X", "")

hwp.SetTextFile(xml3, "HWPML2X", "")
hwp.SaveAs("C:/Users/rootsj/Desktop/hiconcy/static/xml_to_hwp3.hwp","HWPML2X","")

hwp.Quit()