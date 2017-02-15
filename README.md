# Bounce

This simple Ball Bounce Simulator is the result of a Python coding session with my youngest son on a wet Saturday afternoon in 2012. He was nine years old at the time and this was his quick-and-dirty introduction to physics simulation. The program is intentionally procedural (no classes, etc) and the physics are crude but realistic with plausible sound effects. Imagine a ping pong ball dropping on a hard kitchen floor before finally bubbling to a halt. Now you get the picture! At the end of each simulation run, hit the SPACE bar to restart the simulation. It is quite therapeutic -- really!!

We tested this on Windows 7, but there is no reason why it shouldn't work on other platforms. Before running the program on Windows, you will need to install Python 3.2 (standard 32-bit version with IDLE) and then Pygame 1.9.2a0.wn32-py3.2. Unfortunately Pygame is no longer actively maintained even though it still works admirably on modern OSes.

## Educational Challenge

Refactor this code to:

1. Work with latest version of Python using a newer generation game/CGI framework.
2. Use object-oriented methodologies (classes)
2. Normalise physics to reflect real world units independent of frame rate.
3. Add multiple balls and simulate collisions (not as easy as it seems!)

When you've done that, you're well on your way to Programming Nirvana ;-)
