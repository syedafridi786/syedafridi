school_name=input("pk school")
student=input("enter the name :")
s1=int(input("tamil :"))
s2=int(input("english :"))
s3=int(input("maths :"))
s4=int(input("science :"))
s5=int(input("social :"))
total=s1+s2+s3+s4+s5
if s1>=35:
    print(s1,"/100 PASS TAMIL")
elif s1<35:
    print(s1,"/100 FAIL TAMIL")
if s2>=35:
    print(s1,"/100 PASS ENGLISH")
elif s2<35:
    print(s2,"/100 FAIL ENGLISH")
if s3>=35:
    print(s3,"/100 PASS MATHS")
elif s3<35:
    print(s3,"/100 FAIL MATHS")
if s4>=35:
    print(s4,"/100 PASS SCIENCE")
elif s4<35:
    print(s4,"/100 FAIL SCIENCE")
if s5>=35:
    print(s5,"/100 PASS SOCIAL")
elif s5<35:
    print(s5,"/100 FAIL SOCIAL")
print("TOTAL :",total)
avg=(total/500*(100))
print("AVERAGE :",avg)
if avg>=90:
    print("O GRADE")
elif avg>=80:
    print("A GRADE")
elif avg>=60:
    print("B GRADE")
else:
    print("Z GRADE")

