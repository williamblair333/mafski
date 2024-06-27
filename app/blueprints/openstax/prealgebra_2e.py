from flask import Blueprint, render_template
import random
from random import randint, choice
from fractions import Fraction
import sympy


#prealgebra_2e = Blueprint('prealgebra_2e', __name__, template_folder='templates')

prealgebra_2e = Blueprint('prealgebra_2e', __name__,
                          url_prefix='/prealgebra_2e',
                          template_folder='templates',
                          static_folder='static')

#=================================================================================
#CHAPTER 3
#=================================================================================

@prealgebra_2e.route('/translate_algebra')
def translate_algebra():
    num_1, num_2 = randint(1, 10), randint(1, 10)
    equation_1 = f"{num_1} * {num_2}"
    equation_2 = f"15 - x"
    
    num_3 = randint(1, 20)
    operation = '-' if randint(0, 1) == 0 else '+'
    equation_2 = f"{num_3} {operation} x"

    problem = f"In the following exercises, translate from an algebraic equation to English phrases.<br>{equation_1}<br>{equation_2}"

    answer_1 = f"{num_1} multiplied by {num_2}<br>"
    answer_2 = "Fifteen minus x"

    answer = f"{answer_1} {answer_2}"

    explanation = f"The algebraic equation '{equation_1}' translates to English phrase as '{answer_1}'.<br><br>" \
                  f"The algebraic equation '{equation_2}' translates to English phrase as '{answer_2}'."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/identify_expression_equation')
def identify_expression_equation():
    operation1 = random.choice(["+", "-"])
    operation2 = random.choice(["=", ""])
    operation3 = random.choice(["=", ""])

    first_expression = f"6 \cdot {random.randint(1,10)} {operation1} {random.randint(1,10)}"
    second_expression = f"x {operation2} {random.randint(1,10)}"
    third_expression = f"{random.randint(1,10)} \cdot {random.randint(1,10)} {operation3} {random.randint(1,10)}"

    problem = f"In the following exercises, identify each as an expression or equation.<br><br> 1) $ {first_expression} $ <br> 2) $ {second_expression} $ <br> 3) $ {third_expression} $"
    answer_a = "Expression" if "=" not in first_expression else "Equation"
    answer_b = "Expression" if "=" not in second_expression else "Equation"
    answer_c = "Expression" if "=" not in third_expression else "Equation"
    answer = f"1) {answer_a}<br> 2) {answer_b}<br> 3) {answer_c}"
    explanation = f"An expression is a combination of numbers, variables and operators, but it does not have an equals sign.<br>An equation is a statement that two expressions are equal (it has an equals sign)."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/write_exponential_expanded')
def write_exponential_expanded():
    # Select random number for base and power
    base_n = random.randint(2, 10)
    power_n = random.randint(2, 10)
    base_p = random.randint(2, 5)
    power_p = random.randint(2, 5)
    
    # Problem
    problem = "$$ " + " \\cdot ".join([str(base_n)] * power_n) + " $$ Write this in exponential form. <br> \
                $$ " + str(base_p) + "^" + str(power_p) + " $$ Write this in expanded form and then simplify."
    
    # Answer
    answer = "$$ " + str(base_n) + "^" + str(power_n) + " $$ <br> $$ " + " \\cdot ".join([str(base_p)] * power_p) + \
             " = " + str(base_p ** power_p) + " $$"
    
    # Explanation
    explanation = "When the same number is multiplied by itself, we write it in exponential form. Here, " + str(base_n) + \
                  " is multiplied by itself " + str(power_n) + " times, so it is written as $$ " + str(base_n) + "^" + str(power_n) + \
                  " $$. <br> When we expand $$ " + str(base_p) + "^" + str(power_p) + " $$, it means " + str(base_p) + " is multiplied by " + \
                  "itself " + str(power_p) + " times. Therefore, $$ " + str(base_p) + "^" + str(power_p) + " $$ in expanded form is $$ " + \
                  " \\cdot ".join([str(base_p)] * power_p) + " $$. Multiplying these together gives " + str(base_p ** power_p) + "."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/evaluate_expressions')
def evaluate_expressions():
    # Randomly generate numbers
    num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = [random.randint(1, 9) for _ in range(10)]
    # Forming expressions
    exp1 = f"{num1} + {num2} * {num3}"
    exp2 = f"({num4} + {num5}) * {num6}"
    exp3 = f"{num7} + {num8} * ({num9} - {num1})"
    exp4 = f"({num2} + {num3}) / {num4} + {num5}"
    exp5 = f"({num6} + {num7})**2"
    exp6 = f"{num8} * ({num9} + {num10} * ({num1} - {num2}))"
    # LaTeX formatted expressions
    latex_exp1 = f"{num1} + {num2} \\cdot {num3}"
    latex_exp2 = f"({num4} + {num5}) \\cdot {num6}"
    latex_exp3 = f"{num7} + {num8}({num9} - {num1})"
    latex_exp4 = f"({num2} + {num3}) \\div {num4} + {num5}"
    latex_exp5 = f"({num6} + {num7})^2"
    latex_exp6 = f"{num8}[{num9} + {num10}({num1} - {num2})]"
    # Problem
    problem = f"Evaluate these expressions:<br> 1. $$ {latex_exp1} $$ 2. $$ {latex_exp2} $$ 3. $$ {latex_exp3} $$ 4. $$ {latex_exp4} $$ 5. $$ {latex_exp5} $$ 6. $$ {latex_exp6} $$"
    # Answer
    answer = f"1. $$ {eval(exp1)} $$ 2. $$ {eval(exp2)} $$ 3. $$ {eval(exp3)} $$ 4. $$ {eval(exp4)} $$ 5. $$ {eval(exp5)} $$ 6. $$ {eval(exp6)} $$"
    # Explanation
    explanation = "To evaluate these expressions, we follow the order of operations, which is parentheses, exponents, multiplication and division (from left to right), addition and subtraction (from left to right). This can be remembered by the acronym PEMDAS."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@prealgebra_2e.route('/evaluate_expression')
def evaluate_expression():
    # Randomly choose variables
    x_val = randint(1, 10)
    y_val = randint(1, 10)
    a_val = randint(1, 10)
    b_val = randint(1, 10)
    h_val = randint(1, 10)
    w_val = randint(1, 10)

    # Define the expressions
    expressions = [f'8x - 3 \\text{{ when }} x = {x_val}',
                   f'y^3 \\text{{ when }} y = {y_val}',
                   f'6a - 2b \\text{{ when }} a = {a_val} \\text{{ and }} b = {b_val}',
                   f'hw \\text{{ when }} h = {h_val} \\text{{ and }} w = {w_val}']

    # Evaluate the expressions
    answers = [8 * x_val - 3,
               y_val ** 3,
               6 * a_val - 2 * b_val,
               h_val * w_val]

    # Explanations are just the calculation steps
    explanations = [f'8 \\cdot {x_val} - 3 = {answers[0]}',
                    f'{y_val}^3 = {answers[1]}',
                    f'6 \\cdot {a_val} - 2 \\cdot {b_val} = {answers[2]}',
                    f'{h_val} \\cdot {w_val} = {answers[3]}']

    # Choose a random expression
    idx = randint(0, len(expressions) - 1)
    
    problem = f'Evaluate the expression: \\({expressions[idx]}\\)'
    answer = f'The answer is: \\({answers[idx]}\\)'
    explanation = f'Here is the calculation: \\({explanations[idx]}\\)'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/simplify_expression')
def simplify_expression():
    # Randomly choose coefficients
    coeff1, coeff2, coeff3, coeff4 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
    # Randomly choose variables
    variable1, variable2 = choice(['x', 'y', 'z', 'a', 'b', 'c']), choice(['m', 'n', 'o', 'p', 'q', 'r'])

    # Define the expressions
    expressions = [f'{coeff1}{variable1} + {coeff2}{variable1}',
                   f'{coeff3}{variable2} + {coeff4} + {variable2} + 3']

    # Evaluate the expressions
    answers = [f'{coeff1 + coeff2}{variable1}',
               f'{coeff3 + 1}{variable2} + {coeff4 + 3}']

    # Explanations are just the calculation steps
    explanations = [f'Combine like terms: {coeff1}{variable1} + {coeff2}{variable1} = {answers[0]}',
                    f'Combine like terms: {coeff3}{variable2} + {coeff4} + {variable2} + 3 = {answers[1]}']

    # Choose a random expression
    idx = randint(0, len(expressions) - 1)
    
    problem = f'Simplify by combining like terms: \\({expressions[idx]}\\)'
    answer = f'The simplified expression is: \\({answers[idx]}\\)'
    explanation = f'Here is the calculation: {explanations[idx]}'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_equation')
def solve_equation():
    # Randomly choose coefficients and constants
    const1, const2, const3, const4 = randint(1, 50), randint(51, 100), randint(1, 50), randint(51, 100)
    # Randomly choose variables
    variable1, variable2 = choice(['n', 'x', 'y', 'z', 'a', 'b', 'c']), choice(['x', 'y', 'z', 'a', 'b', 'c'])

    # Define the equations
    equations = [f'{variable1} - {const1} = {const2}',
                 f'{variable2} + {const3} = {const4}']

    # Evaluate the equations
    answers = [f'{variable1} = {const2 + const1}',
               f'{variable2} = {const4 - const3}']

    # Explanations are just the calculation steps
    explanations = [f'Solving for {variable1}, we add {const1} to both sides of the equation: {variable1} = {answers[0]}',
                    f'Solving for {variable2}, we subtract {const3} from both sides of the equation: {variable2} = {answers[1]}']

    # Choose a random equation
    idx = randint(0, len(equations) - 1)
    
    problem = f'In the following exercise, solve the equation: \\({equations[idx]}\\)'
    answer = f'The solution is: \\({answers[idx]}\\)'
    explanation = f'Here is the calculation: {explanations[idx]}'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/translate_solve')
def translate_solve():
    # Randomly generate y
    y = randint(35, 100)
    # Randomly choose greater than or less than
    op = randint(0, 1)
    if op == 0:
        problem = f'15 less than a number is {y-15}.'
        equation = f'y - 15 = {y-15}'
        explanation = f"Translating the English sentence into an algebraic equation gives us: {equation}. Solving this equation gives us the value of y."
        answer = f'The equation is: {equation}, so y = {y}'
    else:
        problem = f'A number plus 15 is {y+15}.'
        equation = f'y + 15 = {y+15}'
        explanation = f"Translating the English sentence into an algebraic equation gives us: {equation}. Solving this equation gives us the value of y."
        answer = f'The equation is: {equation}, so y = {y}'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/list_multiples')
def list_multiples():
    # Choose a random number for multiples
    num = randint(2, 10)
    # Choose a random upper limit
    limit = randint(20, 50)
    # Randomly choose less than or greater than
    op = randint(0, 1)
    if op == 0:
        problem = f'List all the multiples of {num} that are less than {limit}.'
        multiples = [i for i in range(num, limit, num)]
        explanation = f'The multiples of {num} less than {limit} are obtained by repeatedly adding {num} starting from 0 until we reach a number less than {limit}.'
    else:
        problem = f'List all the multiples of {num} that are greater than {limit}.'
        multiples = [i for i in range(limit + 1, limit + 10 * num, num)]
        explanation = f'The multiples of {num} greater than {limit} are obtained by repeatedly adding {num} starting from {limit + 1}.'
    answer = ', '.join(str(m) for m in multiples)

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/find_factors')
def find_factors():
    # Choose a random number to factor
    num = randint(50, 100)
    problem = f'Find all the factors of {num}.'
    factors = sympy.divisors(num)
    answer = ', '.join(str(f) for f in factors)
    explanation = f'The factors of {num} are all the integers that divide {num} without leaving a remainder.'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================
#=================================================================================
#CHAPTER 3
#=================================================================================
#=================================================================================

from flask import Flask, render_template
from flask import url_for
import random
import os
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, simplify, Abs


def create_empty_number_line(numbers, min_val=-10, max_val=10):
    fig, ax = plt.subplots(figsize=(10, 2))

    ax.set_xlim(min_val, max_val)
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_ticks([])
    ax.xaxis.set_ticks(np.arange(min_val, max_val+1, 1))
    
    plt.xticks(fontsize=8)
    plt.savefig(os.path.join('static', 'images', 'empty_number_line.png'))
    plt.close()
#=================================================================================

def create_filled_number_line(numbers, min_val=-10, max_val=10):
    fig, ax = plt.subplots(figsize=(10, 2))

    ax.set_xlim(min_val, max_val)
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_ticks([])
    ax.xaxis.set_ticks(np.arange(min_val, max_val+1, 1))
    
    for number in numbers:
        ax.plot(number, 0, marker='o', markersize=5, label=str(number))
    
    ax.legend(fontsize=8)
    plt.xticks(fontsize=8)
    plt.savefig(os.path.join('static', 'images', 'filled_number_line.png'))
    plt.close()
#=================================================================================

