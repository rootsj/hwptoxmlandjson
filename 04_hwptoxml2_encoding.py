import os 
import win32com.client as win32 
import win32gui 

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump
import xml

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwnd = win32gui.FindWindow(None, "빈 문서 1 - 한글")


hwp.Open("C:/Users/rootsj/Desktop/hiconcy/static/json_to_xml.xml")
text = hwp.GetTextFile("HWPML2X", "")
# print(text)

xmlR = xml.fromstring(text.text.encode('utf-8'))

f = open("C:/Users/rootsj/Desktop/hiconcy/static/test2.xml", 'w')

f.write(xmlR)
f.close

hwp.Quit()