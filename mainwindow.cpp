#include "mainwindow.h"
#include <QTabWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QTextEdit>
#include <QTreeView>
#include <QProcess>
#include <QPushButton>
#include <QLineEdit>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent) {
    // ... (rest of the implementation)
}

void MainWindow::onFileSelected(const QModelIndex &index) {
    // ... (implementation)
}

void MainWindow::onExecuteCommand() {
    // ... (implementation)
}