@prealgebra_2e.route('/locate_on_number_line')
def locate_on_number_line():
    numbers = random.sample(range(-10, 11), 4)
    create_empty_number_line(numbers)
    create_filled_number_line(numbers)
    
    problem = "Locate and label {} on a number line.".format(', '.join(map(str, numbers)))
    empty_number_line_url = url_for('static', filename='images/empty_number_line.png')
    problem += '<br><img src="{}" alt="Empty number line">'.format(empty_number_line_url)
    
    filled_number_line_url = url_for('static', filename='images/filled_number_line.png')
    explanation = 'Here is the number line with the numbers labeled:<br><img src="{}" alt="Filled number line">'.format(filled_number_line_url)
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=explanation, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/compare_numbers')
def compare_numbers():
    number_pairs = [tuple(random.sample(range(-10, 10), 2)) for _ in range(2)]

    problem = "In the following exercises, compare the numbers, using <, > or =.<br>"
    for pair in number_pairs:
        problem += f"{pair[0]} __ {pair[1]}<br>"

    answer = ""
    for pair in number_pairs:
        if pair[0] < pair[1]:
            answer += f"{pair[0]} < {pair[1]}<br>"
        elif pair[0] > pair[1]:
            answer += f"{pair[0]} > {pair[1]}<br>"
        else:
            answer += f"{pair[0]} = {pair[1]}<br>"

    explanation = "The greater than symbol '>' means that the number on the left is greater than the number on the right. <br>" \
                  "The less than symbol '<' means that the number on the left is less than the number on the right. <br>" \
                  "The equals symbol '=' means that both numbers are equal.<br>" \
                  "Here are the comparisons for the given pairs:<br>" + answer

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/find_opposite')
def find_opposite():
    numbers = [random.randint(-10, 10) for _ in range(2)]  # generate two random numbers
    
    problem = "Find the opposite of each number:<br>"
    for i, num in enumerate(numbers, start=1):
        problem += f"{chr(64 + i)}. {num}<br>"
        
    answer = [-num for num in numbers]
    answer = ', '.join(map(str, answer))

    explanation = "The opposite of a number is just the number with the opposite sign.<br>"
    for i, (num, ans) in enumerate(zip(numbers, answer), start=1):
        explanation += f"{chr(64 + i)}. The opposite of {num} is {ans}.<br>"
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================


x = symbols('x')

@prealgebra_2e.route('/simplify_expressions')
def simplify_expressions():
    # Randomly generate two numbers for the operations
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Randomly select an operation
    operation = random.choice(["add", "subtract", "multiply", "divide", "absolute", "power"])

    # Construct the problem and its answer based on the selected operation
    if operation == "add":
        problem = f"-{num1} + {num2}"
    elif operation == "subtract":
        problem = f"-{num1} - (-{num2})"
    elif operation == "multiply":
        problem = f"-{num1} * {num2}"
    elif operation == "divide":
        problem = f"{num1 * num2} / (-{num2})"
    elif operation == "absolute":
        problem = f"|{num1} - {num2}|"
        problem_sympy = f"Abs({num1} - {num2})"
    elif operation == "power":
        problem = f"(-{num1})^{num2}"
    else:
        problem = f"-{num1 * num2}"
    
    # Simplify the problem to get the answer
    if operation == "absolute":
        answer = str(simplify(problem_sympy))
    else:
        answer = str(simplify(problem))

    explanation = f"The simplified form of the expression {problem} is {answer}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import sympy as sp

@prealgebra_2e.route('/evaluate_expressions2')
def evaluate_expressions2():
    # Define the variables
    a, r, m, n, y = sp.symbols('a r m n y')

    # Randomly choose a problem type
    problem_type = random.choice(['a', 'r', 'm_n', 'y'])

    # Construct the problem and its answer based on the selected problem type
    if problem_type == 'a':
        a_value = random.randint(-10, 10)
        coefficient = random.randint(-50, 50)
        problem = f"$${coefficient} - a \\quad \\text{{when}} \\quad a = {a_value}$$"
        expression = coefficient - a
        answer = expression.subs(a, a_value)
    elif problem_type == 'r':
        r_value = random.randint(-10, 10)
        coefficient_r = random.randint(-10, 10)
        problem = f"$${coefficient_r}r^2 \\quad \\text{{when}} \\quad r = {r_value}$$"
        expression = (coefficient_r*r)**2
        answer = expression.subs(r, r_value)
    elif problem_type == 'm_n':
        m_value = random.randint(-10, 10)
        n_value = random.randint(-10, 10)
        coefficient_m = random.randint(-10, 10)
        coefficient_n = random.randint(-10, 10)
        problem = f"$${coefficient_m}m - {coefficient_n}n \\quad \\text{{when}} \\quad m = {m_value}, n = {n_value}$$"
        expression = coefficient_m*m - coefficient_n*n
        answer = expression.subs({m: m_value, n: n_value})
    elif problem_type == 'y':
        y_value = random.randint(-10, 10)
        problem = f"$$-|-y| \\quad \\text{{when}} \\quad y = {y_value}$$"
        expression = -sp.Abs(-y)
        answer = expression.subs(y, y_value)

    # Create an explanation
    explanation = f"Substitute the given values into the expression: $${sp.latex(expression)} = {answer}$$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import sympy as sp

@prealgebra_2e.route('/translate_and_simplify')
def translate_and_simplify():
    # Define the variables
    m, n = sp.symbols('m n')

    # Randomly choose a problem type
    problem_type = random.choice(['diff', 'quot'])

    # Construct the problem, its expression and its answer based on the selected problem type
    if problem_type == 'diff':
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        problem = f"Translate and simplify the phrase: 'the difference of {num1} and {num2}'."
        expression = sp.sympify(f"{num1} - {num2}")
        answer = expression.simplify()
    elif problem_type == 'quot':
        num = random.randint(10, 50)
        m_value = random.randint(-10, 10)
        n_value = random.randint(-10, 10)
        problem = f"Translate and simplify the phrase: 'the quotient of {num} and the sum of m and n', when m = {m_value} and n = {n_value}."
        expression = sp.sympify(f"{num} / ({m} + {n})")
        answer = expression.subs({m: m_value, n: n_value}).simplify()

    # Format the expression and answer for rendering in MathJax
    expression_latex = f"$${sp.latex(expression)}$$"
    answer_latex = f"$${sp.latex(answer)}$$"

    # The answer should now include the expression before it is simplified
    answer = f"The algebraic expression for the phrase is {expression_latex}. The simplified form (after substituting the given values, if any) is {answer_latex}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation='')
#=================================================================================

@prealgebra_2e.route('/solve_contextual_problems')
def solve_contextual_problems():
    problem_type = random.choice(["temperature", "credit_card"])
    if problem_type == "temperature":
        initial_temp = random.randint(-30, 30)
        change = random.randint(1, 20)
        final_temp = initial_temp + change
        problem = f"Early one morning, the temperature was {initial_temp}°F. By noon, it had risen {change}°. What was the temperature at noon?"
        answer = f"The temperature at noon was {final_temp}°F."
        explanation = f"The initial temperature was {initial_temp}°F. It rose by {change}°, so we add {initial_temp} + {change} to get the final temperature of {final_temp}°F."
    else:
        initial_balance = random.randint(100, 500)
        charge = random.randint(1, 200)
        final_balance = initial_balance + charge
        problem = f"Collette owed \\${initial_balance} on her credit card. Then she charged \\${charge}. What was her new balance?"
        answer = f"Her new balance was ${final_balance}."
        explanation = f"Collette's initial balance was ${initial_balance}. She charged an additional ${charge}, so we add ${initial_balance} + ${charge} to get the new balance of ${final_balance}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_linear_equations')
def solve_linear_equations():
    problem_type = random.choice(["addition", "subtraction", "multiplication"])
    variable = random.choice(['n', 'p', 'r'])
    constant = random.randint(-10, 10)
    result = random.randint(-10, 10)
    
    if problem_type == "addition":
        problem = f"{variable} + {constant} = {result}"
        answer = result - constant
    elif problem_type == "subtraction":
        problem = f"{variable} - {constant} = {result}"
        answer = result + constant
    else:
        problem = f"{constant}{variable} = {result}"
        answer = result / constant

    explanation = f"The solution to the equation {problem} is {variable} = {answer}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/translate_solve_integers')
def translate_solve_integers():
    problem_type = random.choice(["product", "less"])
    variable = random.choice(['x', 'y'])
    constant = random.randint(5, 20)
    result = random.randint(-50, 50)

    if problem_type == "product":
        problem = f"The product of {constant} and {variable} is {result}."
        answer = result / constant
        expression = f"{constant}{variable} = {result}"
    else:
        problem = f"Eight less than {variable} is {result}."
        answer = result + 8
        expression = f"{variable} = {answer} + 8"

    explanation = f"To solve the problem, translate the given word problem into an equation. <br>\
                    The equation for the problem '{problem}' is ${expression}$. <br>\
                    Solving for {variable}, we get {variable} = {answer}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================
#=================================================================================
#CHAPTER 3
#=================================================================================
#=================================================================================

from fractions import Fraction

from math import gcd

@prealgebra_2e.route('/fraction_conversion')
def fraction_conversion():
    problem_type = random.choice(["improper", "mixed"])
    if problem_type == "improper":
        numerator = random.randint(7, 20)
        denominator = random.randint(2, 6)
        whole_num = numerator // denominator
        remainder = numerator % denominator
        if remainder != 0:
            # Calculate the greatest common divisor of the remainder and the denominator
            divisor = gcd(remainder, denominator)
            # Simplify the fraction
            simplified_remainder = remainder // divisor
            simplified_denominator = denominator // divisor
            problem = f"Convert the improper fraction to a mixed number: $\\frac{{{numerator}}}{{{denominator}}}$"
            answer = f"${whole_num} \\frac{{{simplified_remainder}}}{{{simplified_denominator}}}$"
            explanation = f"The given fraction $\\frac{{{numerator}}}{{{denominator}}}$ can be converted to a mixed number by dividing the numerator by the denominator. The quotient {whole_num} is the whole number part and the remainder {remainder} is the numerator of the fractional part. The fraction is simplified by dividing the numerator and denominator by their greatest common divisor, {divisor}, giving the answer as {answer}."
        else:
            problem = f"Convert the improper fraction to a mixed number: $\\frac{{{numerator}}}{{{denominator}}}$"
            answer = f"${whole_num}$"
            explanation = f"The given fraction $\\frac{{{numerator}}}{{{denominator}}}$ can be converted to a mixed number by dividing the numerator by the denominator. The quotient {whole_num} is the whole number part. There is no fractional part as the division has no remainder, giving the answer as {answer}."

    else:
        whole_num = random.randint(1, 6)
        numerator = random.randint(1, 6)
        denominator = random.randint(numerator+1, 10)
        problem = f"Convert the mixed number to an improper fraction: {whole_num} $\\frac{{{numerator}}}{{{denominator}}}$"
        improper_numerator = (whole_num * denominator) + numerator
        answer = f"$\\frac{{{improper_numerator}}}{{{denominator}}}$"
        explanation = f"The given mixed number {whole_num} $\\frac{{{numerator}}}{{{denominator}}}$ can be converted to an improper fraction by multiplying the whole number part by the denominator and adding the numerator. The result {improper_numerator} is the numerator of the improper fraction, giving the answer as {answer}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/locate_fraction_numbers')
