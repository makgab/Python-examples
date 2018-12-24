# exeption

try:
  print(x)
except:
  print("An exception occurred")


print ("FILE handle")

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
