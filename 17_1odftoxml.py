from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
import odf

with load("static/testhwpx.hwpx") as doc:

    print(doc.meta.childNodes[:])
    print(doc.fontfacedecls.childNodes[:])
    print(doc.scripts.childNodes[:])
    print(doc.settings.childNodes[:])
    print(doc.masterstyles.childNodes[:])
    print(doc.body.childNodes[:])
