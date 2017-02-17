# Bounce

This simple Ball Bounce Simulator is the result of a Python coding session with my youngest son on a damp Saturday afternoon in 2012. He was nine-years old at the time and this was his introduction to physics engines. As such, this program is intentionally procedural (no classes, etc) and the physics are crude but realistic with plausible sound effects. Imagine a ping pong ball dropping on a hard kitchen floor before finally dribbling to a halt with its own inimitable sound. Well, that's basically what this simulator amounts to. At the end of each run, you can hit the SPACE bar to restart the simulation over and over again. It is quite therapeutic -- really!!

We tested this on Windows 7, but there is no reason why it shouldn't work on other platforms (with possibly some tweaking required for audio). Before running the program on Windows, you will need to install Python 3.2 (standard 32-bit version with IDLE) and then Pygame 1.9.2a0.wn32-py3.2.

Unfortunately Pygame is no longer actively maintained even though it still works reliably on modern OSes. Pygame supports double-buffering in full screen mode; however, like most legacy frameworks, this does _not_ work in windowed mode. You will therefore notice a little flicker in this simple implementation. Of course, these imperfections and limitations are themselves educational.

## Screenshot

Click image to watch video. Note that, due to capture limitations, video quality is degraded.

[![](http://img.youtube.com/vi/9Ti2t22JY7o/0.jpg)](http://www.youtube.com/watch?v=9Ti2t22JY7o "Bounce Demo")

## Coding Challenge

Refactor this code to:

1. Work with the latest version of Python using a newer generation game/CGI framework.
2. Use object-oriented methodologies (classes)
3. Normalise physics to reflect real world units independent of frame rate.
4. Employ double/triple buffering to elminate flicker.
5. Add multiple balls and simulate collisions (not as easy as it seems!)

When you've done that, you're well on your way to Programming Nirvana ;-)
