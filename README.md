# portage-mirror-distfiles-script
Script to download all legally-mirrorable distfiles

Add FEATURES="mirror" to /etc/portage/make.conf, then run the script
in a screen session. 

The script "lazily" downloads one file at a time: This is intentional.
It simulates one user downloading stuff, instead of hogging all available
bandwidth. The lazy way to download distfiles involves running the script
in the lazy folder. The total size is about 400GB give or take for all
distfiles.

The more efficient way if you're running the script multiple times is to
run the genlist.py script to generate a list of ebuilds to fetch. genlist.py
will generate a bash script that can be run or piped to xargs/gnu parallel:

cat "fetchlist.sh" | parallel -P<n>

where <n> is the number of threads you want to run. Make sure that
gnu parallel is installed. This will greatly speed up checking the 
already downloaded distfiles against the manifest value, while
new sources tarballs are fetched in the background. 

You might be tempted to think that generating a list of already downloaded
distfiles would greatly speed up execution: sadly, source tarballs are
sometimes updated, and it's not safe to think that an already mirrored
tarball matches the digest values. 
