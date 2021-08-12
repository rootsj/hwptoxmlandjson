import os 
import win32com.client as win32 

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

# #test, HWP -> Str -> HWP
# hwp.Open("C:/Users/rootsj/Desktop/hiconsy/static/test.hwp")
# xml = hwp.GetTextFile("HWPML2X", "")

#test1, HWP -> XML -> HWP
# with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
#     xml1 = f.read()

# # test2, HWP -> XML -> JSON -> XML -> HWP
with open("C:/Users/rootsj/Desktop/hiconsy/static/json_to_xml5.xml",'r', encoding="UTF-8") as f:
    xml2 = f.read()


hwp.SetTextFile(xml2, "HWPML2X", "")
hwp.SaveAs("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_hwp5.hwp","HWPML2X","")

hwp.Quit()