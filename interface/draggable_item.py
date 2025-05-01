import pyqtgraph as pg
from  PyQt5.QtCore import Qt

"""
customisable handle you can drag within specified 
bounds to adjust envelope point on PyQtGraph PlotDataItem in realtime
"""

class DraggableItem(pg.TargetItem):
    """
    draggable control point bound to a specific index in a PlotDataItem

    Attributes:
        line :  The PlotDataItem being manipulates
        point : Integer index into line's data arrayss
        xbounds : Tuple (xmin, xmax) clamping horizintal movement
        ybounds : Tuple (ymin, ymax) clamping vertical movement
    """
    def __init__(self, line, point, pos, pen, hoverPen, xbounds, ybounds):
        """
        Initialise a draggable handle at pos

        Args:
            line (PlotDataItem) : The plot whose data this handle will edit
            point (int) : Index in the plot's data to update
            pos (tuple) : (x, y) initial position of the handle
            pen (QPen)  : Border color/width for the handle
            hoverPen (QPen) : Border styling when hovered
            xbounds (tuple) : (min_x, max_x) horizontal limits
            ybounds (tuple) : (min_y, max_y) vertical limits
        """
        super().__init__(pos, size=20, pen=pen, hoverPen=hoverPen)
        self.line = line
        self.point = point
        self.xbounds = xbounds
        self.ybounds = ybounds
    
    def mouseDragEvent(self, ev):
        """
        Handle mouse drag events
        """
        # only respond to left-button drag if movable
        if not self.movable or ev.button() != Qt.MouseButton.LeftButton:
            return
        ev.accept()
        if ev.isStart():
            self.symbolOffset = self.pos() - self.mapToView(ev.buttonDownPos())
            self.moving = True
        
        # if not actively moving, ignore intermediate events
        if not self.moving:
            return
        
        # compute new unclamped position in data coordinates
        new_pos = self.symbolOffset + self.mapToView(ev.pos())

        # clamp x within allowed range
        if new_pos[0] < self.xbounds[0]:
            new_pos[0] = self.xbounds[0]
        elif new_pos[0] > self.xbounds[1]:
            new_pos[0] = self.xbounds[1]
        
        # clamp y within allowed range
        if new_pos[1] < self.ybounds[0]:
            new_pos[1] = self.ybounds[0]
        elif new_pos[1] > self.ybounds[1]:
            new_pos[1] = self.ybounds[1]

        # move handle to the clamped position
        self.setPos(new_pos)
        
        data_x = self.line.getData()[0]
        data_y = self.line.getData()[1]
        # update the specific point's coordinates
        data_x[self.point] = new_pos[0]
        data_y[self.point] = new_pos[1]

        # redraw the line
        self.line.setData(data_x, data_y)

        # on drag finish, signal that the position change is done
        if ev.isFinish():
            self.moving = False
            self.sigPositionChangeFinished.emit(self)
