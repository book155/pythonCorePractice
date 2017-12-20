
def convert2(minute):
    hour = minute // 60 
    minute = minute - 60* hour
    return hour,minute

hour,minute = convert2(790)
print(hour)
print(minute)