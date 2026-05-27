## SDSS Computing Studies Python Assignment

Objectives:
* Use pyautogui mouse and keyboard controls
* Make use of prebuilt modules not native to the Python basic installation

There are many helper files/libraries/modules that you can import and use in Python.  We often get these from The Python Package Repository at https://pypi.org

You can visit and search for almost anything there and you will usually be directed to someone's Github page where you can get documentation and examples.

Today, we will be installing some modules to your computer and then using one of them: pyautogui

Pyautogui allows you to control your user interface.  It can control the mouse, or your keyboard or even look for things on your screen like you would look with your eyes.

We use pip (the python package installer) to install the modules and then use some of the commands to control the mouse and keyboard

Some useful mouse commands include:

pyautogui.position()
pyautogui.moveTo(x,y,duration)
pyautogui.click(button="left")
pyautogui.scroll()
pyautogui.mouseDown()
pyautogui.mouseUp()

These last 2 commands can be used if you want to mouse down on something, move the mouse somewhere and then mouse up

Some commands are called "wrappers" for other commands, which means they are really a nickname for another command:

pyautogui.leftClick(x,y)
pyautogui.rightClick(x,y)


### Task 1 Install Pyautogui module
Open a terminal and type in:
```
pip install pyautogui
```
It's that simple!
You might sometimes type in:
```
py -m pip install pyautogui --user
```
This does the same, but only installs it to your user account on the computer. It is sometimes considered a good idea to instead install packages to folders that are part of your project, to allow for you to use different version of packages on different projects you might be working on.  You can research environments if you are interested in further exploring this.

**You must also install:**
opencv-python
pillow

### Task 2 Navigate the Maze
We will have you navigate a maze using pyautogui to control your mouse
Visit https://www.google.com/search?tbm=isch&q=maze%20images&tbs=imgo:1 and save some of the maze images.
Open your Visual Studio Code to full screen mode. This will allow you to set a consistent starting point for your maze.
Use physical locations of coordinates to move the mouse using the pyautogui.moveTo() command.  This command uses 2 required parameters and a 3rd optional paramater:

```
pyautogui.moveTo(x,y,time)
```
x is required and specifies the x location on the screen.  You can run "mouseExample.py" to help you find where those locations are
y is required and specifies the y location
time is optional and specifies how long it takes for the mouse to move
to that position
You may want to include a pause to allow you to switch your screen to the correct locations, or use the input options to allow a keyboard input to start the maze run

