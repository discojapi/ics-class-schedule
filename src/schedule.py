class SchClass:
    # name:String, day:int (1-7), block:Int (1-10), desc:String, teacher:String, color:Int (Color set on main.py)
    def __init__(self, name="Class", day=1, block=1,desc="", teacher="", notes="", classroom="",color=0):
        self.name = name
        self.day = day
        self.block = block
        self.dec = desc
        self.teacher = teacher
        self.notes = notes
        self.classroom = classroom
        self.color = color
    
class Configs:
    # p= Period, b= Block, l= Lunch, d= Day
    def __init__(self, pStart=0, pEnd=0, bTime=0, breakT=0, lStart=5, lTime=0, dStart=0, filename="schedule.ics"):
        self.pStart = pStart
        self.pEnd = pEnd
        self.bTime = bTime
        self.breakT = breakT
        self.lStart = lStart
        self.lTime = lTime
        self.dStart = dStart
        self.filename = filename

def checkTime(classTime, strday):
    day = classTime.day
    block = classTime.block
    if strday == True:
        match classTime.day:
            case 1:
                day = "Monday"
                dd = True
            case 2:
                day = "Tuesday"
                dd = True
            case 3:
                day = "Wednesday"
                dd = True
            case 4:
                day = "Thursday"
                dd = True
            case 5:
                day = "Friday"
                dd = True
            case 6:
                day = "Saturday"
                dd = True
            case 7:
                day = "Sunday"
                dd = True
    return (day,block)
        