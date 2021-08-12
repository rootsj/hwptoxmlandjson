import json

from xml.dom import pulldom

with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()
 
doc = pulldom.parseString(xmlString)


for event, node in doc:
    print(node)