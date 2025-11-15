# 1. Addition of two numbers
def add2(a, b):
    return a + b
# 2. Biggest of two numbers
def comparing2(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{b} is greater than {a}"
# 3. Given number is even or odd
def evenOdd(a):
    if a % 2 == 0:
        return f"{a} is even"
    else:
        return f"{a} is odd"
# 4. Grade through average of three subjects
def avggrade(a, b, c):
    avg = (a + b + c) / 3
    if avg >= 90:
        return f"Grade is A+ with average {avg}"
    elif avg >= 80:
        return f"Grade is A with average {avg}"
    elif avg >= 70:
        return f"Grade is A- with average {avg}"
    elif avg >= 60:
        return f"Grade is B+ with average {avg}"
    elif avg >= 50:
        return f"Grade is B with average {avg}"
    else:
        return "You have failed"
# 5. Natural numbers from 1 to 10
def naturalnumbers10():
    return [i for i in range(1, 11)]
# 6. Natural numbers in reverse (10 to 1)
def naturalnumbers10rev():
    return [i for i in range(10, 0, -1)]
# 7. First 10 natural even numbers
def evennaturalnumbers10():
    return [i * 2 for i in range(1, 11)]
# 8. Numbers in a given range
def inrange(initial, final):
    return [i for i in range(initial, final + 1)]
# 9. Mathematical table of a number
def mathtable(x):
    result = ""
    for i in range(1, 11):
        result += f"{x} x {i} = {x * i}\n"
    return result
# 10. Prime or not
def primeornot(a):
    if a <= 1:
        return "Not a prime number"
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return "Not prime"
    return "Prime"
# 11. Sum of digits of a number
def sumofdigits(a):
    total = 0
    while a > 0:
        total += a % 10
        a //= 10
    return total
# 12. First 100 prime numbers
def primestill100():
    primes = []
    num = 2
    while len(primes) < 100:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes
# 13. Lucky number (digit sum repeated until single digit)
def lucky_number(a):
    while a > 9:
        s = 0
        while a > 0:
            s += a % 10
            a //= 10
        a = s
    return a
# 14. Reverse a number
def revnum(a):
    return int(str(a)[::-1])
# 15. Palindrome number check
def palindromenum(a):
    if a == int(str(a)[::-1]):
        return "Number is palindrome"
    else:
        return "Number is not a palindrome"
# 16. Factorial of a number
def factorial(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    return f
# 17. NCR combination formula
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def ncr(n, r):
    return fact(n) // (fact(n - r) * fact(r))
# 18. Convert number to words (0–999)
def number_to_words(n):
    ones = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen",
             "Sixteen","Seventeen","Eighteen","Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
            "Seventy", "Eighty", "Ninety"]

    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n - 10]
    if n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        return tens[n // 10] + " " + ones[n % 10]
    if n < 1000:
        hundred = ones[n // 100] + " Hundred"
        rem = n % 100
        if rem == 0:
            return hundred
        return hundred + " " + number_to_words(rem)
