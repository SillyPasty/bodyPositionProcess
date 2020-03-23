#include "e_box_s.h"
#include "ui_e_box_s.h"

E_box_s::E_box_s(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::E_box_s)
{
    ui->setupUi(this);
}

E_box_s::~E_box_s()
{
    delete ui;
}
