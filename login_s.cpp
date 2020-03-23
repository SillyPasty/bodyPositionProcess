#include "login_s.h"
#include "ui_login_s.h"

//全局变量
QString name;
QString banji;

login_s::login_s(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::login_s)
{
    ui->setupUi(this);
    setFixedSize(400,300);//登录对话框固定大小
    ui->lineEdit_2->setFocus();//口令框置焦点
    ui->lineEdit_2->setEchoMode(QLineEdit::Password);//在构造函数里将密码框的显示设置为黑点，不可见
}

login_s::~login_s()
{
    delete ui;
}

void login_s::on_pushButton_clicked()//登录
{
    //给全局变量复制
    name=ui->lineEdit->text();
    banji=ui->lineEdit_3->text();

    if(!ui->lineEdit_2->text().isEmpty())//输入密码
        {
            QSqlQuery query;
            query.exec("select password from student where name ='"+ui->lineEdit->text()+"'");
            query.next();
            QString pwd=ui->lineEdit_2->text();
            QSqlQuery query1;
            query1.exec("select class from student where name ='"+ui->lineEdit->text()+"'");
            query1.next();
            QString banji=ui->lineEdit_3->text();
            if((query.value(0).toString()==pwd)&&(query1.value(0).toString()==banji))
            {
                QDialog::accept();
            }
            else
            {
                QMessageBox::warning(this,tr("出错"),tr("请输入正确的用户名、班级、密码"),QMessageBox::Ok);
                ui->lineEdit->clear();
                ui->lineEdit_2->clear();
                ui->lineEdit_3->clear();
            }
        }
    else
    {
        ui->lineEdit_2->setFocus();
    }
}

void login_s::on_pushButton_2_clicked()//退出
{
    QDialog::reject();
}
