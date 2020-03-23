#ifndef VIDEO_S_H
#define VIDEO_S_H

#include <QWidget>

namespace Ui {
class Video_s;
}

class Video_s : public QWidget
{
    Q_OBJECT

public:
    explicit Video_s(QWidget *parent = 0);
    ~Video_s();


private slots:
    void print_info();
    void print_chart();



private:
    Ui::Video_s *ui;
};

#endif // VIDEO_S_H
