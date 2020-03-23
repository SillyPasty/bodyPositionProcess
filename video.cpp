#include "video.h"
#include "ui_video.h"

//数据库需要的库文件
#include <QtGui>
#include <QString>
#include <QTextCodec>
#include <QSqlDatabase>
#include <QtSql>

//计时所需库文件
#include<QDateTime>

//图表所需的库文件
#include <QChartView>
#include <QLineSeries>
QT_CHARTS_USE_NAMESPACE

//全局变量
int i=1;
int num_q=0;
int num_u=0;
QString stu_name;
QString stu_class;
int waist=0;
int arm=0;
int elbow=0;
int chin=0;
int time_per;

Video::Video(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Video)
{

    ui->setupUi(this);
    //导航页的设置
    QObject::connect(ui->listWidget,SIGNAL(currentRowChanged(int)),ui->stackedWidget,SLOT(setCurrentIndex(int)));
    //显示数据
    connect(ui->comboBox,SIGNAL(currentTextChanged(QString)),this,SLOT(print_info()));
    connect(ui->comboBox_2,SIGNAL(currentIndexChanged(int)),this,SLOT(print_info()));
    connect(ui->comboBox_4,SIGNAL(currentIndexChanged(int)),this,SLOT(print_info()));
    //先显示班级图表
    connect(ui->comboBox_2,SIGNAL(currentIndexChanged(int)),this,SLOT(print_chart()));
    connect(ui->comboBox_4,SIGNAL(currentIndexChanged(int)),this,SLOT(print_chart()));
    //定时器
    timer=new QTimer(this);
    timer->setInterval(100);
    connect(timer,SIGNAL(timeout()),this,SLOT(now_info()));
    timer->start();
}

Video::~Video()
{
    delete ui;
    delete timer;
}


