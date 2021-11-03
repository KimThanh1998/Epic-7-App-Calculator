import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Epic 7 App Calculator")

        gear_stats = ["Attack(%): ", "Defence(%): ", "HP(%): ", "Effective(%): ", "Resistance(%): ", "Speed: ", "Crit.Chance(%): ", "Crit.Damg(%): "]

        all_stats_label = []
        all_stats_input_value = []
        layout = QGridLayout()

        for stats in range(0,len(gear_stats)):
            stats_label = QLabel(gear_stats[stats])
            all_stats_label.append(stats_label)
            all_stats_input_value.append(QLineEdit())
            layout.addWidget(all_stats_label[stats], stats, 0)
            layout.addWidget(all_stats_input_value[stats], stats, 1)

        push_button = ["Reset", "Calculate", "Exit"]
        all_button = []

        for button in range(0,len(push_button)):
            temp_button = QPushButton(push_button[button])
            all_button.append(temp_button)
            layout.addWidget(all_button[button], len(gear_stats) + 1, button)

        def calculate_button_onClicked():
            result = 0
            result_label = QLabel()
            for stats in range(0,len(gear_stats)):
                if all_stats_input_value[stats].text(): 
                    if gear_stats[stats] == "Speed: ":
                        result += (int(all_stats_input_value[stats].text()) * 2)
                    elif gear_stats[stats] == "Crit.Chance(%): ":
                        result += (int(all_stats_input_value[stats].text()) * 1.5)
                    else:
                        result += int(all_stats_input_value[stats].text())
                else:
                    result += 0
            
            if result != 0:
                result_label = QLabel("Current gear WSS: " + (str(result)))
            else:
                result_label = QLabel("Please input stats")

            layout.addWidget(result_label, len(gear_stats) + 2, 0)

        all_button[1].clicked.connect(calculate_button_onClicked)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
mainProgram = MainWindow()
mainProgram.show()
app.exec_()
