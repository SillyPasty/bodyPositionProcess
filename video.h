#ifndef VIDEO_H
#define VIDEO_H

#include <QWidget>
#include<QTimer>


namespace Ui {
class Video;
}

class Video : public QWidget
{
    Q_OBJECT
    QTimer*timer;

public:
    explicit Video(QWidget *parent = 0);
    ~Video();



private slots:
    void on_comboBox_2_currentIndexChanged();
    void print_info();
    void print_chart();
    void now_info();

private:
    Ui::Video *ui;

};


#endif // VIDEO_H
