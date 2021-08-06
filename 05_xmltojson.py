import json
import xmltodict
 
with open("C:/Users/rootsj/Desktop/hiconcy/static/test1.xml",'r') as f:
    xmlString = f.read()
 
jsonString = json.dumps(xmltodict.parse(xmlString),
ensure_ascii=False, 
indent=4
)
 
# print(type(jsonString))
# print(jsonString)
 
with open("C:/Users/rootsj/Desktop/hiconcy/static/xml_to_json.json", 'w') as f:
    f.write(jsonString)