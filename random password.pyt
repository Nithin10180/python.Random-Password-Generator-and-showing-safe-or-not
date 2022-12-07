import random
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "“QWERTYUIOPASDFGHIKLZXCVBNM"
digit = "@123456789"
spl_char = "~!@#$%*8&*()_ +=-{|?/[}]"
length =int(input("Enter the length of password you want: "))
a = []
a.extend(list(lower))
a.extend(list(upper))
a.extend(list(digit))
a.extend(list(spl_char))
random.shuffle(a)
empty = ""
password=empty.join(a[:length])
print("Password is:",password)
count_lower , count_upper , count_digit , count_spl_char = 0,0,0,0
for i in password:
    if(i.islower()):
        count_lower = count_lower+1
    elif(i.isupper()):
        count_upper = count_upper+1
    elif(i.isdigit()):
        count_digit = count_digit+1
    else:
        count_spl_char = count_spl_char+1
print("No. of special characters are:",count_spl_char)
if(count_spl_char>=3 and length>=12):
    print("Therefore your generated password is safe")
else:
    print("Therefore your generated password is not safe")
