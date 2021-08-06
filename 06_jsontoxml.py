import json
import xmltodict 
 
with open('C:/Users/rootsj/Desktop/hiconcy/static/xml_to_json.json', 'r') as f:
    jsonString = f.read()
 
 
xmlString = xmltodict.unparse(json.loads(jsonString)
# , pretty=True
, encoding='utf-16'
)
 
with open('C:/Users/rootsj/Desktop/hiconcy/static/json_to_xml.xml', 'w') as f:
    f.write(xmlString)