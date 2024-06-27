from flask import Blueprint, render_template
import random
from random import randint, choice
from fractions import Fraction
import sympy


#prealgebra_2e = Blueprint('prealgebra_2e', __name__, template_folder='templates')

elementary_algebra_2e = Blueprint('elementary_algebra_2e', __name__,
                          url_prefix='/elementary_algebra_2e',
                          template_folder='templates',
                          static_folder='static')

#=================================================================================
#CHAPTER 1
#=================================================================================

import random
from flask import render_template

@elementary_algebra_2e.route('/place_value')
def place_value():
    # Generating a random integer with a random number of digits between 3 and 10
    number = random.randint(10**2, 10**10 - 1)

    # Converting the integer to string for easy access of individual digits
    num_str = str(number)
    
    # Randomly selecting 5 digits from the number
    digits = random.sample(num_str, 5) 

    # Computing the place value of each digit
    place_values = [10 ** (len(num_str) - 1 - num_str.index(d)) for d in digits]
    
    problem = f"In the following exercise find the place value of each digit. {number}"
    
    # Generating the table for problem in HTML
    table = '<table>'
    for i in range(5):
        table += f'<tr><td>ⓐ {digits[i]} </td></tr>'
    table += '</table>'
    
    problem += table

    answer = dict(zip(digits, place_values))

    explanation = f"The place value of a digit is determined by its position in the number. From right to left, the place value increases by a factor of 10. " \
                  f"For example, in the number 123, the place value of 1 is 100, 2 is 20 and 3 is 1. So for the number {number}, the place values are {answer}."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

import random
import inflect  # to convert numbers to words

@elementary_algebra_2e.route('/name_the_number')
def name_the_number():
    p = inflect.engine()  # create an inflect engine

    # Generating a random integer with a random number of digits between 3 and 9
    number = random.randint(10**2, 10**9 - 1)

    # Convert number to words
    number_in_words = p.number_to_words(number)

    problem = f"In the following exercise, name the number: {number}"
    answer = number_in_words

    explanation = f"The number {number} is pronounced as '{number_in_words}'."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

import random
import re
import inflect  # to convert numbers to words

p = inflect.engine()  # create an inflect engine

def text2int(textnum, numwords={}):
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

@elementary_algebra_2e.route('/number_to_digits')
def number_to_digits():
    # Generating a random integer with a random number of digits between 1 and 10
    number = random.randint(0, 10**10 - 1)

    # Convert number to words
    number_in_words = p.number_to_words(number)
    # Replace commas with empty spaces to allow for text2int processing
    number_in_words = re.sub(',', '', number_in_words)

    problem = f"In the following exercise, write each number as a whole number using digits: {number_in_words}"
    answer = number

    explanation = f"The number '{number_in_words}' is written as '{number}' in digit form."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

import random

@elementary_algebra_2e.route('/round_to_place_value')
def round_to_place_value():
    # Select randomly from the list of numbers and place values
    numbers = [407, 8564, 25846, 25864, 864951, 3972849]
    place_values = [10, 100, 1000, 10000]
    number = random.choice(numbers)
    place_value = random.choice(place_values)

    # Define problem
    if place_value == 10:
        place_name = "nearest ten"
    elif place_value == 100:
        place_name = "nearest hundred"
    elif place_value == 1000:
        place_name = "nearest thousand"
    elif place_value == 10000:
        place_name = "nearest ten thousand"

    problem = f"Round the number {number} to the {place_name}."

    # Round number
    answer = round(number, -len(str(place_value)) + 1)

    # Define explanation
    explanation = f"The number {number} rounded to the {place_name} is {answer}."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

import random

@elementary_algebra_2e.route('/identify_multiples_factors')
def identify_multiples_factors():
    # Generate a random number between 100 and 1500
    number = random.randint(100, 1500)

    # Divisibility tests
    divisors = [2, 3, 5, 6, 10]
    results = []
    for divisor in divisors:
        if number % divisor == 0:
            results.append(f"{number} is divisible by {divisor}.")
        else:
            results.append(f"{number} is not divisible by {divisor}.")

    # Define problem
    problem = f"Use the divisibility tests to determine whether the number {number} is divisible by 2, 3, 5, 6, and 10."

    # Define answer
    answer = '<br>'.join(results)

    # Define explanation
    explanation = "A number is divisible by: <br>" \
                  "2, if its last digit is 0, 2, 4, 6, or 8. <br>" \
                  "3, if the sum of its digits is divisible by 3. <br>" \
                  "5, if its last digit is 0 or 5. <br>" \
                  "6, if it is divisible by both 2 and 3. <br>" \
                  "10, if its last digit is 0. <br>" + answer

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

