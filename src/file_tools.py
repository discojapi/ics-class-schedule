import schedule
# This Python script processes the schedule setup made in the UI, 
# hence, all the information must enter at once, this includes tuple lists, 
# class layout, and others.

def process(items, configs : schedule.Configs):
    file = open(configs.filename,"w",encoding="utf-8")
    file.write("BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n")
    for a in items:
        file.write("BEGIN:VEVENT" + "\n")
        file.write("END:VEVENT" + "\n")
    file.write("END:VCALENDAR")
    file.close()
    return 0

def save(items, configs, file):
    pass

def load(items, configs, file):
    items.clear()