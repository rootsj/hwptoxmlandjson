import json
import xmltodict
 
with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()
 


jsonString = json.dumps(xmltodict.parse(xmlString.replace("<TAB/>", "$").replace("<FWSPACE/>", "^")
, process_namespaces=True),
ensure_ascii=False, 
indent=4
)
 
with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json12.json", 'w', encoding="UTF-8") as f:
    f.write(jsonString)