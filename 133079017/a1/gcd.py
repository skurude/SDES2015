def gcd(a, b):
    
    if (a<0)or(b<0) : 
        raise ValueError, "Negative number found"
    elif ((type(a) != int) or (type(b) != int)) and ((type(a) != long) or (type(b) != long)):
        raise TypeError, "Number is not of type int or long."
    elif (a==0 and b!=0):
        return abs(b)
    elif (a!=0 and b==0):
        return abs(a)
    else:         
        while b:
            a, b = b, a%b
        return a 