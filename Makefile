ZIPS=extractables/flask_setup.zip
SCRIPTS=scripts/
BUILD=$(SCRIPTS)setup.sh
RUNNABLE=$(SCRIPTS)run.sh

all:
	echo

extract:
	unzip -o $(ZIPS) -d $(SCRIPTS)
	mv $(SCRIPTS)/requirements.txt requirements.txt

build:
	sh $(BUILD)

run:


build_run: build run
	echo

clean:
	rm $(SCRIPTS)/*
