from gpiozero import Button

controls = {}


class Control:
    pin = ''
    btn = 0
    isPressed = False

    function = None
    args = []

    def __init__(self, pin, function, args):
        self.pin = pin
        self.btn = Button(pin)
        self.function = function
        self.args = args


def addControll(pin, function, args):
    if callable(function):
        if pin in controls:
            print("Warning: Used '"+ pin + "'-pin for multiple controlls, only last will be used.")
        controls[pin] = Control(pin, function, args)
    else:
        print("GPIOEvent for '" + pin + "'-pin has to be callable.")


def checkForInput():
    for pin in controls:
        control = controls[pin]
        if control.btn.is_pressed:
            if not control.isPressed:
                control.isPressed = True
                if control.args is not None:
                    control.function(control.args)
                else:
                    control.function()
        else:
            control.isPressed = False