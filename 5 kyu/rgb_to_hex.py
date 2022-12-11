def rgb(r, g, b):
    digits = '0123456789ABCDEF'
    result = []
    start_values = [r, g, b]
    for colors in start_values:
        color_values = ''
        if colors > 255:
            result.append('FF')
        else:
            while colors > 0:
                color_values = digits[colors % 16] + color_values
                colors = colors // 16
            result.append(color_values)

    index = 0

    for colors in result:
        if len(colors) == 0: result[index] = '00'
        if len(colors) == 1: result[index] = '0' + result[index]
        index += 1
    return ''.join(result)

#Better solution:
#
#def rgb(r, g, b):
#    round = lambda x: min(255, max(x, 0))
#    return ("{:02X}" * 3).format(round(r), round(g), round(b))
