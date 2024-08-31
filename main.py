import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QStackedWidget,
    QListWidget,
    QListWidgetItem,
)

from app.pages import OverviewPage, WaterBottlePage


class WaterBottleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-Page Water Bottle Tracker")
        self.setGeometry(300, 300, 600, 400)

        # QStackedWidget을 사용하여 여러 페이지 관리
        self.pages = QStackedWidget()

        # 각 페이지 생성 (서로 다른 색상)
        colors = ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f"]
        self.page_widgets = [WaterBottlePage(color) for color in colors]

        # 페이지 로드
        for page in self.page_widgets:
            page.load_water_data()
            self.pages.addWidget(page)

        # Overview 페이지 생성
        self.overview_page = OverviewPage(self.page_widgets)
        self.pages.addWidget(self.overview_page)

        # 네비게이션 바 설정 (QListWidget)
        self.nav_list = QListWidget()
        nav_items = [f"Page {i+1}" for i in range(len(self.page_widgets))] + [
            "Overview"
        ]
        for i, name in enumerate(nav_items):
            item = QListWidgetItem(name)
            self.nav_list.addItem(item)

        self.nav_list.currentRowChanged.connect(self.change_page)
        self.nav_list.setFixedWidth(120)

        # 레이아웃 설정
        layout = QHBoxLayout()
        layout.addWidget(self.nav_list)
        layout.addWidget(self.pages)

        # QWidget 설정 및 메인 윈도우에 레이아웃 적용
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def change_page(self, index):
        # 페이지 전환
        self.pages.setCurrentIndex(index)

        # Overview 페이지로 이동 시 각 물병 상태를 업데이트
        if index == len(self.page_widgets):
            self.update_overview_page()

    def update_overview_page(self):
        # Overview 페이지의 물병 상태 업데이트
        for i, page in enumerate(self.page_widgets):
            bottle_state = self.overview_page.layout().itemAt(i).widget()
            bottle_state.setValue(page.current_water)
            bottle_state.setStyleSheet(page.water_bottle.styleSheet())


def main():
    app = QApplication(sys.argv)
    window = WaterBottleApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
