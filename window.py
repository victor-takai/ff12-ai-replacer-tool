
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QFrame, QGridLayout, QPushButton, QComboBox, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from action_ai import Action
from target_condition_ai import TargetCondition
from ai import TargetType
from main import find_and_edit_files
from version import __version__

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"FFXII AI Replacer Tool v{__version__}")
        self.setGeometry(200, 200, 800, 150)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(5)
        
        self.grid_frame_1 = QFrame()
        self.grid_layout_1 = QGridLayout(self.grid_frame_1)
        self.create_grid_labels(self.grid_layout_1, "Original")
        self.combo_boxes_original = self.create_combo_box_set(self.grid_layout_1, action_stretch=35, condition_stretch=35, target_stretch=30, default_values=True)
        self.layout.addWidget(self.grid_frame_1)
        
        self.grid_frame_2 = QFrame()
        self.grid_layout_2 = QGridLayout(self.grid_frame_2)
        self.create_grid_labels(self.grid_layout_2, "Replace")
        self.combo_boxes_replace = self.create_combo_box_set(self.grid_layout_2, action_stretch=35, condition_stretch=35, target_stretch=30)
        self.layout.addWidget(self.grid_frame_2)
        
        self.edit_button = QPushButton("Replace AI")
        self.layout.addWidget(self.edit_button)
        
        self.edit_button.clicked.connect(self.edit_button_clicked)
        
        self.grid_frame_1.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.grid_frame_2.setStyleSheet("background-color: rgb(211, 211, 211);")

        self.name_label = QLabel("Made by Kalivos")
        self.name_label.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.name_label)
    
    def create_grid_labels(self, layout, text):
        label = QLabel(text)
        label.setStyleSheet("font-weight: bold; font-size: 14px; color: darkblue;")
        layout.addWidget(label, 0, 0, 1, 3)

    def create_combo_box_set(self, layout, action_stretch, condition_stretch, target_stretch, default_values=False):
        enum_maps = {
            "Action": Action,
            "Target Condition": TargetCondition,
            "Target Type": TargetType
        }

        self.enum_name_to_value = {}

        for title, enum_values in enum_maps.items():
            self.enum_name_to_value[title] = enum_values

        if default_values:
            original_defaults = {
                "Action": Action.ADD_AUGMENT_ACCURACY_BOOST,
                "Target Condition": TargetCondition.AUGMENT_ACCURACY_BOOST_IS_MISSING,
                "Target Type": TargetType.SELF
            }
        else:
            original_defaults = {}

        replace_defaults = {
            "Action": Action.ADD_AUGMENT_UNUSED,
            "Target Condition": TargetCondition.AUGMENT_UNUSED_IS_MISSING,
            "Target Type": TargetType.SELF
        }

        combo_boxes = {}  # Dictionary to store combo boxes

        for col, title in enumerate(enum_maps.keys()):
            title_label = QLabel(title)
            combo_box = QComboBox()

            layout.addWidget(title_label, 1, col)
            layout.addWidget(combo_box, 2, col)

            enum_values = enum_maps[title]
            for enum_member in enum_values:
                combo_box.addItem(enum_member.name)

            if default_values:
                combo_box.setCurrentIndex(combo_box.findText(original_defaults[title].name))
            else:
                combo_box.setCurrentIndex(combo_box.findText(replace_defaults[title].name))

            if title == "Action":
                layout.setColumnStretch(col, action_stretch)
                combo_box.setMinimumWidth(int(self.width() * action_stretch / 100))
            elif title == "Target Condition":
                layout.setColumnStretch(col, condition_stretch)
                combo_box.setMinimumWidth(int(self.width() * condition_stretch / 100))
            elif title == "Target Type":
                layout.setColumnStretch(col, target_stretch)
                combo_box.setMinimumWidth(int(self.width() * target_stretch / 100))

            # Store the combo box in the dictionary
            combo_boxes[title] = combo_box

        layout.setSpacing(5)
    
        return combo_boxes  # Return the dictionary of combo boxes

    def get_enum_from_combo_box(self, combo_box, enum_title):
        selected_text = combo_box.currentText()
        enum_values_map = self.enum_name_to_value[enum_title]
        enum_value = enum_values_map[selected_text]
        return enum_value

    def edit_button_clicked(self):
        input_folder = "unpacked"
        target_filename = "section_003.json"
        output_folder = "edited"

        find_action = self.get_enum_from_combo_box(self.combo_boxes_original["Action"], "Action")
        find_condition = self.get_enum_from_combo_box(self.combo_boxes_original["Target Condition"], "Target Condition")
        find_target = self.get_enum_from_combo_box(self.combo_boxes_original["Target Type"], "Target Type")
        action_replace = self.get_enum_from_combo_box(self.combo_boxes_replace["Action"], "Action")
        condition_replace = self.get_enum_from_combo_box(self.combo_boxes_replace["Target Condition"], "Target Condition")
        target_replace = self.get_enum_from_combo_box(self.combo_boxes_replace["Target Type"], "Target Type")

        if any(os.listdir(output_folder)):
            reply = QMessageBox.warning(
                self,
                "Warning",
                "It seems there are already edited files in the folder. Proceeding will override the files, do you want to continue?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.edit_ai(
                    input_folder, output_folder, target_filename,
                    find_action, find_condition, find_target,
                    action_replace, condition_replace, target_replace
                )
        else:
            self.edit_ai(
                input_folder, output_folder, target_filename,
                find_action, find_condition, find_target,
                action_replace, condition_replace, target_replace
            )

    def edit_ai(self, input_folder, output_folder, target_filename, find_action, find_condition, find_target, action_replace, condition_replace, target_replace):        
        find_and_edit_files(
            input_folder, output_folder, target_filename, 
            find_action, find_condition, find_target, 
            action_replace, condition_replace, target_replace
        )

        QMessageBox.information(self, "Info", "AI replaced!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
