# Python3 program for focal lenght crop factor

# Funtion to multiply APC Crop Factor by Focal Lenght
sony = float(1.5)
canon = float(1.6)
fuji = float(1.5)
leica = float(1.5)


def multiply(select, fl):
    return select * fl

print("Please select sensor by camera brand -\n" \
    "1. Sony\n" \
    "2. Canon\n" \
    "3. Fuji\n" \
    "4. Leica\n") 

# Take input from the user
select = input("Select Crop Factor from 1, 2, 3, 4 : ")

fl = int(input("Enter Focal Lenght: "))

if select == '1':
    print(sony, "*", fl, "=",
          multiply(sony, fl))
    
elif select == '2':
    print(canon, "*", fl, "=",
          multiply(canon, fl))

elif select == '3':
    print(fuji, "*", fl, "=",
          multiply(fuji, fl))

elif select == '4':
    print(leica, "*", fl, "=",
          multiply(leica, fl))
else: 
	print("Invalid input")
