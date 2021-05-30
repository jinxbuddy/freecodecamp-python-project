def add_time(start, duration, starting_day=""):
  start_split=start.split(' ')
  start_time= start_split[0].split(':')
  start_hour= start_time[0]
  start_min= start_time[1]
  duration_split= duration.split(':')
  duration_hour= duration_split[0]
  duration_min= duration_split[1]

  if start_split[1]=='PM':
    start_hour = 12+int(start_hour)

  else:
    pass

  new_hour= int(start_hour) + int(duration_hour)
  new_min= int(start_min) + int(duration_min)

  if new_min>= 60:
    hours_add= new_min//60
    new_min = new_min - 60
    new_hour += hours_add
  add_days= 0
  
  if new_hour > 24 :
    add_days = new_hour // 24
    new_hour -= add_days * 24



  fmt= start_split[1]

  if new_hour > 0 and new_hour < 12 :
    fmt = "AM"
  elif new_hour == 12 :
    fmt = "PM"
  elif new_hour > 12 :
    fmt = "PM"
    new_hour -= 12
  else : # new_hour == 0
    fmt = "AM"
    new_hour += 12

  if add_days > 0 :
    if add_days == 1 :
      days_later = " (next day)"
    else :
      days_later = " (" + str(add_days) + " days later)"
  else :
    days_later = ""

  week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

  if starting_day :
    weeks = add_days // 7
    i = week_days.index(starting_day.lower().capitalize()) + (add_days - 7 * weeks)
    if i > 6 :
      i -= 7
    day = ", " + week_days[i]
  else :
      day = ""
  
  new_time= str(new_hour) + ":" + (str(new_min) if new_min > 9 else ("0" + str(new_min))) +" " + fmt + day + days_later


  return new_time
