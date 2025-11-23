from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 616)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Form)
        self.webEngineView.setUrl(QtCore.QUrl("https://www.openstreetmap.org/"))
        self.webEngineView.setObjectName("webEngineView")
        self.horizontalLayout.addWidget(self.webEngineView)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "VasMaps"))
from PyQt5 import QtWebEngineWidgets