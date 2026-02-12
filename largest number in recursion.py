n=int(input("Enter number:"))
def largest_digit(n):
    if n<10:
        return n
    digit=n%10
    small_digit=largest_digit(n//10) 
    if digit>small_digit:
        return digit
    else:
        return small_digit  
print("the largest number is:",largest_digit(n))          