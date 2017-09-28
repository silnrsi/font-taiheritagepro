#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file

APPNAME='TaiHeritagePro'
VERSION="2.600"
TTF_VERSION="2.600"
LICENSE='OFL.txt'
COPYRIGHT="Copyright (c) 1995-2017, SIL International (www.sil.org)"
out="results"
DESC_NAME="TaiHeritagePro"
DESC_SHORT="The Tai Heritage typeface is designed to reflect the traditional hand-written style of the Tai Viet script."
DESC_LONG = '''
The original Tai Heritage font was designed to reflect the traditional
hand-written style of the Tai Viet script that is treasured by the Tai people
of Vietnam. This gives it its angular style and flowing lines, as opposed to
the more rounded style used by Lao and some modern versions of Tai Viet.

The current Tai Heritage Pro release is Unicode encoded, based on the
Unicode 5.2 standard. It uses either the SIL Graphite technology or OpenType
for correct placement of combining marks (vowels and tones).

The Tai people of northwestern Vietnam and surrounding areas have a long 
tradition of literacy in the Tai Viet script. Their languages belong to 
the Tai-Kadai language family and are closely related to Lao.
'''
DOCDIR="documentation"
OUTDIR="wininstallers"
ZIPDIR="zippackage"
RESERVEDOFL="Heritage"
STANDARDS="tests/reference/"
ftmlTest('tests/xsl/FTMLcreateList.xsl')

finfo = {
    "THP-TaiViet.txt" : "script=DFLT",
    "THP-Roman.txt" : "script=latn"
    }

for f in ("Regular", "Bold"):
    FLsource = "source/"
    font(target="TaiHeritagePro-" + f + ".ttf",
        source=FLsource + "TaiHeritagePro-NoSmartCode-" + f + ".ttf",
        opentype = fea(FLsource + "TaiHeritagePro-" + f + ".fea", no_make=1),
        graphite = gdl("TaiHeritagePro-" + f + ".gdl", master=FLsource + "TaiHeritageRules.gdh", params="-w3521 -w2509 -d", make_params="-n 1 -D BOLD=" + ("1" if f=="Bold" else "0")),
        ap =FLsource + "TaiHeritagePro-" + f + ".xml",
        copyright = COPYRIGHT,
        license = ofl("Heritage",
            version = 1.1,
            file = "OFL.txt"),
        version = VERSION,
        script = [ "DFLT", "latn", "tavt" ],
        woff = woff('web/' + 'TaiHeritagePro-' + f + '.woff', params = '-v ' + VERSION + ' -m ../source/TaiHeritagePro-WOFF-metadata.xml')   ) 
