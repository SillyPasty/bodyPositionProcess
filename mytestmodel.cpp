#include "mytestmodel.h"
#include <QVariant>
#include <QColor>

MyTestModel::MyTestModel()
    :iRow(400),iCol(7)
{
}

QVariant MyTestModel::data(const QModelIndex &index, int role) const
{
    switch(role)
    {
    case Qt::DisplayRole:
        return QVariant(QString(tr("String%1")).arg((index.column() + 1) * 1000 + index.row() + 1));
    case Qt::ForegroundRole:
        switch(index.column() % 3)
        {
        case 0:
            return QVariant(QColor(Qt::red));
        case 1:
            return QVariant(QColor(Qt::green));
        case 2:
            return QVariant(QColor(Qt::blue));
        default://only to disable warning
            return QVariant(QColor(Qt::white));
        }

        break;
    default:
        return QVariant();
    }
}


int MyTestModel::rowCount(const QModelIndex & /*parent*/) const
{
        return iRow;
}


int MyTestModel::columnCount(const QModelIndex & /*parent*/) const
{
        return iCol;
}

void MyTestModel::setMyData(int idata)
{
    iRow = idata;
    //emit dataChanged(createIndex(0,0), createIndex(iRow,iCol));

}
