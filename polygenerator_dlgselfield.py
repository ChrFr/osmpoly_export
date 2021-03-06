# -*- coding: utf-8 -*-

#******************************************************************************
#
# osmpoly_export
# ---------------------------------------------------------
# Export vector polygons to poly-files used by Osmosis for cliping OpenStreetMap data
#
# Author: 2008-2016 Maxim Dubinin (maxim.dubinin@nextgis.com)
# Copyright (C) NextGIS (info@nextgis.com)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
#******************************************************************************

from PyQt5.QtWidgets import (QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton,
                             QDialog, QRadioButton)



class dlgSelField(QDialog):
    def __init__(self, myFieldsNames, parent=None):
        QDialog.__init__(self)
        gr = QGroupBox(self)
        vbox = QVBoxLayout(gr)
        names = myFieldsNames
        self.rbl = [QRadioButton(name, gr) for name in names]
        self.rbl[0].setChecked(True)
        for rb in self.rbl: vbox.addWidget(rb)
        gr.adjustSize()

        hbox = QHBoxLayout()
        pbnYes = QPushButton('Yes', self)
        pbnCancel = QPushButton('Cancel', self)
        hbox.addWidget(pbnYes)
        hbox.addWidget(pbnCancel)

        layout = QVBoxLayout(self)
        layout.addWidget(gr)
        layout.addLayout(hbox)

        pbnYes.clicked.connect(self.accept)
        pbnCancel.clicked.connect(self.reject)
    def selectedAttr(self):
        for rb in self.rbl:
            if rb.isChecked():
                return rb.text()
