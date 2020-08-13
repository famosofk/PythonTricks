#readHours = int( input("Number of hours"))
#readRate = float(input("Rate: "))

#if readHours <= 40:
#    print(readHours*readRate)
#else:
#    print(40*readRate + (readHours-40)*(readRate*1.5))
'''
try:
    number = float(score)
    if(0.0 <= number <= 1.0):
        if number < 0.6:
            print("F")
        elif number < 0.7:
            print("D")
        elif number < 0.8:
            print("C")
        elif number < 0.9:
            print("B")
        else:
            print("A")

    else:
        print("It's not a percent value.")
        #raise TypeError("Out of range.")
except:
            print("It's not a number.")
'''



def computepay(readHours, readRate):
    if readHours <= 40:
        return readHours*readRate
    else:
        return 40*readRate + (readHours-40)*(readRate*1.5)

readHours = int( input("Number of hours: "))
readRate = float(input("Rate: "))
p = computepay(readHours, readRate)
print("Pay", p)
