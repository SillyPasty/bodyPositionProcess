#include "identity.h"
#include "ui_identity.h"

Identity::Identity(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Identity)
{
    ui->setupUi(this);
}

Identity::~Identity()
{
    delete ui;
}

void Identity::on_pushButton_clicked()//学生
{
    QDialog::accept();
}

void Identity::on_pushButton_2_clicked()//老师
{
    QDialog::reject();
}
