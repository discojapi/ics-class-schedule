import schedule
# This Python script processes the schedule setup made in the UI, 
# hence, all the information must enter at once, this includes tuple lists, 
# class layout, and others.

def process(items, configs : schedule.Configs):
    file = open(configs.filename,"w")
    for a in items:
        file.write(a.name + "\n")
    file.close()
    return 0