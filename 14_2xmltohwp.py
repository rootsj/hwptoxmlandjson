import os 
import win32com.client as win32 

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

with open("C:/Users/rootsj/Desktop/hiconsy/static/json_to_xml14.xml",'r', encoding="UTF-8") as f:
    xml2 = f.read()


hwp.SetTextFile(xml2, "HWPML2X", "")
hwp.SaveAs("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_hwp14.hwp","HWPML2X","")

hwp.Quit()