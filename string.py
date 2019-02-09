astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# mencari huruf o pertama
print (astring.index("o"))

# menghitung total huruf o
print astring.count("o")

# slicing print, mulai dari index ke-3 sampai index-7
print astring[3:7]

# mengambil -3 huruf terakhir
print astring[3:7:2]

# mengambil tiap 1 step dari huruf terakhir
print astring[3:7:1]

# membuat reverse kata
print astring[::-1]

# cek kata / huruf awal dan terakhir
print(astring.startswith("Hello"))
print(astring.endswith("ld!"))

# memisah dan menjadi array
afewwords= astring.split(" ")
print afewwords