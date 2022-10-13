# Batman
# n --> Patient Number
# step --> patient steps
def findNumOfStepsRequired(n, step):
    
    if n<=10:
        return n*step
    else:
        Print("Patient count is wrong")
# patient =int(input())
# steps = 10
# print(findNumOfStepsRequired(patient, steps))
print(findNumOfStepsRequired(3, 10))
