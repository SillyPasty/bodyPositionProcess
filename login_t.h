#ifndef LOGIN_T_H
#define LOGIN_T_H

//数据库
#include<QSql>
#include <QDialog>
#include <QDebug>
#include <QMessageBox>
#include<QSqlError>
#include<QSqlDatabase>
#include<QSqlQuery>


namespace Ui {
class login_t;
}

class login_t : public QDialog
{
    Q_OBJECT

public:
    explicit login_t(QWidget *parent = 0);
    ~login_t();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::login_t *ui;
};

#endif // LOGIN_T_H
