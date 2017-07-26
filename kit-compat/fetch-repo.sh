#!/bin/sh

function fetch_branch {
	local logfile="/var/www/ceresia.ch/arczero/fetchlog/\$$branch/\$$time.log"
	find $1 -type f \( -iname '*.ebuild' ! -iname 'skel.ebuild' \) | \
	sed s'/\//ebuild \//' | sed s'/\.ebuild/\.ebuild fetch/' | parallel -P${2} 
}

function fetch_repo {
	cd $1
	current_branch=$(git branch -v | sed s'/ /\n/g' | awk 'FNR == 2 {print}')
	
	all_branches=( $( git branch -a | sed '/HEAD/d' | sed '/\*/d' | sed s'/..remotes\/origin\///' ) )
	for i in "${all_branches[@]}"; do 
		git checkout $i
		fetch_branch $1 $2; done;
	git checkout $current_branch
}

fetch_repo "/var/git/core-kit/" "3"
