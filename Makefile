ZIPS=extractables/flask_setup.zip
SCRIPTS=scripts/
BUILD=$(SCRIPTS)setup.sh
RUNNABLE=$(SCRIPTS)run.sh

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


extract:	## Extract from the zip file all of its contents into the script and root dir
	unzip -o $(ZIPS) -d $(SCRIPTS)
	mv $(SCRIPTS)requirements.txt ./requirements.txt

build:	## Install a virtualenv to download the required files via pip3
	sh $(BUILD)

run:	## The entry point to mostly anything you're doing. Executes run.py
	sh ${RUNNABLE}

build_run: build run	## Combining two steps into one

create_zip:	## Creates a zip of all the files necessary for development
	zip flask_setup requirements.txt scripts/*.sh

clean:	## Get rid of your scripts files for a clean installation
	rm $(SCRIPTS)/*
