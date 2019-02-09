#  operator pangkat 
square = 7 ** 2
cube = 2 ** 3
print square
print cube

#  operator with string
helloworld = "hello" + " " + "world"
print helloworld

hello = "hello " * 10
# print hello 10x
print hello

# operator with list
even_number = [2,4,6,8]
odd_number = [1,3,5,7]
# menggabung list 
all_number = even_number + odd_number , haha
print sorted(all_number) 

print ([1,2,3] * 3) # print array (1,2,3) 3x sama seperti diatas

# Exercise
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")