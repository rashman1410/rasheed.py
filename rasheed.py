# grading calculator 

import math
maths = int(input(" maths score"))
english = int(input(" english score"))
java = int(input(" java score"))
web = int(input(" web score"))
grade = (maths+english+java+web/4)*(100)

A= 70, 100
B= 69, 60
C= 59, 50
D= 49, 45
E= 44, 40
F= 39, 0


if grade >= 70 and  grade <= 100:
        print("You received an A")

elif grade >= 60 and  grade< 69:
        print ("You received a B")

elif grade >= 50 and grade < 59:
        print("You received a C")

elif grade >= 45 and  grade< 49:
        print("You received a D")

elif grade >= 40 and  grade< 44:
        print("You received a D")

else:
        print("Sorry, you received an F")
