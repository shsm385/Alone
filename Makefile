PYCS := $(shell find . -name "*.pyc")
PYOPENGL	= PyOpenGL-3.0.2
OPENGL	= OpenGL
NAME = "filename"
TARGET = Bodies.py
PACKAGE = "プログラムの入っているパッケージ"
INSTDIR = Bodies.app/Contents/Resources/Python/

all:
	@if [ ! -e $(PYOPENGL) ] ; then unzip $(PYOPENGL).zip ; fi
	@if [ ! -e $(OPENGL) ] ; then ln -s $(PYOPENGL)/$(OPENGL) $(OPENGL) ; fi

clean:
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	if [ -e $(INSTDIR) ] ; then rm -f -r $(INSTDIR) ; fi

wipe:
	if [ -e $(OPENGL) ] ; then rm -f $(OPENGL) ; fi
	if [ -e $(PYOPENGL) ] ; then rm -f -r $(PYOPENGL) ; fi

test: 
	python ${TARGET}

install:
	if [ ! -e $(INSTDIR) ] ; then mkdir $(INSTDIR) ; fi
	cp -p -r $(TARGET) $(PACKAGE) $(INSTDIR)


zip: clean
	(cd .. ; zip -r $(NAME).zip ./$(NAME)/)

sdist: clean
	python setup.py sdist

pydoc: clean
	(sleep 3 ; open http://localhost:9999/$(PACKAGE).html) & pydoc -p 9999
	



