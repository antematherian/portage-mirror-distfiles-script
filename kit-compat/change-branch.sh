#!/bin/bash

cd /var/git/core-kit

current_branch=$(git branch -v | sed s'/ /\n/g' | awk 'FNR == 2 {print}')

all_branches=( $( git branch -a | sed '/HEAD/d' | sed '/\*/d' | sed s'/..remotes\/origin\///' ) )

for i in "${all_branches[@]}"; do printf $i; done
