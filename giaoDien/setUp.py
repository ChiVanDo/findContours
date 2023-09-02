import sys
import cv2
import numpy as np
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class WebcamApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam Display")
        self.setGeometry(100, 100, 640, 480)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.video_label = QLabel(self)
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.video_label)
        central_widget.setLayout(central_layout)

        self.video_capture = cv2.VideoCapture(0)  # Sử dụng webcam mặc định (0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Tần số cập nhật khung hình (30 ms)

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.video_label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    window = WebcamApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
