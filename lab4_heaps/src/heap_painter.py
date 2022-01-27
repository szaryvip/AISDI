from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGraphicsSimpleTextItem, QGraphicsScene
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from ui_mapview import MapView
from math import log, floor
from heap import Heap


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Map of the heap")

        self.main_widget = QWidget()
        self.appBox = QVBoxLayout()
        self.appBox.maximumSize()
        self.main_widget.setLayout(self.appBox)

        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.map = MapView(self.page)
        self.appBox.addWidget(self.map)

        self._scene = QGraphicsScene()
        self.map.setScene(self._scene)
        self.map.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self.main_widget)

    def _get_width(self, height: int, num_child: int) -> int:
        return (num_child**(height-1))-1

    def _draw_node(self, value, x: float, y: float):
        """
        Drawing the Node on the map.
        """
        text_item = QGraphicsSimpleTextItem()

        font = text_item.font()
        font.setPointSize(font.pointSize()-2)
        font.setPixelSize(self._font_size)

        text_item.setText(str(value))
        text_item.setPos(x, y)
        text_item.setFont(font)

        self._scene.addItem(text_item)

    def _draw_line(self, x1: float, y1: float, x2: float, y2: float):
        """
        Drawing line from (x1, y1) point to (x2, y2) point.
        """
        self._scene.addLine(x1, y1, x2, y2)

    def draw_heap(self, heap, num_child: int, font_size=20):
        """
        Drawing heap.
        """
        if heap == []:
            return
        self._font_size = font_size
        height = floor(log(len(heap), num_child)) + 1
        width = self._get_width(height, num_child)*num_child
        print(width)
        dist = 75
        x = 0
        start = y = 0
        elements_counter = 1
        elements_limit = 1
        actual_elements = []
        last_elements = []
        while heap != []:
            element = heap.pop(0)
            actual_elements.append((x*dist, y*dist))
            self._draw_node(element, x*dist, y*dist)
            if 0 != y:
                x2, y2 = last_elements[(elements_counter-1)//num_child]
                self._draw_line(x*dist, y*dist, x2, y2)

            if elements_counter == elements_limit:
                print(last_elements)
                last_elements = actual_elements
                actual_elements = []
                elements_counter = 1
                elements_limit *= num_child
                width /= num_child
                start -= width
                x = start
                y += 1
            else:
                elements_counter += 1
                if num_child == 2:
                    x += width*num_child
                elif num_child == 3:
                    x += width
                elif num_child == 4:
                    x += width*(2/3)
        print(last_elements)


def draw(heap: Heap, font_size=20):
    """
    Drawing heap in Qt window.
    """
    app = QApplication([])

    window = MainWindow()
    window.draw_heap(heap.get_raw_data(), heap.num_children(), font_size)
    window.show()

    app.exec_()
    exit()
