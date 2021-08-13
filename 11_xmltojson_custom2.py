from collections import defaultdict
import json

def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

from xml.etree import cElementTree as ET

with open("C:/Users/rootsj/Desktop/hiconsy/static/test.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()

e = ET.XML(xmlString)

from pprint import pprint

xmldict = etree_to_dict(e)

jsonString = json.dumps(xmldict,
ensure_ascii=False, 
indent=4
)
with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json11_2.json", 'w', encoding="UTF-8") as f:
    f.write(jsonString)