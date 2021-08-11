import json
# import xmltodict
import xmltodict_test as xmltodict
# xmltodict customize

# import xmltodict_test2 as xmltodict
# xmltodict 초기버전 v0.2

with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()
 
def postprocessor(path, key, value):
    if key == 'CHAR':
        return key, str(value)
    return key, value

jsonString = json.dumps(xmltodict.parse(xmlString
,postprocessor=postprocessor
),
ensure_ascii=False, 
indent=4
)

print(jsonString)
 
# with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json.json", 'w', encoding="UTF-8") as f:
#     f.write(jsonString)