def locate_fraction_numbers():
    # Generate random fractions in decimal form
    numbers = [round(random.uniform(-3, 3), 2) for _ in range(4)]
    numbers.sort()
    create_empty_number_line(numbers)  # Assuming these functions have been defined as per previous discussions
    create_filled_number_line(numbers)

    # Convert the decimal numbers back to fractions for the problem statement
    fractions = [Fraction(num).limit_denominator() for num in numbers]
    fraction_strings = [f"${frac.numerator}/{frac.denominator}$" if frac.denominator != 1 else f"${frac.numerator}$" for frac in fractions]

    problem = f"Locate and label {', '.join(fraction_strings)} on a number line."
    empty_number_line_url = url_for('static', filename='images/empty_number_line.png')
    problem += '<br><img src="{}" alt="Empty number line">'.format(empty_number_line_url)
    
    filled_number_line_url = url_for('static', filename='images/filled_number_line.png')
    explanation = 'Here is the number line with the numbers labeled:<br><img src="{}" alt="Filled number line">'.format(filled_number_line_url)

    return render_template('problem_prealgebra_2e.html', problem=problem, answer='See explanation', explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/fraction_operations')
def fraction_operations():
    operation = random.choice(["simplify", "multiply", "divide", "add", "subtract"])
    is_mixed = random.choice([True, False])
    
    notice = f"Do about 10 of these each time Anki prompts you.<br>"
    
    if operation == "simplify":
        fraction = Fraction(random.randint(1, 50), random.randint(51, 100))
        problem = f"Simplify ${fraction.numerator}/{fraction.denominator}$"
        answer = fraction
        explanation = f"The fraction ${fraction.numerator}/{fraction.denominator}$ simplifies to ${answer.numerator}/{answer.denominator}$"
    else:
        fraction1 = Fraction(random.randint(1, 50), random.randint(51, 100))
        fraction2 = Fraction(random.randint(1, 50), random.randint(51, 100))
        if operation == "multiply":
            problem = f"Multiply ${fraction1.numerator}/{fraction1.denominator}$ by ${fraction2.numerator}/{fraction2.denominator}$"
            answer = fraction1 * fraction2
            explanation = f"${fraction1.numerator}/{fraction1.denominator} \times {fraction2.numerator}/{fraction2.denominator} = {answer.numerator}/{answer.denominator}$"
        elif operation == "divide":
            problem = f"Divide ${fraction1.numerator}/{fraction1.denominator}$ by ${fraction2.numerator}/{fraction2.denominator}$"
            answer = fraction1 / fraction2
            explanation = f"${fraction1.numerator}/{fraction1.denominator} \div {fraction2.numerator}/{fraction2.denominator} = {answer.numerator}/{answer.denominator}$"
        elif operation == "add":
            problem = f"Add ${fraction1.numerator}/{fraction1.denominator}$ to ${fraction2.numerator}/{fraction2.denominator}$"
            answer = fraction1 + fraction2
            explanation = f"${fraction1.numerator}/{fraction1.denominator} + {fraction2.numerator}/{fraction2.denominator} = {answer.numerator}/{answer.denominator}$"
        else:  # subtract
            problem = f"Subtract ${fraction2.numerator}/{fraction2.denominator}$ from ${fraction1.numerator}/{fraction1.denominator}$"
            answer = fraction1 - fraction2
            explanation = f"${fraction1.numerator}/{fraction1.denominator} - {fraction2.numerator}/{fraction2.denominator} = {answer.numerator}/{answer.denominator}$"

    return render_template('problem_prealgebra_2e.html', notice=notice, problem=problem, answer=f"${answer.numerator}/{answer.denominator}$", explanation=explanation)
#=================================================================================

from sympy import symbols, simplify, Eq, solve

@prealgebra_2e.route('/evaluate_random_fraction_expression')
def evaluate_random_fraction_expression():
    # Randomly choose the variable name
    variable_name = random.choice(['x', 'y', 'z', 'a', 'b', 'c'])
    variable = symbols(variable_name)

    # Randomly generate a fraction
    random_fraction = Fraction(random.randint(1, 9), random.randint(10, 99))
    expression = variable + random_fraction

    # Generate a couple of random fractions for the variable values
    values_for_variable = [Fraction(random.randint(1, 9), random.randint(10, 99)) for _ in range(2)]
    chosen_value_for_variable = random.choice(values_for_variable)

    # Evaluate the expression
    evaluation = simplify(expression.subs(variable, chosen_value_for_variable))

    # Create the equation and solve it
    equation = Eq(expression, evaluation)
    solution = solve(equation, variable)

    # Format the problem, answer, and explanation
    problem = "Evaluate the expression \( {} + \\frac{{{}}}{{{}}} \) when \( {} = \\frac{{{}}}{{{}}} \)".format(variable_name, random_fraction.numerator, random_fraction.denominator, variable_name, chosen_value_for_variable.numerator, chosen_value_for_variable.denominator)
    answer = "The solution to the equation \( {} + \\frac{{{}}}{{{}}} = {} \) when \( {} = \\frac{{{}}}{{{}}} \) is \( {} \)".format(variable_name, random_fraction.numerator, random_fraction.denominator, evaluation, variable_name, chosen_value_for_variable.numerator, chosen_value_for_variable.denominator, solution[0])
    explanation = "Substitute \( {} = \\frac{{{}}}{{{}}} \) into the expression to get the evaluated expression, and then solve the resulting equation to find the solution.".format(variable_name, chosen_value_for_variable.numerator, chosen_value_for_variable.denominator)

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from sympy import symbols, Eq, solve

@prealgebra_2e.route('/solve_fraction_equation')
def solve_fraction_equation():
    # Randomly choose the variable name
    variable_name = random.choice(['y', 'a', 'f', 'm', 'c', 'p'])
    variable = symbols(variable_name)

    # Randomly generate two fractions for the coefficients and the right side of the equation
    coeff_fraction = Fraction(random.randint(-9, 9), random.choice([i for i in range(1, 10) if i != 0]))
    rhs_fraction = Fraction(random.randint(-9, 9), random.choice([i for i in range(1, 10) if i != 0]))

    # Randomly choose an operation (addition, subtraction, multiplication, or division)
    operation = random.choice(['+', '-', '*', '/'])

    # Create the equation
    if operation == '+':
        equation = Eq(variable + coeff_fraction, rhs_fraction)
    elif operation == '-':
        equation = Eq(variable - coeff_fraction, rhs_fraction)
    elif operation == '*':
        equation = Eq(variable * coeff_fraction, rhs_fraction)
    else:
        # For division, make sure we are not dividing by zero
        if coeff_fraction != 0:
            equation = Eq(variable / coeff_fraction, rhs_fraction)
        else:
            equation = Eq(variable, rhs_fraction)

    # Solve the equation
    solution = solve(equation, variable)

    # Create the problem, answer, and explanation
    notice = f"Do about 10 of these each time Anki prompts you.<br>"
    problem = "Solve the equation \( {} {} \\frac{{{}}}{{{}}} = \\frac{{{}}}{{{}}} \)".format(variable_name, operation, abs(coeff_fraction.numerator), coeff_fraction.denominator, rhs_fraction.numerator, rhs_fraction.denominator)
    answer = "The solution to the equation is \( {} = {} \)".format(variable_name, solution[0])
    explanation = "To solve the equation, use the inverse operation of {} with \\(\\frac{{{}}}{{{}}}\\) on both sides.".format(operation, abs(coeff_fraction.numerator), coeff_fraction.denominator)

#    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

    return render_template('problem_prealgebra_2e.html', notice=notice, problem=problem, answer=answer, explanation=explanation)
#=================================================================================
#=================================================================================
#CHAPTER 5
#=================================================================================
#=================================================================================

import random
from fractions import Fraction

@prealgebra_2e.route('/convert_whole_and_thousandths_to_decimal')
def convert_whole_and_thousandths_to_decimal():
    whole_num = random.randint(1, 9)
    thousandths = random.randint(1, 999)
    problem = f"Write {whole_num} and {str(thousandths).zfill(3)} thousandths as a decimal."
    answer = f"{whole_num}.{str(thousandths).zfill(3)}"
    explanation = f"{whole_num} and {str(thousandths).zfill(3)} thousandths is written as a decimal like this: {answer}"
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from fractions import Fraction

@prealgebra_2e.route('/convert_decimal_to_fraction')
def convert_decimal_to_fraction():
    numerator = random.randint(1, 9)
    denominator = random.choice([10, 100, 1000])  # Ensure we get a decimal number after division
    decimal = numerator / denominator

    # Create a Fraction object to simplify the fraction
    fraction = Fraction(numerator, denominator)

    problem = f"Write {decimal} as a fraction."
    answer = f"$\\frac{{{fraction.numerator}}}{{{fraction.denominator}}}$"
    explanation = f"{decimal} is equivalent to $\\frac{{{fraction.numerator}}}{{{fraction.denominator}}}$"
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/convert_fraction_to_decimal')
def convert_fraction_to_decimal():
    numerator = random.randint(1, 9)
    denominator = random.randint(1, 9)
    problem = f"Write $\\frac{{{numerator}}}{{{denominator}}}$ as a decimal."
    answer = round(numerator / denominator, 2)
    explanation = f"$\\frac{{{numerator}}}{{{denominator}}} = {answer}$"
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/round_decimal')
def round_decimal():
    decimal = round(random.uniform(10, 20), 3)
    problem = f"Round {decimal} to the nearest ⓐ tenth ⓑ hundredth ⓒ whole number"
    tenth = round(decimal, 1)
    hundredth = round(decimal, 2)
    whole_num = round(decimal)
    answer = f"ⓐ {tenth} ⓑ {hundredth} ⓒ {whole_num}"
    explanation = f"{decimal} rounded to the nearest tenth is {tenth}, to the nearest hundredth is {hundredth}, and to the nearest whole number is {whole_num}."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/sort_mixed_numbers')
def sort_mixed_numbers():
    # Generate random numbers and fractions
    numbers = [round(random.uniform(-10, 10), 3) for _ in range(4)]
    fractions = [Fraction(random.randint(-10, 10), random.randint(1, 10)) for _ in range(2)]
    mixed_numbers = numbers + [float(frac) for frac in fractions]

    # Sort the mixed numbers
    sorted_numbers = sorted(mixed_numbers, key=float)

    # Format the numbers for display
    problem_numbers = ', '.join([str(num) if isinstance(num, float) else r'\(\frac{{{}}}{{{}}}\)'.format(num.numerator, num.denominator) for num in mixed_numbers])
    sorted_numbers_str = ', '.join([str(num) if isinstance(num, float) else r'\(\frac{{{}}}{{{}}}\)'.format(num.numerator, num.denominator) for num in sorted_numbers])

    problem = f"Write the numbers {problem_numbers} in order from smallest to largest."
    answer = sorted_numbers_str
    explanation = "The numbers are sorted by comparing their decimal values."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import operator
from sympy import *

@prealgebra_2e.route('/simplify_decimal_expressions')
def simplify_decimal_expressions():
    operators = [
        ("+", operator.add),
        ("-", operator.sub),
        ("*", operator.mul),
        ("/", operator.truediv),
        ("^2", operator.pow)
    ]
    op_symbol, op_func = random.choice(operators)
    if op_symbol == "^2":
        num1 = round(random.uniform(0.1, 1), 2)
        num2 = 2
    else:
        num1 = round(random.uniform(1, 100), 2)
        num2 = round(random.uniform(0.1, 100), 2)
    
    # ensure no division by zero
    if op_symbol == "/" and num2 == 0:
        num2 = round(random.uniform(0.1, 100), 2)
        
    notice = f"Do about 10 of these each time Anki prompts you.<br>"
    problem = f"Simplify the expression: $ {num1} {op_symbol} {num2} $"
    answer = round(op_func(num1, num2), 2)
    explanation = f"The expression $ {num1} {op_symbol} {num2} $ equals {answer} when simplified."
    
    #return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
    return render_template('problem_prealgebra_2e.html', notice=notice, problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from sympy import *

@prealgebra_2e.route('/decimal_addition')
def decimal_addition():
    num1 = round(random.uniform(1, 100), 2)
    num2 = round(random.uniform(1, 100), 2)
    
    problem = f"Simplify the expression: $ {num1} + {num2} $"
    answer = round(N(num1 + num2), 2)
    explanation = f"The expression $ {num1} + {num2} $ equals {answer} when simplified."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/decimal_subtraction')
def decimal_subtraction():
    num1 = round(random.uniform(20, 100), 2)
    num2 = round(random.uniform(1, 20), 2)
    
    problem = f"Simplify the expression: $ {num1} - {num2} $"
    answer = round(N(num1 - num2), 2)
    explanation = f"The expression $ {num1} - {num2} $ equals {answer} when simplified."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/decimal_multiplication')
def decimal_multiplication():
    num1 = round(random.uniform(0, 10), 2)
    num2 = round(random.uniform(0, 10), 2)
    
    problem = f"Simplify the expression: $ {num1} \\times {num2} $"
    answer = round(N(num1 * num2), 2)
    
    explanation = f"The expression $ {num1} \\times {num2} $ equals {answer} when simplified."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/decimal_division')
def decimal_division():
    num1 = round(random.uniform(1, 10), 2)
    num2 = round(random.uniform(1, 10), 2)

    problem = f"Simplify the expression: $ \\frac{{{num1}}}{{{num2}}} $"
    answer = round(N(num1 / num2), 2)
    explanation = f"The expression $ \\frac{{{num1}}}{{{num2}}} $ equals {answer} when simplified."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/decimal_power')
def decimal_power():
    num = round(random.uniform(0, 1), 2)
    power = random.randint(1, 3)

    problem = f"Simplify the expression: $ {num}^{power} $"
    answer = round(N(num ** power), 2)
    explanation = f"The expression $ {num}^{power} $ equals {answer} when simplified."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/decimal_parentheses_add_subtract_multiply')
def decimal_parentheses_add_subtract_multiply():
    num1 = round(random.uniform(1, 10), 2)
    num2 = round(random.uniform(1, 10), 2)
    num3 = round(random.uniform(1, 10), 2)

    problem = f"Simplify the expression: $ {num3}( {num1} - {num2} ) $"
    answer = round(N(num3 * (num1 - num2)), 2)
    explanation = f"The expression $ {num3}( {num1} - {num2} ) $ equals {answer} when simplified."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/decimal_parentheses_add_subtract_divide')
def decimal_parentheses_add_subtract_divide():
    num1 = round(random.uniform(1, 10), 2)
    num2 = round(random.uniform(1, 10), 2)
    num3 = round(random.uniform(1, 10), 2)

    problem = f"Simplify the expression: $ \\frac{{{num3}}}{{ {num1} + {num2} }} $"
    answer = round(N(num3 / (num1 + num2)), 2)
    explanation = f"The expression $ \\frac{{{num3}}}{{ {num1} + {num2} }} $ equals {answer} when simplified."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_simple_equation_add')
def solve_simple_equation_add():
    num = round(random.uniform(1, 10), 2)
    result = round(random.uniform(1, 10), 2)
    problem = f"Solve for $m$: $m + {num} = {result}$"
    answer = round(result - num, 2)
    explanation = f"To isolate $m$, we subtract {num} from both sides of the equation, giving us $m = {answer}$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_simple_equation_divide')
def solve_simple_equation_divide():
    result = round(random.uniform(1, 10), 2)
    divisor = round(random.uniform(1, 10), 2)
    problem = f"Solve for $h$: $\\frac{{h}}{{{divisor}}} = {result}$"
    answer = round(result * divisor, 2)
    explanation = f"To isolate $h$, we multiply both sides of the equation by {divisor}, giving us $h = {answer}$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_simple_equation_multiply')
def solve_simple_equation_multiply():
    multiplier = round(random.uniform(1, 10), 2)
    result = round(random.uniform(1, 100), 2)
    problem = f"Solve for $y$: $-{multiplier}y = -{result}$"
    answer = round(result / multiplier, 2)
    explanation = f"To isolate $y$, we divide both sides of the equation by -$({multiplier}), giving us $y = {answer}$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_simple_equation_subtract')
def solve_simple_equation_subtract():
    subtractor = round(random.uniform(1, 10), 2)
    result = round(random.uniform(1, 10), 2)
    problem = f"Solve for $a$: $-{subtractor} = a - {result}$"
    answer = round(result + subtractor, 2)
    explanation = f"To isolate $a$, we add {subtractor} to both sides of the equation, giving us $a = {answer}$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/split_bill')
def split_bill():
    total_bill = round(random.uniform(50, 150), 2)
    num_friends = random.randint(2, 5)
    problem = f" {num_friends} friends went out to dinner and agreed to split the bill evenly. The bill was ${total_bill}. How much should each person pay?"
    answer = round(total_bill / num_friends, 2)
    explanation = f"Each person should pay ${answer} because ${total_bill} divided by {num_friends} equals {answer}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/find_circle_circumference_area')
def find_circle_circumference_area():
    radius = random.randint(5, 20)
    problem = f"A circle has radius {radius}. Find the ⓐ circumference and ⓑ area. [Use 3.14 for π.]"
    circumference = round(2 * 3.14 * radius, 2)
    area = round(3.14 * radius ** 2, 2)
    answer = f"ⓐ {circumference} ⓑ {area}"
    explanation = f"The formula for the circumference of a circle is $2πr$ and for the area is $πr^2$. So, the circumference is {circumference} and the area is {area}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/calculate_mean_median_mode')
def calculate_mean_median_mode():
    num_children = random.randint(5, 11)
    ages = [random.randint(48, 60) for _ in range(num_children)]
    ages.sort()
    problem = f"The ages, in months, of {num_children} children in a preschool class are: {ages}. Find the ⓐ mean ⓑ median ⓒ mode"
    mean = round(sum(ages) / len(ages), 2)
    median = ages[len(ages)//2] if len(ages) % 2 == 1 else round((ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2, 2)
    mode = max(set(ages), key = ages.count)
    answer = f"ⓐ {mean} ⓑ {median} ⓒ {mode}"
    explanation = f"The mean is the sum of all ages divided by the number of ages.<br> The median is the middle value when the ages are arranged in ascending order.<br> The mode is the age that occurs most frequently.<br>"

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/nurse_probability')
def nurse_probability():
    total_nurses = random.randint(12, 20)
    female_nurses = random.randint(8, total_nurses - 2)
    male_nurses = total_nurses - female_nurses
    problem = f"Of the {total_nurses} nurses in Doreen’s department, {female_nurses} are women and {male_nurses} are men. One of the nurses will be assigned at random to work an extra shift next week.<br><br> ⓐ Find the probability a woman nurse will be assigned the extra shift.<br> ⓑ Convert the fraction to a decimal."
    probability_fraction = Fraction(female_nurses, total_nurses)
    probability_decimal = round(female_nurses / total_nurses, 2)
    answer = f"ⓐ The probability that a woman nurse will be assigned the extra shift is $\\frac{{ {female_nurses} }}{{ {total_nurses} }}$.<br> ⓑ The decimal equivalent of this probability is {probability_decimal}."
    explanation = f"To find the probability, divide the number of favourable outcomes (number of female nurses) by the total number of outcomes (total number of nurses). To convert the fraction to a decimal, divide the numerator by the denominator."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/better_buy')
def better_buy():
    ounces1 = random.randint(50, 70)
    price1 = round(random.uniform(8, 12), 2)
    ounces2 = random.randint(40, 60)
    price2 = round(random.uniform(6, 10), 2)
    unit_price1 = round(price1 / ounces1, 2)
    unit_price2 = round(price2 / ounces2, 2)
    better_buy = "Option 1" if unit_price1 < unit_price2 else "Option 2"
    
    problem = f"Find each unit price and then the better buy.<br>Laundry detergent: {ounces1} ounces for \${price1} or {ounces2} ounces for \${price2}"
    answer = f"Option 1: \${unit_price1} per ounce, Option 2: \${unit_price2} per ounce. The better buy is {better_buy}."
    explanation = f"The unit price for Option 1 is calculated as $\\frac{{\\text{{Price}}}}{{\\text{{Ounces}}}}$ = $\\frac{{\${price1}}}{{ {ounces1}\\,\\text{{oz}} }} = \${unit_price1}/\\text{{oz}}$, " + \
                  f"and for Option 2 it is $\\frac{{\\text{{Price}}}}{{\\text{{Ounces}}}}$ = $\\frac{{\${price2}}}{{ {ounces2}\\,\\text{{oz}} }} = \${unit_price2}/\\text{{oz}}$. " + \
                  f"Therefore, the better buy is {better_buy}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/travel_time')
def travel_time():
    distance = random.randint(100, 200)
    speed = random.randint(40, 80)
    problem = f"The distance between two cities is {distance} miles. If a car travels at an average speed of {speed} miles per hour, how long will it take to travel from one city to the other?"
    time = round(distance / speed, 2)
    answer = f"It will take {time} hours."
    explanation = f"Time is calculated by dividing distance by speed. So, $\\frac{{ {distance}\\,\\text{{miles}} }}{{ {speed}\\,\\text{{mph}} }} = {time}$ hours."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import math

@prealgebra_2e.route('/sqrt_sum')
def sqrt_sum():
    number1 = random.randint(30, 50)
    number2 = random.randint(50, 70)
    answer = round(math.sqrt(number1) + number2, 2)
    problem = f"Find the value of $\\sqrt{{{number1}}} + {number2}$"
    explanation = f"$\\sqrt{{{number1}}} = {math.sqrt(number1)}$ and $\\sqrt{{{number1}}} + {number2} = {answer}$"
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/sqrt_n_square')
def sqrt_n_square():
    l = random.randint(1, 15)
    n = random.randint(1, 10)
    
    answer = l * n
    problem = f"Simplify: $\\sqrt{{{l}n^2}}$, where n = {n}"
    explanation = f"Since $\\sqrt{{{l}n^2}} = {{{l}}}n$, substituting n = {n} gives us 12 * {n} = {answer}."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================


@prealgebra_2e.route('/estimate_sqrt')
def estimate_sqrt():
    number = random.randint(50, 60)
    lower_bound = math.floor(math.sqrt(number))
    upper_bound = math.ceil(math.sqrt(number))
    problem = f"Estimate $\\sqrt{{{number}}}$ to between two whole numbers."
    answer = f"{lower_bound} and {upper_bound}"
    explanation = f"The square root of {number} is between {lower_bound} and {upper_bound}."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/square_patio')
def square_patio():
    square_feet = random.randint(200, 300)
    side_length = math.sqrt(square_feet)
    problem = f"Yanet wants a square patio in her backyard. She has {square_feet} square feet of tile. How long can a side of the patio be?"
    answer = f"{round(side_length, 2)}"
    explanation = f"A square's area is found by squaring one of its sides. So to find the length of a side when the area is known, we take the square root of the area. Therefore, the side length is $\\sqrt{{{square_feet}}} = {round(side_length, 2)}$"
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================
#=================================================================================
#CHAPTER 6
#=================================================================================
#=================================================================================

@prealgebra_2e.route('/percent_to_decimal_fraction')
def percent_to_decimal_fraction():
    percent = random.randint(1, 400)
    decimal = round(percent / 100, 2)
    fraction = Fraction(percent, 100)
    
    problem = f"Convert {percent}% to: ⓐ a decimal ⓑ a simplified fraction."
    answer = f"ⓐ Decimal: {decimal}, ⓑ Simplified Fraction: {str(fraction)}."
    explanation = f"ⓐ To convert a percent to a decimal, divide the percent by 100.<br> So, {percent}% as a decimal is {decimal}. <br><br>" + \
                  f"ⓑ To convert a percent to a simplified fraction, write the percent over 100 and simplify.<br> So, {percent}% as a simplified fraction is {str(fraction)}."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/fraction_to_percent')
def fraction_to_percent():
    numerator = random.randint(1, 12)
    denominator = random.randint(numerator + 1, 13)  # denominator is larger than numerator to avoid improper fractions
    fraction = Fraction(numerator, denominator)
    percent = round((numerator / denominator) * 100, 3)

    problem = f"Convert $\\frac{{{numerator}}}{{{denominator}}}$ to a percent. (Round to 3 decimal places if needed.)"
    answer = f"{percent}%"
    explanation = f"To convert a fraction to a percent, divide the numerator by the denominator and multiply by 100. " + \
                  f"So, $\\frac{{{numerator}}}{{{denominator}}}$ as a percent (rounded to three decimal places if needed) is {percent}%."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/percent_problem_2')
def percent_problem_2():
    problem_choice = random.choice(range(7))

    if problem_choice == 0:
        total = random.randint(200, 300)
        portion = random.randint(50, 150)
        percent = round((portion / total) * 100, 2)
        notice = f"Do about 10 of these each time Anki prompts you.<br>"
        problem = f"{portion} is what percent of {total}?"
        answer = f"{percent}%"
        explanation = f"To find the percentage, divide the portion by the total and multiply by 100. So, \\({portion} ÷ {total} × 100 = {percent}%\\)."

    elif problem_choice == 1:
        percent = random.randint(20, 30)
        total = random.randint(2000, 3000)
        number = round((percent / 100) * total, 2)
        notice = f"Do about 10 of these each time Anki prompts you.<br>"
        problem = f"What number is {percent}% of {total}?"
        answer = f"{number}"
        explanation = f"To find the number, multiply the total by the percentage (divided by 100). So, \\({total} × ({percent} ÷ 100) = {number}\\)."

    elif problem_choice == 2:
        percent = random.randint(130, 200)
        number = random.randint(40, 70)
        total = round((number / (percent / 100)), 2)
        notice = f"Do about 10 of these each time Anki prompts you.<br>"
        problem = f"{percent}% of what number is {number}?"
        answer = f"{total}"
        explanation = f"To find the total, divide the number by the percentage (divided by 100). So, \\({number} ÷ ({percent} ÷ 100) = {total}\\)."

    elif problem_choice == 3:
        total_paycheck = random.randint(3500, 4000)
        rent = random.randint(800, 1000)
        percent_rent = round((rent / total_paycheck) * 100, 2)
        notice = f"Do about 10 of these each time Anki prompts you.<br>"
        problem = f"Yuki’s monthly paycheck is \${total_paycheck}. She pays \${rent} for rent. What percent of her paycheck goes to rent?"
        answer = f"{percent_rent}%"
        explanation = f"The percentage of the paycheck that goes to rent can be found by dividing the rent by the total paycheck and multiplying by 100. So, \\(${rent} ÷ ${total_paycheck} × 100 = {percent_rent}%\\)."

    elif problem_choice == 4:
        initial_vehicles = random.randint(80000, 90000)
        final_vehicles = random.randint(70000, 79000)
        percent_decrease = round(((initial_vehicles - final_vehicles) / initial_vehicles) * 100, 2)
        notice = f"Do about 10 of these each time Anki prompts you.<br>"
        problem = f"The total number of vehicles on one freeway dropped from {initial_vehicles} to {final_vehicles}. Find the percent decrease (round to the nearest tenth of a percent)."
        answer = f"{percent_decrease}%"
        explanation = f"The percentage decrease can be found by subtracting the final number of vehicles from the initial number, dividing by the initial number, and multiplying by 100. So, \\((${initial_vehicles} - ${final_vehicles}) ÷ ${initial_vehicles} × 100 = {percent_decrease}%\\)."

    elif problem_choice == 5:
        purchase_price = random.randint(500, 700)
        sales_tax_percent = round(random.uniform(6, 9), 2)
        total_cost = round(purchase_price + (purchase_price * (sales_tax_percent / 100)), 2)
        
        notice = f"Do about 10 of these each time Anki prompts you.<br>"
        problem = f"Kyle bought a bicycle in Denver where the sales tax was {sales_tax_percent}% of the purchase price. The purchase price of the bicycle was ${purchase_price}. What was the total cost?"
        answer = f"${total_cost}"
        explanation = f"The total cost can be found by adding the purchase price and the sales tax (which is the purchase price multiplied by the sales tax percent divided by 100). So, \\(${purchase_price} + ${purchase_price} × ({sales_tax_percent} ÷ 100) = ${total_cost}\\)."

    elif problem_choice == 6:
        sale_price = random.randint(750, 900)
        commission = round(random.uniform(25, 50), 2)
        commission_rate = round((commission / sale_price) * 100, 2)
        
        notice = f"Do about 10 of these each time Anki prompts you.<br>"
        problem = f"Mara received \${commission} commission when she sold a \${sale_price} suit. What was her rate of commission?"
        answer = f"{commission_rate}%"
        explanation = f"The rate of commission can be found by dividing the commission by the sale price and multiplying by 100. So, \\(${commission} ÷ ${sale_price} × 100 = {commission_rate}%\\)."

    return render_template('problem_prealgebra_2e.html', notice=notice, problem=problem, answer=answer, explanation=explanation)

#=================================================================================
#=================================================================================
#CHAPTER 7 real_numbers_properties
#=================================================================================
#=================================================================================

@prealgebra_2e.route('/simplify_mult_div')
def simplify_mult_div():
    a = round(random.uniform(1, 10), 2)
    b = round(random.uniform(1, 10), 2)
    c = round(random.uniform(1, 10), 2)
    problem = f"Simplify the expression: {a}({-b})({c})"
    answer = round(a * -b * c, 2)
    explanation = f"The expression simplifies as follows: {a}({-b})({c}) = {answer}."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@prealgebra_2e.route('/simplify_add_sub')
def simplify_add_sub():
    a = -random.randint(1, 10)
    b = random.randint(1, 20)
    c = random.randint(1, 10)
    problem = f"Simplify the given expression: {a} + {b}y + {c}"
    answer = f"{b}y + {a+c}"
    explanation = "Combine the constants (numbers without variables). The y-term remains as it is."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/simplify_distribution')
def simplify_distribution():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    problem = f"Simplify the given expression: {a}({b}x-{c})"
    answer = f"{a*b}x - {a*c}"
    explanation = "Apply the distributive property, a(bx-c) = abx - ac."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/simplify_complex_expression')
def simplify_complex_expression():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    problem = f"Simplify the given expression: {a}p + ({-b}z) + {c}p + {d}z"
    answer = f"{a+c}p + {d-b}z"
    explanation = "Combine like terms, which are terms with the same variable. The p-terms are combined, and the z-terms are combined."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from flask import Flask, render_template
import random

app = Flask(__name__)

@prealgebra_2e.route('/unit_conversion')
def unit_conversion():
    problems = [
        {
            "problem": "Azize walked {0} miles. Convert this distance to feet. (1 mile=5,280 feet).",
            "answer": "{0} miles is equivalent to {1} feet.",
            "unit": 5280,
            "min_range": 1,
            "max_range": 1000,
            "unit_name": "miles"
        },
        {
            "problem": "One cup of milk contains {0} milligrams of calcium. Convert this to grams. (1 milligram=0.001 gram)",
            "answer": "{0} milligrams is equivalent to {1} grams.",
            "unit": 0.001,
            "min_range": 50,
            "max_range": 500,
            "unit_name": "milligrams"
        },
        {
            "problem": "Janice ran {0} kilometers. Convert this distance to miles. Round to the nearest hundredth of a mile. (1 mile=1.61 kilometers)",
            "answer": "{0} kilometers is equivalent to {1} miles.",
            "unit": 1/1.61,
            "min_range": 1,
            "max_range": 100,
            "unit_name": "kilometers"
        },
        {
            "problem": "Yolie is {0} inches tall. Convert her height to centimeters. Round to the nearest centimeter. (1 inch=2.54 centimeters)",
            "answer": "{0} inches is equivalent to {1} centimeters.",
            "unit": 2.54,
            "min_range": 50,
            "max_range": 80,
            "unit_name": "inches"
        },
    ]
    chosen_problem = random.choice(problems)
    random_value = random.randint(chosen_problem['min_range'], chosen_problem['max_range'])
    problem = chosen_problem['problem'].format(random_value)
    answer = chosen_problem['answer'].format(random_value, round(random_value*chosen_problem['unit'], 2))
    explanation = f"The conversion factor is 1 {chosen_problem['unit_name']} = {chosen_problem['unit']} units. Therefore, {random_value} {chosen_problem['unit_name']} = {random_value} * {chosen_problem['unit']} = {round(random_value*chosen_problem['unit'], 2)} units."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

#=================================================================================
#=================================================================================
#CHAPTER 8 Solving Linear Equations
#=================================================================================
#=================================================================================

import random

@prealgebra_2e.route('/check_solution_linear')
def check_solution_linear():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(2, 30)
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    problem = f"Determine whether each number is a solution to the equation ${a}x + {b} = {c}$.<br/>\
                ⓐ {x1}<br/>\
                ⓑ {x2}"
    is_x1_solution = "is" if a * x1 + b == c else "is not"
    is_x2_solution = "is" if a * x2 + b == c else "is not"
    answer = f"$x = {x1}$ {is_x1_solution} a solution;<br> $x = {x2}$ {is_x2_solution} a solution."
    explanation = f"For $x = {x1}$, the left-hand side of the equation is ${a} * {x1} + {b} = {a * x1 + b}$.<br> For $x = {x2}$, the left-hand side of the equation is ${a} * {x2} + {b} = {a * x2 + b}$.<br> Therefore, the answer is that $x = {x1}$ {is_x1_solution} a solution, and $x = {x2}$ {is_x2_solution} a solution."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from sympy import symbols, Eq, solve

@prealgebra_2e.route('/solve_linear_equation')
def solve_linear_equation():
    x = symbols('x')
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(2, 30)
    d = random.randint(1, 10)

    equation_type = random.choice(['single', 'bracket', 'decimal'])

    if equation_type == 'single':
        equation = Eq(a*x + b, c)
    elif equation_type == 'bracket':
        equation = Eq(a*(x+b), c)
    else: # decimal
        equation = Eq(a*x + b/10, c)

    problem = f"Solve the equation: ${sympy.latex(equation)}$"
    solution = solve(equation)[0]

    answer = f"x = {round(solution, 2)}"
    explanation = f"To solve for x, we set the equation equal to zero and solve: <br/>\
                    ${sympy.latex(equation)} = 0$<br/>\
                    The solution is ${answer}$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/difference_equation')
def difference_equation():
    x = symbols('x')

    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(2, 30)

    equation = Eq(2*a*x - b, c)
    
    problem = f"Translate and solve: The difference of twice {a}x and {b} is {c}."
    solution = solve(equation)[0]

    answer = f"x = {round(solution, 2)}"
    explanation = f"Translating the problem into an equation gives: ${sympy.latex(equation)}$ <br/>\
                    Solving the equation gives: ${answer}$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/gas_payment')
def gas_payment():
    this_week_payment = round(random.uniform(20, 30), 2)
    difference = round(random.uniform(1, 5), 2)

    last_week_payment = this_week_payment + difference

    problem = f"Samuel paid \${this_week_payment} for gas this week, which was \${difference} less than he paid last week. \
                How much did he pay last week?"

    answer = f"Samuel paid ${round(last_week_payment, 2)} last week."
    explanation = f"Since this week's payment was ${difference} less than last week's, we add this week's payment and the difference \
                    to find out how much was paid last week: ${this_week_payment} + ${difference} = ${answer}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

#=================================================================================
#=================================================================================
#CHAPTER 9 Math Models and Geometry
#=================================================================================
#=================================================================================

import math

@prealgebra_2e.route('/hike_people')
def hike_people():
    # Problem parameters
    numerator = random.randint(1, 4)  # Random numerator for the fraction
    denominator = random.randint(numerator + 1, 5)  # Random denominator for the fraction (greater than numerator)

    total_people = random.randint(10, 50)  # Random total number of people
    children = math.ceil(total_people * (numerator / denominator))  # Compute the number of children, rounding up

    problem = f"{numerator}/{denominator} of the people on a hike are children. If there are {children} children, what is the total number of people on the hike?"
    answer = f"{total_people}"
    explanation = f"Since {numerator}/{denominator} of the people are children, and we know there are {children} children, we can find the total number of people by using the equation: children = total_people * {numerator}/{denominator}. Solving for total_people, we find there are {total_people} people on the hike."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================


@prealgebra_2e.route('/sum_twice_number')
def sum_twice_number():
    random_number = random.randint(-25, -1)

    # The sum of random_number and twice a number is -19
    x = (-19 - random_number) / 2

    problem = f"The sum of {random_number} and twice a number is −19. Find the number."
    answer = f"{x}"
    explanation = f"The sum of {random_number} and twice a number equals -19. To find the unknown number, we subtract {random_number} from -19 and then divide the result by 2."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@prealgebra_2e.route('/two_number_sum')
def two_number_sum():
    number1 = random.randint(30, 50)
    sum_of_two_numbers = random.randint(70, 90)

    # One number is number1 less than another number. Their sum is sum_of_two_numbers
    number2 = (sum_of_two_numbers + number1) / 2

    problem = f"One number is {number1} less than another number. Their sum is {sum_of_two_numbers}. Find the numbers."
    answer = f"{number2 - number1}, {number2}"
    explanation = f"The two numbers are {number2 - number1} and {number2}."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@prealgebra_2e.route('/dimes_and_quarters')
def dimes_and_quarters():
    quarter, dime = symbols('quarter dime')

    # Random number of quarters
    num_quarters = random.randint(1, 20)
    # Ensure extra dimes is less than or equal to number of quarters
    extra_dimes = random.randint(0, num_quarters)

    num_dimes = num_quarters + extra_dimes
    total_money = round(0.25 * num_quarters + 0.10 * num_dimes, 2)

    problem = f"Bonita has ${total_money} in dimes and quarters in her pocket. If she has {extra_dimes} more dimes than quarters, how many of each coin does she have?"
    answer = f"She has {num_quarters} quarters and {num_dimes} dimes."
    explanation = f"We are given two pieces of information:<br> \n \
    1. The total amount of money Bonita has, which is \${total_money}. This is made up of the value of the quarters (25 cents each) and the dimes (10 cents each). So we have the equation \({0.25} \\times \\text{{quarters}} + {0.10} \\times \\text{{dimes}} = ${total_money}\).<br><br> \n \
    2. Bonita has {extra_dimes} more dimes than quarters, which gives us the equation \(\\text{{dimes}} = \\text{{quarters}} + {extra_dimes}\). \n \
    Using these two equations, we find that Bonita has {num_quarters} quarters and {num_dimes} dimes."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from random import randint

@prealgebra_2e.route('/tickets_sold')
def tickets_sold():
    adult_price = randint(5, 20)
    child_price = randint(1, 10)
    adult_tickets_less = randint(10, 50)
    
    child_tickets_sold = randint(50, 150)
    adult_tickets_sold = 2 * child_tickets_sold - adult_tickets_less

    total_sales = adult_tickets_sold * adult_price + child_tickets_sold * child_price

    problem = f"At a concert, \\${total_sales} in tickets were sold. Adult tickets were \\${adult_price} each and children’s tickets were \\${child_price} each. If the number of adult tickets was {adult_tickets_less} fewer than twice the number of children’s tickets, how many of each kind were sold?"

    answer = f"{adult_tickets_sold} adult tickets and {child_tickets_sold} children's tickets were sold."

    explanation = f"""
    We know that the total sales amount is made up of adult ticket sales and children ticket sales. Given that each adult ticket costs \\${adult_price} and each children's ticket costs \\${child_price}, we can form an equation: <br>

    \\[{adult_price}a + {child_price}c = \\${total_sales}\\] <br>

    From the problem, we also know that the number of adult tickets sold is {adult_tickets_less} fewer than twice the number of children's tickets sold. So, we form another equation: <br>

    \\[a = 2c - {adult_tickets_less}\\] <br>

    By solving this system of equations, we find that {child_tickets_sold} children's tickets and {adult_tickets_sold} adult tickets were sold. 
    """


    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from matplotlib import patches

def create_angle_image(angle, filename='static/images/angle_image.png'):
    fig, ax = plt.subplots()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])

    ax.annotate("", xy=(np.cos(np.radians(angle)), np.sin(np.radians(angle))), xytext=(0,0),
                arrowprops=dict(arrowstyle="->"))

    ax.annotate("", xy=(1, 0), xytext=(0,0),
                arrowprops=dict(arrowstyle="->"))
                
    arc = patches.Arc((0, 0), 0.4, 0.4, theta1=0, theta2=angle, color='red')
    ax.add_patch(arc)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

#=================================================================================

@prealgebra_2e.route('/angle_complement')
def angle_complement():
    angle = random.randint(10, 80)
    complement = 90 - angle

    # Create an image of the angle
    create_angle_image(angle)

    problem = f'Find the complement of a {angle}° angle. <br><img src="/static/images/angle_image.png" alt="Angle image">'
    answer = f'{complement}°'
    explanation = f'The complement of an angle is defined as 90° - the given angle. So, the complement of {angle}° is {complement}°.'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@prealgebra_2e.route('/triangle_angles')
def triangle_angles():
    smallest_angle = random.randint(1, 50)

    # The measure of one angle of a triangle is twice the measure of the smallest angle
    angle_2 = 2 * smallest_angle

    # The measure of the third angle is whatever is left to reach 180°
    angle_3 = 180 - (smallest_angle + angle_2)

    problem = f"The measure of one angle of a triangle is twice the measure of the smallest angle which is {smallest_angle}°. The measure of the third angle is whatever is left to reach a total of 180°. Find the measures of all three angles."
    
    answer = f"{smallest_angle}°, {angle_2}°, {angle_3}°"
    explanation = "The measure of the smallest angle is denoted as $x$. Therefore, the second angle, being twice the smallest, is $2x$ and the third angle is whatever is left to reach a total of 180°. " \
                  "We know that the sum of the angles in a triangle is 180°, so we can write the equation: $x + 2x + (180 - (x + 2x)) = 180$. Solving this equation gives us the measures of the three angles as " + str(smallest_angle) + "°, " + str(angle_2) + "°, " + str(angle_3) + "°."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/equilateral_triangle')
def equilateral_triangle():
    perimeter = random.randint(100, 200)

    # As it is an equilateral triangle, all sides are equal
    side_length = perimeter / 3

    problem = f"The perimeter of an equilateral triangle is {perimeter} feet. Find the length of each side."
    answer = f"{round(side_length, 2)} feet"
    explanation = "An equilateral triangle has all sides of equal length. So to find the length of each side, we just divide the perimeter by 3."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_triangle(a, b, h, filename):
    # Specify the figure size (width, height) in inches
    fig, ax = plt.subplots(figsize=(2, 2))

    # Create the triangle
    triangle = patches.Polygon([[0, 0], [a, 0], [0, b]], closed=True, color='skyblue')

    # Add the triangle to the plot
    ax.add_patch(triangle)
    
    # Set the limits of the plot
    ax.set_xlim([0, a+h])
    ax.set_ylim([0, b+h])

    # Add the lengths to the plot
    ax.text(a/2, b/2, f"a={a}", size=10)
    ax.text(0, b/2, f"b={b}", size=10)
    ax.text(a/2, 0, f"h={h}", size=10)

    # Remove the axes for better visualization
    ax.axis('off')

    # Save the image
    plt.savefig(f'static/images/{filename}')

    # Close the plot to free up memory
    plt.close(fig)
#=================================================================================

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_triangle(a, b, h, filename):
    # Specify the figure size (width, height) in inches
    fig, ax = plt.subplots(figsize=(3, 3))

    # Create the triangle
    triangle = patches.Polygon([[0, 0], [a, 0], [0, b]], closed=True, color='skyblue')

    # Add the triangle to the plot
    ax.add_patch(triangle)
    
    # Set the limits of the plot
    ax.set_xlim([0, a+h])
    ax.set_ylim([0, b+h])

    # Add the lengths to the plot
    #ax.text(a/2, b/2, f"a={a}", size=8)
    #ax.text(0, b/2, f"b={b}", size=8)
    #ax.text(a/2, 0, f"h={h}", size=8)

    # Remove the axes for better visualization
    ax.axis('on')

    # Save the image
    plt.savefig(f'static/images/{filename}')

    # Close the plot to free up memory
    plt.close(fig)
#=================================================================================

@prealgebra_2e.route('/similar_triangles')
def similar_triangles():
    # Triangle side lengths and ratio
    a1 = random.randint(2, 10)
    b1 = random.randint(2, 10)
    ratio = round(random.uniform(1.1, 2.5), 2)

    # Calculate side lengths of second triangle
    a2 = round(a1 * ratio, 2)
    b2 = round(b1 * ratio, 2)

    # Calculate hypotenuse
    c1 = round(math.sqrt(a1**2 + b1**2), 2)
    c2 = round(c1 * ratio, 2)

    # Create the triangles
    create_triangle(a1, b1, c1, 'triangle1.png')
    create_triangle(a2, b2, c2, 'triangle2.png')

    # Formulate problem and solution
    problem = f"Triangle ABC is similar to Triangle XYZ. Here is triangle ABC:<br>\
      <img src=/static/images/triangle1.png> <br> \
      Side AB = {a1} units.<br> \
      Side BC = {b1} units.<br> \
      Hypotenuse AC = {c1} units.<br><br> \
      \
      For triangle XYZ<br><br><img src=/static/images/triangle2.png><br> \
      Side XZ = {a2} units<br> \
      Side ZY = {b2} units.<br> \
      Find the length of Hypotenuse XY."
    answer = f"The hypotenuse XY = {c2} units"
    explanation = f"Since the triangles are similar, the ratios of the corresponding sides are the same.<br> \
    So, XY/AC = XZ/AB = YZ/BC = {ratio}<br> \
    XY = AC * {ratio} = {c2} units."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import matplotlib.pyplot as plt

def create_right_triangle_image(height, hypotenuse):
    # Create a right triangle
    base = (hypotenuse**2 - height**2)**0.5
    triangle_coords = [(0, 0), (base, 0), (0, height), (0, 0)]
    fig, ax = plt.subplots()

    # Plot the triangle
    ax.plot(*zip(*triangle_coords), 'b')

    # Label the sides
    #"b" side
    ax.text(-1, height/2, f"{height}", va='center', rotation='vertical')
    
    #"a" side
    #ax.text(base/2, -1, f"{base}", ha='center')
    
    #hypotenuse side
    ax.text(base/2, height/2, f"{hypotenuse}", ha='center', rotation=45.0)

    # Adjust plot parameters
    ax.axis('equal')
    ax.axis('off')

    # Save the figure
    plt.savefig('static/images/right_triangle.png')
    plt.close()
#=================================================================================

from random import randint

@prealgebra_2e.route('/right_triangle_missing_side_1')
def right_triangle_missing_side_1():
    height = randint(20, 25)
    hypotenuse = randint(height+1, 30)

    base = round((hypotenuse**2 - height**2)**0.5, 2)

    # Create an image of the triangle
    create_right_triangle_image(height, hypotenuse)

    image_url = url_for('static', filename='images/right_triangle.png')
    problem = f"Find the length of the missing side. A right triangle is shown. The height is labeled {height} and the hypotenuse is labeled {hypotenuse}."
    problem += f'<br><img src="{image_url}" alt="Right triangle">'

    answer = f"{base}"
    explanation = f"By using the Pythagorean theorem, the length of the base can be found by taking the square root of the difference of the squares of the hypotenuse and the height. So, it's \({hypotenuse}^2 - {height}^2 = {base}\)."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================


import matplotlib.pyplot as plt
from math import sqrt
from random import randint
from flask import url_for

def create_baseball_diamond_image(side_length, filename='static/images/baseball_diamond.png'):
    diamond_coords = [(0, 0), (side_length, 0), (side_length, side_length), (0, side_length), (0, 0), (side_length, side_length)]
    fig, ax = plt.subplots()

    # Plot the square
    ax.plot(*zip(*diamond_coords), 'b')

    # Label the sides
    ax.text(side_length/2, -side_length/10, f"{side_length} ft", ha='center')
    ax.text(-side_length/10, side_length/2, f"{side_length} ft", va='center', rotation='vertical')
    ax.text(side_length/2, side_length/2, f"?", ha='center', rotation=45.0)

    # Adjust plot parameters
    ax.axis('equal')
    ax.axis('off')

    # Save the figure
    plt.savefig(filename)
    plt.close()

@prealgebra_2e.route('/baseball_diamond_diagonal')
def baseball_diamond_diagonal():
    side_length = 90 # the side length of a baseball diamond is always 90 feet

    diagonal = round(sqrt(2) * side_length, 2)

    # Create an image of the baseball diamond
    create_baseball_diamond_image(side_length)

    image_url = url_for('static', filename='images/baseball_diamond.png')
    problem = "A baseball diamond is shaped like a square with sides 90 feet long. How far is it from home plate to second base, as shown?"
    problem += f'<br><img src="{image_url}" alt="Baseball diamond">'

    answer = f"{diagonal}"
    explanation = f"The distance from home plate to second base is the length of the diagonal of a square. In a square with side length 'a', the length of the diagonal 'd' can be found by \(d = \sqrt{2} \times a\). For a baseball diamond with side length 90 feet, the distance from home plate to second base is \(d = \sqrt{2} \times 90 = {diagonal} feet\)."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from random import randint
from math import pi
from flask import url_for

# Problem 482.
@prealgebra_2e.route('/find_rectangle_dimensions')
def find_rectangle_dimensions():
    width = randint(5, 7)
    additional_length = randint(1, 3)
    length = additional_length + 5 * width
    perimeter = 2 * (length + width)

    problem = f"The length of a rectangle is {additional_length} feet more than five times the width. The perimeter is {perimeter} feet. Find the dimensions of the rectangle."
    answer = f"Length: {length} ft, Width: {width} ft"
    explanation = f"Let's denote the width as $w$. Then the length is $ {additional_length} + 5w $. The perimeter of a rectangle is $2 \\times (length + width) = {perimeter}$. Solving this equation for $w$, we find that $w = {width}$ ft. Then the length is $ {additional_length} + 5 \\times {width} = {length} $ ft."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

# Problem 483.
@prealgebra_2e.route('/find_triangle_area')
def find_triangle_area():
    base = randint(70, 90)
    height = randint(50, 60)
    area = 0.5 * base * height

    problem = f"A triangular poster has base {base} centimeters and height {height} centimeters. Find the area of the poster."
    answer = f"{area} square cm"
    explanation = f"The area of a triangle is given by $0.5 \\times \\text{{base}} \\times \\text{{height}} = 0.5 \\times {base} \\times {height} = {area}$ square cm."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

# Problem 484.
@prealgebra_2e.route('/find_trapezoid_area')
def find_trapezoid_area():
    height = randint(12, 16)
    base1 = randint(18, 22)
    base2 = randint(21, 25)
    area = 0.5 * height * (base1 + base2)

    problem = f"A trapezoid has height {height} inches and bases {base1} inches and {base2} inches. Find the area of the trapezoid."
    answer = f"{area} square inches"
    explanation = f"The area of a trapezoid is given by $0.5 \\times \\text{{height}} \\times (\\text{{base1}} + \\text{{base2}}) = 0.5 \\times {height} \\times ({base1} + {base2}) = {area}$ square inches."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

# Problem 485.
@prealgebra_2e.route('/find_pool_circumference')
def find_pool_circumference():
    diameter = randint(80, 100)
    circumference = round(pi * diameter, 1)

    problem = f"A circular pool has diameter {diameter} inches. What is its circumference? Round to the nearest tenth."
    answer = f"{circumference} inches"
    explanation = f"The circumference of a circle is given by $\\pi \\times \\text{{diameter}} = {pi} \\times {diameter} = {circumference}$ inches."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

def create_shaded_region_image(side_length, radius):
    fig, ax = plt.subplots()

    # Draw the square
    square = patches.Rectangle((0,0), side_length, side_length, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(square)

    # Draw the circle
    circle = patches.Circle((radius, radius), radius, linewidth=1, edgecolor='black', facecolor='grey', alpha=0.5)
    ax.add_patch(circle)

    # Label the sides
    ax.text(side_length/2, -2, f"{side_length}", ha='center')
    ax.text(-2, side_length/2, f"{side_length}", va='center', rotation='vertical')

    # Adjust plot parameters
    ax.axis('equal')
    ax.axis('off')

    plt.savefig('static/images/shaded_region.png')
    plt.close()

#=================================================================================

@prealgebra_2e.route('/find_shaded_area')
def find_shaded_area():
    # For the scope of this problem and without further specification, let's assume we are dealing with a circle and a square
    side_length = randint(10, 20)
    radius = side_length / 2
    circle_area = round(pi * radius**2, 1)
    square_area = side_length**2
    shaded_area = round(square_area - circle_area, 1)

    # Create an image of the shaded region
    create_shaded_region_image(side_length, radius)

    image_url = url_for('static', filename='images/shaded_region.png')
    problem = f"Find the area of the shaded region in a square with side length {side_length} units, and a circle inscribed in the square. Round to the nearest tenth."
    problem += f'<br><img src="{image_url}" alt="Shaded region">'
    answer = f"{shaded_area} square units"
    explanation = f"The area of the square is \( {side_length}^{{2}} = {square_area} \) square units, and the area of the circle is \( \pi \cdot ({radius})^{{2}} = {circle_area} \) square units. The area of the shaded region is \( {square_area} - {circle_area} = {shaded_area} \) square units."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

# Problem 487
@prealgebra_2e.route('/find_room_volume')
def find_room_volume():
    width = randint(10, 20)
    length = randint(20, 30)
    height = randint(7, 10)

    volume = width * length * height

    problem = f"Find the volume of a rectangular room with width {width} feet, length {length} feet, and height {height} feet."
    answer = f"{volume} cubic feet"
    explanation = f"The volume of a rectangular room is given by \( \text{{length}} \times \text{{width}} \times \text{{height}} = {length} \times {width} \times {height} = {volume} \) cubic feet."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================
   
from random import uniform
import math

@prealgebra_2e.route('/coffee_can_cylinder')
def coffee_can_cylinder():
    radius = round(uniform(3, 10), 2)
    height = round(uniform(5, 15), 2)

    volume = round(math.pi * radius**2 * height, 2)
    surface_area = round(2 * math.pi * radius * (radius + height), 2)

    problem = f"A coffee can is shaped like a cylinder with height {height} inches and radius {radius} inches. <br> Find:<br> <br>(a) the volume and <br>(b) the surface area of the can."
    answer = f"(a) Volume: {volume} cubic inches<br> (b) Surface area: {surface_area} square inches"

    explanation = f"The volume of a cylinder is given by \( \pi \cdot r^2 \cdot h = \pi \cdot ({radius})^2 \cdot {height} = {volume} \) cubic inches.<br> The surface area of a cylinder is given by \( 2 \cdot \pi \cdot r \cdot (r + h) = 2 \cdot \pi \cdot {radius} \cdot ({radius} + {height}) = {surface_area} \) square inches."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/traffic_cone_volume')
def traffic_cone_volume():
    height = randint(60, 80)
    radius = randint(15, 25)

    # calculate volume
    volume = round((1 / 3) * pi * (radius ** 2) * height, 2)

    problem = f"A traffic cone has height {height} centimeters. The radius of the base is {radius} centimeters. Find the volume of the cone. Round to the nearest tenth."
    answer = f"{volume}"
    explanation = f"The volume of a cone is given by \( V = \\frac{1}{3} \pi r^2 h \). Here, \( r = {radius} \) cm, \( h = {height} \) cm. Substituting these values in, we get \( V = \\frac{1}{3} \pi ({radius}^2)({height}) = {volume} \) cubic centimeters."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/distance_driven')
def distance_driven():
    speed = round(uniform(55, 70), 2)
    time = round(uniform(3, 5), 2)

    distance = round(speed * time, 2)

    problem = f"Leon drove from his house in Cincinnati to his sister’s house in Cleveland. He drove at a uniform rate of {speed} miles per hour and the trip took {time} hours. What was the distance?"
    answer = f"{distance} miles"

    #explanation = f"The distance travelled is given by the formula \( speed \times time = {speed} \times {time} = {distance} \) miles."
    #explanation = f"The distance travelled is given by the formula \( \text{{speed}} \times \text{{time}} = {speed} \times {time} = {distance} \) miles."
    explanation = f"The distance travelled is given by the formula \( \\text{{speed}} \\times \\text{{time}} = {speed} \\times {time} = {distance} \) miles."



    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/speed_of_boat')
def speed_of_boat():
    time = round(uniform(1, 2), 2)
    distance = round(uniform(20, 25), 2)

    speed = round(distance / time, 2)

    problem = f"The Catalina Express takes {time} hours to travel from Long Beach to Catalina Island, a distance of {distance} miles. To the nearest tenth, what is the speed of the boat?"
    answer = f"{speed} mph"

    explanation = f"The speed of the boat is given by the formula \( speed = \\frac{{distance}}{{time}} \).\
    So, substituting in the given values, we have \( speed = \\frac{{{distance}}}{{{time}}} = {speed:.1f} \) mph."


    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@prealgebra_2e.route('/solve_principal')
def solve_principal():
    interest = random.randint(1000, 2000)
    rate = random.randint(1, 10)
    time = random.randint(1, 5)

    principal = round(interest / (rate / 100 * time), 2)

    problem = f"Use the formula I=Prt to solve for the principal, P, for: \
                <br>ⓐ I=${interest}, r={rate}%, t={time} years"
    answer = f"${principal}"
    explanation = f"The formula I=Prt is used to calculate interest. We can rearrange this formula to solve for P: P = I / (rt). \
                  So, substituting in the given values, we have P = {interest} / ({rate}/100 * {time}) = ${principal}."  
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_formula_for_h')
def solve_formula_for_h():
    A = random.randint(1000, 2000)
    b = random.randint(50, 100)

    while b == 0:  # To avoid division by zero
        b = random.randint(50, 100)

    h = round((2 * A) / b, 2)

    problem = f"Solve the formula \(A=\\frac{1}{2}bh\) for \(h\):\n\n(a) When \(A={A}\) and \(b={b}\)\n(b) In general"

    answer = h
    explanation = f"(a) The formula for the height is given by \(h = \\frac{{2A}}{{b}}\). So, substituting in the given values, we have \(h = \\frac{{2 \\times {A}}}{{{b}}} = {h}\)\\<br>"

    explanation += "\n(b) In general, the formula for the height is given by \(h = \\frac{{2A}}{{b}}\)."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/solve_for_y')
def solve_for_y():
    right_side = random.randint(10, 20)  # Random constant for the right side of the equation
    coefficient = random.randint(1, 9)  # Random coefficient for y
    x = random.randint(1, 10)  # Random x value
    y = round((right_side - x) / coefficient, 2)  # Solve for y

    problem = f"Solve the equation \(x + {coefficient}y = {right_side}\) for \(y\) when \(x = {x}\)."
    
    answer = y
    explanation = f"The equation \(x + {coefficient}y = {right_side}\) can be rearranged to solve for \(y\) by subtracting \(x\) from both sides, then dividing by the coefficient of \(y\), which gives \(y = \\frac{{{right_side} - x}}{{{coefficient}}} = {y}\)."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from flask import Flask, render_template
import random

app = Flask(__name__)

@prealgebra_2e.route('/polynomial_properties')
def polynomial_properties():
    num_terms = random.choice([1, 2, 3])  # Randomly choose the number of terms (1-3)
    coefficients = [random.randint(1, 10) for _ in range(num_terms)]
    degrees = [random.randint(1, 4) for _ in range(num_terms)]

    # Construct the polynomial
    terms = [f"{coefficients[i]}y^{degrees[i]}" for i in range(num_terms)]
    polynomial = " - ".join(terms)

    # Determine if it's a monomial, binomial, or trinomial
    polynomial_type = ['monomial', 'binomial', 'trinomial'][num_terms - 1]

    # The degree of the polynomial is the highest degree of any term
    degree = max(degrees)

    problem = f"For the polynomial \( {polynomial} \)<br><br>"
    problem += "\n\n ⓐ Is it a monomial, binomial, or trinomial?<br>"
    problem += "\n\n ⓑ What is its degree?"

    answer = f"ⓐ It is a {polynomial_type}. \n\n <br>ⓑ Its degree is {degree}."

    explanation = "<br>A polynomial's type (monomial, binomial, trinomial) is determined by the number of terms it has. A polynomial's degree is the highest degree of any term.<br>"

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import sympy as sp
import random

# define variables for symbolic computation
a, b, x, y, z = sp.symbols('a b x y z')

def generate_term():
    """Helper function to generate a random term for a polynomial"""
    coefficient = random.randint(1, 10)
    variable = random.choice([a, b, x, y, z])
    return coefficient*variable

@prealgebra_2e.route('/polynomial_operations')
def polynomial_operations():
    term1 = generate_term()
    term2 = generate_term()
    term3 = generate_term()
    term4 = generate_term()

    problem = (term1 + term2) + (term3 + term4)
    problem_str = f"\( ({str(term1)} + {str(term2)}) + ({str(term3)} + {str(term4)}) \)"

    answer = sp.simplify(problem)
    answer_str = f"\({str(answer)}\)"

    explanation = "Combine like terms to simplify the expression."

    return render_template('problem_prealgebra_2e.html', problem=problem_str, answer=answer_str, explanation=explanation)

#=================================================================================

def generate_poly():
    """Helper function to generate a random polynomial of degree 2 or 3"""
    coefficient1 = random.randint(1, 10) * 10
    coefficient2 = random.randint(1, 10) * 10
    coefficient3 = random.randint(1, 10) * 10
    variable = random.choice(['a', 'x'])
    return f"{coefficient1}{variable}^3+{coefficient2}{variable}^2+{coefficient3}{variable}"
#=================================================================================

@prealgebra_2e.route('/factor_gcf')
def factor_gcf():
    # Generate random coefficients
    coefficient = random.randint(1, 10)
    term1_power = random.randint(2, 5)
    term2_power = random.randint(1, term1_power - 1)
    term3_power = 0  # Constant term

    problem = f"Factor the greatest common factor from the polynomial: \({coefficient}a^{{{term1_power}}} + {coefficient}a^{{{term2_power}}} + {coefficient}\)."

    # Answer
    answer = f"\({coefficient}a^{{{term3_power}}} (a^{{{term1_power - term3_power}}} + a^{{{term2_power - term3_power}}} + 1)\)"

    # Explanation
    explanation = "Factor out the greatest common factor from each term in the polynomial."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/scientific_notation')
def scientific_notation():
    coefficient = random.randint(1, 9)
    power = random.randint(3, 7)
    problem = f"A certain number averages out to {coefficient * 10**power} pounds per person. Write this number in scientific notation."
    answer = f"\({coefficient} \cdot 10^{power}\)"
    explanation = "A number is in scientific notation if it is written as the product of a number (between 1 and 10) and a power of 10."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/decimal_form')
def decimal_form():
    coefficient = random.randint(1, 10)
    power = random.randint(-3, -1)
    problem = f"Convert \({coefficient} \cdot 10^{{{power}}}\) to decimal form."
    answer = f"{coefficient * 10**power}"
    explanation = "In scientific notation, \(a \cdot 10^b\) is equal to the number \(a\) moved \(b\) places to the right (if \(b\) is positive) or left (if \(b\) is negative) in decimal form."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/multiply_scientific_notation')
def multiply_scientific_notation():
    a, b = round(random.uniform(1, 3), 1), round(random.uniform(1, 3), 1)
    exponent_a, exponent_b = random.randint(-3, 3), random.randint(-3, 3)
    result_base = a * b
    result_exponent = exponent_a + exponent_b
    #result = "{:.2e}".format(result_base * 10 ** result_exponent)  # Convert to decimal format while maintaining precision
    result = round((result_base * 10 ** result_exponent), 7)

    problem = f"Simplify and write your answer in decimal form: \(({a} \\times 10^{{{exponent_a}}})({b} \\times 10^{{{exponent_b}}})\)"
    answer = result

    explanation = f"We multiply the numbers and then add the exponents in scientific notation. The result is {result}."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/divide_scientific_notation')
def divide_scientific_notation():
    #a, b = random.uniform(1, 10), random.uniform(1, 10)
    a, b = round(random.uniform(1, 3), 1), round(random.uniform(1, 3), 1)
    #exponent_a, exponent_b = random.randint(-10, 10), random.randint(-10, 10)
    exponent_a, exponent_b = random.randint(-3, 3), random.randint(-3, 3)
    while b == 0:
        b = random.uniform(1, 10)
    result = round((a / b) * 10 ** (exponent_a - exponent_b), 3)
    problem = f"Simplify and write your answer in decimal form: \({a} \\times 10^{{{exponent_a}}}/{b} \\times 10^{{{exponent_b}}}\)"
    answer = result
    explanation = f"We divide the numbers and then subtract the exponents in scientific notation. The result is {result}."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/find_height')
def find_height():
    t = random.randint(1,4)
    initial_height = random.randint(200,300)
    coefficient = random.randint(-20,-10)
    height = round(coefficient*t**2 + initial_height, 2)
    
    problem = f"A hiker drops a pebble from a bridge {initial_height} feet above a canyon. The polynomial \( {coefficient}t^2 + {initial_height} \) gives the height of the pebble \( t \) seconds after it was dropped. Find the height when \( t={t} \)."
    answer = height
    explanation = f"Substitute \( t = {t} \) into the polynomial to get the height. The height after {t} seconds is {height} feet."
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import matplotlib.pyplot as plt
import numpy as np
import random
import os

def create_point_image(points, filename='static/images/point_image.png', show_labels=False):
    # Creating the figure and the axes
    fig, ax = plt.subplots()
    
    # Sorting points by x value first (left to right) and then by y value (top to bottom)
    sorted_points = sorted(points, key=lambda point: (-point[1], point[0]))

    # Plotting the points
    for i, (x, y) in enumerate(sorted_points):
        if show_labels:
            ax.plot(x, y, 'o', label=f'Point {chr(65+i)}: ({x},{y})')
        else:
            ax.plot(x, y, 'o', label=f'Point {chr(65+i)}')

    # Setting the limits of the plot
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    
    # Adding a grid
    ax.grid(True)
    
    # Set the ticks
    ax.set_xticks(np.arange(-10, 10, 1))
    ax.set_yticks(np.arange(-10, 10, 1))
    
    # Drawing vertical and horizontal lines
    ax.axhline(0, color='black',linewidth=1.25)
    ax.axvline(0, color='black',linewidth=1.25)
    
    # Adding legend
    ax.legend()

    # Saving the figure
    fig.savefig(filename)

    plt.close()


@prealgebra_2e.route('/plot_and_label_points')
def plot_and_label_points():
    # Randomly generate five pairs of (x, y) coordinates
    coordinates = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]

    # Create an image of the points
    create_point_image(coordinates)

    # Generate the problem statement
    problem = "Plot and label these points: <br>"
    for i, point in enumerate(coordinates):
        problem += f"- Point {chr(65+i)}: {point}<br>"

    answer = "The points are plotted on the graph as shown.<br><br>"
    answer += '<img src="/static/images/point_image.png" alt="Point image">'
    
    explanation = "Each point represents a location on the graph. The first number is the x-coordinate which shows the location on the horizontal axis and the second number is the y-coordinate which shows the location on the vertical axis."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@prealgebra_2e.route('/name_ordered_pairs')
def name_ordered_pairs():
    points = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]
    create_point_image(points, filename='static/images/points.png', show_labels=False)

    problem = f'Name the ordered pair for each point shown.<br><img src="/static/images/points.png" alt="Points">'
    
    create_point_image(points, filename='static/images/points_solution.png', show_labels=True)
    answer = f'<img src="/static/images/points_solution.png" alt="Solution">'
    explanation = f'The points on the graph correspond to the following ordered pairs: ' + ', '.join([f'{p}' for p in points]) + '.'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

