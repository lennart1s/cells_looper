import keyboard

controls = {}


class Control:
    key = ''
    isPressed = False

    function = None
    args = []

    def __init__(self, key, function, args):
        self.key = key
        self.function = function
        self.args = args


def addControll(key, function, args):
    if callable(function):
        if key in controls:
            print("Warning: Used '"+ key + "'-key for multiple controlls, only last will be used.")
        controls[key] = Control(key, function, args)
    else:
        print("KeyEvent for '" + key + "'-key has to be callable.")


def checkForInput():
    for key in controls:
        control = controls[key]
        if keyboard.is_pressed(key):
            if not control.isPressed:
                control.isPressed = True
                if control.args is not None:
                    control.function(control.args)
                else:
                    control.function()
        else:
            control.isPressed = False