//实时数据反馈
void Video::now_info()
{
   //读一条元组
   QSqlQuery query;
   query.exec(QString("select*from Queue where id=%1").arg(i));
   query.next();
   int id=query.value(0).toInt();//id
   if(id=i)//读到数据
   {
       //是否开始读下一个人的信息
       int flag=query.value(1).toInt();
       if(flag==1)
       {
           QString s_id=query.value(2).toString;
           ui->textBrowser_3->setText(s_id);//显示学号
           QSqlQuery query2;
           query2.exec(QString("select*from student where id='%1'").arg(s_id));
           query2.next();
           stu_class=query2.value(2).toString();
           ui->textBrowser_2->setText(stu_class);//显示班级
           stu_name=query2.value(1).toString();
           ui->textBrowser_4->setText(stu_name);//显示姓名
           ui->textBrowser_5->clear();
           ui->textBrowser_6->clear();
           ui->textBrowser_7->clear();
           ui->textBrowser_8->clear();
           ui->textBrowser_9->clear();

           QDateTime dateTime0=query.value(6).toDateTime();
           QString dateTime_str0 = dateTime0.toString("yyyy-MM-dd hh:mm:ss:zzz");
           time_per=QDateTime::fromString(dateTime_str0, "yyyy-MM-dd hh:mm:ss:zzz").toTime_t();
           i=i+1;
       }
       else
       {
           int stand=query.value(5).toInt();
           //判断是否合格
           if(stand==1)
           {
               num_q=num_q+1;
               QString yes=QString::number(num_q,10);
               ui->textBrowser_7->setText(yes);//显示合格数目

           }
           else if(stand==0)
           {
               num_u=num_u+1;
               QString no=QString::number(num_u,10);
               ui->textBrowser_6->setText(no);//显示不合格数目
           }

           //判断姿势
           int w_s=query.value(7).toInt();
           waist=waist+w_s;
           QString waist_t=QString::number(wasit,10);
           int a_s=query.value(8).toInt();
           arm=arm+a_s;
           QString arm_t=QString::number(arm,10);
           int e_s=query.value(9).toInt();
           elbow=elbow+e_s;
           QString elbow_t=QString::number(elbow,10);
           int c_s=query.value(9).toInt();
           chin=chin+c_s;
           QString chin_t=QString::number(chin,10);

           QString type=query.value(3).toString();//显示科目
           if(type=="PullUp")
           {
               ui->textBrowser_5->setText("引体向上");
               ui->textBrowser_9->setText("下巴"+chin_t+"次未达到标准高度");
           }
           else if(type=="PushUp")
           {
               ui->textBrowser_5->setText("俯卧撑");
               ui->textBrowser_9->setText("肘部角度"+elbow_t+"次不标准");
           }
           else if(type=="SitUp")
           {
               ui->textBrowser_5->setText("仰卧起坐");
               ui->textBrowser_9->setText("腰部抬起幅度"+waist_t+"次不达标，手臂摆放位置"+arm_t+"次不正确");
           }

           //计算动作速率
           QDateTime dateTime=query.value(6).toDateTime();
           QString dateTime_str = dateTime.toString("yyyy-MM-dd hh:mm:ss:zzz");
           int time_now=QDateTime::fromString(dateTime_str, "yyyy-MM-dd hh:mm:ss:zzz").toTime_t();
           int time_c=time_now-time_per;
           QSqlQuery query3;
               query3.exec(QString("update speed set time=%1 where id=%2")
                           .arg(time_c)
                           .arg(i-1));
           time_per=time_now;

           int flag2=query.value(11).toInt();//判断是否继续读数
           if(flag2==1)//结束读书数据初始化
           {
                i=1;
                num_q=0;
                num_u=0;
                waist=0;
                arm=0;
                elbow=0;
                chin=0;
           }

       }//flag=0
       i++;
   }//id=i
   //画速率变化图
   QGraphicsScene *scene = new QGraphicsScene;
   QGraphicsView*view=new QGraphicsView;
   view->setWindowTitle("  ");
   view->setRenderHint(QPainter::Antialiasing);
   scene->setBackgroundBrush(QBrush(QColor(240, 240, 240)));
   view->setSceneRect(0, 0, 630, 280);
   QLineSeries *lineseries = new QLineSeries();
for(int a=0;a<i;a++)
{
   QSqlQuery query0;
       query0.exec(QString("select *from speed where id=%1").arg(a));
       query0.next();
       int spped=query0.value(1).toInt();
   QPoint point=QPoint(a,speed);
   lineseries->append(point);
}
QChart *lineChart = new QChart();
   lineChart->legend()->hide();  // 隐藏图例
   lineChart->addSeries(lineseries);  // 将 series 添加至图表中
   lineChart->createDefaultAxes();  // 基于已添加到图表的 series 来创建轴
   lineChart->setTitle("(横轴——完成个数/纵轴——平均速率)");//图表显示的标题
   lineChart->axisX()->setRange(0,a);
   lineChart->axisY()->setRange(0,10);
   lineChart->setGeometry(5, 5, 400, 260);
   scene->addItem(lineChart);
   ui->graphicsView->setScene(10);
   ui->graphicsView->show();


}
//班级的下拉列表与姓名关联
void Video::on_comboBox_2_currentIndexChanged()
{
    switch (ui->comboBox_2->currentIndex()) {
    case 1:
    {
        //与姓名的下拉列表二级关联二级关联
        ui->comboBox->clear();
        ui->comboBox->insertItem(0," ");
        ui->comboBox->insertItem(1,"甲");
        ui->comboBox->insertItem(2,"乙");
        ui->comboBox->insertItem(3,"丙");
    }
          break;
    case 2://二班
    {
        ui->comboBox->clear();
        ui->comboBox->insertItem(0," ");
        ui->comboBox->insertItem(1,"丁");
        ui->comboBox->insertItem(2,"戊");
    }

        break;        
    default:
        break;
}
}

