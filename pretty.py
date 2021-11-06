import skia
import matplotlib.pyplot as plt

class Pretty:

    def boardbackground(self, canvas):
        #shader = skia.Shaders.Blend(
        #    skia.BlendMode.kMultiply,
        #    skia.GradientShader.MakeRadial((self.size/2, self.size/2), 180.0, [0xff8888ff, 0xffff88ff]),
        #    skia.PerlinNoiseShader.MakeTurbulence(0.025, 0.025, 2, 0.0))
        #canvas.drawPaint({'Shader': shader})
        canvas.drawColor(skia.ColorWHITE)

    # draw the background of cells
    def cellbackground(self, canvas):

        y = 0
        for row in self.grid.grid:
            x = 0
            for c in row:
                weight = self.grid.dist_weight(c)
                dark = int(weight * 255)
                light = int(127 + weight*127)
                paint = skia.Paint(
                    Style=skia.Paint.kFill_Style,
                    AntiAlias=True,
                    StrokeWidth=10,
                    Color=skia.Color(dark,light,dark, 255))
                rect = skia.Rect(x, y, x+self.step, y+self.step)
                canvas.drawRect(rect, paint)

                x += self.step

            y += self.step

    # draws current path through the maze
    def path(self, canvas):
        last_path = self.grid.get_last_path()
        paint = skia.Paint(
            Style=skia.Paint.kFill_Style,
            AntiAlias=True,
            StrokeWidth=10,
            PathEffect=skia.CornerPathEffect.Make(self.step),
            Color=skia.ColorBLUE)
        # BUGBUG: skia red and blue channels are flipped ..
        paint.setStrokeCap(skia.Paint.kRound_Cap)

        # start
        half_step = self.step // 2
        x = last_path[0].column * self.step + half_step
        y = last_path[0].row * self.step + half_step
        xend = last_path[len(last_path)-1].column * self.step + half_step
        yend = last_path[len(last_path)-1].row * self.step + half_step

        canvas.drawCircle(x,y,half_step-5, paint)

        #paint.setShader(skia.GradientShader.MakeLinear(
        #    points=[(x, y), (xend, yend)],
        #    colors=[skia.ColorBLUE, skia.ColorYELLOW]))

        paint.setStyle(skia.Paint.kStroke_Style)

        path = skia.Path()
        path.moveTo(x, y)
        for i in range(1, len(last_path)):
            x = last_path[i].column * self.step + half_step
            y = last_path[i].row * self.step + half_step
            path.lineTo(x, y)

        canvas.drawPath(path, paint)

    def cellborder(self, canvas):
        paint = skia.Paint(
            Style=skia.Paint.kStroke_Style,
            AntiAlias=True,
            StrokeWidth=7,
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

    def boardborder(self, canvas):
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

        self.boardbackground(canvas)
        self.cellbackground(canvas)
        self.path(canvas)
        self.cellborder(canvas)
        self.boardborder(canvas)

        image = surface.makeImageSnapshot()
        plt.imshow(image)
        plt.show()
