#ifndef E_BOX_S_H
#define E_BOX_S_H

#include <QWidget>

namespace Ui {
class E_box_s;
}

class E_box_s : public QWidget
{
    Q_OBJECT

public:
    explicit E_box_s(QWidget *parent = 0);
    ~E_box_s();

private:
    Ui::E_box_s *ui;
};

#endif // E_BOX_S_H
