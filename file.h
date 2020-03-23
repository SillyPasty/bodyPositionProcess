#ifndef FILE_H
#define FILE_H

#include <QWidget>
#include "MyTestModel.h"

namespace Ui {
class File;
}

class File : public QWidget
{
    Q_OBJECT

public:
    explicit File(QWidget *parent = 0);
    ~File();

protected:
    void changeEvent(QEvent *e);

private:
    Ui::File *ui;
    //数据库相关
    MyTestModel *myModel;

//下拉列表控制table view中显示内容的函数；
public slots:
    void print_s();


private slots:
    void on_pushButton_7_clicked();
    void on_pushButton_5_clicked();
    void on_pushButton_4_clicked();
    void on_pushButton_3_clicked();
};

#endif // FILE_H