import matplotlib.pyplot as plt
import numpy as np
import random
import os

def create_line_image(points, filename='static/images/line_image.png', show_intercepts=False):
    fig, ax = plt.subplots()
    
    # Create line
    ax.plot(*zip(*points), color='blue')

    # If show_intercepts is true, show intercept points on the graph
    if show_intercepts:
        for x, y in points:
            ax.plot(x, y, 'ro')
            ax.annotate(f'({x},{y})', (x, y), textcoords="offset points", xytext=(-10,-10), ha='center')

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    
    ax.grid(True)
    
    ax.set_xticks(np.arange(-10, 10, 1))
    ax.set_yticks(np.arange(-10, 10, 1))
    
    ax.axhline(0, color='black',linewidth=1.25)
    ax.axvline(0, color='black',linewidth=1.25)
    
    fig.savefig(filename)

    plt.close()

@prealgebra_2e.route('/find_intercepts')
def find_intercepts():
    x_intercept = random.randint(-9, 9)
    y_intercept = random.randint(-9, 9)

    # Create a line image without intercept points
    create_line_image([(x_intercept, 0), (0, y_intercept)], filename='static/images/line_image.png', show_intercepts=False)

    problem = f'Find the x-intercept and y-intercept on the line shown.<br><img src="/static/images/line_image.png" alt="Line image">'
    answer = f'The x-intercept is ({x_intercept}, 0) and the y-intercept is (0, {y_intercept}).'
    explanation = f'The x-intercept is the point where the line crosses the x-axis, and the y-intercept is the point where the line crosses the y-axis. Therefore, the x-intercept is ({x_intercept}, 0) and the y-intercept is (0, {y_intercept}).'

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

