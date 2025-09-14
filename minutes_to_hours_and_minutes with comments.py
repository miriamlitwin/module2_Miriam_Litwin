""" Miriam Litwin. This assignment converts a user's input of minutes into hours and minutes"""
def minutes_to_hours_and_minutes():
    #ask the user how many minutes they would like to calculate
    question = "how many minutes would you like to calculate?"
    minutes_to_hours_and_minutes = float(input(question)) #convert input which is a string to a float
    hours = minutes_to_hours_and_minutes //60 #convert minutes to hours
    minutes = minutes_to_hours_and_minutes %60 #convert hours to minutes
    #print how many hours and minutes can be extracted from the user's minute entry
    print("minutes to hours and minutes is", hours, "and", minutes)
    #call the function minutes_to_hours_and_minutes
minutes_to_hours_and_minutes()





