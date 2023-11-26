x=5
print(type(x))






x=int(input("Number1 "))
y=int(input("Number2 "))

print((x+12)**2-y**3)//9

my_string="welcome to python world"
print(my_string)

print("my_string[1:5]=",my_string[1:5])
print("my_string[5:-2]=",my_string[5:-2])

name = "aminat"
print(name[0])
print(name[-1])
print[0:4]



print("PARENTAL GUIDANCE")
parental_guidance=input("Enter pg rating")
age=input("How old are you")
if age >= parental_guidance:
    print("Welcome")
else:
    if age < 17:
        print("You are not allowed  on this content")







        # LEAP YEAR
        year = int(input("Enter year to check leap year "))
        if year % 4 == 0:
            print("The year is leap")
        else:
            print("This year is not leap")




numbers = [6,5,3,8,4,2,5,4,11]
for val in numbers:
    val = val *2
    print(val)
print("the for ends here")



sum = 0
i = 1
n=5
while i <= n:
    sum = sum + i
    i = i+1

    print("The sum is",sum)

    My_List = (2, 4, 6)
    for fo in My_List:
        print(2 * fo)


My_List =(2,4,6)
My_List=(2*4*6)
print(My_List)



my_list = ["Apples","Oranges","Watermelon","Pawpaw","Pineapple"]
print(my_list[0])
print(my_list[2])





Grades = [2,8,5,3,10]
print(Grades[2]+Grades[0])
print(Grades[1]*Grades[2])





my_list = [2,8,5,3,10]
print(my_list[2:5])
print(len(my_list))
my_list.append(20)
print(my_list)
my_list.insert(0,7)
print(my_list)
my_list[2]=11
print(my_list)


my_list = ["Apples","Oranges","Watermelon","Pawpaw","Pineapple"]
print(my_list[0])
print(my_list[2])
my_list[2]="Peas"
print(my_list)





my_list = [2,8,5,3,10]
print(my_list[2:5])
print(len(my_list))
my_list.append(20)
print(my_list)
my_list.insert(0,7)
print(my_list)
my_list[2]=11
print(my_list)
my_list.remove(11)
print(my_list)
del my_list[1]
print(my_list)


my_dictionary = {"Knowledge":"Data Science","tool":"python","year":2020}
for key in my_dictionary.keys():
    print(key)

    my_dictionary = {"Knowledge": "Data Science", "tool": "Python", "year": 2020}
    my_dictionary["Knowledge = Web Development"] = True
    print(my_dictionary)
    my_dictionary.pop("tool")
    print(my_dictionary)
    del my_dictionary

    my_set = {"python", "java", "R"}
    my_set.add("Scala")  # This adds "Scala" to my_set
    print(my_set)
    my_set.remove("R")  # This removes "R" from my_set
    print(my_set)

    liste = [1, 2, 3]
    Length = 0
    for i in liste:
        Length += 1
    # print('new Length',Length)
    print(Length)
    print(len(liste))