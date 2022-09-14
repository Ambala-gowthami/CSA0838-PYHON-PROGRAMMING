total_user=int(input("Total Number of users : "))
if(total_user<=0):
    print("Invalid Input")
else:
    teach_staff_user=int(input("Staff Users : "))
    if (teach_staff_user>total_user):
        print("Invalid Input")
    elif (teach_staff_user<=0):
        print("Invalid Input")
    elif(total_user==teach_staff_user):
        print("Number of Student Users and Non-Teaching Staff Users are 0")
    else:
        non_teach_staff_user=teach_staff_user/3
        total_staff_user=teach_staff_user+non_teach_staff_user
        student_user=total_user-total_staff_user
        print("Number of Student user : ",student_user)
