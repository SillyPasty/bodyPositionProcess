#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include"e_box.h"
#include"video.h"
#include"file.h"

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();

private:
    Ui::Widget *ui;
    E_box*e_box;
    Video*video;
    File*file;


};

#endif // WIDGET_H
