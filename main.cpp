#include "identity.h"
#include "widget.h"
#include "student.h"
#include "login_s.h"
#include "login_t.h"
#include <QApplication>

//数据库需要的文件
#include<QSql>
#include <QDialog>
#include <QDebug>
#include <QMessageBox>
#include<QSqlError>
#include<QSqlDatabase>
#include<QSqlQuery>

//连接数据库并打开
bool OpenDatabase()
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QODBC");   //数据库驱动类型为SQL Server
    qDebug()<<"ODBC driver?"<<db.isValid();
    QString dsn = QString::fromLocal8Bit("QTDSN2");      //数据源名称
    db.setHostName("localhost");                        //选择本地主机，127.0.1.1
    db.setDatabaseName(dsn);                            //设置数据源名称
    db.setUserName("sa");                               //登录用户
    db.setPassword("123456");                              //密码
    if(!db.open())                                      //打开数据库
    {
        qDebug()<<db.lastError().text();
        QMessageBox::critical(0, QObject::tr("Database error"), db.lastError().text());
        return false;                                   //打开失败
    }
    else
    {
        qDebug()<<"database open success!";
        QSqlQuery query(db);
        query.exec("SELECT * FROM SchoolInfo");
        QSqlQuery query1(db);
        query1.exec("SELECT * FROM Class1");
        QSqlQuery query2(db);
        query2.exec("SELECT * FROM Class2");
        QSqlQuery query3(db);
        query3.exec("SELECT * FROM Exam1PullUpClass1");
        QSqlQuery query4(db);
        query4.exec("SELECT * FROM Exam1PullUpClass2");
        QSqlQuery query5(db);
        query5.exec("SELECT * FROM Exam1PushUpClass1");
        QSqlQuery query6(db);
        query6.exec("SELECT * FROM Exam1PushUpClass2");
        QSqlQuery query7(db);
        query7.exec("SELECT * FROM Exam1SitUpClass1");
        QSqlQuery query8(db);
        query8.exec("SELECT * FROM Exam1SitUpClass2");
        QSqlQuery query9(db);
        query9.exec("SELECT * FROM Exam2PullUpClass1");
        QSqlQuery query10(db);
        query10.exec("SELECT * FROM Exam2PullUpClass2");
        QSqlQuery query11(db);
        query11.exec("SELECT * FROM Exam2PushUpClass1");
        QSqlQuery query12(db);
        query12.exec("SELECT * FROM Exam2PushUpClass2");
        QSqlQuery query13(db);
        query13.exec("SELECT * FROM Exam2SitUpClass1");
        QSqlQuery query14(db);
        query14.exec("SELECT * FROM Exam2SitUpClass2");


    }return true;
}

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    if(!OpenDatabase())
        return 1;

    Identity i;
    if(i.exec()==QDialog::Accepted)//选择学生身份
        {
          login_s s;
          if(s.exec()==QDialog::Accepted)//登录成功
              {
                Student s;
                s.show();
                return a.exec();
              }
          else
          {
              return 0;
          }
        }
    else if(i.exec()==QDialog::Rejected)//选择教师身份
      {
        login_t t;
        if(t.exec()==QDialog::Accepted)//登录成功
            {
              Widget w;
              w.show();
              return a.exec();
            }
        else
        {
            return 0;
        }
      }

}

