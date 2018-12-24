# file handle

print ("FILE write...")

f = open("demofile.txt", "w")
f.write("Now the file has one more line!")
f.close()

print ("FILE read...")

f = open("demofile.txt", "r")
print(f.read())

# read a line
f = open("demofile.txt", "r")
print(f.readline())

