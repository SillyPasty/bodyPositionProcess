#include "e_box.h"
#include "ui_e_box.h"

E_box::E_box(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::E_box)
{
    ui->setupUi(this);
}

E_box::~E_box()
{
    delete ui;
}
