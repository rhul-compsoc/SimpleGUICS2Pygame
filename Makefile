# Makefile of SimpleGUICS2Pygame --- March 10, 2020

.SUFFIXES:

SRC = $(sort $(wildcard *.py)) $(sort $(wildcard SimpleGUICS2Pygame/*.py)) \
	$(sort $(wildcard SimpleGUICS2Pygame/*/*.py)) \
	$(sort $(wildcard SimpleGUICS2Pygame/*/*/*.py)) \
	$(sort $(wildcard SimpleGUICS2Pygame/*/*/*/*.py))


JOB = 1

MYPY      = mypy  # http://www.mypy-lang.org/
MYPYFLAGS = --ignore-missing-imports

PEP8      = pep8  # https://pypi.org/project/pep8/
PEP8FLAGS = -v --statistics  # --ignore=E501

PYDEPS      = pydeps  # https://github.com/thebjorn/pydeps
PYDEPSFLAGS = --noshow

PYFLAKES      = pyflakes3  # https://pypi.org/project/pyflakes/
PYFLAKESFLAGS =

PYLINT      = pylint3  # https://www.pylint.org/
PYLINTFLAGS = -j $(JOB) --disable=line-too-long,locally-disabled

PYTYPE      = pytype  # https://google.github.io/pytype/
PYTYPEFLAGS = -j $(JOB)


PYTHON2      = python2  # https://www.python.org/
PYTHON2FLAGS =

PYTHON3      = python3
PYTHON3FLAGS =


CHECKTXT = checkTxtPy.py  # not public program


CD    = cd
CP    = cp -p
ECHO  = echo
GZIP  = gzip
RM    = rm -f
RMDIR = rmdir
SHELL = sh
TAR   = tar
TEE   = tee



# default goal
test3:



###
# #
###
.PHONY: install2 install3 installs

install2:
	@$(ECHO) "==================="
	@$(ECHO) "Install to Python 2"
	@$(ECHO) "==================="
	$(PYTHON2) $(PYTHON2FLAGS) setup.py install -O1

install3:
	@$(ECHO) "==================="
	@$(ECHO) "Install to Python 3"
	@$(ECHO) "==================="
	$(PYTHON3) $(PYTHON3FLAGS) setup.py install -O1

installs:	distclean install2 install3



################
# Distribution #
################
.PHONY: all_dist bdist_egg bdist_wininst sdist

all_dist:	sdist bdist_egg # bdist_wininst

bdist_egg:
	$(PYTHON2) $(PYTHON2FLAGS) setup.py bdist_egg
	$(PYTHON3) $(PYTHON3FLAGS) setup.py bdist_egg

bdist_wininst:
	$(PYTHON3) $(PYTHON3FLAGS) setup.py bdist_wininst --no-target-compile --no-target-optimize --bitmap SimpleGUICS2Pygame/_img/SimpleGUICS2Pygame_152x261.bmp

sdist:
	$(PYTHON3) $(PYTHON3FLAGS) setup.py sdist --formats=gztar



#######
# Doc #
#######
.PHONY: docs docstgz links

docs:	links
	$(CP) -t Sphinx/_static/img pydeps_all.svg pydeps_only.svg
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) Sphinx; $(MAKE) html

docstgz:	docs
		@$(CD) Sphinx/_build; $(TAR) -cvf SimpleGUICS2Pygame_html.tar html
		@$(CD) Sphinx/_build; $(GZIP) -9 SimpleGUICS2Pygame_html.tar
		@$(RM) Sphinx/_build/SimpleGUICS2Pygame_html.tar
		@$(GZIP) -t Sphinx/_build/SimpleGUICS2Pygame_html.tar.gz

links:
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) $(PYTHON3FLAGS) make_img_links.py
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) $(PYTHON3FLAGS) make_prog_links.py
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) $(PYTHON3FLAGS) make_snd_links.py
	-@$(CD) Sphinx/_static/links/data; $(RM) -r __pycache__/*.pyc; $(RMDIR) __pycache__



#################
# Static checks #
#################
.PHONY: lint lintlog mypy pep8 pydeps pyflakes pylint pytype

lint:	pep8 pyflakes pylint mypy

lintlog:
	$(ECHO) "Lint" | $(TEE) lint.log
	@$(ECHO) ===== pep8 ===== | $(TEE) -a lint.log
	-$(PEP8) $(PEP8FLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pyflakes ===== | $(TEE) -a lint.log
	-$(PYFLAKES) $(PYFLAKESFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pylint ===== | $(TEE) -a lint.log
	-$(PYLINT) $(PYLINTFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pytype --tree ===== | $(TEE) -a lint.log
	-$(PYTYPE) $(PYTYPEFLAGS) --tree $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) ===== pytype --unresolved ===== | $(TEE) -a lint.log
	-$(PYTYPE) $(PYTYPEFLAGS) --unresolved $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) ===== pytype ===== | $(TEE) -a lint.log
	-$(PYTYPE) $(PYTYPEFLAGS) -k $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) ===== mypy ===== | $(TEE) -a lint.log
	-$(MYPY) $(MYPYFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log

mypy:
	-$(MYPY) $(MYPYFLAGS) $(SRC)

pep8:
	-$(PEP8) $(PEP8FLAGS) $(SRC)

pydeps:
	$(PYDEPS) $(PYDEPSFLAGS) SimpleGUICS2Pygame --cluster -o pydeps_all.svg
	$(PYDEPS) $(PYDEPSFLAGS) SimpleGUICS2Pygame --cluster -o pydeps_only.svg --only SimpleGUICS2Pygame.simpleguics2pygame

pyflakes:
	-$(PYFLAKES) $(PYFLAKESFLAGS) $(SRC)

pylint:
	-$(PYLINT) $(PYLINTFLAGS) $(SRC)

pytype:
	-$(PYTYPE) --tree $(PYTYPEFLAGS) $(SRC)
	-$(PYTYPE) --unresolved $(PYTYPEFLAGS) $(SRC)
	-$(PYTYPE) $(PYTYPEFLAGS) $(SRC)



########
# Test #
########
.PHONY: checkTxt requirement2 requirement3 requirements test2 test3 tests

checkTxt:
	@$(CHECKTXT) .hgignore Makefile "*.py" "*.rst" "*.txt"
	@$(CHECKTXT) "Sphinx/*.py" "Sphinx/*.rst" "Sphinx/*.txt"
	@$(CHECKTXT) "Sphinx/_static/*.css*"
	@$(CHECKTXT) "Sphinx/_static/links/*" "Sphinx/_static/links/*/*"
	@$(CHECKTXT) "SimpleGUICS2Pygame/*.py" "SimpleGUICS2Pygame/*/*.py" "SimpleGUICS2Pygame/*/*/*.py"


requirement2:
	@$(ECHO) "========================="
	@$(ECHO) "Requirement with Python 2"
	@$(ECHO) "========================="
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/script; $(PYTHON2) $(PYTHON2FLAGS) SimpleGUICS2Pygame_check.py

requirement3:
	@$(ECHO) "========================="
	@$(ECHO) "Requirement with Python 3"
	@$(ECHO) "========================="
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/script; $(PYTHON3) $(PYTHON3FLAGS) SimpleGUICS2Pygame_check.py

requirements: requirement2 requirement3


test2:
	@$(ECHO) "=================="
	@$(ECHO) "Test with Python 2"
	@$(ECHO) "=================="
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); export PYGAME_HIDE_SUPPORT_PROMPT=hide; $(CD) SimpleGUICS2Pygame/test; $(PYTHON2) $(PYTHON2FLAGS) test_all.py

test3:
	@$(ECHO) "=================="
	@$(ECHO) "Test with Python 3"
	@$(ECHO) "=================="
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); export PYGAME_HIDE_SUPPORT_PROMPT=hide; $(CD) SimpleGUICS2Pygame/test; $(PYTHON3) $(PYTHON3FLAGS) test_all.py

tests:	test2 test3



#########
# Clean #
#########
.PHONY:	clean cleanbuild cleandist cleandocs distclean overclean
clean:	cleanbuild
	$(RM) -r *.pyc *.pyo */*.pyc */*.pyo */*/*.pyc */*/*.pyo */*/*/*.pyc */*/*/*.pyo */*/*/*/*.pyc */*/*/*/*.pyo */*/*/*/*/*.pyc */*/*/*/*/*.pyo
	-$(RMDIR) __pycache__ */__pycache__ */*/__pycache__ */*/*/__pycache__ */*/*/*/__pycache__
	$(RM) SimpleGUICS2Pygame.egg-info/*
	-$(RMDIR) SimpleGUICS2Pygame.egg-info
	$(RM) -r .mypy_cache
	$(RM) -r .pytype

cleanbuild:
	$(PYTHON3) $(PYTHON3FLAGS) setup.py clean
	$(RM) -r build

cleandist:	cleandocs
		$(RM) dist/*
		-$(RMDIR) dist

cleandocs:
		@$(CD) Sphinx; $(MAKE) clean

distclean:	clean cleandist

overclean:	distclean
	$(RM) lint.log
	$(RM) pydeps_*.svg
