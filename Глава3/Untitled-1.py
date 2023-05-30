
seconds = 100
days = seconds // 60
dayRemainder = seconds % 60
if seconds == 100:
    seconds += 24
    if seconds > 100:
        seconds = 8 + 3
        print(seconds)
