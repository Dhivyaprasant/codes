number = int(input("enter the number:"))
reverse_no = 0
while(number>0):
    remainder = number%10
    reverse_no=(reverse_no*10)+remainder
    number = number//10
    print("the reversed number:",reverse_no)


# other way to solve

number=input("enter the number:")
    reversed_no= (number[::-1])
    print(reversed_no)
