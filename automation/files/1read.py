file = open("name")
print(file.readline()) ## reads the first line
print(file.readline()) ## reads the second line
print(file.read()) ##reads all the file from current position
file.close()
with open("name") as file:
    print(file.read())
#This will automatically close the file for us

with open("name") as file:
    for line in file:
        print(line.strip().upper()) #Prints the whole file with upper case without duplicated \n

nFile = open("name")
lines = file.readlines()
nFile.close()
#the lines from file are saved on lines variable