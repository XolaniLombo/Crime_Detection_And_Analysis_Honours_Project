import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Booster import DetectorBooster, AnalyzorBooster


class OtherWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Social Media Message Crime Detector and Analyse")
        self.setGeometry(100, 50, 400, 600)
        self.show()
        self.detection_booster = None
        self.analysis_booster = None
        self.is_file_chosen = False


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Social Media Message Crime Detector and Analyse")

        btn = QPushButton("Open File")
        self.report_txt = QPlainTextEdit()
        self.report_txt.setStyleSheet("font-size: 14px; margin:15; border-color: #042b6e ;border-width: 2px")
        btn.setStyleSheet("background-color: #6e043b;"
                          " color:white;font-weight:bold ;"
                          "font-size:15px; max-height: 50px;max-width: 150px; border-radius:10px")
        detect_btn = QPushButton("Detect Crime")
        detect_btn.setStyleSheet("background-color: #046e30; color:white;font-weight:bold ;"
                                 "font-size:15px;height: 50px;max-width: 150px")
        analyse_btn = QPushButton("Analyse Crime")
        analyse_btn.setStyleSheet("background-color: #04636e;color:white;font-weight:bold ;"
                                  "font-size:15px;height: 50px;max-width: 150px;")
        header = QLabel("Crime Detector and Analyser")
        header.setFont(QFont('Times', 30))
        header.setStyleSheet("font-weight: bold;color: #042b6e; margin:35")

        self.file_name_lbl = QLabel("**please choose file containing messages**")

        layout = QGridLayout()
        layout.addWidget(header, 1, 1)
        layout.addWidget(self.file_name_lbl, 2, 1)
        layout.addWidget(btn, 3, 3)
        layout.addWidget(detect_btn, 3, 0)
        layout.addWidget(analyse_btn, 3, 1)
        layout.addWidget(self.report_txt, 4, 1)

        widget = QWidget()
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet('background-color: #d8dce3;')

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        btn.clicked.connect(self.openFile)  # connect clicked to self.open()
        detect_btn.clicked.connect(self.printDetectionReport)
        analyse_btn.clicked.connect(self.printAnalysisReport)

        self.setGeometry(230, 50, 500, 700)
        self.show()

    def openFile(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])
            self.file_name_lbl.setText(path[0])
            self.detection_booster = DetectorBooster(filename=path[0])
            self.analysis_booster = AnalyzorBooster(filename=path[0])
            self.is_file_chosen = True

    def printDetectionReport(self):

        if self.is_file_chosen:
            num = 1
            report = "~~~~~~~~~~~~~~~~~~~~~Crime Detection Report~~~~~~~~~~~\n\n\n"
            crime_list, rate = self.detection_booster.detect()

            report += "<<<<Crime Related Messages>>>>\n\n"
            for m in crime_list:
                report += str(num) + ". " + m + "\n"
                num += 1
            rate = str(round(rate * 100, 2))

            report += "\n\n#Crime % Detected Is= " + rate + "%"

            self.report_txt.setPlainText(report)
        else:
            self.report_txt.setPlainText("******Choose file first****")

    def printAnalysisReport(self):
        if self.is_file_chosen:
            report = "~~~~~~~~~~~~~~~~~~~~~Crime Analysis Report~~~~~~~~~~~\n\n\n"
            attack_list, drug_list, a_rate, d_rate = self.analysis_booster.analyse()

            num = 1
            report += "<<<<Attack Related Messages>>>>\n\n"
            for m in attack_list:
                report += str(num) + ". " + m + "\n"
                num += 1
            a_rate = str(round(a_rate * 100, 2))
            report += "\n #Attack Related Crime % Detected Is= " + a_rate + "%\n\n\n"

            num = 1
            report += "<<<<Drug Related Messages>>>>>\n\n"
            for m in drug_list:
                report += str(num) + ". " + m + "\n"
                num += 1
            d_rate = str(round(d_rate * 100, 2))
            report += "\n #Drug Related Crime % Detected Is= " + d_rate + "%"

            self.report_txt.setPlainText(report)
        else:
            self.report_txt.setPlainText("******Choose file first****")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
