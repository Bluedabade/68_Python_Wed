def calculate_jumps(d, s):
    if d == s :
        return(1)
    else:
        if d % s == 0:
            return(d //s)
        else:
            return(d //s +1)

d = 22
s = 7
print(calculate_jumps(d, s))