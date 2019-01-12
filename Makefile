ZIPS=extractables/flask_setup.zip
SCRIPTS=scripts/
BUILD=$(SCRIPTS)setup.sh
RUNNABLE=$(SCRIPTS)demo.sh

all:
	echo

extract:
	unzip -o $(ZIPS) -d $(SCRIPTS)

build:
	bash $(BUILD)

run:
	bash $(RUNNABLE)

build_run: build run
	cat

clean:
	rm $(SCRIPTS)/*
