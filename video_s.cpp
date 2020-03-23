#include "video_s.h"
#include "ui_video_s.h"

//引入全局变量
#include "login_s.h"
extern QString name;
extern QString banji;

//数据库需要的文件
#include <QtGui>
#include <QString>
#include <QTextCodec>
#include <QSqlDatabase>
#include <QSql>

//图表所需文件
#include <QChartView>
#include <QLineSeries>
QT_CHARTS_USE_NAMESPACE

Video_s::Video_s(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Video_s)
{
    ui->setupUi(this);
    ui->lineEdit->setText(name);

    connect(ui->comboBox,SIGNAL(currentIndexChanged(int)),this,SLOT(print_info()));
    connect(ui->comboBox_2,SIGNAL(currentIndexChanged(int)),this,SLOT(print_info()));

    connect(ui->comboBox_2,SIGNAL(currentIndexChanged(int)),this,SLOT(print_chart()));
}

Video_s::~Video_s()
{
    delete ui;
}

//下拉列表控制数据显示
void Video_s::print_info()
{
    QString title;
    QString  project;

    if(ui->comboBox->currentIndex()==0)title="1";
    else title="2";

    if(ui->comboBox_2->currentIndex()==0)project="SitUp";
    else if(ui->comboBox_2->currentIndex()==1)project="PushUp";
    else if(ui->comboBox_2->currentIndex()==2)project="PullUp";

    QSqlQuery query;
    query.exec(QString("select*from Exam%1%2Class%3 where StudentName='%4'")
               .arg(title)
               .arg(project)
               .arg(banji)
               .arg(name));
    query.next();
    ui->lineEdit_2->setText(query.value(0).toString());
    ui->lineEdit_3->setText(query.value(2).toString());
    ui->lineEdit_4->setText(query.value(4).toString());
    ui->lineEdit_5->setText(query.value(6).toString());
    ui->lineEdit_6->setText(query.value(5).toString());
    ui->textEdit->setText(query.value(7).toString());


}

//科目下拉列表控制历史成绩折线图
void Video_s::print_chart()

{
   QString project;
   if(ui->comboBox_2->currentIndex()==0)project="SitUp";
   else if(ui->comboBox_2->currentIndex()==1)project="PushUp";
   else if(ui->comboBox_2->currentIndex()==2)project="PullUp";

   QSqlQuery query;
   query.exec(QString("select*from Exam1%1Class%2 where StudentName='%3'")
              .arg(project)
              .arg(banji)
              .arg(name));
   query.next();
   QString strqualified=query.value(5).toString();
   int qualified=strqualified.toInt(nullptr,10);
   QString strunqualified=query.value(6).toString();
   int unqualified=strunqualified.toInt(nullptr,10);

   QSqlQuery query1;
   query1.exec(QString("select*from Exam2%1Class%2 where StudentName='%3'")
              .arg(project)
              .arg(banji)
              .arg(name));
   query1.next();
   QString strqualified1=query1.value(5).toString();
   int qualified1=strqualified1.toInt(nullptr,10);
   QString strunqualified1=query1.value(6).toString();
   int unqualified1=strunqualified1.toInt(nullptr,10);

   //画图表
        QGraphicsScene *scene = new QGraphicsScene;
        QGraphicsView*view=new QGraphicsView;

        view->setWindowTitle("  ");
        view->setRenderHint(QPainter::Antialiasing);
        scene->setBackgroundBrush(QBrush(QColor(240, 240, 240)));
        view->setSceneRect(0, 0, 630, 280);

        QLineSeries *lineseries = new QLineSeries();
            lineseries->append(1,qualified);
            lineseries->append(2,qualified1);
        QLineSeries *lineseries2 = new QLineSeries();
            lineseries2->append(1,unqualified );
            lineseries2->append(2,unqualified1);

            QChart *lineChart = new QChart();
            lineChart->legend()->hide();  // 隐藏图例
            lineChart->addSeries(lineseries);  // 将 series 添加至图表中
            lineChart->createDefaultAxes();  // 基于已添加到图表的 series 来创建轴
            lineChart->setTitle("(横轴——考试次数/纵轴——合格个数)");//图表显示的标题
            lineChart->setGeometry(5, 5, 400, 260);
            QChart *lineChart2 = new QChart();
            lineChart2->legend()->hide();  // 靠右
            lineChart2->addSeries(lineseries2);  // 将 series 添加至图表中
            lineChart2->createDefaultAxes();  // 基于已添加到图表的 series 来创建轴
            lineChart2->setTitle("(横轴——考试次数/纵轴——不合格个数)");//图表显示的标题
            lineChart2->setGeometry(410, 5, 400, 260);

             scene->addItem(lineChart);
             scene->addItem(lineChart2);
             ui->graphicsView_3->setScene(scene);
             ui->graphicsView_3->show();

}
