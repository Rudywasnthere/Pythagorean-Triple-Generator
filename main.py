##Rudy Garcia

print("Hi, I\'m here to give you Pythagorean triples!")
x= int(input("All I need is for yu to give me the smallest number in it:\n"))
y=x/2
z= x/4
if y.is_integer() is True:
  if z.is_integer() is True:
    print("This actually makes a triple starting with an odd number")
    triple_2= ((x**2)-4)/4
    triple_3= x +1
    print(f"Here it is:\n({triple_2},{int(x)},{triple_3})")
  if z.is_integer() is False:
    triple_2= ((x**2)-4)/4
    triple_3= triple_2 + 2
    print(f"Here it is:\n({int(x)},{triple_2},{triple_3})")
else:
  triple_2= ((x**2)-1)/2
  triple_3= triple_2 + 1
  print(f"Here it is:\n({int(x)},{triple_2},{triple_3})")
print("If you'd like to know the math behind it go here:")