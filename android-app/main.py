"""Panda3D on Android: a first test for Toontown: Anywhere.

Draws a grid of separately coloured cards (about as many separate draws as a busy Toontown playground) under a slowly turning camera,
with Panda's frame-rate meter in the corner. Tap the screen to switch between 300, 1200 and 2400 cards."""
import math
import random

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import CardMaker, NodePath, TextNode, loadPrcFileData

loadPrcFileData("", "sync-video 1\nshow-frame-rate-meter 1\nframe-rate-meter-scale 0.06")


class Test(ShowBase):
    COUNTS = (300, 1200, 2400)

    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.setBackgroundColor(0.4, 0.7, 1.0, 1)
        self.root = None
        self.which = 1
        self.label = OnscreenText(text="", pos=(0, -0.92), scale=0.06, fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1), align=TextNode.ACenter)
        self.build()
        self.accept("mouse1", self.next)
        self.taskMgr.add(self.spin, "spin")

    def build(self):
        if self.root is not None:
            self.root.removeNode()
        n = self.COUNTS[self.which]
        self.root = self.render.attachNewNode("cards")
        cm = CardMaker("c")
        cm.setFrame(-0.4, 0.4, -0.4, 0.4)
        side = int(math.ceil(math.sqrt(n)))
        rnd = random.Random(1)
        for i in range(n):
            c = self.root.attachNewNode(cm.generate())
            c.setPos((i % side - side / 2) * 1.1, (i // side) * 1.1 + 4, rnd.uniform(-0.5, 0.5))
            c.setColor(rnd.random(), rnd.random(), rnd.random(), 1)
            c.setTwoSided(True)
        self.label.setText("Panda3D on Android - %d separate draws - tap to change" % n)

    def next(self):
        self.which = (self.which + 1) % len(self.COUNTS)
        self.build()

    def spin(self, task):
        t = task.time * 0.2
        self.camera.setPos(math.sin(t) * 6, -14, 9)
        self.camera.lookAt(0, 20, 0)
        return task.cont


Test().run()
