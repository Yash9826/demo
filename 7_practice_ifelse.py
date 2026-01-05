a = 50
b = 20
# if a>b: print(a)
temp = a if a<b else b
print(temp)

score = 50
attendance = 90
submitted = True

if score >= 60:
    if attendance>=80:
        if submitted:
            print("passed with good standing")
        else:
            print("passed but not have assginment")
    else:
        print("passed but low attendance")   
else:
    print("Failed")    