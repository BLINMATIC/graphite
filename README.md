![](https://github.com/BLINMATIC/graphite/raw/main/logo.png)
# Code Template
```python
import graphite

screen = graphite.Screen("icon.png", 640, 480, "Graphite")
clock = graphite.time.Clock()

while True:
    clock.tick(120)
    screen.fill((255, 255, 255))

    screen.update()
```  
The code on the above is the bare minimums for a graphite app.  
But the graphite module is not just made of these components.  
# Notes Before Starting
1) If you see any variable named `rgb` then it means `(red, green, blue)`. Each variable is an integer that goes from 0 to 255
2) There are dependancies in the project. These dependancies are `keyboard` and `PIL`
# Screen
## Creation Of The Screen
The screen object is the most important object of a graphite app. The screen object is created with the syntax of:  
```python
<name> = graphite.Screen(icon="file.png", width=int, height=int, title="text")
```
Just note that the following code is outside of the main loop.
## Screen On The Mainloop
### Filling The Background With A Color
To fill the background with a color:
```python
<name>.fill(rgb)
```
Note: Is not mandatory.
### Updating The Screen
To update the screen use:
```python
<name>.update()
```
Note: Put this in the end of the mainloop.
## Getting Information Back
To get the screen info:
```python
<name>.get_width() # Returns integer width
<name>.get_width() # Returns integer height
<name>.get_title() # Returns string title
```
# Timing
## Wait X Miliseconds
To wait x miliseconds there are 2 ways to do it:  
```python
# 1) Get the precise delay
graphite.time.wait_precise(int)
# 2) Get the rounded delay
graphite.time.wait(int)
```
## App Clock
If you need a clock for any purpose:
```python
<name> = graphite.time.Clock()

# MAINLOOP
while True:
    <name>.tick(int)
```
Note: The clock.tick is recommended to be put into the very top of a mainloop.
# Drawing Objects
## Rectangle
```python
graphite.draw.rectangle(x, y, width, height, rgb, screen)
```
## Line
```python
graphite.draw.line(x, y, end_x, end_y, rgb, screen)
```
## Circle
```python
graphite.draw.ellipsis(x, y, width, width, rgb, screen)
```
## Ellipsis
```python
graphite.draw.ellipsis(x, y, width, height, rgb, screen)
```
## Image
```python
graphite.draw.image(x, y, "image.png", screen)
```