//三个下拉列表的变化互相控制数据显示
void Video::print_info()
{
    QString title;
    QString project;
    QString banji=ui->comboBox_2->currentText();
    QString name=ui->comboBox->currentText();

    if(ui->comboBox_4->currentIndex()==1||ui->comboBox_4->currentIndex()==2||ui->comboBox_4->currentIndex()==3)
        title="1";
    else if(ui->comboBox_4->currentIndex()==4||ui->comboBox_4->currentIndex()==5||ui->comboBox_4->currentIndex()==6)
        title="2";

    if(ui->comboBox_4->currentIndex()==1||ui->comboBox_4->currentIndex()==4)
        project="SitUp";
    else if(ui->comboBox_4->currentIndex()==2||ui->comboBox_4->currentIndex()==5)
        project="PushUp";
    else if(ui->comboBox_4->currentIndex()==3||ui->comboBox_4->currentIndex()==6)
        project="PullUp";

    //显示班级总人数
                   QSqlQueryModel *model = new QSqlQueryModel;
                   model->setQuery(QString("select *from class%1").arg(banji));
                   int sum =model->rowCount()-1;
                   QString strsum=QString::number(sum,16);
                   ui->lineEdit->setText(strsum);
                   double sum1=sum;//为后面的计算做准备
    //显示缺考同学
                   QSqlQuery query;
                   query.exec(QString("select StudentName from Exam%1%2Class%3 where Grade is null")
                              .arg(title)
                              .arg(project)
                              .arg(banji));
                   QString nameout=" ";
                   while (query.next())
                   {
                       QString name = query.value(0).toString();
                       nameout=nameout+name;
                       ui->lineEdit_2->setText(nameout);
                   }

     //显示得优率
        //显示得优人数num
                    QSqlQuery query1;
                    query1.exec(QString("select StudentName from Exam%1%2Class%3 where Grade='优'")
                                .arg(title)
                                .arg(project)
                                .arg(banji));
                    int num=0;
                     while (query1.next())
                           {num++;}
                    double num_1=num;
                    double you=num_1/sum1;
                    double youlv=you*100;
                    QString stryou=QString::number(youlv,'f',2);
                    ui->lineEdit_3->setText(stryou+"%");
     //显示及格率
         //不及格人数num1
                    QSqlQuery query2;
                    query2.exec(QString("select StudentName from Exam%1%2Class%3 where Grade='不及格'")
                                .arg(title)
                                .arg(project)
                                .arg(banji));
                    int num1=0;
                    while (query2.next())
                        {num1++;}
                    double num1_1=sum1-num1;
                    double jige=num1_1/sum1;
                    double jigelv=jige*100;
                    QString strjige=QString::number(jigelv,'f',2);
                    ui->lineEdit_4->setText(strjige+"%");
    //学生信息
                    QSqlQuery query3;
                    query3.exec(QString("select* from Exam%1%2Class%3 where StudentName='%4'")
                                .arg(title)
                                .arg(project)
                                .arg(banji)
                                .arg(name));
                    query3.next();
                    QString id=query3.value(0).toString();
                    ui->lineEdit_5->setText(id);//学号
                    QString unqualified=query3.value(6).toString();
                    ui->lineEdit_6->setText(unqualified);//不合格个数
                    QString qualified=query3.value(5).toString();
                    ui->lineEdit_7->setText(qualified);//合格个数
                    QString grade=query3.value(4).toString();
                    ui->lineEdit_8->setText(grade);//成绩
                    QString analysis=query3.value(8).toString();
                    ui->textEdit->setText(analysis);//分析


}

