#-------------------------------------------------
#
# Project created by QtCreator 2019-12-17T15:35:34
#
#-------------------------------------------------

QT       += core gui axcontainer  sql charts


greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = teacher
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        main.cpp \
        widget.cpp \
    file.cpp \
    e_box.cpp \
    video.cpp \
    exportexcelobject.cpp \
    mytestmodel.cpp \
    identity.cpp \
    login_s.cpp \
    student.cpp \
    login_t.cpp \
    e_box_s.cpp \
    video_s.cpp \
    file_s.cpp

HEADERS += \
        widget.h \
    file.h \
    e_box.h \
    video.h \
    exportexcelobject.h \
    mytestmodel.h \
    identity.h \
    login_s.h \
    student.h \
    login_t.h \
    e_box_s.h \
    video_s.h \
    file_s.h

FORMS += \
        widget.ui \
    e_box.ui \
    video.ui \
    file.ui \
    identity.ui \
    login_s.ui \
    student.ui \
    login_t.ui \
    e_box_s.ui \
    video_s.ui \
    file_s.ui
