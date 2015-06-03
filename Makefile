# Makefile of SimpleGUICS2Pygame --- 2015-06-03

.SUFFIXES:

CD       = cd
CHECKTXT = checkTxtPy.py
CP       = cp -p
ECHO     = echo
GZIP     = gzip
PYTHON2  = python2
PYTHON3  = python3
RM       = rm -f
RMDIR    = rmdir
SHELL    = sh
TAR      = tar



test3:



###
# #
###
.PHONY: install2 install3 installs

install2:
	@$(ECHO) "==================="
	@$(ECHO) "Install to Python 2"
	@$(ECHO) "==================="
	$(PYTHON2) setup.py install -O1

install3:
	@$(ECHO) "==================="
	@$(ECHO) "Install to Python 3"
	@$(ECHO) "==================="
	$(PYTHON3) setup.py install -O1

installs:	distclean install2 install3



################
# Distribution #
################
.PHONY: all_dist bdist_egg bdist_wininst sdist

all_dist:	sdist bdist_egg # bdist_wininst

bdist_egg:
	$(PYTHON2) setup.py bdist_egg
	$(PYTHON3) setup.py bdist_egg

bdist_wininst:
	$(PYTHON3) setup.py bdist_wininst --no-target-compile --no-target-optimize --bitmap SimpleGUICS2Pygame/_img/SimpleGUICS2Pygame_152x261.bmp

sdist:
	$(PYTHON3) setup.py sdist --formats=gztar



#######
# Doc #
#######
.PHONY: docs docstgz links

docs:	links
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) Sphinx; $(MAKE) html

docstgz:	html
		@$(CD) Sphinx/_build; $(TAR) -cvf SimpleGUICS2Pygame_html.tar html
		@$(CD) Sphinx/_build; $(GZIP) -9 SimpleGUICS2Pygame_html.tar
		@$(RM) Sphinx/_build/SimpleGUICS2Pygame_html.tar
		@$(GZIP) -t Sphinx/_build/SimpleGUICS2Pygame_html.tar.gz

links:
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) make_img_snd_links.py
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) make_prog_links.py
	-@$(CD) Sphinx/_static/links/data; $(RM) -r __pycache__/*.pyc; $(RMDIR) __pycache__



########
# Test #
########
.PHONY: checkTxt test2 test3 tests

checkTxt:
	@$(CHECKTXT) .hgignore Makefile "*.py" "*.rst" "*.txt"
	@$(CHECKTXT) "Sphinx/*.py" "Sphinx/*.rst" "Sphinx/*.txt"
	@$(CHECKTXT) "Sphinx/_static/*.css*"
	@$(CHECKTXT) "Sphinx/_static/links/*" "Sphinx/_static/links/*/*"
	@$(CHECKTXT) "SimpleGUICS2Pygame/*.py" "SimpleGUICS2Pygame/*/*.py" "SimpleGUICS2Pygame/*/*/*.py"

test2:
	@$(ECHO) "=================="
	@$(ECHO) "Test with Python 2"
	@$(ECHO) "=================="
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/test; $(PYTHON2) test_all.py

test3:
	@$(ECHO) "=================="
	@$(ECHO) "Test with Python 3"
	@$(ECHO) "=================="
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/test; $(PYTHON3) test_all.py

tests:	test2 test3



#########
# Clean #
#########
.PHONY:	clean cleanbuild cleandist cleandocs distclean
clean:	cleanbuild
	$(RM) -r *.pyc *.pyo */*.pyc */*.pyo */*/*.pyc */*/*.pyo */*/*/*.pyc */*/*/*.pyo */*/*/*/*.pyc */*/*/*/*.pyo */*/*/*/*/*.pyc */*/*/*/*/*.pyo
	-$(RMDIR) __pycache__ */__pycache__ */*/__pycache__ */*/*/__pycache__ */*/*/*/__pycache__
	$(RM) SimpleGUICS2Pygame.egg-info/*
	-$(RMDIR) SimpleGUICS2Pygame.egg-info

cleanbuild:
	$(PYTHON3) setup.py clean
	$(RM) -r build

cleandist:	cleandocs
		$(RM) dist/*
		-$(RMDIR) dist

cleandocs:
		@$(CD) Sphinx; $(MAKE) clean

distclean:	clean cleandist
