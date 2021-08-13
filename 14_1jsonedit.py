from collections import defaultdict
import json
import xmltodict 
 
with open('C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json13.json', 'r', encoding="UTF-8") as f:
    jsonString = f.read()
 
 
jsonData = json.loads(jsonString)


q1 = jsonData['HWPML']['BODY']['SECTION']['P'].copy()
jsonData['HWPML']['BODY']['SECTION']['P'] = jsonData['HWPML']['BODY']['SECTION']['P'] + q1

# print(len(q1))
# print(type(q1))
# for i in q1:
#     print(i)

# jsonString = json.dumps(jsonData,
# ensure_ascii=False, 
# indent=4
# )
 
# with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json14.json", 'w', encoding="UTF-8") as f:
#     f.write(jsonString)

xmlString = xmltodict.unparse(jsonData
# , pretty=True
, encoding='utf-16' #16 중요 안하면 한글에서 인식 못함
)


with open('C:/Users/rootsj/Desktop/hiconsy/static/json_to_xml14.xml', 'w', encoding="UTF-8") as f:
    f.write(xmlString)