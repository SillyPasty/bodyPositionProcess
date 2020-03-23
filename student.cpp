#include "student.h"
#include "ui_student.h"
#include "login_s.h"

extern QString name;//引入全局变量

Student::Student(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Student)
{
    ui->setupUi(this);
    ui->label->setText("欢迎"+name+"同学登录");

    e_box_s=new E_box_s();
    ui->tabWidget->insertTab(0,e_box_s,tr("我的信箱"));

    video_s=new Video_s();
    ui->tabWidget->insertTab(1,video_s,tr("调看考试信息"));

    file_s=new File_s();
    ui->tabWidget->insertTab(2,file_s,tr("导出文件"));

}

Student::~Student()
{
    delete ui;
}
