def valid_parentheses(string):
    open = "("
    closed = ")"
    queue = []
        
    for character in string:
        if character in open:
            queue.append(character) # If it finds an openening parenthesis, adds to the queue
        elif character in closed:
            position = closed.index(character) # Gets the position of the closing parenthesis
            if (len(queue) > 0) and (open[position] == queue[len(queue) - 1]):
                queue.pop()
            else:
                return False
    if len(queue) == 0:
        return True
    else:
        return False