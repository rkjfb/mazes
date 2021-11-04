import skia
import matplotlib.pyplot as plt

class Pretty:

    def background(self, canvas):
        #shader = skia.Shaders.Blend(
        #    skia.BlendMode.kMultiply,
        #    skia.GradientShader.MakeRadial((self.size/2, self.size/2), 180.0, [0xff8888ff, 0xffff88ff]),
        #    skia.PerlinNoiseShader.MakeTurbulence(0.025, 0.025, 2, 0.0))
        #canvas.drawPaint({'Shader': shader})
        canvas.drawColor(skia.ColorWHITE)

    def cells(self, canvas):
        paint = skia.Paint(
            Style=skia.Paint.kStroke_Style,
            AntiAlias=True,
            StrokeWidth=10,
            Color=0xff000000)
        paint.setStrokeCap(skia.Paint.kRound_Cap)

        path = skia.Path()
        y = 0
        for row in self.grid.grid:
            x = 0
            for c in row:
                if not c.east in c.links:
                    path.moveTo(x + self.step, y)
                    path.lineTo(x + self.step, y + self.step)

                if not c.south in c.links:
                    path.moveTo(x + self.step, y + self.step)
                    path.lineTo(x, y + self.step)

                x += self.step

            y += self.step

        canvas.drawPath(path, paint)


    def border(self, canvas):
        paint = skia.Paint(
            Style=skia.Paint.kStroke_Style,
            AntiAlias=True,
            StrokeWidth=10,
            Color=skia.Color(0, 0, 0))
        #paint.setShader(skia.GradientShader.MakeLinear(
        #    points=[(0.0, 0.0), (self.size, self.size)],
        #    colors=[0xFFFF0000, 0xFF888800]))
        paint.setShader(skia.GradientShader.MakeSweep(
            cx=128.0,
            cy=128.0,
            colors=[
                skia.ColorCYAN,
                skia.ColorMAGENTA,
                skia.ColorYELLOW,
                skia.ColorCYAN
            ]
        ))

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
