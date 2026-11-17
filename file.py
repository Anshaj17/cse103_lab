f = open("numbers.txt","r")
total = 0
for line in f:
    num = int(line)
    total = total + num

f.close()

result = open("result.txt","w")
result.write("sum of numbers="+str(total))
result.close()
print("sum calculated successfully!")