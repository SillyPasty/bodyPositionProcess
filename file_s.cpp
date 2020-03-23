#include "file_s.h"
#include "ui_file_s.h"

//导出表格需要的文件
#include "exportexcelobject.h"
#include <QFileDialog>
#include <QMessageBox>

//数据库需要的库文件
#include <QtGui>
#include <QString>
#include <QTextCodec>
#include <QSqlDatabase>
#include <QtSql>

//引入全局变量
#include "login_s.h"
extern QString name;
extern QString banji;

//编辑tableView所需文件
#include <QStandardItemModel>
#include <QTableView>

File_s::File_s(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::File_s)
{
    ui->setupUi(this);

    //添加代码
    //文件导出相关
    ui->progressBar->setValue(0);
    myModel = new MyTestModel;
    ui->tableView->setModel(myModel);

    //下拉列表
    connect(ui->comboBox,SIGNAL(currentIndexChanged(QString)),this,SLOT(print_s()));
}

File_s::~File_s()
{
    delete ui;
}

//下拉列表的函数
void File_s::print_s()
{

     QSqlQuery query;
     query.exec(QString("select*from Exam1SitUpClass%1 where StudentName='%2'").arg(banji).arg(name));
     query.next();
     QSqlQuery query1;
     query1.exec(QString("select*from Exam1PushUpClass%1 where StudentName='%2'").arg(banji).arg(name));
     query1.next();
     QSqlQuery query2;
     query2.exec(QString("select*from Exam1PullUpClass%1 where StudentName='%2'").arg(banji).arg(name));
     query2.next();
     QSqlQuery query3;
     query3.exec(QString("select*from Exam2SitUpClass%1 where StudentName='%2'").arg(banji).arg(name));
     query3.next();
     QSqlQuery query4;
     query4.exec(QString("select*from Exam2PushUpClass%1 where StudentName='%2'").arg(banji).arg(name));
     query4.next();
     QSqlQuery query5;
     query5.exec(QString("select*from Exam2SitUpClass%1 where StudentName='%2'").arg(banji).arg(name));
     query5.next();

     QStandardItemModel*model=new QStandardItemModel();
     model->setItem(0,0,new QStandardItem("序号"));
     model->setItem(0,1,new QStandardItem("考试标题"));
     model->setItem(0,2,new QStandardItem("任课老师"));
     model->setItem(0,3,new QStandardItem("学生姓名"));
     model->setItem(0,4,new QStandardItem("体育成绩"));
     model->setItem(0,5,new QStandardItem("合格个数"));
     model->setItem(0,6,new QStandardItem("不合格个数"));
     model->setItem(0,7,new QStandardItem("姿势分析"));
     ui->tableView->setModel(model);
     
     if(ui->comboBox->currentIndex()==1)
     {
         model->setItem(1,0,new QStandardItem("1"));
         model->setItem(1,1,new QStandardItem(query.value(1).toString()));
         model->setItem(1,2,new QStandardItem(query.value(2).toString()));
         model->setItem(1,3,new QStandardItem(query.value(3).toString()));
         model->setItem(1,4,new QStandardItem(query.value(4).toString()));
         model->setItem(1,5,new QStandardItem(query.value(5).toString()));
         model->setItem(1,6,new QStandardItem(query.value(6).toString()));
         model->setItem(1,7,new QStandardItem(query.value(7).toString()));
         
         model->setItem(2,0,new QStandardItem("2"));
         model->setItem(2,1,new QStandardItem(query1.value(1).toString()));
         model->setItem(2,2,new QStandardItem(query1.value(2).toString()));
         model->setItem(2,3,new QStandardItem(query1.value(3).toString()));
         model->setItem(2,4,new QStandardItem(query1.value(4).toString()));
         model->setItem(2,5,new QStandardItem(query1.value(5).toString()));
         model->setItem(2,6,new QStandardItem(query1.value(6).toString()));
         model->setItem(2,7,new QStandardItem(query1.value(7).toString()));
         
         model->setItem(3,0,new QStandardItem("3"));
         model->setItem(3,1,new QStandardItem(query2.value(1).toString()));
         model->setItem(3,2,new QStandardItem(query2.value(2).toString()));
         model->setItem(3,3,new QStandardItem(query2.value(3).toString()));
         model->setItem(3,4,new QStandardItem(query2.value(4).toString()));
         model->setItem(3,5,new QStandardItem(query2.value(5).toString()));
         model->setItem(3,6,new QStandardItem(query2.value(6).toString()));
         model->setItem(3,7,new QStandardItem(query2.value(7).toString()));
         
         
     }
     else if(ui->comboBox->currentIndex()==2)
     {
         model->setItem(1,0,new QStandardItem("1"));
         model->setItem(1,1,new QStandardItem(query3.value(1).toString()));
         model->setItem(1,2,new QStandardItem(query3.value(2).toString()));
         model->setItem(1,3,new QStandardItem(query3.value(3).toString()));
         model->setItem(1,4,new QStandardItem(query3.value(4).toString()));
         model->setItem(1,5,new QStandardItem(query3.value(5).toString()));
         model->setItem(1,6,new QStandardItem(query3.value(6).toString()));
         model->setItem(1,7,new QStandardItem(query3.value(7).toString()));
         
         model->setItem(2,0,new QStandardItem("2"));
         model->setItem(2,1,new QStandardItem(query4.value(1).toString()));
         model->setItem(2,2,new QStandardItem(query4.value(2).toString()));
         model->setItem(2,3,new QStandardItem(query4.value(3).toString()));
         model->setItem(2,4,new QStandardItem(query4.value(4).toString()));
         model->setItem(2,5,new QStandardItem(query4.value(5).toString()));
         model->setItem(2,6,new QStandardItem(query4.value(6).toString()));
         model->setItem(2,7,new QStandardItem(query4.value(7).toString()));
         
         model->setItem(3,0,new QStandardItem("3"));
         model->setItem(3,1,new QStandardItem(query5.value(1).toString()));
         model->setItem(3,2,new QStandardItem(query5.value(2).toString()));
         model->setItem(3,3,new QStandardItem(query5.value(3).toString()));
         model->setItem(3,4,new QStandardItem(query5.value(4).toString()));
         model->setItem(3,5,new QStandardItem(query5.value(5).toString()));
         model->setItem(3,6,new QStandardItem(query5.value(6).toString()));
         model->setItem(3,7,new QStandardItem(query5.value(7).toString()));
     }
     else if(ui->comboBox->currentIndex()==3)
     {
         model->setItem(1,0,new QStandardItem("1"));
         model->setItem(1,1,new QStandardItem(query.value(1).toString()));
         model->setItem(1,2,new QStandardItem(query.value(2).toString()));
         model->setItem(1,3,new QStandardItem(query.value(3).toString()));
         model->setItem(1,4,new QStandardItem(query.value(4).toString()));
         model->setItem(1,5,new QStandardItem(query.value(5).toString()));
         model->setItem(1,6,new QStandardItem(query.value(6).toString()));
         model->setItem(1,7,new QStandardItem(query.value(7).toString()));

         model->setItem(2,0,new QStandardItem("2"));
         model->setItem(2,1,new QStandardItem(query1.value(1).toString()));
         model->setItem(2,2,new QStandardItem(query1.value(2).toString()));
         model->setItem(2,3,new QStandardItem(query1.value(3).toString()));
         model->setItem(2,4,new QStandardItem(query1.value(4).toString()));
         model->setItem(2,5,new QStandardItem(query1.value(5).toString()));
         model->setItem(2,6,new QStandardItem(query1.value(6).toString()));
         model->setItem(2,7,new QStandardItem(query1.value(7).toString()));

         model->setItem(3,0,new QStandardItem("3"));
         model->setItem(3,1,new QStandardItem(query2.value(1).toString()));
         model->setItem(3,2,new QStandardItem(query2.value(2).toString()));
         model->setItem(3,3,new QStandardItem(query2.value(3).toString()));
         model->setItem(3,4,new QStandardItem(query2.value(4).toString()));
         model->setItem(3,5,new QStandardItem(query2.value(5).toString()));
         model->setItem(3,6,new QStandardItem(query2.value(6).toString()));
         model->setItem(3,7,new QStandardItem(query2.value(7).toString()));


         model->setItem(4,0,new QStandardItem("4"));
         model->setItem(4,1,new QStandardItem(query3.value(1).toString()));
         model->setItem(4,2,new QStandardItem(query3.value(2).toString()));
         model->setItem(4,3,new QStandardItem(query3.value(3).toString()));
         model->setItem(4,4,new QStandardItem(query3.value(4).toString()));
         model->setItem(4,5,new QStandardItem(query3.value(5).toString()));
         model->setItem(4,6,new QStandardItem(query3.value(6).toString()));
         model->setItem(4,7,new QStandardItem(query3.value(7).toString()));

         model->setItem(5,0,new QStandardItem("5"));
         model->setItem(5,1,new QStandardItem(query4.value(1).toString()));
         model->setItem(5,2,new QStandardItem(query4.value(2).toString()));
         model->setItem(5,3,new QStandardItem(query4.value(3).toString()));
         model->setItem(5,4,new QStandardItem(query4.value(4).toString()));
         model->setItem(5,5,new QStandardItem(query4.value(5).toString()));
         model->setItem(5,6,new QStandardItem(query4.value(6).toString()));
         model->setItem(5,7,new QStandardItem(query4.value(7).toString()));

         model->setItem(6,0,new QStandardItem("6"));
         model->setItem(6,1,new QStandardItem(query5.value(1).toString()));
         model->setItem(6,2,new QStandardItem(query5.value(2).toString()));
         model->setItem(6,3,new QStandardItem(query5.value(3).toString()));
         model->setItem(6,4,new QStandardItem(query5.value(4).toString()));
         model->setItem(6,5,new QStandardItem(query5.value(5).toString()));
         model->setItem(6,6,new QStandardItem(query5.value(6).toString()));
         model->setItem(6,7,new QStandardItem(query5.value(7).toString()));
     }



}

