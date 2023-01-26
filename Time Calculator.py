def add_time(start, duration, day_of_week=None):
    import datetime

    # convert start time to datetime object
    start_time = datetime.datetime.strptime(start, "%I:%M %p")

    # extract hours and minutes from duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # add duration to start time
    end_time = start_time + datetime.timedelta(hours=duration_hours, minutes=duration_minutes)

    # handle next day or multiple days later
    days_later = end_time.day - start_time.day
    if days_later > 0:
        end_time_str = end_time.strftime("%I:%M %p") + " (" + str(days_later) + " days later)"
    else:
        end_time_str = end_time.strftime("%I:%M %p")

    # handle optional day of week parameter
    if day_of_week is not None:
        day_of_week = day_of_week.capitalize()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days.index(day_of_week)
        end_day_index = (start_day_index + days_later) % 7
        end_time_str += ", " + days[end_day_index]

    return end_time_str
