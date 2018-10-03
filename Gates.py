class andGate():
    def __init__(self, dgtl1, dgtl2):
        self.on = False
        self.dgtl1 = dgtl1
        self.dgtl2 = dgtl2

    def run():
        if self.dgtl1 and self.dgtl2:
            return True

class orGate():
    def __init__(self, dgtl1, dgtl2):
        self.on = False
        self.dgtl1 = dgtl1
        self.dgtl2 = dgtl2

    def run():
        if self.dgtl1 or self.dgtl2:
            return True

class notGate():
    def __init__(self, dgtl):
        self.on = False
        self.dgtl = dgtl

    def run():
        return not dgtl

class
