#!/bin/bash

QTINCDIR=$(qmake -query QT_INSTALL_HEADERS)
QTLIBDIR=$(qmake -query QT_INSTALL_LIBS)

# Run moc on mainwindow.h
moc mainwindow.h -o moc_mainwindow.cpp

# Compile the project
clang++ -std=c++11 -fPIC \
    -I. \
    -I$QTINCDIR \
    -I$QTINCDIR/QtWidgets \
    -I$QTINCDIR/QtGui \
    -I$QTINCDIR/QtCore \
    main.cpp mainwindow.cpp moc_mainwindow.cpp \
    -o gui \
    -L$QTLIBDIR \
    -lQt5Widgets -lQt5Gui -lQt5Core