import json
import xmltodict
# import xmltodict_test as xmltodict
# xmltodict customize

with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()
 
# class SkipValues:
#     def __init__(self, key):
#         self.key = key
#         self.count = 0

#     def __call__(self, path, key, value):
#         if key != self.key:
#             return key, value
#         self.count += 1
#         if self.count % 2 == 1:
#             return None
#         else:
#             return key, value

# def postprocessor(path, key, value):
#     if key == 'CHAR':
#         return key, str(path)
#     return key, value

# def handle(path, item):
#      print('path:%s item:%s' % (path, item))
#      return True

jsonString = json.dumps(xmltodict.parse(xmlString
# ,item_depth=2
# ,item_callback=handle
# ,postprocessor=postprocessor
),
ensure_ascii=False, 
indent=4
)

# print(jsonString)
# jsonString = json.dumps(xmltodict.parse(xmlString),
# ensure_ascii=False, 
# indent=4
# )

 
# print(xmlString)
# with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json.json", 'w', encoding="UTF-8") as f:
#     f.write(jsonString)



xml  =  ''' 
<doc> 
    <item>Item1</item> 
    <item>Item2</item> 
    <item>Item3</item> 
    <item>Item4</item> 
</doc>''' 

class SkipOddValues:
    def __init__(self, key):
        self.key = key
        self.count = 0

    def __call__(self, path, key, value):
        if key != self.key:
            return key, value
        self.count += 1
        if self.count % 2 == 1:
            return None
        else:
            return key, value

doc = xmltodict.parse(xml, postprocessor=SkipOddValues('item'))

print(doc)