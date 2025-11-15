#addition of two numbers    1
def add2(a,b):
    return a+b

#biggest of two numbers     2
def comparing2(a,b):
    if  a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{b} is greater than {a}"

#given number is even or odd    3
def evenOdd(a):
    if a%2==0:
        return f"{a} is even"
    else:
        return f"{a} is odd"

#grade through average of three subjects    4
def avggrade(a,b,c):
    avg=(a+b+c)/3
    if avg>=90:
        return f"grade is A+ with average {avg}"
    elif avg<90 and avg>=80:
        return f"grade is A with average {avg}"
    elif avg<80 and avg>=70:
        return f"grade is A- with average {avg}"
    elif avg<70 and avg>=60:
        return f"grade is B+ with average{avg}"
    elif avg<60 and avg>=50:
        return f"grade is B with average {avg}"
    else:
        return "You have failed"

#natural numbers in order   5
def naturalnumbers10():
    for i in range(1,11):
        return i

#natural numbers in reverse order   6
def naturalnumbers10rev():
    for i in range(10,0,-1):
        return i

#first ten natural even numbers     7
def evennaturalnumbers10():
    for i in range(1,11):
        result = i*2
        return result

#function to print numbers between the range(10 to 100 or 100 to 200)   8
def inrange(initial,final):
    for i in range(initial, final+1):
        return i

#print mathetical table of a number     9
def mathtable(x):
    result = ""
    for i in range(1,11):
        result+= f"{x}x{i}={x*i}"
    return result

#prime or not   10
def primeornot(a):
    if a<=1:
        return "Not a prime number"
    for i in range(2,a):
        if a%i==0:
            return "Not prime"
    return "prime"

#sum of digits of given number   11
def sumofdigits(a):
    sum=0
    while a>0:
        digit=a%10
        sum+=digit
        a//=10
    return sum

#prime numbers till 100     12
def primestill100():
    count=0
    a=1
    while count<100:
        prime=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                prime=False
                break
        if prime:
            print(a)
            count+=1
        a+=1

#lucky number?      13
def lucky_number(a):
    while a > 9:
        sum = 0
        while a > 0:
            sum += a % 10
            a //= 10
        a = sum
    return a

#reverse a given number     14
def revnum(a):
    return int(str(a)[::-1])

#palindrome number  15
def palindromenum(a):
    if a==int(str(a)[::-1]):
        return "Number is palindrome"
    else:
        return "Number is not a palindrome"

#factorial of a number    16
def factorial(a):
    factorial=1
    for i in range(1,a+1):
        factorial=factorial*i
    return factorial

#number of combinations for given n and r (ncr)     17
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def ncr(n, r):
    return fact(n) // (fact(n - r) * fact(r))

#convert digit into word format     18
def number_to_words(n):
    ones = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n - 10]
    if n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + " " + ones[n % 10]
    if n < 1000:
        hundred_part = ones[n // 100] + " Hundred"
        remaining = n % 100
        if remaining == 0:
            return hundred_part
        else:
            return hundred_part + " " + number_to_words(remaining)
