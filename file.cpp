#include "file.h"
#include "ui_file.h"

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

File::File(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::File)
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

File::~File()
{
    delete ui;
}
//下拉列表的函数
void File::print_s()
{
    if(ui->comboBox->currentIndex()==0)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam1PullUpClass1");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==1)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam1PushUpClass1");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==2)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam1SitUpClass1");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==3)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam1PullUpClass2");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==4)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam1PushUpClass2");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==5)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam1SitUpClass2");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==6)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam2PullUpClass1");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==7)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam2PushUpClass1");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==8)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam2SitUpClass1");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==9)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam2PullUpClass2");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==10)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam2PushUpClass2");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==11)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Exam2SitUpClass2");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==12)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Class1");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==13)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from Class2");
        ui->tableView->setModel(model);
    }
    else if(ui->comboBox->currentIndex()==14)
    {
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery("select * from SchoolInfo");
        ui->tableView->setModel(model);
    }
}
void File::changeEvent(QEvent *e)
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

void File::on_pushButton_3_clicked()
{
    myModel->setMyData(400);
}

void File::on_pushButton_4_clicked()
{
    myModel->setMyData(4000);
}

void File::on_pushButton_5_clicked()
{
    myModel->setMyData(40000);
}

void File::on_pushButton_7_clicked()
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


