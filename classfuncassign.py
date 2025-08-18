class MultipleClass:
    def subfields():
        list1 = ["MachineLearning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in list1:
            print(i)

    def odd_even():
        num1 = int(input("Enter a number: "))
        if num1 % 2 == 0:
            print(f"{num1} is Even number")
            cast1 = "Even num"
        else:
            print(f"{num1} is Odd number")
            cast1 = "Odd number"
        return cast1

    def eligible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if gender == "male" and age >= 21:
            print("ELIGIBLE")
        elif gender == "female" and age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage(sub1, sub2, sub3, sub4, sub5):
        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = (total / 500) * 100
        print(f"Subject1= {sub1}")
        print(f"Subject2= {sub2}")
        print(f"Subject3= {sub3}")
        print(f"Subject4= {sub4}")
        print(f"Subject5= {sub5}")
        print(f"Total : {total}")
        print(f"Percentage : {percentage}")
    

    def area(self, height, breadth):
        result = (height * breadth) / 2
        print("Height:", height)
        print("Breadth:", breadth)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", result)

    def perimeter(self, height1, height2, breadth):
        result = height1 + height2 + breadth
        print("Height1:", height1)
        print("Height2:", height2)
        print("Breadth:", breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", result)

    def triangle(self):
        self.area(32, 34)
        self.perimeter(2, 4, 4)