from sympy import primefactors
import random

@elementary_algebra_2e.route('/prime_factorization')
def prime_factorization():
    # Random number for prime factorization
    number = random.randint(100, 1000)

    # Prime Factorization
    factors = primefactors(number)
    prime_factorization = ' x '.join(map(str, factors))

    # Define problem
    problem = f"Find the prime factorization of the number {number}."

    # Define answer
    answer = f"The prime factorization of {number} is {prime_factorization}."

    # Define explanation
    explanation = f"The prime factorization of a number is obtained by dividing the number by prime numbers starting from 2 until the number becomes 1."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

from sympy import lcm
import random

@elementary_algebra_2e.route('/least_common_multiple')
def least_common_multiple():
    # Random numbers for which LCM is to be found
    num1 = random.randint(10, 30)
    num2 = random.randint(10, 30)

    # Least Common Multiple
    lcm_value = lcm(num1, num2)

    # Define problem
    problem = f"Find the Least Common Multiple (LCM) of {num1} and {num2}."

    # Define answer
    answer = f"The Least Common Multiple (LCM) of {num1} and {num2} is {lcm_value}."

    # Define explanation
    explanation = f"The Least Common Multiple (LCM) of two integers {num1} and {num2} is the smallest positive integer that is divisible by both {num1} and {num2}."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@elementary_algebra_2e.route('/combine_like_terms')
def combine_like_terms():
    # Random numbers for the terms
    coef1 = random.randint(1, 10)
    coef2 = random.randint(1, 10)
    constant1 = random.randint(1, 10)
    constant2 = -random.randint(1, 10)

    # Combine like terms
    combined_coef = coef1 + coef2
    combined_constant = constant1 + constant2

    # Define problem
    problem = f"Combine like terms: {coef1}n + {constant1} + {coef2}n + {constant2}."

    # Define answer
    answer = f"The result of combining like terms is {combined_coef}n + {combined_constant}."

    # Define explanation
    explanation = f"We combine the 'n' terms ({coef1}n + {coef2}n = {combined_coef}n) and the constant terms ({constant1} + {constant2} = {combined_constant}) separately."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@elementary_algebra_2e.route('/evaluate_expression')
def evaluate_expression():
    # Random numbers for the variables and constant
    x = -random.randint(1, 10)
    a = -random.randint(1, 10)
    num = random.randint(1, 20)

    # Evaluate the expressions
    value_x = -abs(x)
    value_a = num - a

    # Define problems and answers
    problem_x = f"Evaluate -|x| when x = {x}"
    answer_x = f"The result of -|x| when x = {x} is {value_x}."
    explanation_x = f"-|x| is negative of the absolute value of x. When x = {x}, |x| = {-x}, so -|x| = {value_x}."

    problem_a = f"Evaluate {num} - a when a = {a}"
    answer_a = f"The result of {num} - a when a = {a} is {value_a}."
    explanation_a = f"{num} - a is simply subtracting a from {num}. When a = {a}, {num} - a = {value_a}."

    # Decide randomly which problem to display
    if random.choice([True, False]):
        return render_template('problem_elementary_algebra_2e.html', problem=problem_x, answer=answer_x, explanation=explanation_x)
    else:
        return render_template('problem_elementary_algebra_2e.html', problem=problem_a, answer=answer_a, explanation=explanation_a)
#=================================================================================

import random

