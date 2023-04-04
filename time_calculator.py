def add_time(start_time, duration_time, starting_weekday=None):
  time = 0

  x = start_time.split(':')
  x[1] = x[1].split()
  x.extend(x[1])
  del x[1]
  if x[2] == "PM":
    hr = 12 + int(x[0])
  else:
    hr = int(x[0])

  time = [str(hr), x[1]]

  # adding duration time to starting time
  duration_time = duration_time.split(':')

  # Process Minutes
  min_t = int(time[1]) + int(duration_time[1])
  min_t_60 = int(min_t / 60)
  min_t_remain = min_t % 60

  # Process Hours
  hr_t = int(time[0]) + int(duration_time[0]) + min_t_60
  days = int(hr_t / 24)
  hours = hr_t % 24

  time = [days, hours, min_t_remain]

  # processing added time with starting weekday

  # Check length of minutes. Need to have 2 digits
  if time[2] < 10:
    minutes = "0" + str(time[2])
  else:
    minutes = str(time[2])

  # AM or PM
  am_pm = None
  hr_am_pm = None

  if time[1] < 12:
    am_pm = "AM"
    hr_am_pm = time[1]
  else:
    am_pm = "PM"
    hr_am_pm = time[1] - 12

  # Make sure that "hr_am_pm" is not zero and convert to string
  if hr_am_pm == 0:
    hr_am_pm = str(12)
  else:
    hr_am_pm = str(hr_am_pm)

  # Today, the next day, or n-days
  n_days = None
  if time[0] == 0:
    n_days = ""
  elif time[0] == 1:
    n_days = " (next day)"
  else:
    n_days = " (" + str(time[0]) + " days later)"

  # Check if week day is required
  if starting_weekday != None:
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                 "Saturday", "Sunday")
    week_day = week_days.index(starting_weekday.lower().capitalize()) + time[0]
    week_day_no = week_day % 7

    # Assemble final time
    final_time = hr_am_pm + ":" + minutes + ' ' + am_pm + ', ' + week_days[
      week_day_no] + n_days

  else:
    # Assemble final time
    final_time = hr_am_pm + ":" + minutes + ' ' + am_pm + n_days

  return final_time
