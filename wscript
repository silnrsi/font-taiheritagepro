#!/usr/bin/python

APPNAME='TaiHeritagePro'
VERSION="2.519"
TTF_VERSION="2.519"
### 2.518 was given to last build using VOLT, which is to be used as Standard for first FEA build.
### 2.519 is for first FEA build.
### working towards FEA build and v 2.520 release
LICENSE='OFL.txt'
COPYRIGHT="Copyright (c) 1995-2012, SIL International (www.sil.org)"
out="results"
DESC_NAME="TaiHeritagePro"
DESC_SHORT="The Tai Heritage typeface is designed to reflect the traditional hand-written style of the Tai Viet script."
DOCDIR="documentation"
OUTDIR="wininstallers"
ZIPDIR="zippackage"
RESERVEDOFL="Heritage"
STANDARDS="standards/"

finfo = {
	"THP-TaiViet.txt" : "script=DFLT",
	"THP-Roman.txt" : "script=latn"
	}

#t=fonttest(targets = {
#	"pdfs" : tex(files=finfo),
#	"test" : tests(files=finfo) } )

#Current Repo Folder Structure#################
for f in ("R", "B"):
	FLsource = "sources/"
	font(target="TaiHeritagePro-" + f + ".ttf",
	   	source=FLsource + "TaiHeritagePro" + f + ".ttf",
#	    opentype = volt("TaiHeritagePro-" + f + ".vtp", master=FLsource + "TaiHeritagePro" + f + ".vtp"),
        opentype = fea(FLsource + "TaiHeritagePro" + f + ".fea", no_make=1),
#        opentype = fea("TaiHeritagePro-" + f + ".fea", master=FLsource + "TaiHeritagePro" + f + ".fea"),
#        opentype = fea("TaiHeritagePro-" + f + ".fea", master=FLsource + "TaiHeritagePro" + f + ".fea", make_params="-z 8"),
# Which of the above is correct? They are based on a similar line from ShiShan, but what is the effect of the make_params?
		graphite = gdl("TaiHeritagePro-" + f + ".gdl", master=FLsource + "TaiHeritageRules.gdh", params="-w3521 -w2509 -d", make_params="-n 1 -D BOLD=" + ("1" if f=="B" else "0")),
		ap =FLsource + "TaiHeritagePro" + f + ".xml",
		copyright = COPYRIGHT,
		license = ofl("Heritage",
            version = 1.1,
            file = "OFL.txt"),
		version = VERSION,
#		tests = t
		script = [ "DFLT", "latn", "tavt" ] ) 