def create_intercept_image(coeff_x, coeff_y, constant, x_intercept, y_intercept, filename='static/images/intercept_image.png'):
    fig, ax = plt.subplots()

    x = np.linspace(-10, 10, 400)
    y = (coeff_x * x - constant) / coeff_y

    ax.plot(x, y, '-r', label=f'{coeff_x}x - {abs(coeff_y)}y = {constant}')
    ax.plot(x_intercept, 0, 'go', label=f'x-intercept ({x_intercept}, 0)')
    ax.plot(0, y_intercept, 'bo', label=f'y-intercept (0, {y_intercept})')

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.legend()

    fig.savefig(filename)
    plt.close()

@prealgebra_2e.route('/solve_intercepts')
def solve_intercepts():
    # Generate random x and y intercepts
    x_intercept = random.randint(-10, 10)
    y_intercept = random.randint(-10, 10)

    # Make sure neither of the intercepts are zero to avoid trivial cases
    while x_intercept == 0 or y_intercept == 0:
        x_intercept = random.randint(-10, 10)
        y_intercept = random.randint(-10, 10)

    # Calculate coefficients from the intercepts
    coeff_x = y_intercept
    coeff_y = -x_intercept

    # Calculate constant from the intercepts
    constant = x_intercept * y_intercept

    # Create the image
    create_intercept_image(coeff_x, coeff_y, constant, x_intercept, y_intercept, filename='static/images/answer_intercept_image.png')

    # Handle plus/minus signs for the equation to be displayed in the problem
    y_sign = '+' if coeff_y > 0 else '-'
    
    problem = f"Find the x-intercept and y-intercept of the equation {coeff_x}x {y_sign} {abs(coeff_y)}y = {constant}."
    answer = f"The x-intercept is ({x_intercept}, 0) and the y-intercept is (0, {y_intercept}). <br> <img src='/static/images/answer_intercept_image.png' alt='Intercepts image'>"
    explanation = f"The x-intercept is found by setting y to 0 in the equation and solving for x. Similarly, the y-intercept is found by setting x to 0 in the equation and solving for y."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================