void File_s::changeEvent(QEvent *e)
{
    QWidget::changeEvent(e);
    switch (e->type()) {
    case QEvent::LanguageChange:
        ui->retranslateUi(this);
        break;
    default:
        break;
    }
}

void File_s::on_pushButton_3_clicked()
{
    myModel->setMyData(400);
}

void File_s::on_pushButton_4_clicked()
{
    myModel->setMyData(4000);
}

void File_s::on_pushButton_5_clicked()
{
    myModel->setMyData(40000);
}

void File_s::on_pushButton_7_clicked()
{
    QString fileName = QFileDialog::getSaveFileName(this, tr("Excel file"), qApp->applicationDirPath (),
                                                    tr("Excel Files (*.xls)"));
    if (fileName.isEmpty())
        return;

    ExportExcelObject obj(fileName, "mydata", ui->tableView);

    // you can change the column order and
    // choose which colum to export
    //obj.addField(0, "colum1", "char(20)");
    obj.addField(3, "colum4", "char(20)");
    obj.addField(1, "colum2", "char(20)");
    obj.addField(2, "colum3", "char(20)");

    obj.addField(4, "colum5", "char(20)");
    obj.addField(5, "colum6", "char(20)");
    //obj.addField(6, "colum7", "char(20)");

    ui->progressBar->setValue(0);
    ui->progressBar->setMaximum(ui->tableView->model()->rowCount());

    connect(&obj, SIGNAL(exportedRowCount(int)), ui->progressBar, SLOT(setValue(int)));

    int retVal = obj.export2Excel();
    if( retVal > 0)
    {
        QMessageBox::information(this, tr("Done"),
                                 QString(tr("%1 records exported!")).arg(retVal)
                                 );
    }
}