//班级和考试标题下拉列表控制班级折线图显示
void Video::print_chart()
{
    QString project;
    QString banji=ui->comboBox_2->currentText();
    QString name=ui->comboBox->currentText();
    if(ui->comboBox_4->currentIndex()==1||ui->comboBox_4->currentIndex()==4)
        project="SitUp";
    else if(ui->comboBox_4->currentIndex()==2||ui->comboBox_4->currentIndex()==5)
        project="PushUp";
    else if(ui->comboBox_4->currentIndex()==3||ui->comboBox_4->currentIndex()==6)
        project="PullUp";
//显示班级总人数
        QSqlQueryModel *model = new QSqlQueryModel;
        model->setQuery(QString("select *from class%1").arg(banji));
        int sum =model->rowCount()-1;
        QString strsum=QString::number(sum,16);
        ui->lineEdit->setText(strsum);
        double sum1=sum;//为后面的计算做准备
  //第一次考试
            //显示得优率
                         //显示得优人数num
                       QSqlQuery query1;
                       query1.exec(QString("select StudentName from Exam1%1Class%2 where Grade='优'")
                                   .arg(project)
                                   .arg(banji));
                       int num=0;
                       while (query1.next())
                           {num++;}
                       double num_1=num;
                       double you=num_1/sum1;
                       double youlv=you*100;
                       QString stryou=QString::number(youlv,'f',2);
                       double valyou=stryou.toDouble();

           //显示及格率
                         //不及格人数num1
                       QSqlQuery query2;
                       query2.exec(QString("select StudentName from Exam1%1Class%2 where Grade='不及格'")
                                   .arg(project)
                                   .arg(banji));
                       int num1=0;
                       while (query2.next())
                           {num1++;}
                       double num1_1=sum1-num1;
                       double jige=num1_1/sum1;
                       double jigelv=jige*100;
                       QString strjige=QString::number(jigelv,'f',2);
                       double valjige=strjige.toDouble();
          //第二次考试
                       //显示得优率
                                    //显示得优人数num
                                  QSqlQuery query3;
                                  query3.exec(QString("select StudentName from Exam2%1Class%2 where Grade='优'")
                                              .arg(project)
                                              .arg(banji));
                                  int num2=0;
                                  while (query3.next())
                                      {num2++;}
                                  double num2_1=num2;
                                  double you2=num2_1/sum1;
                                  double youlv2=you2*100;
                                  QString stryou2=QString::number(youlv2,'f',2);
                                  double valyou2=stryou2.toDouble();

                      //显示及格率
                                    //不及格人数num1
                                  QSqlQuery query4;
                                  query2.exec(QString("select StudentName from Exam2%1Class%2 where Grade='不及格'")
                                              .arg(project)
                                              .arg(banji));
                                  int num3=0;
                                  while (query4.next())
                                      {num3++;}
                                  double num3_1=sum1-num3;
                                  double jige2=num3_1/sum1;
                                  double jigelv2=jige2*100;
                                  QString strjige2=QString::number(jigelv2,'f',2);
                                  double valjige2=strjige2.toDouble();
             //绘制图表

                                  QGraphicsScene *scene = new QGraphicsScene;
                                       QGraphicsView*view=new QGraphicsView;
                                       view->setWindowTitle("  ");
                                       view->setRenderHint(QPainter::Antialiasing);
                                       scene->setBackgroundBrush(QBrush(QColor(240, 240, 240)));
                                       view->setSceneRect(0, 0, 630, 280);
                                       QLineSeries *lineseries = new QLineSeries();
                                           lineseries->append(1,valyou);
                                           lineseries->append(2,valyou2);
                                       QLineSeries *lineseries2 = new QLineSeries();
                                           lineseries2->append(1,valjige );
                                           lineseries2->append(2,valjige2);
                                           QChart *lineChart = new QChart();
                                           lineChart->legend()->hide();  // 隐藏图例
                                           lineChart->addSeries(lineseries);  // 将 series 添加至图表中
                                           lineChart->createDefaultAxes();  // 基于已添加到图表的 series 来创建轴
                                           lineChart->setTitle("(横轴——考试次数/纵轴——得优率)");//图表显示的标题
                                           lineChart->setGeometry(5, 5, 400, 260);
                                           QChart *lineChart2 = new QChart();
                                           lineChart2->legend()->hide();  // 靠右
                                           lineChart2->addSeries(lineseries2);  // 将 series 添加至图表中
                                           lineChart2->createDefaultAxes();  // 基于已添加到图表的 series 来创建轴
                                           lineChart2->setTitle("(横轴——考试次数/纵轴——及格率)");//图表显示的标题
                                           lineChart2->setGeometry(410, 5, 400, 260);
                                            scene->addItem(lineChart);
                                            scene->addItem(lineChart2);
                                            ui->graphicsView_6->setScene(scene);
                                            ui->graphicsView_6->show();

 }


