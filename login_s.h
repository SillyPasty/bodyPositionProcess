#ifndef LOGIN_S_H
#define LOGIN_S_H

//数据库
#include<QSql>
#include <QDialog>
#include <QDebug>
#include <QMessageBox>
#include<QSqlError>
#include<QSqlDatabase>
#include<QSqlQuery>


namespace Ui {
class login_s;
}

class login_s : public QDialog
{
    Q_OBJECT

public:
    explicit login_s(QWidget *parent = 0);
    ~login_s();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::login_s *ui;
};

#endif // LOGIN_S_H
