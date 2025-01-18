class SchClass:
    # name:String, time:String *, desc:String, teacher:String
    # * Class time layout: DXX;DXX : D=Day of the week : X=Time block
    def __init__(self, name, time, desc, teacher, notes):
        self.name = name

    def getName(self):
        return self.name

Scheduling = []
Scheduling.append(SchClass("John",0,0,0))
print(Scheduling[0].getName())