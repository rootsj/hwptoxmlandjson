import lxml.html
from lxml import etree
 
xslt_doc = etree.parse("static\\testxml.xsl")
xslt_transformer = etree.XSLT(xslt_doc)
 
source_doc = etree.parse("testxml.xml")
output_doc = xslt_transformer(source_doc)
 
print(str(output_doc))
output_doc.write("test0824.html", pretty_print=True)