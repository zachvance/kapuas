import pickle
import os.path
import os
import doctest

"""

Persistent Switch is a small module utilizing pickle to make persistent, nameable, boolean variables and alter or test
their states.

"""

def make(key):
    file = "d.pickle"
    if os.path.isfile(file) is True:
        with open("d.pickle", "rb") as f:
            d = pickle.load(f)
            if key in d:
                print("Switch already exists!")
            else:
                d[key] = 0
                print(d)
                with open("d.pickle", "wb") as f:
                    pickle.dump(d, f)
    else:
        d = {}
        d[key] = 0
        print(d)
        with open("d.pickle", "wb") as f:
            pickle.dump(d, f)

def ison(key):
    try:
        file = "d.pickle"
        if os.path.isfile(file) is True:
            with open("d.pickle", "rb") as f:
                d = pickle.load(f)
                if d[key] == 1:
                    return True
                else:
                    return False
    except:
        print("Error: Switch does not exist")

def isoff(key):
    try:
        file = "d.pickle"
        if os.path.isfile(file) is True:
            with open("d.pickle", "rb") as f:
                d = pickle.load(f)
                if d[key] == 0:
                    return True
                else:
                    return False
    except:
        print("Error: Switch does not exist")

def on(key):
    try:
        file = "d.pickle"
        if os.path.isfile(file) is True:
            with open("d.pickle", "rb") as f:
                d = pickle.load(f)
                d[key] = 1
                with open("d.pickle", "wb") as f:
                    pickle.dump(d, f)
    except:
        print("Error: Switch does not exist")

def off(key):
    try:
        file = "d.pickle"
        if os.path.isfile(file) is True:
            with open("d.pickle", "rb") as f:
                d = pickle.load(f)
                d[key] = 0
                with open("d.pickle", "wb") as f:
                    pickle.dump(d, f)
    except:
        print("Error: Switch does not exist")

def toggle(key):
    try:
        file = "d.pickle"
        if os.path.isfile(file) is True:
            with open("d.pickle", "rb") as f:
                d = pickle.load(f)
                if d[key] == 1:
                    d[key] = 0
                else:
                    d[key] = 1
                with open("d.pickle", "wb") as f:
                    pickle.dump(d, f)
    except:
        print("Error: Switch does not exist")

def explode():
    if os.path.exists("d.pickle"):
        os.remove("d.pickle")
    else:
        print("The file does not exist")

def show():
    pass

def delete(key):
    pass
