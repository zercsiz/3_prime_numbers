from functions import primeinrange ,listsort, isprime

givennumber = int((input("Please enter the Number : ")))
myprimelist = primeinrange(givennumber)
print(myprimelist)
print("-"*100)

answers = []

first = 0
second = 0
third = 0

for i in myprimelist:
    first = i
    for j in myprimelist:
        second = j
        third = givennumber - (first+second)
        if givennumber - (first+second) > 0:
            third = givennumber - (first+second)
            if isprime(third):
                newanswer = [first, second, third]
            else:
                newanswer = []
            listsort(answers, newanswer)
            
answers.sort()
answers.remove([])
print(answers)
print("-"*100)

print(f"Tedade halat ha : {len(answers)}")

    