@elementary_algebra_2e.route('/translate_and_simplify_expression')
def translate_and_simplify_expression():
    # Randomly defining the numbers in the expression
    number = random.randint(-50, 50)  # Random integer between -50 and 50
    less_value = random.randint(1, 50)  # Random integer between 1 and 50

    # Evaluating the expression
    result = number - less_value

    # Define the problem statement
    if number < 0:
        number_statement = f"negative {abs(number)}"
    else:
        number_statement = str(number)
    problem = f"Translate to an algebraic expression and simplify: {less_value} less than {number_statement}."

    # Define the answer
    answer = f"{number} - {less_value} = {result}"

    # Explanation
    explanation = f"The term '{less_value} less than {number_statement}' means we subtract {less_value} from {number}. This is represented as the algebraic expression '{number} - {less_value}'. The simplified result is {result}."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@elementary_algebra_2e.route('/calculate_new_balance')
def calculate_new_balance():
    # Generate random initial balance and deposit
    initial_balance = -random.randint(1, 100)  # random negative balance
    deposit = random.randint(1, 200)

    # Calculate the new balance
    new_balance = initial_balance + deposit

    # Define the problem statement
    problem = f"Monique has a balance of −\${abs(initial_balance)} in her checking account. She deposits \${deposit} to the account. What is the new balance?"

    # Define the answer
    answer = f"${new_balance}"

    # Explanation
    explanation = f"Given that Monique had an initial balance of −${abs(initial_balance)} and she deposited ${deposit} to the account, her new balance becomes: <br> New balance = Initial balance + Deposit <br> New balance = (−${abs(initial_balance)}) + ${deposit} = ${new_balance}"

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@elementary_algebra_2e.route('/round_to_nearest_hundredth')
def round_to_nearest_hundredth():
    # Generate random number
    number = random.uniform(1, 1000)  # This will ensure a number between 1 and 1000 with decimal places

    # Round the number to the nearest hundredth
    rounded_number = round(number, 2)

    # Define the problem statement
    problem = f"Round {number:.4f} to the nearest hundredth."

    # Define the answer
    answer = f"{rounded_number:.2f}"

    # Explanation
    explanation = f"To round {number:.4f} to the nearest hundredth, consider the third decimal place. Since it's {int((number*1000) % 10)}, the number rounds to {rounded_number:.2f}."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@elementary_algebra_2e.route('/convert_fraction_to_decimal')
def convert_fraction_to_decimal():
    # Generate random numerator and denominator ensuring no division by zero
    numerator = random.randint(1, 20)
    denominator = random.randint(1, 20)
    while denominator == 0:
        denominator = random.randint(1, 20)
    
    # Convert the fraction to decimal
    decimal_value = numerator / denominator

    # Define the problem statement
    problem = f"Convert \\(\\frac{{{numerator}}}{{{denominator}}}\\) to a decimal."

    # Define the answer
    answer = f"{decimal_value:.2f}"

    # Explanation
    explanation = f"Dividing {numerator} by {denominator} gives the decimal value {decimal_value:.2f}."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@elementary_algebra_2e.route('/convert_decimal_to_percent')
def convert_decimal_to_percent():
    # Generate a random decimal value between 0 and 5
    decimal_value = random.uniform(0, 5)

    # Convert the decimal to a percent
    percent = decimal_value * 100

    # Define the problem statement
    problem = f"Convert {decimal_value:.2f} to a percent."

    # Define the answer
    answer = f"{percent:.2f}%"

    # Explanation
    explanation = f"To convert a decimal to a percent, you multiply by 100. So, {decimal_value:.2f} multiplied by 100 gives {percent:.2f}%."

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random
from flask import Flask, render_template

app = Flask(__name__)

@elementary_algebra_2e.route('/simplify_expression_1')
def simplify_expression_1():
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)
    z = random.randint(-20, 20)
    a = random.randint(2, 5)  # Keeping the exponent range between 2 and 5 for reasonable results.
    
    # Generate problem
    problem_expression = f"{x} + 10({y} + {z}) - {a}^2"
    problem_latex = f"${x} + 10({y} + {z}) - {a}^2$"
    
    # Compute answer
    answer = x + 10*(y + z) - a**2
    
    explanation = f"The solution to the expression {problem_latex} is {answer}."
    
    return render_template('problem_elementary_algebra_2e.html', problem=problem_latex, answer=answer, explanation=explanation)
#=================================================================================

