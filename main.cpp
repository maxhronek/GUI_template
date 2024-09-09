g++ -fPIC -I. -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -I/usr/include/x86_64-linux-gnu/qt5/QtGui -I/usr/include/x86_64-linux-gnu/qt5/QtCore -lQt5Widgets -lQt5Gui -lQt5Core main.cpp -o gui
#include <QApplication>
#include <QMainWindow>
#include <QTabWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QTextEdit>
#include <QTreeView>
#include <QFileSystemModel>
#include <QProcess>
#include <QPushButton>
#include <QLineEdit>

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr) : QMainWindow(parent) {
        QTabWidget *tabWidget = new QTabWidget(this);
        setCentralWidget(tabWidget);

        // Main tab
        QWidget *mainTab = new QWidget();
        QHBoxLayout *mainLayout = new QHBoxLayout(mainTab);

        // File manager pane
        QFileSystemModel *model = new QFileSystemModel;
        model->setRootPath(QDir::rootPath());
        QTreeView *fileTree = new QTreeView(mainTab);
        fileTree->setModel(model);
        fileTree->setRootIndex(model->index(QDir::homePath()));
        mainLayout->addWidget(fileTree);

        // Detail pane
        QTextEdit *detailPane = new QTextEdit(mainTab);
        detailPane->setReadOnly(true);
        mainLayout->addWidget(detailPane);

        tabWidget->addTab(mainTab, "Main");

        // Console tab
        QWidget *consoleTab = new QWidget();
        QVBoxLayout *consoleLayout = new QVBoxLayout(consoleTab);
        QTextEdit *consoleOutput = new QTextEdit(consoleTab);
        consoleOutput->setReadOnly(true);
        QLineEdit *consoleInput = new QLineEdit(consoleTab);
        QPushButton *executeButton = new QPushButton("Execute", consoleTab);
        
        consoleLayout->addWidget(consoleOutput);
        consoleLayout->addWidget(consoleInput);
        consoleLayout->addWidget(executeButton);

        tabWidget->addTab(consoleTab, "Console");

        // Connect signals and slots
        connect(fileTree, &QTreeView::clicked, this, &MainWindow::onFileSelected);
        connect(executeButton, &QPushButton::clicked, this, &MainWindow::onExecuteCommand);
        connect(consoleInput, &QLineEdit::returnPressed, this, &MainWindow::onExecuteCommand);

        resize(800, 600);
    }

private slots:
    void onFileSelected(const QModelIndex &index) {
        QFileSystemModel *model = qobject_cast<QFileSystemModel*>(
            centralWidget()->findChild<QTreeView*>()->model());
        QString filePath = model->filePath(index);

        // Call Python backend to process the file
        QProcess process;
        process.start("python", QStringList() << "backend.py" << filePath);
        process.waitForFinished();
        QString output = process.readAllStandardOutput();

        // Update detail pane
        QTextEdit *detailPane = centralWidget()->findChild<QTextEdit*>();
        detailPane->setText(output);
    }

    void onExecuteCommand() {
        QLineEdit *consoleInput = centralWidget()->findChild<QLineEdit*>();
        QString command = consoleInput->text();
        consoleInput->clear();

        QProcess process;
        process.start(command);
        process.waitForFinished();
        QString output = process.readAllStandardOutput();

        QTextEdit *consoleOutput = centralWidget()->findChild<QTextEdit*>();
        consoleOutput->append("> " + command);
        consoleOutput->append(output);
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    MainWindow window;
    window.show();
    return app.exec();
}

#include "main.moc"