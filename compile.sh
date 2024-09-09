#!/bin/bash

QTINCDIR=$(qmake -query QT_INSTALL_HEADERS)
QTLIBDIR=$(qmake -query QT_INSTALL_LIBS)

clang++ -std=c++11 -fPIC \
    -I. \
    -I$QTINCDIR \
    -I$QTINCDIR/QtWidgets \
    -I$QTINCDIR/QtGui \
    -I$QTINCDIR/QtCore \
    main.cpp moc_main.cpp \
    -o gui \
    -L$QTLIBDIR \
    -lQt5Widgets -lQt5Gui -lQt5Core