# portage-mirror-distfiles-script
Script to download all legally-mirrorable distfiles

Add FEATURES="mirror" to /etc/portage/make.conf, then run the script
in a screen session.

The script "lazily" downloads one file at a time: This is intentional.
It simulates one user downloading stuff, instead of hogging all available
bandwidth.

Anyone, breaking out xargs and GNU parallel wasn't worth it. Might do it in the future. 
