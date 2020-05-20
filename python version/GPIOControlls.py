import RPi.GPIO as GPIO

controls = {}
GPIO.setmode(GPIO.BCM)

class Control:
    pin = 0
    isPressed = False

    function = None
    args = []

    def __init__(self, pin, function, args):
        self.pin = pin
        self.function = function
        self.args = args


def addControll(pin, function, args):
    if callable(function):
        if pin in controls:
            print("Warning: Used '"+ pin + "'-pin for multiple controlls, only last will be used.")
        GPIO.setup(pin, GPIO.IN)
        controls[pin] = Control(pin, function, args)
    else:
        print("GPIOEvent for '" + pin + "'-pin has to be callable.")


def checkForInput():
    for pin in controls:
        control = controls[pin]
        if GPIO.input(pin) == 1:
            if not control.isPressed:
                control.isPressed = True
                if control.args is not None:
                    control.function(control.args)
                else:
                    control.function()
        else:
            control.isPressed = False