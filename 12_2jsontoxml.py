import json
import xmltodict 
 
with open('C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json12.json', 'r', encoding="UTF-8") as f:
    jsonString = f.read()
 
 
xmlString = xmltodict.unparse(json.loads(jsonString)
# , pretty=True
, encoding='utf-16' #16 중요 안하면 한글에서 인식 못함  
)

xmlString = xmlString.replace("$", "<TAB/>").replace("^", "<FWSPACE/>")


with open('C:/Users/rootsj/Desktop/hiconsy/static/json_to_xml12.xml', 'w', encoding="UTF-8") as f:
    f.write(xmlString)