import random
import sympy as sp

@prealgebra_2e.route('/check_point_solution')
def check_point_solution():
    # Generate random coefficients, constant, and point
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    point = (random.randint(-10, 10), random.randint(-10, 10))

    # Create the problem, answer and explanation
    problem = f"Is {point} a solution to the equation {a}x+{b}y={c}? How do you know?"
    is_solution = (a * point[0] + b * point[1] == c)
    answer = "Yes" if is_solution else "No"
    explanation = (f"When we substitute x={point[0]} and y={point[1]} into the equation, "
                   f"we get {a} * {point[0]} + {b} * {point[1]} = {a * point[0] + b * point[1]}, "
                   f"which is {'equal to' if is_solution else 'not equal to'} {c}. "
                   f"Therefore, {point} is {'a' if is_solution else 'not a'} solution to the equation.")

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/complete_table')
def complete_table():
    # Generate a random coefficient and constant
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    # Generate random x values
    x_values = [random.randint(-10, 10) for _ in range(4)]

    # Calculate corresponding y values
    y_values = [round(a * x + b, 2) for x in x_values]

    # Creating the table for the problem
    problem_table = '<table><tr><th>x</th><th>y</th><th>(x,y)</th></tr>'
    for x in x_values:
        problem_table += f'<tr><td>{x}</td><td>?</td><td>?</td></tr>'
    problem_table += '</table>'

    problem = f"Complete the table to find four solutions to the equation y={a}x+{b}.<br>{problem_table}"

    # Creating the table for the answer
    answer_table = '<table><tr><th>x</th><th>y</th><th>(x,y)</th></tr>'
    for x, y in zip(x_values, y_values):
        answer_table += f'<tr><td>{x}</td><td>{y}</td><td>({x},{y})</td></tr>'
    answer_table += '</table>'

    answer = answer_table

    # Creating the table for the explanation
    explanation_table = '<table><tr><th>x</th><th>y calculation</th><th>y</th></tr>'
    for x, y in zip(x_values, y_values):
        explanation_table += f'<tr><td>{x}</td><td>{a} * {x} + {b}</td><td>{y}</td></tr>'
    explanation_table += '</table>'

    explanation = f"The values of y were calculated by substituting each x into the equation y={a}x+{b}.<br>{explanation_table}"

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/complete_table_for_equation')
def complete_table_for_equation():
    # Generating random coefficients and constant
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-20, 20)

    # Make sure neither of the coefficients are zero to avoid division by zero error
    while a == 0 or b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    # Generate distinct x values to use
    x_values = list(set([0, round(random.uniform(-10, 10), 2), round(random.uniform(-10, 10), 2)]))
    while len(x_values) < 3:
        x_values.append(round(random.uniform(-10, 10), 2))

    # Corresponding y values for the equation ax+by=c
    y_values = [round((c - a * x) / b, 2) for x in x_values]

    problem = f"Complete the table to find three solutions to the equation {a}x + {b}y = {c}<br>" \
              f"<table border='1'><tr><th>x</th><th>y</th><th>(x,y)</th></tr>" \
              f"<tr><td>{x_values[0]}</td><td>___</td><td>( , )</td></tr>" \
              f"<tr><td>___</td><td>{y_values[1]}</td><td>( , )</td></tr>" \
              f"<tr><td>{x_values[2]}</td><td>___</td><td>( , )</td></tr></table>"

    answer = f"The completed table is:<br>" \
             f"<table border='1'><tr><th>x</th><th>y</th><th>(x,y)</th></tr>" \
             f"<tr><td>{x_values[0]}</td><td>{y_values[0]}</td><td>({x_values[0]},{y_values[0]})</td></tr>" \
             f"<tr><td>{x_values[1]}</td><td>{y_values[1]}</td><td>({x_values[1]},{y_values[1]})</td></tr>" \
             f"<tr><td>{x_values[2]}</td><td>{y_values[2]}</td><td>({x_values[2]},{y_values[2]})</td></tr></table>"

    explanation = "To complete the table, substitute the given x values into the equation and solve for y. Conversely, substitute the given y values into the equation and solve for x."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import matplotlib.pyplot as plt
