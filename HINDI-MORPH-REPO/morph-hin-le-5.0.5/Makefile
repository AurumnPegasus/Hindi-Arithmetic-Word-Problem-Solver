#
# Makefile -- compiling/copying/install/uninstall the module
#

PREFIX = $(setu)

# Program and Data files and directories.
DEST_PROG_DIR = $(PREFIX)/src/sl/morph/hin
DEST_DATA_DIR = $(PREFIX)/data_src/sl/morph/hin
DEST_BIN_DATA_DIR = $(PREFIX)/data_bin/sl/morph/hin
DEST_COMMON_DIR = $(PREFIX)/bin/sys/common

#VER = 2.0 
CPFR = cp -fr

# make all -- make programs, data, library, documentation, etc.

all:install-src install-data

install-src:
	mkdir -p $(DEST_PROG_DIR)
	$(CPFR) src/sl/morph/hin/* $(DEST_PROG_DIR)
	$(CPFR) README INSTALL ChangeLog nukta-adder.py docs $(DEST_PROG_DIR)
	$(CPFR) adj-gen-1.1 tests morph_run.sh morph_web.sh morph.sh morph.spec test.sh $(DEST_PROG_DIR)
	cp Makefile.stage2 $(DEST_PROG_DIR)/Makefile
	mkdir -p $(DEST_COMMON_DIR)
	cp -fr addsentencetag.pl deletesentencetag.pl remove_ssf.pl $(DEST_COMMON_DIR)
#        $(CPFR) addsentencetag.pl deletesentencetag.pl remove_ssf.pl $(DEST_COMMON_DIR)

install-data:
	mkdir -p $(DEST_DATA_DIR)
	mkdir -p $(DEST_BIN_DATA_DIR)
	cp -fr data_src/sl/morph/hin/* $(DEST_DATA_DIR)

# make compile -- Compiles the source code as well as the data
# compile: compile-exec compile-data

# make install -- Install what all needs to be installed, copying the files from the packages tree to systemwide directories.# it installs the engine and the corpus, dictionary, etc.


# remove the module files from sampark
clean:uninstall
uninstall:
	$(MAKE) -C  $(DEST_PROG_DIR) clean
	rm -fr $(DEST_PROG_DIR) $(DEST_DATA_DIR)

.PHONY: all clean install uninstall install-src install-data