@elementary_algebra_2e.route('/multiply_fractions')
def multiply_fractions():
    # Generate random numerators and denominators for the fractions
    num1 = random.randint(1, 12)
    den1 = random.randint(1, 12)
    
    num2 = random.randint(1, 12)
    den2 = random.randint(1, 12)

    # Generate problem in LaTeX format
    problem_latex = f"\\frac{{{num1}}}{{{den1}}} \\times \\frac{{{num2}}}{{{den2}}}"
    problem = f"Solve the expression: $${problem_latex}$$"

    # Compute answer
    numerator_result = num1 * num2
    denominator_result = den1 * den2

    # Simplifying the result
    from math import gcd
    common_factor = gcd(numerator_result, denominator_result)
    simplified_numerator = numerator_result // common_factor
    simplified_denominator = denominator_result // common_factor

    answer_latex = f"\\frac{{{simplified_numerator}}}{{{simplified_denominator}}}"
    answer = f"$${answer_latex}$$"

    explanation = (f"To solve the expression, multiply the numerators and the denominators respectively. "
                   f"The result is {answer_latex}. After simplifying, this becomes our final answer.")

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@elementary_algebra_2e.route('/divide_fractions')
def divide_fractions():
    # Generate random numerators and denominators for the fractions
    num1 = random.randint(1, 12)
    den1 = random.randint(1, 12)
    
    num2 = random.randint(1, 12)
    den2 = random.randint(1, 12)

    # Ensure denominator of second fraction (which will become the numerator during division) isn't 0
    while num2 == 0:
        num2 = random.randint(1, 12)

    # Generate problem in LaTeX format for division of fractions
    problem_latex = f"\\frac{{{num1}}}{{{den1}}} \\div \\frac{{{num2}}}{{{den2}}}"
    problem = f"Solve the expression: $${problem_latex}$$"

    # To divide fractions, multiply by the reciprocal of the second fraction
    numerator_result = num1 * den2
    denominator_result = den1 * num2

    # Simplifying the result
    from math import gcd
    common_factor = gcd(numerator_result, denominator_result)
    simplified_numerator = numerator_result // common_factor
    simplified_denominator = denominator_result // common_factor

    answer_latex = f"\\frac{{{simplified_numerator}}}{{{simplified_denominator}}}"
    answer = f"$${answer_latex}$$"

    explanation = (f"To divide the two fractions, multiply the first fraction by the reciprocal of the second fraction. "
                   f"The result is $${answer_latex}$$. After simplifying, this becomes our final answer.")

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@elementary_algebra_2e.route('/simplify_expression')
def simplify_expression():
    # Generate a random coefficient for the outside of the expression
    coefficient = random.randint(-20, -10)
    
    # Generate a random coefficient for the inside of the expression, multiplied with a variable 'p'
    inner_coefficient = random.randint(50, 60)

    # Calculate the answer
    answer_value = coefficient * inner_coefficient
    answer = f"{answer_value}p"

    # Construct the problem expression
    problem = f"{coefficient}({inner_coefficient}p)"

    # Explanation in the form of a Mathjax formatted string
    explanation = f"To solve this, distribute {coefficient} across the inside of the parentheses: "
    explanation += f"\\\\ {coefficient} \\times {inner_coefficient}p = {answer}"

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@elementary_algebra_2e.route('/simplify_fraction_expression')
def simplify_fraction_expression():
    # The coefficient is -14
    coefficient = -14

    # Fixed values for the fraction
    numerator = 5
    denominator = 7

    # Calculate the intermediate result by multiplying coefficient with fraction's numerator
    intermediate_value = coefficient * numerator

    # Final multiplication with the variable p
    answer = f"{int(intermediate_value/denominator)}p"

    # Construct the problem expression
    problem = f"{coefficient}({numerator}/{denominator}p)"

    # Explanation in the form of a Mathjax formatted string
    explanation = f"To simplify this expression, distribute the coefficient {coefficient} across the fraction: "
    explanation += f"\\\\ {coefficient} \\times ({numerator}/{denominator}p) = {int(intermediate_value/denominator)}p"
    explanation += f"\\\\ So, the simplified expression is: {answer}"

    return render_template('problem_elementary_algebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================









