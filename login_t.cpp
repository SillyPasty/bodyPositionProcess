#include "login_t.h"
#include "ui_login_t.h"

login_t::login_t(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::login_t)
{
    ui->setupUi(this);
    setFixedSize(400,300);//登录对话框固定大小
    ui->lineEdit_2->setFocus();//口令框置焦点
    ui->lineEdit_2->setEchoMode(QLineEdit::Password);//在构造函数里将密码框的显示设置为黑点，不可见
}

login_t::~login_t()
{
    delete ui;
}

void login_t::on_pushButton_clicked()//登录
{
    if(!ui->lineEdit_2->text().isEmpty())//输入密码
        {
            QSqlQuery query;
            query.exec("select password from teacher where name ='"+ui->lineEdit->text()+"'");
            query.next();
            QString pwd=ui->lineEdit_2->text();
            if(query.value(0).toString()==pwd)
            {
                QDialog::accept();
            }
            else
            {
                QMessageBox::warning(this,tr("用户名或密码输入错误"),tr("请输入正确的用户名和密码"),QMessageBox::Ok);
                ui->lineEdit->clear();
                ui->lineEdit_2->clear();
            }
        }
    else
    {
        ui->lineEdit_2->setFocus();
    }
}

void login_t::on_pushButton_2_clicked()//退出
{
    QDialog::reject();
}

