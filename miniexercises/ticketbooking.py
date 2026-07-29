age=int(input("enter ypur age"))
student=input("are you a student(y/n)??")
weekend=input("are you booking tickets for weekend(y/n)??")
vip=input("do you want vip ticket(y/n)??")

total=0
base=200
child_disc=0
student_disc=0
weekend_charge=0
vip_charge=0

if age>0 and age <15:
    child_disc=0.10*base
    student_disc=0
elif student=='y' or student=='Y':
    student_disc=0.5*base
    child_disc=0
else:
    student_disc=0
    child_disc=0

if weekend=='y' or weekend=='Y':
    weekend_charge=100
else:
    weekend_charge=0

if vip=='y' or vip =='Y':
    vip_charge=150
else:
    vip_charge=0

total=base+weekend_charge+vip_charge

total=total-student_disc-child_disc

print("\n total charge is: ",total)

