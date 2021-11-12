#1
def divide (x,y):
    return x / y

print(divide(4,2))

#2
def sum_numbers(numbers):
    return sum(numbers)

print(sum_numbers([1,2,3,4,5,6,7,8,9,10]))

#3
compare_list = lambda list_of_numbers : print("Big list" if len(list_of_numbers) >= 5 else "Small list")
compare_list([1,2,3,7])

#4
def string_upper_lower(text):
    letters_lowercase = []
    letters_uppercase = []

    for letter in text:
        if letter.isupper():
            letters_uppercase.append(letter)
        else:
            letters_lowercase.append(letter)
    def output():
        print(f"Uppercase letters: {len(letters_uppercase)}")
        print(f"Lowercase letters: {len(letters_lowercase)}")

    return output()

string_upper_lower("We are, all of us, given such a brief moment of time together, it hardly seems fair. But it’s precious, and maybe it’s enough, and maybe it’s right that our bodies dissolve into the earth, giving our energy back to it, feeding the little creatures in the ground and giving nutrients to the soil, and maybe it’s right that our consciousness rests. The thought is peaceful.")


#5
def meal_vouchers(lunch_cost, meal_voucher_value):
    print(f"Lunch cost: {lunch_cost} CZK")
    print(f"Pay in cash: {lunch_cost % meal_voucher_value} CZK")
    print(f"Pay in meal vouchers: {lunch_cost // meal_voucher_value} pcs, {meal_voucher_value} CZK each")

meal_vouchers(500,74)

#6
def compute_factorial(n):
    if n < 0:
       return "Factorial does not exist for negative numbers."
    elif n == 1:
        return n
    elif n == 0:
        return "1"
    else:
        return n*compute_factorial(n-1)

print(compute_factorial(0))

