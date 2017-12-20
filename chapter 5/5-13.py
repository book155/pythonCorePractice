def convert(time):
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    print (int(hour) * 60 + 10)

convert('13:10')
