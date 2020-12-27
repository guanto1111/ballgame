from campy.gui.events.timer import pause
from breakoutgraphics2 import BreakoutGraphics
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage


FRAME_RATE = 1000 / 100   # 120 frames per second.
NUM_LIVES = 10
a = 1


   






def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        if lives <= 0:
            break
        else:
            pause(FRAME_RATE)
            graphics.create()
            graphics.move()
            graphics.reflect()
            graphics.remove_and_point()
            graphics.window.remove(graphics.life)
            graphics.life.text = "Lives: " + str(lives)
            graphics.window.add(graphics.life)
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.window.remove(graphics.life)
                graphics.life.text = "Lives: " + str(lives)
                graphics.window.add(graphics.life)
                graphics.reset_ball()
                graphics.switch_off()

            if lives <= 0:
                break
            finished = graphics.finished()
            if finished:
                break


if __name__ == '__main__':
    main()