def minutes_to_hours(minutes):
    hours = int(minutes) / 60
    minutes %= 60
    print hours, 'hours and', minutes, 'minutes'
