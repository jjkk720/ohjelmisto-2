class Hissi:
    def __init__(self, ylin, alin=1, kerrosnyt=0):
        self.alin=alin
        self.ylin=ylin

    def siirry(self, kerros):
        if kerros < kerrosnyt:
            kerros_ylös()
        if kerros > kerrosnyt:
            kerros_alas()
        else:
            break





h=Hissi(10)



