# Calculates prime numbers until the given number and appends to a list
def primeinrange(end):
    primelist = []
    
    for adad in range(1, end):
        shod = False
        for i in range(2, adad):
            if adad % i == 0:
                shod = True
            else:
                pass
        if shod == False:
            primelist.append(adad)    
                
    return primelist

def isprime(number):
    shod = False
    for i in range(2, number):
        if number % i == 0:
            shod = True
        else:
            pass
    if shod == False:
        return number
    else:
        return None


    ## Gets a list and sorts it
## Gets a new member, checks if its not already in the list, then appends it.
def listsort(list,new):
    new.sort()
    if len(list) != 0:
        for i in range(len(list)):
            list[i].sort()
        ispresent = False
        for j in list:
            if new == j:
                ispresent = True
                break
            else:
                pass
        if ispresent == False:
            list.append(new)
    else:
        list.append(new)


    return list



