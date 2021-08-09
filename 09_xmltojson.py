import json
import xmltodict_test as xmltodict
# xmltodict customize

with open("C:/Users/rootsj/Desktop/hiconcy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()
 

jsonString = json.dumps(xmltodict.parse(xmlString),
ensure_ascii=False, 
indent=4
)
 
# print(xmlString)
# with open("C:/Users/rootsj/Desktop/hiconcy/static/xml_to_json.json", 'w', encoding="UTF-8") as f:
#     f.write(jsonString)