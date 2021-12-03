import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.gear_stats = ["Stat 1: ", "Stat 2: ", "Stat 3: ", "Stat 4: ", "Speed: ", "Crit.Chance(%): ", "Upgrade Level: ", "Item Level: "]
        self.upgrade_level = ["0", "3", "6", "9", "12"]
        self.push_button = ["Reset", "Calculate", "Exit"]
        self.item_level = ["85", "88"]
        self.all_stats_label = []
        self.all_stats_input_value = []
        self.all_upgrade_level_button = []
        self.all_calculate_button = []
        self.all_item_level_button = []
        self.layout_calculate_button = QGridLayout()
        self.layout_upgrade_level_button = QHBoxLayout()
        self.layout_for_stats_button = QGridLayout()
        self.layout_for_result = QVBoxLayout()
        self.layout_for_item_level = QHBoxLayout()
        self.mainLayout = QVBoxLayout()
        self.widget = QWidget()
        self.WSS_result_label = QLabel()
        self.final_result_label = QLabel()

        self.item_level_input = 0
        self.upgrade_level_input = 0

    def create_label_and_input_for_stats(self):
        for stats in range(0,len(self.gear_stats)):
            stats_label = QLabel(self.gear_stats[stats])
            self.all_stats_label.append(stats_label)
            self.all_stats_input_value.append(QLineEdit())
            self.layout_for_stats_button.addWidget(self.all_stats_label[stats], stats, 0)
            self.layout_for_stats_button.addWidget(self.all_stats_input_value[stats], stats, 1)

    def create_label_and_button_for_upgrade_level(self):
        for level in range(0, len(self.upgrade_level)):
            upgrade_level_button = QPushButton(self.upgrade_level[level])
            self.all_upgrade_level_button.append(upgrade_level_button)
            self.layout_upgrade_level_button.addWidget(self.all_upgrade_level_button[level])
    
    def create_calculate_button(self):
        for button in range(0,len(self.push_button)):
            temp_button = QPushButton(self.push_button[button])
            self.all_calculate_button.append(temp_button)
            self.layout_calculate_button.addWidget(self.all_calculate_button[button],0 , button)

    def create_item_level_button(self):
        for button in range(0,len(self.item_level)):
            temp_button = QPushButton(self.item_level[button])
            self.all_item_level_button.append(temp_button)
            self.layout_for_item_level.addWidget(self.all_item_level_button[button])

    def create_layout_for_result(self):
        self.layout_for_result.addWidget(self.WSS_result_label)
        self.layout_for_result.addWidget(self.final_result_label)

    def add_each_layout_to_main_layout(self):
        self.mainLayout.addLayout(self.layout_for_stats_button)
        self.mainLayout.addLayout(self.layout_upgrade_level_button)
        self.mainLayout.addLayout(self.layout_for_item_level)
        self.mainLayout.addLayout(self.layout_calculate_button)
        self.mainLayout.addLayout(self.layout_for_result)

    def calculate_result_for_item_88(self, WSS_value):
        if self.item_level_input == 88:
            if self.upgrade_level_input == 0 and WSS_value >= 22:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 22))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 3 and WSS_value >= 29:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 29))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 6 and WSS_value >= 36:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 36))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 9 and WSS_value >= 42:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 42))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 12 and WSS_value >= 48:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 48))
                self.final_result_label.setStyleSheet("color: green;")
            else:
                self.final_result_label.setText("SELL")
        else:
            self.final_result_label.setText("INVALID CASE")

    def calculate_result_for_item_85(self, WSS_value):
        if self.item_level_input == 85:
            if self.upgrade_level_input == 0 and WSS_value >= 20:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 20))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 3 and WSS_value >= 26:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 26))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 6 and WSS_value >= 32:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 32))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 9 and WSS_value >= 38:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 38))
                self.final_result_label.setStyleSheet("color: green;")
            elif self.upgrade_level_input == 12 and WSS_value >= 44:
                self.final_result_label.setText("UPGRADEABLE: Result WSS: {} >= {}".format(WSS_value, 44))
                self.final_result_label.setStyleSheet("color: green;")
            else:
                self.final_result_label.setText("SELL")
                self.final_result_label.setStyleSheet("color: red;")
        else:
            self.final_result_label.setText("INVALID CASE")
            self.final_result_label.setStyleSheet("color: red;")

    
    def calculate_final_result(self, WSS_value):
        if self.item_level_input == 85:
            self.calculate_result_for_item_85(WSS_value)
        elif self.item_level_input == 88:
            self.calculate_result_for_item_88(WSS_value)
        else:
            self.final_result_label.setText("MISSING ITEM LEVEL")
            self.final_result_label.setStyleSheet("color: red;")
        

    def calculate_button_onClicked(self):
        result = 0
        for stats in range(0,len(self.gear_stats) - 2):
            if self.all_stats_input_value[stats].text(): 
                if self.gear_stats[stats] == "Speed: ":
                    result += (int(self.all_stats_input_value[stats].text()) * 2)
                elif self.gear_stats[stats] == "Crit.Chance(%): ":
                    result += (int(self.all_stats_input_value[stats].text()) * 1.5)
                else:
                    result += int(self.all_stats_input_value[stats].text())
            else:
                result += 0
        
        if result != 0:
            self.WSS_result_label.setText("Current gear WSS: " + (str(result)))
            self.calculate_final_result(result)
        else:
            self.WSS_result_label.setText("Please input stats")

    def reset_button_onClicked(self):
        for input_value in range(0, len(self.all_stats_input_value)):
            self.all_stats_input_value[input_value].clear()
        self.WSS_result_label.clear()

    def upgrade_level_onClicked(self, number):
        for input_value in range(0, len(self.gear_stats)):
            if self.gear_stats[input_value] == "Upgrade Level: ":
                self.all_stats_input_value[input_value].setText(str(number))
                self.upgrade_level_input = number

    def exit_button_onClicked(self):
        app.quit()

    def item_level_onClicked(self, number):
        for input_value in range(0, len(self.gear_stats)):
            if self.gear_stats[input_value] == "Item Level: ":
                if number == 1:
                    self.all_stats_input_value[input_value].setText(str(88))
                    self.item_level_input = 88
                else:
                    self.all_stats_input_value[input_value].setText(str(85))
                    self.item_level_input = 85

    def add_function_to_each_button(self):
        self.all_calculate_button[1].clicked.connect(self.calculate_button_onClicked)
        self.all_calculate_button[0].clicked.connect(self.reset_button_onClicked)
        self.all_calculate_button[2].clicked.connect(self.exit_button_onClicked)

        for button in range(0, len(self.all_upgrade_level_button)):
            #clicked[bool] is a MUST with pyside, no need with PyQT
            self.all_upgrade_level_button[button].clicked[bool].connect(lambda checked, number = button: self.upgrade_level_onClicked(number*3))

        for button in range(0, len(self.all_item_level_button)):
            #clicked[bool] is a MUST with pyside, no need with PyQT
            self.all_item_level_button[button].clicked[bool].connect(lambda checked, number = button: self.item_level_onClicked(number))

    def setting_main_layout(self):
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

    def create_and_show(self):
        self.create_label_and_input_for_stats()
        self.create_label_and_button_for_upgrade_level()
        self.create_calculate_button()
        self.create_item_level_button()
        self.create_layout_for_result()
        self.add_function_to_each_button()
        self.add_each_layout_to_main_layout()
        self.setting_main_layout()

mainProgram = MainWindow()
mainProgram.create_and_show()
mainProgram.show()
app.exec_()
