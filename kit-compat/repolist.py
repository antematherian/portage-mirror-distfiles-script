#!/usr/bin/python

import portage
import portage.repository.config
repobj =portage.repository.config.load_repository_config(portage.settings)
print (repobj.repoLocationList())
