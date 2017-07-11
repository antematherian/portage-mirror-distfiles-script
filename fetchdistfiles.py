#!/usr/bin/python3

import subprocess
import portage
import re
import sys

if sys.argc < 3:
    print("This script requires two arguments. Run it like this:")
    print("./fetchdistfiles.py /usr/portage 10")
    print("To download the whole portage tree with 10 processes spawned at a time")
try:
    rawstr = subprocess.check_output( \
    "find {} -type f \( -iname '*.ebuild' ! -iname 'skel.ebuild' \)".format(sys.argv[1]) , \
    universal_newlines=True, shell=True)
except subprocess.CalledProcessError:
    print("Could not fetch the packagelist using equery --quiet list '*'. Aborting")
    exit()
rawlist = rawstr.split('\n')

#|  sed s,\/usr\/portage\/,, | sed s,\/.*\/,\/, | \
#    sed s'/\.ebuild//'" 
    

ptree = portage.db[portage.root]["porttree"].dbapi

commandlist = ""
for ebuild in rawlist:
    fineebuild = ebuild.replace("/usr/portage/", "").replace(".ebuild", "").strip()
    fineebuild = re.sub(r'/.*/', '/',  fineebuild)
    #print(fineebuild)
    if fineebuild == "":
        pass
    try:
        restrict = ptree.aux_get(fineebuild, ["RESTRICT"])
    except:
        pass
    if not ( 'mirror' in restrict[0] or 'fetch' in restrict[0]):
        commandlist += "ebuild %s fetch\n" % ebuild 

with open("fetchlist.sh", "w") as cfile:
    cfile.write("#!/bin/bash\n") 
    cfile.write(commandlist)

try:
    fetchstatus = subprocess.check_output(["chmod", "+x", "./fetchlist.sh"], \
        universal_newlines=True)
except subprocess.CalledProcessError:
    print(fetchstatus)

try:
    fetchstatus = subprocess.check_output(\
        "nice -n 10 sh -c 'cat fetchlist.sh | parallel -P{}'".format(sys.argv[2]), \
        universal_newlines=True, shell=True)
except subprocess.CalledProcessError:
    print(fetchstatus)
