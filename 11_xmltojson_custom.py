from enum import EnumMeta
from xml import etree
from xml.etree import cElementTree as ElementTree
import json
import re
from collections import OrderedDict


class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            # print(element)
            # print(element.items())

            if element.items(): #attributes
                elem = [('@'+key, value) for (key, value) in element.items()]
                print(len(element.items()))
                # for ele in element:
                #     print(ele)
                # print(element.items())
                # print(len(element))
                # print(elem1 for elem1 in element)
                # print('-----')
                # for elem in element:
                    # if elem:
                    #     print(elem)
                    #     print(type(elem))
                        # aDict = XmlDictConfig(element)
                        # self.append({elem.tag: aDict})
                self.append(OrderedDict(elem))
            if element:
                # print(element)
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    # print(element)
                    # if len(element) > 1:
                    #     print('lif')
                    #     print(len(element))
                    #     print(element[0].tag)
                    #     print(eement[1].tag)
                    #     print('---')
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    
                    # print(element)
                    # for ele in element:
                        # print(ele.items())
                    # print(element[-1].tag)
                    # for (key, value) in element.items():
                    #     print(value)
                    #     print(type(value))
                    # self.append(dict(('@'+key, value) for (key, value) in element.items()))
                    self.append(XmlListConfig(element))
            # elif element.items():
            #     self.append(OrderedDict(element.items()))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
    def __init__(self, parent_element):
        # childrenNames = [child.tag for child in parent_element.getchildren()]

        if parent_element.items(): #attributes
            element = [('@'+key, value) for (key, value) in parent_element.items()]
            self.update(dict(element))
        
        for element in parent_element:
            # print(element.tag)
            if element.tag == 'CHAR':
                xmlstr = ElementTree.tostring(element , encoding='unicode', method='xml')
                xmlstr = re.split('<CHAR>|</CHAR>', xmlstr)
                if len(xmlstr) == 3:
                    self.update({element.tag: xmlstr[1]})
                else:
                    self.update({element.tag: element.text})
            elif element:
            # if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    # print(element.tag)
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # print(element.tag)
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself 
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))

                # if childrenNames.count(element.tag) > 1:
                #     try:
                #         currentValue = self[element.tag]
                #         currentValue.append(aDict)
                #         # print(aDict)
                #         self.update({element.tag: currentValue})
                #     except: #the first of its kind, an empty list must be created
                #         self.update({element.tag: list(aDict)}) #aDict is written in [], i.e. it will be a list
                # else:
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a 
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
                # self[element.tag].update({"__Content__":element.text})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})

'''
Example usage:

>>> tree = ElementTree.parse('your_file.xml')
>>> root = tree.getroot()
>>> xmldict = XmlDictConfig(root)

Or, if you want to use an XML string:

>>> root = ElementTree.XML(xml_string)
>>> xmldict = XmlDictConfig(root)

And then use xmldict for what it is... a dict.
    '''

with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()

root = ElementTree.XML(xmlString)
# print(type(root)) # <class 'xml.etree.ElementTree.Element'>
# print(root.tag) # HWPML
# print(root.attrib)# {'Style': 'embed', 'SubVersion': '10.0.0.0', 'Version': '2.91'}
xmldict = XmlDictConfig(root)


xmldict = {"HWPML" : xmldict}
# 임시

# print(xmldict)

jsonString = json.dumps(xmldict,
ensure_ascii=False, 
indent=4
)
with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json11.json", 'w', encoding="UTF-8") as f:
    f.write(jsonString)