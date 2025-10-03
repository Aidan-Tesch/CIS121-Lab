#Functions Questions
# Question 1
def volume_pyramid(base, height):
   volume = ((base**2)*height)/3
   return volume

# Question 2
def volume_cone(radius, height):
   volume = ((radius**2)*height)/3
   return volume

# Question 3
def basketball_score(two_pnts, three_pnts):
   total = (two_pnts*2) + (three_pnts*3)
   return total

# Question 4
def tennis_score(aces, winning_shots):
   total = (aces*2) + winning_shots
   return total

# Question 5
def leg_Counter(chickens, cows, pigs):
   total_legs = (chickens*2) + (cows*4) + (pigs*4)
   return total_legs

# Question 6
def total_batteries(e_dolls, rc_cars, robo_dogs):
   total = (e_dolls*2) + (rc_cars*4) + (robo_dogs*6)
   return total
'''
# Question 7
def avg_heart_rate(age, athleticism):
   if 20 <= age <= 39:
      if athleticism == "Below Average":
  '''       

# Question 8
def pool_time(user_grade, user_time):
    if user_grade == "k":
       user_grade = 0

    if user_time == "Morning":
       if 0 <= user_grade <= 3:
          time_output = "9AM"
       elif 4 <= user_grade <= 8:
          time_output = "10AM"
       elif 9 <= user_grade <= 12:
          time_output = "11AM"
       else:
          time_output = "Error" 

    elif user_time == "Afternoon":
       if  0 <= user_grade <= 3:
          time_output = "1PM"
       elif 4 <= user_grade <= 8:
          time_output = "2PM"
       elif 9 <= user_grade <= 12:
          time_output = "3PM"
       else:
          time_output = "Error"     

    return time_output

# Question 11
def convert_knuts(knuts):
    output = ""

    galleons = knuts//(29*17)
    knuts = knuts%(29*17)
    sickles = knuts//29
    knuts = knuts%29
    if galleons > 0:
       output += f'Galleons: {galleons} '
    if sickles > 0:
       output += f'Sickles: {sickles} '
    if knuts > 0:
       output += f'Knuts: {knuts} '

    return output

#Strings Questions

# Question 1
def reverse_string(string):
   for i in range(len(string)-1, 0, -1):
      new_string += string[i]
   return new_string

# Question 2
def is_fever(temperature):
   measure = temperature[-1]
   degrees = int(temperature[0:-1])
   if measure == "C":
      if degrees >= 37:
         return True
      else:
         return False
   elif measure == "F":
      if degrees >= 98.6:
         return True
      else:
         return False

# Question 3
def is_boiling(temperature):
   measure = temperature[-1]
   degrees = int(temperature[0:-1])
   if measure == "C":
      if degrees >= 100:
         return True
      else:
         return False
   elif measure == "F":
      if degrees >= 212:
         return True
      else:
         return False


print(reverse_string("banana"))