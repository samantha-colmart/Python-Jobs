def time_to_text(minutes) :
    heures = minutes // 60
    reste_minutes = minutes % 60
    print (f"{heures} heures et {reste_minutes} minutes")

time_to_text(125)
time_to_text(60)
time_to_text(45)
time_to_text(0)
time_to_text(226)