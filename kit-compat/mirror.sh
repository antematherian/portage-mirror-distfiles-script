#!/bin/bash

REPO_DIR=/var/git/core-kit

find $REPO_DIR -type f \( -iname '*.ebuild' ! -iname 'skel.ebuild' \) | \

sed s'/\//ebuild \//' | sed s'/\.ebuild/\.ebuild fetch/' >> fetchlist.sh
