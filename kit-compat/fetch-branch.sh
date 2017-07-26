#!/bin/bash

function fetch_branch {
	cd $1
	local branch=$( git branch -v | sed s'/ /\n/' | awk 'FNR == 2 {print}' )
	local time=$(date --utc +%F%T)
	local logfile="/var/www/ceresia.ch/arczero/fetchlog/\$$branch/\$$time.log"
	find $1 -type f \( -iname '*.ebuild' ! -iname 'skel.ebuild' \) | \
	sed s'/\//ebuild \//' | sed s'/\.ebuild/\.ebuild fetch/' | parallel -P${2} \
	2> logfile
}
fetch_branch "/var/git/core-kit" "3"

fetch_branch "/var/git/net-kit" "3"
