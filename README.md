# 100LEDs
Assign a color to any 100LEDs by ID or by all.
## Create virtual environment
It is optional to install project modules to a virtual environment to isolate the needed module to the Main PC
```
100LEDs> cd 100LEDs
100LEDs> python -m venv ./venv
```
## Run env
### for Windows CMD
```
100LEDs> venv/Scripts/activate.bat
```
## Install necessary modules
```
100LEDs> pip install -r requirements
```
## Fixed for pyqt_color_picker
Error:
```
TypeError: arguments did not match any overloaded call:
QPoint(): too many arguments
QPoint(int, int): argument 1 has unexpected type 'float'
QPoint(QPoint): argument 1 has unexpected type 'float'
```

Solution: Cast int to the ff arguments

file: colorHueBarWidget.py
```
|61| geo.moveTo(int(0), int(y))
```
file: colorSquareWidget.py
```
|69| geo.moveCenter(QPoint(int(x), int(y)))
```

## Run the code
```
100LEDs> python ColorDialogue.py
```
## Run example color picker code
```
100LEDs> python colorpicker_example\example.py