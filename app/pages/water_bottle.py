import os

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QProgressBar
from PyQt6.QtCore import Qt


class WaterBottlePage(QWidget):
    def __init__(self, color, initial_water=50):
        super().__init__()

        self.current_water = initial_water

        # 물병 ProgressBar 생성 (가로형) 및 색상 설정
        self.water_bottle = QProgressBar(self)
        self.water_bottle.setOrientation(Qt.Orientation.Horizontal)
        self.water_bottle.setMinimum(0)
        self.water_bottle.setMaximum(100)
        self.water_bottle.setValue(self.current_water)
        self.water_bottle.setStyleSheet(
            f"""
            QProgressBar::chunk {{
                background-color: {color};
            }}
        """
        )

        # 여러 버튼 생성 (양이 다른 버튼들)
        self.buttons = {
            "Small Fill (+5)": 5,
            "Medium Fill (+10)": 10,
            "Large Fill (+20)": 20,
            "Small Remove (-5)": -5,
            "Medium Remove (-10)": -10,
            "Large Remove (-20)": -20,
        }

        button_layout = QHBoxLayout()
        for label, value in self.buttons.items():
            button = QPushButton(label)
            button.clicked.connect(lambda _, v=value: self.adjust_water(v))
            button_layout.addWidget(button)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.water_bottle)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def adjust_water(self, amount):
        # 물의 양 조정
        new_water_level = self.current_water + amount
        if 0 <= new_water_level <= 100:
            self.current_water = new_water_level
            self.update_water_bottle()

    def update_water_bottle(self):
        self.water_bottle.setValue(self.current_water)
        print(os.getcwd())

        # 데이터 저장 로직
        with open(f"data/water_data_{id(self)}.txt", "w") as file:
            file.write(str(self.current_water))

    def load_water_data(self):
        try:
            with open(f"data/water_data_{id(self)}.txt", "r") as file:
                self.current_water = int(file.read())
                self.update_water_bottle()
        except FileNotFoundError:
            self.current_water = 50
            self.update_water_bottle()
