from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
import odf

doc = load("static/testhwpx.hwpx")

print(doc.meta.childNodes[:])
print(doc.fontfacedecls.childNodes[:])
print(doc.scripts.childNodes[:])
print(doc.settings.childNodes[:])
print(doc.masterstyles.childNodes[:])
print(doc.body.childNodes[:])
