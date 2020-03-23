#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    e_box=new E_box();
    ui->tabWidget->insertTab(0,e_box,tr("我的信箱"));

    video=new Video();
    ui->tabWidget->insertTab(1,video,tr("考试情况分析"));

    file=new File();
    ui->tabWidget->insertTab(2,file,tr("文件导出"));
}
Widget::~Widget()
{
    delete ui;
}
