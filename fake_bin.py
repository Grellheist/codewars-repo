def fake_bin(x):
    binaryString = ""
    for digit in x:
        if int(digit) < 5:
            binaryString += '0'
        else:
            binaryString += '1'
    return binaryString