import numpy as np
import os
import random

import matplotlib.pyplot as plt
import numpy as np
import os
import random

def create_line_graph_with_dots(a, b, c, x_values, y_values, filename='static/images/line_graph.png'):
    # Calculate corresponding y values for the line at a larger range of x_values
    x_line = np.linspace(min(x_values)-1, max(x_values)+1, 400)
    y_line = (c - a*x_line) / b
    # Create the figure and axis
    fig, ax = plt.subplots()
    # Plot the line
    ax.plot(x_line, y_line, '-r', label=f'{a}x+{b}y={c}')
    # Plot the points
    ax.scatter(x_values, y_values, color='blue')
    # Set the x and y axis limits
    ax.set_xlim([min(x_values)-1, max(x_values)+1])
    ax.set_ylim([min(y_values)-1, max(y_values)+1])
    # Adding a grid
    ax.grid(True)
    # Set the ticks
    ax.set_xticks(np.arange(min(x_values)-1, max(x_values)+2, 1))
    ax.set_yticks(np.arange(min(y_values)-1, max(y_values)+2, 1))
    # Drawing vertical and horizontal lines
    ax.axhline(0, color='black',linewidth=1.25)
    ax.axvline(0, color='black',linewidth=1.25)
    # Adding legend
    ax.legend()
    # Save the figure
    fig.savefig(filename)
    plt.close()


