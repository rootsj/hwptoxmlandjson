from enum import EnumMeta
from xml.etree import cElementTree as ElementTree
import json
import re

class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
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
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
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
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself 
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a 
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})



with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()

root = ElementTree.XML(xmlString)
xmldict = XmlDictConfig(root)

# print(xmldict)
print(type(xmldict))
# print({"HWPML" : xmldict})
xmldict = {"HWPML" : xmldict}

jsonString = json.dumps(xmldict,
ensure_ascii=False, 
indent=4
)
with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json2.json", 'w', encoding="UTF-8") as f:
    f.write(jsonString)