#!/usr/bin/python3

import subprocess
import portage
import re
try:
    rawstr = subprocess.check_output( \
    "find /usr/portage -type f \( -iname '*.ebuild' ! -iname 'skel.ebuild' \)" , \
    universal_newlines=True, shell=True)
except subprocess.CalledProcessError:
    print("Could not fetch the packagelist using equery --quiet list '*'. Aborting")
    exit()
rawlist = rawstr.split('\n')

#|  sed s,\/usr\/portage\/,, | sed s,\/.*\/,\/, | \
#    sed s'/\.ebuild//'" 
    

ptree = portage.db[portage.root]["porttree"].dbapi

logfile = open('/var/log/mirrorlog.log', 'w')

for ebuild in rawlist:
    fineebuild = ebuild.replace("/usr/portage/", "").replace(".ebuild", "")
    fineebuild = re.sub(r'/.*/', '/',  fineebuild)
    #print(fineebuild)
    try:
        restrict = ptree.aux_get(fineebuild, ["RESTRICT"])
    except:
        pass
    if( 'mirror' in restrict[0] or 'fetch' in restrict[0]):
        pass
    else:
        try:
            fetchstatus = subprocess.check_output( \
            ["ebuild", ebuild, "fetch"], \
            universal_newlines=True)
            logfile.write(fineebuild)
        except subprocess.CalledProcessError:
            print("Fetch error: Could not fetch " + fineebuild)

logfile.close()
