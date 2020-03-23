// Copyright (c) 2010 Joel Gao <joel_gao@sina.com>
// MyTableView is a subclass of QTableView
// You can use this class to print easily
//
// I don't know much about the license part
// I think you can use this piece of code for FREE
// But
// Some of the code of this class "MyTableView" is from "textprinter"
// by David Johnson <david@usermode.org>
// see the copyright and license information below
//
// Copyright (c) 2007 David Johnson <david@usermode.org>
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions
// are met:
//
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
///////////////////////////////////////////////////////////////////////////////

#ifndef MYTABLEVIEW_H
#define MYTABLEVIEW_H

#include <QTableView>
#include <QPrinter>

class MyTableView : public QTableView
{
    Q_OBJECT
public:
    MyTableView();
    ~MyTableView();

    // Print the view
    void print_print(const QString &caption=QString());

    // Export the document to PDF
    void print_exportPdf( const QString &caption=QString(),
                          const QString &filename=QString());
    // Display the document in a preview dialog
    void print_preview(const QString &caption=QString());

public Q_SLOTS:
    void print_print(QPrinter *printer);

public:
    // Get page size
    QPrinter::PageSize print_pageSize() const;
    // Set page size
    void print_setPageSize(QPrinter::PageSize size);

    // Get page orientation
    QPrinter::Orientation print_orientation() const;
    // Set page orientation
    void print_setOrientation(QPrinter::Orientation orientation);

    // Get left margin width
    double print_leftMargin() const;
    // Set left margin width
    void print_setLeftMargin(double margin);

    // Get right margin width
    double print_rightMargin() const;
    // Set right margin width
    void print_setRightMargin(double margin);

    // Get top margin width
    double print_topMargin() const;
    // Set top margin width
    void print_setTopMargin(double margin);

    // Get bottom margin width
    double print_bottomMargin() const;
    // Set bottom margin width
    void print_setBottomMargin(double margin);

    // Set all margins
    void print_setMargins(double margin);

    // Get spacing between content and header and footer
    double print_spacings() const;
    // Set spacing between content and header and footer
    void print_setSpacings(double spacing);

    // Get header size
    double print_headerSize() const;
    // Set header size
    void print_setHeaderSize(double size);

    // Set header rule size
    double print_headerRule() const;
    // Get header rule size
    void print_setHeaderRule(double pointsize);

    // Get header text
    const QString &print_headerText() const;
    // Set header text
    void print_setHeaderText(const QString &text);

    // Get footer size
    double print_footerSize() const;
    // Set footer size
    void print_setFooterSize(double size);

    // Get footer rule size
    double print_footerRule() const;
    // Set footer rule size
    void print_setFooterRule(double pointsize);

    // Get footer text
    const QString &print_footerText() const;
    // Set footer text
    void print_setFooterText(const QString &text);

private:
    // return paper rect
    QRectF print_paperRect(QPaintDevice *device);
    // return printable rects
    QRectF print_contentRect(QPaintDevice *device);
    QRectF print_headerRect(QPaintDevice *device);
    QRectF print_footerRect(QPaintDevice *device);

    // paint specific page
    void print_paintPage(QPainter *painter, int pagenum);
private:
    QPrinter *print_printer;

    double print_leftmargin;
    double print_rightmargin;
    double print_topmargin;
    double print_bottommargin;
    double print_spacing;

    double print_headersize;
    double print_headerrule;
    QString print_headertext;
    double print_footersize;
    double print_footerrule;
    QString print_footertext;

    int print_currow;
    int print_curcol;
};

#endif // MYTABLEVIEW_H
