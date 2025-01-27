import schedule
# This Python script processes the schedule setup made in the UI, 
# hence, all the information must enter at once, this includes tuple lists, 
# class layout, and others.

def process(items, configs : schedule.Configs, filename : str):
    file = open(filename,"w+",encoding="utf-8")
    def writeline(text:str):
        file.write(text + "\n")
    file.write("BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n")
    for a in items:
        file.write("BEGIN:VEVENT" + "\n")
        file.write("END:VEVENT" + "\n")
    file.write("END:VCALENDAR")
    file.close()
    return 0

# SCHEDULE FILE DOCUMENTATION
# The schedule information plus the settings must be stored on a plain text file (.txt, utf-8 encoding)
# The file must mantain the following structure
'''
    ###
    PSTART:
    PEND:
    BLOCKTIME:
    BREAKTIME:
    LUNCHSTART:
    LUNCHTIME:
    DAYSTART:
    SCHEDULE:
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
 
def save(items, configs : schedule.Configs, file : str):
    write = open(file,"w",encoding="utf-8")
    def writeline(text:str):
        write.write(text + "\n")
    writeline("###")
    writeline("PSTART:"+str(configs.pStart))
    writeline("PEND:"+str(configs.pEnd))
    writeline("BLOCKTIME:"+str(configs.blockTime))
    writeline("BREAKTIME:"+str(configs.breakT))
    writeline("LUNCHSTART:"+str(configs.lStart))
    writeline("LUNCHTIME:"+str(configs.lTime))
    writeline("DAYSTART:"+str(configs.dStart))
    writeline("SCHEDULE:"+configs.schedule)
    for item in items:
        writeline("---")
        writeline("CLASSNAME:"+item.name)
        writeline("DAY:"+str(item.day))
        writeline("BLOCK:"+str(item.block))
        writeline("TEACHER:"+item.teacher)
        writeline("NOTES:"+item.notes)
        writeline("CLASSROOM:"+item.classroom)
        writeline("COLOR:"+str(item.color))
    writeline("####")
    write.close()

def load(items, configs : schedule.Configs, file):
    read = open(file,"r",encoding="utf-8")
    lect = []
    for a in read:
        lect.append(a.strip())
    read.close()
    checkClass = False
    if lect[0] != "###" or lect[len(lect)-1]!= "####":
        return(1)
    items.clear()
    configs = schedule.Configs()
    newClass = schedule.SchClass()
    for b in lect:
        if b == "---" or b == "####":
            checkClass = True
            if newClass != schedule.SchClass():
                items.append(newClass)
                newClass = schedule.SchClass()
        else:
            cur = b.split(":")
            if checkClass:
                match cur[0]:
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
            else:
                match cur[0]:
                    case "PSTART":
                        configs.pStart = int(cur[1])
                    case "PEND":
                        configs.pEnd = int(cur[1])
                    case "BLOCKTIME":
                        configs.blockTime = int(cur[1])
                    case "BREAKTIME":
                        configs.breakT = int(cur[1])
                    case "LUNCHSTART":
                        configs.lStart = int(cur[1])
                    case "LUNCHTIME":
                        configs.lTime = int(cur[1])
                    case "DAYSTART":
                        pass
                        #configs.dStart = int(cur[1])
                    case "SCHEDULE":
                        configs.schedule = cur[1]
            
    if len(items) == 0:
        items.append(schedule.SchClass())
    return(0)

