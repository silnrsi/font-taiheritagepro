#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file

# THIS FILE NEEDS TO BE UPDATED FOR THE GITHUB REPO STRUCTURE.

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

finfo = {
    "THP-TaiViet.txt" : "script=DFLT",
    "THP-Roman.txt" : "script=latn"
    }

#t=fonttest(targets = {
#   "pdfs" : tex(files=finfo),
#   "test" : tests(files=finfo) } )

#Current Repo Folder Structure#################
for f in ("R", "B"):
    FLsource = "source/"
    font(target="TaiHeritagePro-" + f + ".ttf",
        source=FLsource + "TaiHeritagePro" + f + ".ttf",
#       opentype = volt("TaiHeritagePro-" + f + ".vtp", master=FLsource + "TaiHeritagePro" + f + ".vtp"),
        opentype = fea(FLsource + "TaiHeritagePro" + f + ".fea", no_make=1),
        graphite = gdl("TaiHeritagePro-" + f + ".gdl", master=FLsource + "TaiHeritageRules.gdh", params="-w3521 -w2509 -d", make_params="-n 1 -D BOLD=" + ("1" if f=="B" else "0")),
        ap =FLsource + "TaiHeritagePro" + f + ".xml",
        copyright = COPYRIGHT,
        license = ofl("Heritage",
            version = 1.1,
            file = "OFL.txt"),
        version = VERSION,
#       tests = t
        script = [ "DFLT", "latn", "tavt" ],
#example of woff syntax from...
# Harmatan:
#       woff = woff('web/' + APPNAME    + style + '.woff', params = '-v ' + VERSION + ' -m ../source/' + APPNAME + '-WOFF-metadata.xml')
        woff = woff('web/' + TaiHeritagePro + f + '.woff', params = '-v ' + VERSION + ' -m ../source/TaiHeritagePro-WOFF-metadata.xml')   ) 
