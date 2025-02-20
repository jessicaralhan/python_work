class engine:
    def start(self):
        print("engine starts")

class wheels:
    def rotate(self):
        print("wheels rotate")

class car(engine, wheels):
    def drive(self):
        print("driving")


c = car()
c.start()
c.rotate()
c.drive()

