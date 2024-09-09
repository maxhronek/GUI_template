1. First, ensure you have Clang installed. You mentioned having Clang version 7.0.0, so we'll use that.
We'll need to use the clang++ command for C++ compilation. Here's the modified compilation command:
clang++ -std=c++11 -fPIC -I. -I/usr/include/qt5 -I/usr/include/qt5/QtWidgets -I/usr/include/qt5/QtGui -I/usr/include/qt5/QtCore main.cpp -o gui -lQt5Widgets -lQt5Gui -lQt5Core
3. Before compiling, we need to run the Meta-Object Compiler (moc) on our main.cpp file. The moc is needed because we're using the Q_OBJECT macro in our MainWindow class. Here's how to do that:
moc main.cpp -o moc_main.cpp
Now, let's modify our compilation command to include the moc-generated file:
clang++ -std=c++11 -fPIC -I. -I/usr/include/qt5 -I/usr/include/qt5/QtWidgets -I/usr/include/qt5/QtGui -I/usr/include/qt5/QtCore main.cpp moc_main.cpp -o gui -lQt5Widgets -lQt5Gui -lQt5Core
If you're still having issues with finding the Qt headers, you can use qmake to find the correct paths:
QTINCDIR=$(qmake -query QT_INSTALL_HEADERS)
QTLIBDIR=$(qmake -query QT_INSTALL_LIBS)

Then use these variables in your compilation command:
clang++ -std=c++11 -fPIC -I. -I$QTINCDIR -I$QTINCDIR/QtWidgets -I$QTINCDIR/QtGui -I$QTINCDIR/QtCore main.cpp moc_main.cpp -o gui -L$QTLIBDIR -lQt5Widgets -lQt5Gui -lQt5Core

6. If you're still encountering issues, you might want to create a CMakeLists.txt file to manage the build process. Here's a simple one:
Then you can build your project using:
mkdir build
cd build
cmake -DCMAKE_CXX_COMPILER=clang++ ..
make

This approach lets CMake handle the complexities of building a Qt application, including running the moc when necessary.
Remember to keep your backend.py file in the same directory as your executable when you run the program.