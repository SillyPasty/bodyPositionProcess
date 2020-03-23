#ifndef E_BOX_H
#define E_BOX_H

#include <QWidget>

namespace Ui {
class E_box;
}

class E_box : public QWidget
{
    Q_OBJECT

public:
    explicit E_box(QWidget *parent = 0);
    ~E_box();

private:
    Ui::E_box *ui;
};

#endif // E_BOX_H
