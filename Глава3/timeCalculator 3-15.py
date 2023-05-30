time = 0
days = 0
hours = 0
minutes = 0
seconds = 0


time = int(input("Input the amount of seconds: "))

if time < 60:
    print("It's less than 1 minute.")
elif time >= 86400:
    days = time // 86400
    seconds = time % 86400
    if seconds >= 3600 and seconds < 86400:
        hours = seconds // 3600
        seconds = seconds % 3600
        if seconds >= 60 and seconds < 3600:
            minutes = seconds // 60
            seconds = seconds % 60
        print("You've input", time, "seconds. It's", days, "day(s),",
              hours, "hour(s),",
              minutes, "minute(s) and", seconds, "second(s)")
elif time >= 3600:
    hours = time // 3600
    seconds = time % 3600
    if seconds >= 60 and seconds < 3600:
        minutes = seconds // 60
        seconds = seconds % 60
    print("You've input", time, "seconds. It's", hours, "hour(s),",
          minutes, "minute(s) and", seconds, "second(s)")
elif time >= 60:
    minutes = time // 60
    print("You've input", time, "seconds. It's", minutes, "minute(s).")
