import json
import xmltodict
 
with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()
 

jsonString = json.dumps(xmltodict.parse(xmlString, process_namespaces=True),
ensure_ascii=False, 
indent=4
)
 
with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json.json", 'w', encoding="UTF-8") as f:
    f.write(jsonString)