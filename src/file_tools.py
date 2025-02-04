from schedule import Configs, SchClass, checkZero, checkBlock, checkTime, getShowName, getDescription
# This Python script processes the schedule setup made in the UI using iCalendar standard, 
# hence, all the information must enter at once, this includes tuple lists, 
# class layout, and others.


def process(items : list, configs : Configs, filename : str):
    file = open(filename,"w+",encoding="utf-8")
    def writeline(text:str):
        file.write(text + "\n")
    file.write("BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n")
    for a in items:
        writeline("BEGIN:VEVENT")
        writeline(f"DTSTART;TZID=America/Santiago:{configs.pStart[0]}{checkZero(configs.pStart[1])}{checkZero(configs.pStart[2]+a.day-1)}T{checkZero(checkBlock(a.block, configs)[0])}{checkZero(checkBlock(a.block, configs)[1])}00")
        writeline(f"DTEND;TZID=America/Santiago:{configs.pStart[0]}{checkZero(configs.pStart[1])}{checkZero(configs.pStart[2]+a.day-1)}T{checkZero(checkBlock(a.block, configs, False)[0])}{checkZero(checkBlock(a.block, configs, False)[1])}00")
        writeline(f"RRULE:FREQ=WEEKLY;WKST={checkTime(a,2)[0]};UNTIL={configs.pEnd[0]}{checkZero(configs.pEnd[1])}{checkZero(configs.pEnd[2])}T235959Z")
        writeline(f"DESCRIPTION:{getDescription(a, configs.desclayout)}")
        writeline(f"SUMMARY:{getShowName(configs.layout, a.id, a.name, a.color)}")
        writeline("STATUS:CONFIRMED\nEND:VEVENT")
    file.write("END:VCALENDAR")
    file.close()
    return 0

# SCHEDULE FILE DOCUMENTATION
# The schedule information plus the settings must be stored on a plain text file (.txt, utf-8 encoding)
# The file must mantain the following structure
'''
    ###
    PSTARTY:
    PSTARTM:
    PSTARTD:
    PENDY:
    PENDM:
    PENDD:
    BLOCKTIME:
    BREAKTIME:
    LUNCHSTART:
    LUNCHTIME:
    DAYSTARTH:
    DAYSTARTM:
    SCHEDULE:
    LAYOUT:
    DESCLAYOUT:
    --- (indicates class)
    CLASSNAME:
    DAY:
    BLOCK:
    TEACHER:
    NOTES:
    CLASSROOM:
    COLOR:
    ---
    CLASSNAME:
    DAY:
    BLOCK:
    TEACHER:
    NOTES:
    CLASSROOM:
    COLOR:
    ####
'''
 
def save(items, configs : Configs, file : str):
    write = open(file,"w",encoding="utf-8")
    def writeline(text:str):
        write.write(text + "\n")
    writeline("###")
    writeline("PSTARTY:"+str(configs.pStart[0]))
    writeline("PSTARTM:"+str(configs.pStart[1]))
    writeline("PSTARTD:"+str(configs.pStart[2]))
    writeline("PENDY:"+str(configs.pEnd[0]))
    writeline("PENDM:"+str(configs.pEnd[1]))
    writeline("PENDD:"+str(configs.pEnd[2]))
    writeline("BLOCKTIME:"+str(configs.blockTime))
    writeline("BREAKTIME:"+str(configs.breakT))
    writeline("LUNCHSTART:"+str(configs.lStart))
    writeline("LUNCHTIME:"+str(configs.lTime))
    writeline("DAYSTARTH:"+str(configs.dStart[0]))
    writeline("DAYSTARTM:"+str(configs.dStart[1]))
    writeline("SCHEDULE:"+configs.schedule)
    writeline("LAYOUT:"+str(configs.layout))
    writeline("DESCLAYOUT:"+str(configs.desclayout))
    for item in items:
        writeline("---")
        writeline("CLASSID:"+item.id)
        writeline("CLASSNAME:"+item.name)
        writeline("DAY:"+str(item.day))
        writeline("BLOCK:"+str(item.block))
        writeline("SECTION:"+str(item.section))
        writeline("TEACHER:"+item.teacher)
        writeline("NOTES:"+item.notes)
        writeline("CLASSROOM:"+item.classroom)
        writeline("COLOR:"+str(item.color))
    writeline("####")
    write.close()

def load(items, file):
    read = open(file,"r",encoding="utf-8")
    lect = []
    for a in read:
        lect.append(a.strip())
    read.close()
    configs = Configs()
    checkClass = False
    if lect[0] != "###" or lect[len(lect)-1]!= "####":
        return(0)
    items.clear()
    newClass = SchClass()
    pStart = []
    pEnd = []
    for b in lect:
        if b == "---" or b == "####":
            if checkClass:
                items.append(newClass)
                newClass = SchClass()
            checkClass = True
        else:
            cur = b.split(":")
            if checkClass:
                match cur[0]:
                    case "CLASSID":
                        newClass.id = cur[1]
                    case "CLASSNAME":
                        newClass.name = cur[1]
                    case "DAY":
                        newClass.day = int(cur[1])
                    case "BLOCK":
                        newClass.block = int(cur[1])
                    case "TEACHER":
                        newClass.teacher = cur[1]
                    case "NOTES":
                        newClass.notes = cur[1]
                    case "CLASSROOM":
                        newClass.classroom = cur[1]
                    case "COLOR":
                        newClass.color = int(cur[1])
                    case "SECTION":
                        newClass.section = int(cur[1])
            else:
                match cur[0]:
                    case "PSTARTY":
                        pStart.append(int(cur[1]))
                    case "PSTARTM":
                        pStart.append(int(cur[1]))
                    case "PSTARTD":
                        configs.pStart = (pStart[0],pStart[1],int(cur[1]))
                    case "PENDY":
                        pEnd.append(int(cur[1]))
                    case "PENDM":
                        pEnd.append(int(cur[1]))
                    case "PENDD":
                        configs.pEnd = (pEnd[0],pEnd[1],int(cur[1]))
                    case "BLOCKTIME":
                        configs.blockTime = int(cur[1])
                    case "BREAKTIME":
                        configs.breakT = int(cur[1])
                    case "LUNCHSTART":
                        configs.lStart = int(cur[1])
                    case "LUNCHTIME":
                        configs.lTime = int(cur[1])
                    case "DAYSTARTH":
                        configs.dStart[0] = int(cur[1])
                    case "DAYSTARTM":
                        configs.dStart[1] = int(cur[1])
                    case "SCHEDULE":
                        configs.schedule = cur[1]
                    case "LAYOUT":
                        configs.layout = int(cur[1])
                    case "DESCLAYOUT":
                        configs.desclayout = int(cur[1])
    if len(items) == 0:
        items.append(SchClass())
    return(True, configs)

