#ifndef IDENTITY_H
#define IDENTITY_H

#include <QDialog>

namespace Ui {
class Identity;
}

class Identity : public QDialog
{
    Q_OBJECT

public:
    explicit Identity(QWidget *parent = 0);
    ~Identity();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::Identity *ui;
};

#endif // IDENTITY_H
