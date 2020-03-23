#ifndef STUDENT_H
#define STUDENT_H

#include "video_s.h"
#include "file_s.h"
#include "e_box_s.h"

#include <QWidget>

namespace Ui {
class Student;
}

class Student : public QWidget
{
    Q_OBJECT

public:
    explicit Student(QWidget *parent = 0);
    ~Student();

private:
    Ui::Student *ui;
    E_box_s*e_box_s;
    Video_s*video_s;
    File_s*file_s;


};

#endif // STUDENT_H
