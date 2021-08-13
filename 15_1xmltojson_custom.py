from xml.etree import cElementTree as ET
from collections import defaultdict
import json
import re

def etree_to_dict(t):
    a = 0
    # CHAR 검증하는 객체

    if t.tag == 'CHAR': # <CHAR> tag일 때
        xmlstr = ET.tostring(t , encoding='unicode', method='xml')
        xmlstr = re.split('<CHAR>|</CHAR>', xmlstr)
        #<CHAR>① ㄱ<TAB/>② ㄴ<TAB/>③ ㄷ<TAB/>④ ㄱ, ㄴ<TAB/>⑤ ㄴ, ㄷ</CHAR>
        #<CHAR>&lt;<FWSPACE/>보<FWSPACE/>기<FWSPACE/>&gt;</CHAR>
        #위와 같은 XML에서 tag를 포함한 text 출력

        if len(xmlstr) == 3: 
            # <CHAR>안에 text 있을 때
            d = {t.tag: xmlstr[1]}
            a = 1
            # 검증 코드 CHAR일때 하위 tag검색 X
        else:
            d = {t.tag: t.text}
            # 텍스트 내용 없을 때 t.text = null 값
    else:
        d = {t.tag: {} if t.attrib else None}
        # t.tag 하위에 t.attrib 존재

    children = list(t)
    # 리스트화

    if children and a != 1:
        # 하위 tag 있을 때
        dd = defaultdict(list) 
        # 빈 dict
        if t.attrib:
            #attrib가 있으면
            for k, v in t.attrib.items():
                dd['@'+k].append(v)
        for dc in map(etree_to_dict, children):
            #하위 tag
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}

    if t.attrib:
        # 하위 tag가 없더라도 attrib 있을 때
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())

    if t.text and a != 1:
        # text가 있을 때, <CHAR> 태그는 제외
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d


with open("C:/Users/rootsj/Desktop/hiconsy/static/test2.xml",'r', encoding="UTF-8") as f:
    xmlString = f.read()

e = ET.XML(xmlString)
xmldict = etree_to_dict(e)

# print()


jsonString = json.dumps(xmldict,
ensure_ascii=False, 
indent=4
)
with open("C:/Users/rootsj/Desktop/hiconsy/static/xml_to_json15.json", 'w', encoding="UTF-8") as f:
    f.write(jsonString)