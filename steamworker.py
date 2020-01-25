import ctypes
import time
import random
import win32gui


SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def releasekey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def pressw():
    PressKey(0x11)
    time.sleep(0.05)
    releasekey(0x11)


def pressa():
    PressKey(0x1E)
    time.sleep(0.05)
    releasekey(0x1E)


def pressd():
    PressKey(0x20)
    time.sleep(0.05)
    releasekey(0x20)


def pressspace():
    PressKey(0x39)
    time.sleep(0.025)
    releasekey(0x39)


def pressskip():
    PressKey(0x2D)
    time.sleep(0.025)
    releasekey(0x2D)


def steamworker(functionsList):
    time.sleep(0.05)

    shufflerB = functionsList
    options = [0, 1, 2]
    random.shuffle(options)
    app = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if app[0:7] == "MONSTER":
        shufflerB[options[0]]()
        time.sleep(0.05)
    else:
        time.sleep(1)
    app = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if app[0:7] == "MONSTER":
        shufflerB[options[1]]()
        time.sleep(0.05)
    else:
        time.sleep(1)
    app = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if app[0:7] == "MONSTER":
        shufflerB[options[2]]()
        time.sleep(0.05)
    else:
        time.sleep(1)
    app = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if app[0:7] == "MONSTER":
        pressspace()
        pressskip()
    else:
        time.sleep(1)


def main():
    global killfunc
    numformat = True
    print("\nMake sure you are in the Steamworks starting screen BEFORE you run the script!")
    print("|| script will only run while MHW is the active window ||\n")
    print("-----------------------------------")

    while numformat:
        try:
            killfunc = float(input("Enter max active running time in h: "))
            numformat = False
        except ValueError:
            numformat = True
    print("-----------------------------------")
    print("\nRunning ...\n")

    funclist = [pressa, pressw, pressd]
    cycle = 0
    while cycle < (killfunc * 9000):
        active = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        while(active[0:7] == "MONSTER"):
            steamworker(funclist)
            cycle = cycle + 1
            #print(cycle)
            break
        # print(cycle)

    print("Program finished")
    input("Press any button to quit")


if __name__ == "__main__":
    main()

# 0.01666 1min
# 0.00833 30sec
