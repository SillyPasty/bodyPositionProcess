#ifndef MYTESTMODEL_H
#define MYTESTMODEL_H

#include <QAbstractTableModel>

class MyTestModel : public QAbstractTableModel
{
    Q_OBJECT
public:
    MyTestModel();

    void setMyData(int idata);
    QVariant data(const QModelIndex &item, int role) const;
    int rowCount(const QModelIndex &parent = QModelIndex()) const;
    int columnCount(const QModelIndex &parent = QModelIndex()) const;
private:
    int iRow;
    int iCol;
};

#endif // MYTESTMODEL_H