@prealgebra_2e.route('/find_three_solutions_and_graph')
def find_three_solutions_and_graph():
    # Generating random coefficients and constant
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-20, 20)

    # Make sure neither of the coefficients are zero to avoid division by zero error
    while a == 0 or b == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    # Generate distinct x values to use
    x_values = list(set([random.randint(-10, 10) for _ in range(3)]))
    while len(x_values) < 3:
        x_values.append(random.randint(-10, 10))

    # Corresponding y values for the equation ax+by=c
    y_values = [(c - a * x) // b for x in x_values]

    problem = f"Find three solutions to the equation {a}x + {b}y = {c} and then graph the line."
    create_line_graph_with_dots(a, b, c, x_values, y_values, filename='static/images/line_graph.png')
    answer = f"The three solutions are: ({x_values[0]}, {y_values[0]}), ({x_values[1]}, {y_values[1]}), ({x_values[2]}, {y_values[2]}).<br> \
              <img src='/static/images/line_graph.png' alt='Graph of the line'>"
    explanation = "The three solutions are found by picking any three values for x and solving the equation for y. The resulting pairs (x, y) are solutions to the equation."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import matplotlib.pyplot as plt
import numpy as np
import random

def create_slope_image(point1, point2, filename='static/images/slope_image.png'):
    # Calculating slope
    slope = round((point2[1] - point1[1]) / (point2[0] - point1[0]), 2)
    
    # Creating the figure and the axes
    fig, ax = plt.subplots()
    
    # Plotting the points and the line between them
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    ax.plot(x_values, y_values, marker = 'o')
    
    # Setting the limits of the plot
    ax.set_xlim([min(x_values)-1, max(x_values)+1])
    ax.set_ylim([min(y_values)-1, max(y_values)+1])
    
    # Adding a grid
    ax.grid(True)
    
    # Set the ticks
    ax.set_xticks(np.arange(min(x_values)-1, max(x_values)+2, 1))
    ax.set_yticks(np.arange(min(y_values)-1, max(y_values)+2, 1))
    
    # Drawing vertical and horizontal lines
    ax.axhline(0, color='black',linewidth=1.25)
    ax.axvline(0, color='black',linewidth=1.25)
    
    # Saving the figure
    fig.savefig(filename)
    
    plt.close()
    
    return slope

@prealgebra_2e.route('/find_slope')
def find_slope():
    # Generate random points within a reasonable range
    point1 = [random.randint(-7, 7), random.randint(-5, 5)]
    point2 = [random.randint(-7, 7), random.randint(-5, 5)]
    
    # Create the image
    slope = create_slope_image(point1, point2, filename='static/images/slope_image.png')
    
    problem = f"The graph shows the x y-coordinate plane. The axes run from -7 to 7. A line passes through the points “ordered pair {point1}” and “ordered pair {point2}”. Find the slope of the line."
    answer = f"The slope of the line is {slope}. <br> <img src='/static/images/slope_image.png' alt='Slope image'>"
    explanation = f"The slope of a line is calculated as the difference in y-coordinates divided by the difference in x-coordinates. Here, the slope is ({point2[1]} - {point1[1]}) / ({point2[0]} - {point1[0]}) = {slope}."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/find_slope_given_points')
def find_slope_given_points():
    # Generate random points within a reasonable range
    point1 = [random.randint(-7, 7), random.randint(-5, 5)]
    point2 = [random.randint(-7, 7), random.randint(-5, 5)]
    
    # Calculating the slope
    slope = round((point2[1] - point1[1]) / (point2[0] - point1[0]), 2)
    
    problem = f"Use the slope formula to find the slope of the line between {point1} and {point2}."
    answer = f"The slope of the line is {slope}."
    explanation = f"The slope of a line is calculated as the difference in y-coordinates divided by the difference in x-coordinates. Here, the slope is ({point2[1]} - {point1[1]}) / ({point2[0]} - {point1[0]}) = {slope}."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@prealgebra_2e.route('/find_slope_horizontal_line')
def find_slope_horizontal_line():
    # Generate random y value within a reasonable range
    y_value = random.randint(-5, 5)
    
    problem = f"Find the slope of the line y = {y_value}."
    answer = "The slope of the line is 0."
    explanation = "The slope of a horizontal line is always 0, regardless of the value of y."
    
    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

def create_line_graph_with_slope(point, slope, filename='static/images/line_graph.png'):
    # Compute the coordinates for the line
    x_values = np.array(range(-10, 11))
    y_values = slope * (x_values - point[0]) + point[1]

    # Create the figure and axis
    fig, ax = plt.subplots()

    # Plot the line
    ax.plot(x_values, y_values, '-r')

    # Set the x and y axis limits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # Adding a grid
    ax.grid(True, which='both')

    # Set the ticks
    ax.set_xticks(np.arange(-10, 11, 1))
    ax.set_yticks(np.arange(-10, 11, 1))

    # Drawing vertical and horizontal lines
    ax.axhline(0, color='black', linewidth=1.25)
    ax.axvline(0, color='black', linewidth=1.25)

    # Save the figure
    fig.savefig(filename)
    plt.close()


import numpy as np
import matplotlib.pyplot as plt

@prealgebra_2e.route('/graph_line_with_slope')
def graph_line_with_slope():
    # Generate random point and slope for the line
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    numerator = random.randint(-10, 10)
    denominator = random.randint(-10, 10)

    # Make sure the denominator is not zero to avoid undefined slope
    while denominator == 0:
        denominator = random.randint(-10, 10)

    # Calculating slope as a fraction
    slope = Fraction(numerator, denominator)

    # Create the image
    create_line_graph_with_slope((x, y), slope, filename='static/images/line_graph.png')

    problem = f"Graph the line passing through ({x},{y}) with slope $m=\\frac{{{numerator}}}{{{denominator}}}$."
    answer = f"<img src='/static/images/line_graph.png' alt='Line graph image'>"
    explanation = f"To graph a line with a given point and slope, follow these steps:<br>\
    1. Start by plotting the given point on the graph, which is ({x},{y}) in this case.<br>\
    2. Since the slope is $\\frac{{{numerator}}}{{{denominator}}}$, this means that for every {denominator} steps you move to the right on the x-axis, you move {numerator} steps up/down on the y-axis (up if the slope is positive, down if it's negative).<br>\
    3. From the initial point, use the slope to find a second point and plot it.<br>\
    4. Draw a straight line through these points, extending it past the points to cover the entire graph.<br>\
    The line on the graph above follows these steps."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from fractions import Fraction

@prealgebra_2e.route('/bicycle_slope')
def bicycle_slope():
    # Define the values for the slope calculation
    rise = random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    run = random.choice([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000])

    # Calculate the slope
    slope_fraction = Fraction(rise, run)
    slope_fraction = slope_fraction.limit_denominator()

    # Check if the slope is a whole number
    if slope_fraction.denominator == 1:
        answer = f"The slope of the bicycle route is {slope_fraction.numerator}."
    else:
        answer = f"The slope of the bicycle route is $\\frac{{{slope_fraction.numerator}}}{{{slope_fraction.denominator}}}$."

    # Define the problem statement
    problem = f"A bicycle route climbs {rise} feet for {run} feet of horizontal distance. What is the slope of the route?"

    # Define the explanation
    explanation = f"The slope of the route is calculated as rise over run, which in this case is $\\frac{{{rise}}}{{{run}}}$."

    return render_template('problem_prealgebra_2e.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================


