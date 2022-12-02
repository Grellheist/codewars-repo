def create_phone_number(n):
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, " ")
    n.insert(9, "-")
    return ''.join([str(digit) for digit in n])
    
    #Better solution:
    #def create_phone_number(n):
	#return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)