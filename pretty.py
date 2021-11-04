import skia
import matplotlib.pyplot as plt

class Pretty:

    def background(self, canvas):
        canvas.drawColor(skia.ColorWHITE)

    def cells(self, canvas):
        paint = skia.Paint(
            Style=skia.Paint.kStroke_Style,
            AntiAlias=True,
            StrokeWidth=10,
            Color=0xff222222)
        paint.setStrokeCap(skia.Paint.kRound_Cap)

        y = 0
        for row in self.grid.grid:
            x = 0
            for c in row:
                path = skia.Path()
                if not c.east in c.links:
                    path.moveTo(x + self.step, y)
                    path.lineTo(x + self.step, y + self.step)

                if not c.south in c.links:
                    path.moveTo(x + self.step, y + self.step)
                    path.lineTo(x, y + self.step)

                canvas.drawPath(path, paint)

                x += self.step

            y += self.step


    def border(self, canvas):
        paint = skia.Paint(
            Style=skia.Paint.kStroke_Style,
            AntiAlias=True,
            StrokeWidth=10,
            Color=skia.Color(0, 0, 0))

        rect = skia.Rect.MakeXYWH(0, 0, self.step*len(self.grid.grid[0]), self.step*len(self.grid.grid))
        canvas.drawRect(rect, paint)

    def __init__(self, ing):
        self.inset = 15
        self.size = 800
        self.grid = ing
        m = max(len(ing.grid), len(ing.grid[0]))
        self.step = (self.size - self.inset * 2) / m

        surface = skia.Surface(self.size, self.size)
        canvas = surface.getCanvas()
        canvas.translate(self.inset, self.inset)

        self.background(canvas)
        self.cells(canvas)
        self.border(canvas)

        image = surface.makeImageSnapshot()
        plt.imshow(image)
        plt.show()
