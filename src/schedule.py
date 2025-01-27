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
    # p= Period, b= Block, l= Lunch, d= Day ; dStart[h,m] ; pStart / pEnd = [yyyy, mm, dd]
    def __init__(self, pStart=(2025,1,1), pEnd=(2026,1,1), blockTime=70, breakT=15, lStart=5, lTime=60, dStart=[8,15], schedule="Schedule"):
        self.pStart = pStart
        self.pEnd = pEnd
        self.blockTime = blockTime
        self.breakT = breakT
        self.lStart = lStart
        self.lTime = lTime
        self.dStart = dStart
        self.schedule = schedule

def checkTime(classTime, dowtype):
    day = classTime.day
    block = classTime.block
    if dowtype == 1:
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
    elif dowtype == 2:
        match classTime.day:
            case 1:
                day = "MO"
            case 2:
                day = "TU"
            case 3:
                day = "WE"
            case 4:
                day = "TH"
            case 5:
                day = "FR"
            case 6:
                day = "SA"
            case 7:
                day = "SU"
        
    return (day,block)

def checkDiff(hour, minute, diff):
    return (hour + math.trunc((minute+diff)/60), minute + (diff-60*math.trunc((minute+diff)/60)))

def checkZero(i):
    if i < 10:
        return "0" + str(i)
    return i

def checkBlock(block : int, configs : Configs, start = True):
    check = 0
    if block >= configs.lStart:
        check += configs.lTime - configs.breakT
    check += configs.blockTime*(block-1) + configs.breakT*(block-1)
    if start:
        return checkDiff(configs.dStart[0], configs.dStart[1], check)
    else:
        return checkDiff(configs.dStart[0], configs.dStart[1], check + configs.blockTime)
     
    