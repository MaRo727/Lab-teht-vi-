def show_time(sec):
    second = sec % 60
    minute = (sec // 60) % 60
    hour = sec // 3600
    return f"{hour:02d}:{minute:02d}:{second:02d}"

print(show_time(500))
print(show_time(10000))
print(show_time(121000))