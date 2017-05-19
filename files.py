f = open("sample.txt", "r")

quote = f.read()

print(quote)

quote2 = f.read() + "1" + "\n"

print(quote2)
f.seek(0)

quote3 = f.read()
print(quote3)

f.close()
