from PyQt6.QtWidgets import (
   QVBoxLayout, QWidget,
    QProgressBar, QStackedWidget, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import Qt


class OverviewPage(QWidget):
    def __init__(self, pages):
        super().__init__()
        layout = QVBoxLayout()

        # 각 페이지의 물병 상태를 표시
        for page in pages:
            bottle_state = QProgressBar(self)
            bottle_state.setOrientation(Qt.Orientation.Horizontal)
            bottle_state.setMinimum(0)
            bottle_state.setMaximum(100)
            bottle_state.setValue(page.current_water)
            bottle_state.setStyleSheet(page.water_bottle.styleSheet())
            layout.addWidget(bottle_state)

        self.setLayout(layout)