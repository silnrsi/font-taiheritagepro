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
        source=FLsource + "TaiHeritagePro-" + f + ".ttf",
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
