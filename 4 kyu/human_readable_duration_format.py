def format_duration(seconds):
    result = [] #Final result
    no_comma = [] #Removes the comma from the second to last element to add "and" after it
    auxiliary = [] #Helps remove the last comma
    pos = 0
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    if year > 1:
        result.append(str(year) + " years,")
    elif year == 1:
        result.append(str(year)+ " year,")
    if day > 1:
        result.append(str(day) + " days,")
    elif day == 1:
        result.append(str(day)+ " day,")
    if hour > 1:
        result.append(str(hour) + " hours,")
    elif hour == 1:
        result.append(str(hour)+ " hour,")
    if min > 1:
        result.append(str(min) + " minutes,")
    elif min == 1:
        result.append(str(min)+ " minute,")
    if sec > 1:
        result.append(str(sec) + " seconds,")
    elif sec == 1:
        result.append(str(sec)+ " second,")
    elif seconds == 0:
        return "now"
    if len(result) > 1: #Gets the position of the second to last element and removes the comma
        pos = result.index(result[-2])
        for letter in result[pos]:
            no_comma += letter
        no_comma.pop()
        result[pos] = ''.join(no_comma)
        result.insert(-1, "and")
    for letter in result[-1]: #Removes the final comma
        auxiliary += letter
    auxiliary.pop()
    result[-1] = ''.join(auxiliary)
    return ' '.join(result)
