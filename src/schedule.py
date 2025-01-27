import math

class SchClass:
    # name:String, day:int (1-7), block:Int (1-10),  teacher:String, color:Int (Color set on main.py)
    def __init__(self, name="Class", day=1, block=1, teacher="", notes="", classroom="",color=0):
        self.name = name
        self.day = day
        self.block = block
        self.teacher = teacher
        self.notes = notes
        self.classroom = classroom
        self.color = color
    
class Configs:
    # p= Period, b= Block, l= Lunch, d= Day ; dStart[h,m]
    def __init__(self, pStart=0, pEnd=0, blockTime=70, breakT=15, lStart=5, lTime=60, dStart=[8,15], schedule="Schedule"):
        self.pStart = pStart
        self.pEnd = pEnd
        self.blockTime = blockTime
        self.breakT = breakT
        self.lStart = lStart
        self.lTime = lTime
        self.dStart = dStart
        self.schedule = schedule

def checkTime(classTime, strday):
    day = classTime.day
    block = classTime.block
    if strday == True:
        match classTime.day:
            case 1:
                day = "Monday"
            case 2:
                day = "Tuesday"
            case 3:
                day = "Wednesday"
            case 4:
                day = "Thursday"
            case 5:
                day = "Friday"
            case 6:
                day = "Saturday"
            case 7:
                day = "Sunday"
    return (day,block)

def checkDiff(hour, minute, diff):
    return (hour + math.trunc((minute+diff)/60), minute + (diff-60*math.trunc((minute+diff)/60)))

def checkZero(i):
    if i < 10:
        return "0" + str(i)
    return i