from flask import Blueprint, render_template, url_for

import random
from random import randint, uniform
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import math
from math import pi, pow

qr_1a1 = Blueprint('qr_1a1', __name__, template_folder='templates')
#=================================================================================

@qr_1a1.route('/sedans_ratio')
def sedans_ratio():
    black_sedans = random.randint(100, 999)
    non_black_sedans = random.randint(100, 999)
    ratio = Fraction(non_black_sedans, black_sedans)
    problem = f"There are {black_sedans} black sedans in the parking lot and {non_black_sedans} non-black sedans in the parking lot. What is the ratio of non-black sedans to black sedans? Write your answer as a simplified fraction."
#    answer = f"${ratio.numerator}:{ratio.denominator}$"    
    answer = f"$\\frac{{{ratio.numerator}}}{{{ratio.denominator}}}$"
    explanation = f"$\\frac{{{'total-number-of-non-black-sedans'}}}{{{'total-number-of-black-sedans'}}}$"
    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/mixed_numbers_ratio')
def mixed_numbers_ratio():
    # Generate random mixed numbers
    whole1 = random.randint(1, 9)
    whole2 = random.randint(1, 9)
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    den1 = random.randint(1, 9)
    den2 = random.randint(1, 9)

    # Convert mixed numbers to improper fractions
    frac1 = Fraction(whole1 * den1 + num1, den1)
    frac2 = Fraction(whole2 * den2 + num2, den2)

    # Calculate the ratio as a simplified fraction
    ratio = Fraction(frac1, frac2)

    problem = f"Write the ratio {whole1} {num1}/{den1} to {whole2} {num2}/{den2} as a simplified fraction."
    answer = f"$\\frac{{{ratio.numerator}}}{{{ratio.denominator}}}$"
    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

@qr_1a1.route('/whole_numbers_fraction_ratio')
def whole_numbers_fraction_ratio():
    # Generate random whole numbers
    whole1 = random.randint(1, 9)
    whole2 = random.randint(1, 9)

    # Calculate the ratio as a simplified fraction
    ratio = Fraction(whole1, whole2)

    problem = f"Write the ratio {whole1} to {whole2} as a fraction of whole numbers."
    answer = f"$\\frac{{{ratio.numerator}}}{{{ratio.denominator}}}$"
    
    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

@qr_1a1.route('/decimal_numbers_fraction_ratio')
def decimal_numbers_fraction_ratio():
    # Generate random floating-point numbers up to hundredths place
    float1 = round(random.uniform(0.01, 9.99), 2)
    float2 = round(random.uniform(0.01, 9.99), 2)

    # Convert floats to whole number fractions (multiply by 100 and simplify)
    frac1 = Fraction(int(float1 * 100), 100)
    frac2 = Fraction(int(float2 * 100), 100)

    # Calculate the ratio as a simplified fraction
    ratio = Fraction(frac1, frac2)

    problem = f"Write the ratio {float1} to {float2} as a fraction of whole numbers."
    answer = f"$\\frac{{{ratio.numerator}}}{{{ratio.denominator}}}$"
    
    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

def generate_cpi(start_year, end_year):
    cpi = {}
    last_cpi = 20
    for year in range(start_year, end_year + 1):
        cpi_increase = round(random.uniform(0.1, 3), 3)
        new_cpi = last_cpi + cpi_increase
        cpi[year] = new_cpi
        last_cpi = new_cpi
    return cpi
#=================================================================================

@qr_1a1.route('/proportion_using_cpi')
def proportion_using_cpi():

    start_year = 1959
    end_year = 2019
    hamburger_price = round(random.uniform(0.10, 1.99), 2)

    # Generate random CPIs for the years in the range
    cpi = generate_cpi(start_year, end_year)

    # Pick a random year in the range greater than 1973
    year = random.randint(1974, end_year)
    cpi_1973 = cpi[1973]
    cpi_year = cpi[year]

    # Calculate the price of a hamburger adjusted for inflation
    adjusted_price = round(hamburger_price * (cpi_year / cpi_1973), 2)

    problem = (f"The price of a hamburger was\${hamburger_price} in 1973 (CPI: {cpi_1973:.3f}). What would the price of a hamburger be in {year} (CPI: {cpi_year:.3f}) if inflation were the only factor impacting the price? Round your answer to the nearest cent.")
    answer = f"${adjusted_price:.2f}"

    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

@qr_1a1.route('/proportion_using_rates')
def proportion_using_rates():
    year = random.randint(1973, 2023)
    employees = random.randint(7300, 10300)
    fans = random.randint(17300, 20230)

    # Calculate the number of fans per employee
    fans_per_employee = round(fans / employees, 1)

    problem = (f"In {year}, Madison Square Garden employed {employees} people. "
               f"For a basketball game at the garden, there are seats for {fans} fans. "
               f"What is the number of fans per employee during a basketball game? Round to the nearest tenth.")

    answer = f"${fans_per_employee:.1f}$"

    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

@qr_1a1.route('/proportion_rates_per_100k')
def proportion_rates_per_100k():
    births = random.randint(80000, 98000)
    population = random.randint(6000000, 9000000)

    # Calculate the number of births per 100,000 people
    births_per_100k = round((births / population) * 100000)

    problem = (f"Indiana averages {births} births each year to a population of {population}. "
               f"How many births could we contribute to 100,000 people in Indiana? Round to the nearest whole.")

    answer = f"${births_per_100k}$"

    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

@qr_1a1.route('/proportional_comparison')
def proportional_comparison():
    atlanta_shops = random.randint(100, 400)
    atlanta_population = random.randint(2000000, 3800000)
    brooklyn_shops = random.randint(100, 400)
    brooklyn_population = random.randint(2000000, 3800000)

    # Calculate the ratio of coffee shops to population in Brooklyn
    brooklyn_ratio = brooklyn_shops / brooklyn_population

    # Calculate the number of coffee shops Atlanta should have if it were proportional to Brooklyn
    atlanta_target_shops = round(atlanta_population * brooklyn_ratio)

    problem = (f"There are {atlanta_shops} coffee shops in Atlanta with a population of {atlanta_population}. "
               f"Brooklyn has {brooklyn_shops} coffee shops with a population of {brooklyn_population}. "
               f"If Atlanta was proportional to Brooklyn in coffee shops to population, "
               f"how many coffee shops should Atlanta have? Round to the nearest whole number.")

    answer = f"${atlanta_target_shops}$"

    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

@qr_1a1.route('/mean_shark_attacks')
def mean_shark_attacks():
    start_year = 1837
    end_year = start_year + random.randint(130, 180)
    num_states = random.randint(8, 12)

    # Generate a list of random numbers of shark attacks for each state
    attack_numbers = [random.randint(1, 16) for _ in range(num_states)]

    # Calculate the mean number of shark attacks
    mean_attacks = round(sum(attack_numbers) / num_states)

    # Convert attack_numbers list to a string representation
    attack_numbers_str = ', '.join(map(str, attack_numbers))

    problem = (f"The International Shark Attack File recorded the number of shark attacks "
               f"between {start_year} and {end_year} for {num_states} different U.S. states. "
               f"What is the mean number of shark attacks over these states?\n\n"
               f"{attack_numbers_str}")

    answer = f"${mean_attacks}$"

    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

from collections import Counter

@qr_1a1.route('/mode_president_ages')
def mode_president_ages():
    ages = [42, 60, 61, 51, 55, 62, 43, 54, 52, 51, 64, 69, 46, 56, 56, 51]
    num_presidents = random.randint(8, 17)
    selected_ages = random.sample(ages, num_presidents)
    random.shuffle(selected_ages)

    age_counts = Counter(selected_ages)
    mode_age = max(age_counts, key=age_counts.get)

    ages_str = ', '.join(map(str, selected_ages))
    problem = (f"The ages at inauguration of {num_presidents} U.S. presidents are below. "
               f"What is the mode?\n\n"
               f"{ages_str}")

    answer = f"${mode_age}$"
    explanation = f"The mode is the value that appears most frequently in the data set. In this case, the age {mode_age} appears most frequently among the selected ages."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

from statistics import median

@qr_1a1.route('/median_worm_length')
def median_worm_length():
    num_worms = random.randint(6, 8)
    worm_lengths = [random.randint(6, 12) for _ in range(num_worms)]

    worm_lengths_str = ', '.join(map(str, worm_lengths))
    problem = (f"Find the median of the following list of inches traveled by {num_worms} randomly "
               f"selected worms in a two-minute time period.\n\n"
               f"{worm_lengths_str}")

    med = median(worm_lengths)
    answer = f"${med}$"
    explanation = f"The median is the middle value when the data is arranged in ascending order. In this case, the median length is {med} inches."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/gpa_calculation')
def weighted_averages_gpa_calculation():
    class_names = ['Quantitative Reasoning', 'Science', 'Psychology', 'Science Lab', 'Economics', 'History', 'English', 'Physics']
    credit_hours_options = [2, 3, 4]
    grade_options = ['A', 'B', 'C', 'D', 'F']
    grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

    num_classes = random.randint(3, 5)
    selected_classes = random.sample(class_names, num_classes)

    class_data = []
    total_credits = 0
    weighted_sum = 0
    for class_name in selected_classes:
        credit_hours = random.choice(credit_hours_options)
        grade = random.choice(grade_options)
        class_data.append((class_name, credit_hours, grade))
        
        total_credits += credit_hours
        weighted_sum += grade_points[grade] * credit_hours

    gpa = round(weighted_sum / total_credits, 2)
    answer = f"GPA: {gpa}"

    problem = "Find the grade point average (GPA) for a student using the following information:<br><br>"
    problem += "<table><tr><th>Class</th><th>Credit Hour</th><th>Grade</th></tr>"
    for class_info in class_data:
        problem += f"<tr><td>{class_info[0]}</td><td>{class_info[1]}</td><td>{class_info[2]}</td></tr>"
    problem += "</table><br>Round to the nearest hundredth.<br><br>"
    problem += "To find the GPA, use A = 4 points, B = 3 points, C = 2 points, D = 1 point, F = 0 points."

    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================

@qr_1a1.route('/weighted_average_salary')
def weighted_average_salary():
    levels = [
        {"name": "Entry Level", "salary": random.randrange(32000, 45000, 10000)},
        {"name": "Associates", "salary": random.randrange(42000, 62000, 10000)},
        {"name": "Managers", "salary": random.randrange(82000, 102000, 10000)},
        {"name": "Administration", "salary": random.randrange(240000, 260000, 10000)},
    ]

    for level in levels:
        level["percent"] = random.randint(5, 50)

    problem = "Ted's Technology Company lists the average salary for the different leveled positions in the company, as shown in the table below. Calculate the weighted average for the salary of employees at Ted's Technology Company.<br><br>"
    problem += "<table><tr><th>Level</th><th>Salary</th><th>Percent of Employees</th></tr>"
    
    for level in levels:
        problem += f"<tr><td>{level['name']}</td><td>${level['salary']}</td><td>{level['percent']}%</td></tr>"
    
    problem += "</table><br>"

    weighted_average = sum(level["salary"] * level["percent"] / 100 for level in levels)

    answer = f"The weighted average salary is\${weighted_average:,.2f}"

    explanation = "To find the weighted average salary, we multiply the salary of each level by the corresponding percentage of employees and sum up the results:<br>"
    explanation += f"Weighted average = $({levels[0]['salary']} \\times {levels[0]['percent']}\\%) + $({levels[1]['salary']} \\times {levels[1]['percent']}\\%) + $({levels[2]['salary']} \\times {levels[2]['percent']}\\%) + $({levels[3]['salary']} \\times {levels[3]['percent']}\\%)<br>"
    explanation += f"Weighted average =\${weighted_average:,.2f}<br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

#weighted_average_items = Blueprint("weighted_average_items", __name__, template_folder="templates")
from random import randint

@qr_1a1.route("/weighted_average_items")
def weighted_average_items():
    pens = randint(20, 50) * 10
    pen_price = randint(2, 10)
    paper = randint(20, 50) * 10
    paper_price = randint(10, 40)
    cases = randint(25, 85)
    case_price = randint(50, 95)

    total_pens_cost = pens * pen_price
    total_paper_cost = paper * paper_price
    total_cases_cost = cases * case_price

    total_items = pens + paper + cases
    total_cost = total_pens_cost + total_paper_cost + total_cases_cost

    average_price = total_cost / total_items

    problem = f"Lindsey sells school supplies to districts. Last month she sold {pens} boxes of pens for \\${pen_price} each, {paper} boxes of paper for \\${paper_price} each, and {cases} cases of toner for \\${case_price} each. Calculate her average price per item for last month. Round to the nearest penny."
    answer = round(average_price, 2)
    explanation = f"The total cost of pens is {pens} *\${pen_price} = \\${total_pens_cost}, the total cost of paper is {paper} * \\${paper_price} = \\${total_paper_cost}, and the total cost of cases is {cases} * \\${case_price} = \\${total_cases_cost}. The total cost of items is \\${total_cost}. There are {total_items} items in total. The average price per item is \\${total_cost} / {total_items} = \\${answer}."
    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@qr_1a1.route('/weighted_average_grades')
def weighted_average_grades():
    homework_weight = random.randint(5, 20)
    discussion_weight = random.randint(5, 20)
    projects_weight = random.randint(20, 40)
    exams_weight = 100 - (homework_weight + discussion_weight + projects_weight)

    homework_scores = [random.randint(0, 100) for _ in range(random.randint(4, 6))]
    discussion_scores = [random.randint(0, 100) for _ in range(random.randint(4, 6))]
    projects_scores = [random.randint(0, 100) for _ in range(random.randint(2, 3))]
    exams_scores = [random.randint(0, 100) for _ in range(random.randint(2, 3))]

    def weighted_average(scores, weight):
        return sum(scores) / len(scores) * weight / 100

    final_grade = round(
        weighted_average(homework_scores, homework_weight) +
        weighted_average(discussion_scores, discussion_weight) +
        weighted_average(projects_scores, projects_weight) +
        weighted_average(exams_scores, exams_weight)
    )

    problem = f"Tim completed an online class this semester with a weighted grading system. Within this course, homework was {homework_weight}% of his grade, discussion boards were {discussion_weight}%, projects were {projects_weight}%, and exams were {exams_weight}%. Below is a summary of each category. Use the information provided to calculate Tim's final grade in the course. Do not round until the final step, and round to the nearest whole number."
    problem += f"<br><br><table><tr><th>Category</th><th>Scores</th></tr><tr><td>Homework</td><td>{' '.join(map(str, homework_scores))}</td></tr><tr><td>Discussion Boards</td><td>{' '.join(map(str, discussion_scores))}</td></tr><tr><td>Projects</td><td>{' '.join(map(str, projects_scores))}</td></tr><tr><td>Exams</td><td>{' '.join(map(str, exams_scores))}</td></tr></table>"


    answer = final_grade
    explanation = f"Calculate the weighted average for each category and sum them up:\nHomework: {weighted_average(homework_scores, homework_weight):.2f}\nDiscussion Boards: {weighted_average(discussion_scores, discussion_weight):.2f}\nProjects: {weighted_average(projects_scores, projects_weight):.2f}\nExams: {weighted_average(exams_scores, exams_weight):.2f}\n\nAdd them up to get the final grade: {final_grade}"
    
    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/relative_change_watch')
def relative_change_watch():
    watch_initial_price = random.randint(150, 250)
    price_reduction_percent = random.randint(10, 25) / 100
    watch_final_price = round(watch_initial_price * (1 - price_reduction_percent))

    rounding_choices = ['tenth', 'hundredth', 'thousandth']
    rounding_choice = random.choice(rounding_choices)
    if rounding_choice == 'tenth':
        rounding_decimal = 1
    elif rounding_choice == 'hundredth':
        rounding_decimal = 2
    else:
        rounding_decimal = 3

    relative_change = round((watch_final_price - watch_initial_price) / watch_initial_price, rounding_decimal)

    problem = f"The price of a certain watch fell from\${watch_initial_price} to \\${watch_final_price} over the past year. What is the relative change in the price of the watch, rounded to the nearest {rounding_choice}?"
    answer = f"{relative_change}"
    explanation = f"The relative change in price is calculated as (final price - initial price) / initial price: (${watch_final_price} -\${watch_initial_price}) /\${watch_initial_price} = {relative_change}. Rounded to the nearest {rounding_choice}, the relative change is {relative_change}."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/absolute_change_screen_time')
def absolute_change_screen_time():
    screen_time_last_month = random.uniform(3, 12)
    screen_time_reduction_percent = random.uniform(40, 75) / 100
    screen_time_this_month = round(screen_time_last_month * (1 - screen_time_reduction_percent), 1)

    absolute_change = round(abs(screen_time_this_month - screen_time_last_month), 1)

    problem = f"Last month Terrell averaged {screen_time_last_month:.1f} hours of screen time per day. He decided to make efforts to decrease his screen time. This month he has averaged {screen_time_this_month:.1f} hours per day. What is the absolute change in Terrell's screen time?"
    answer = f"{absolute_change}"
    explanation = f"The absolute change in screen time is calculated as the difference between the two averages: {screen_time_this_month:.1f} - {screen_time_last_month:.1f} = {absolute_change}. The absolute change in Terrell's screen time is {absolute_change} hours."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/percent_change_salary')
def percent_change_salary():
    initial_wage = random.uniform(10, 15)
    raise_percentage = random.uniform(10, 35) / 100
    new_wage = round(initial_wage * (1 + raise_percentage), 2)

    percent_change = round((new_wage - initial_wage) / initial_wage * 100, 2)

    problem = f"If you get a raise from \\${initial_wage:.2f} per hour to \\${new_wage:.2f} per hour, what is the percent change?"
    answer = f"{percent_change}%"
    explanation = f"The percent change in salary is calculated as the difference between the new wage and the initial wage, divided by the initial wage, and multiplied by 100: (( \\${new_wage:.2f} -\${initial_wage:.2f}) / \\${initial_wage:.2f}) * 100 = {percent_change}%. The percent change in salary is {percent_change}%."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/percent_change_initial_price')
def percent_change_initial_price():
    discount_percent = random.randint(10, 25)
    discounted_price = random.randint(800, 1500)
    
    initial_price = discounted_price / (1 - (discount_percent / 100))
    initial_price_rounded = round(initial_price)
    
    problem = f"A Prodigiks laptop is sold for \\${discounted_price} at a reduction of {discount_percent}% on its recommended retail price. What was the computer's initial (recommended retail) price? Round your answer to the nearest dollar."
    answer = f"{initial_price_rounded}"
    explanation = "To find the initial price, divide the discounted price by (1 - (discount_percent / 100)). In this case, $\\frac{\\textrm{" + str(discounted_price) + "}}{1 - \\frac{\\textrm{" + str(discount_percent) + "}}{100}} = " + str(initial_price_rounded) + "$."
    
    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/percent_change_profit')
def percent_change_profit():
    initial_profit = random.randint(100000, 200000)
    final_profit = initial_profit + random.randint(10000, 50000)
    
    percent_change = (final_profit - initial_profit) / initial_profit * 100
    percent_change_rounded = round(percent_change, 2)
    
    problem = f"Company L's profit increased from \\${initial_profit} last year to \\${final_profit} this year. Interpret the change in profit using percents."
    answer = f"{percent_change_rounded}%"
    explanation = f"To find the percent change, use the formula $\\frac{{\\textrm{{new value}} - \\textrm{{old value}}}}{{\\textrm{{old value}}}} \\times 100$. In this case, $\\frac{{ \\${final_profit} - \\${initial_profit}}}{{ \\${initial_profit}}} \\times 100 = {percent_change_rounded}\\%$."
    
    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/slope_population_change')
def slope_population_change():
    initial_population = random.randint(10000, 25000)
    final_population = initial_population + random.randint(1000, 5000)
    initial_year = random.randint(2000, 2010)
    final_year = initial_year + random.randint(4, 10)
    
    population_change = final_population - initial_population
    year_change = final_year - initial_year
    population_change_per_year = population_change / year_change
    population_change_per_year_rounded = round(population_change_per_year, 2)

    problem = f"The population of Big Green, Texas increased from {initial_population} to {final_population} between {initial_year} and {final_year}. Find the change of population per year if we assume the change was constant from {initial_year} to {final_year}."
    answer = f"{population_change_per_year_rounded}"
    explanation = f"The total population change between {initial_year} and {final_year} is {final_population} - {initial_population} = {population_change}. The number of years between {initial_year} and {final_year} is {year_change}. So, the change of population per year is $\\frac{{\\textrm{{population change}}}}{{\\textrm{{year change}}}} = \\frac{{{population_change}}}{{{year_change}}} = {population_change_per_year_rounded}$."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/slope_saving_rate')
def slope_saving_rate():
    initial_saving = random.randint(150, 250)
    months_passed = random.randint(2, 5)
    final_saving = initial_saving + random.randint(25, 100) * months_passed
    
    saving_change = final_saving - initial_saving
    saving_rate = saving_change / months_passed
    saving_rate_rounded = round(saving_rate, 2)

    problem = f"Cole is saving money at a constant rate. Suppose he initially has \\${initial_saving} saved, and after {months_passed} months, he has \\${final_saving} saved. Express the rate at which Cole is saving."
    answer = f"${saving_rate_rounded}"
    explanation = f"The total saving change between the initial and final amounts is \\${final_saving} - \\${initial_saving} = \\${saving_change}. The rate at which Cole is saving is $\\frac{{\\textrm{{saving change}}}}{{\\textrm{{months passed}}}} = \\frac{{{saving_change}}}{{{months_passed}}} = {saving_rate_rounded}$. So, Cole is saving at a rate of\${saving_rate_rounded} per month."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/slope_identify_y_intercept')
def slope_identify_y_intercept():
    initial_blueberries = random.randint(15, 25)
    blueberries_per_pie = round(random.uniform(1, 2), 1)

    problem = f"A pie shop receives a delivery of {initial_blueberries} pounds of blueberries. Each blueberry pie requires {blueberries_per_pie} pounds of blueberries. Identify the y-intercept in this situation."
    answer = f"{initial_blueberries}"
    explanation = f"The y-intercept represents the initial amount of blueberries the pie shop has when it hasn't made any pies yet. In this case, the y-intercept would be {initial_blueberries} pounds of blueberries."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/slope_identify_m_temp_increase')
def slope_identify_m_temp_increase():
    initial_temp = random.randint(55, 65)
    increase_rate = random.randint(2, 4)
    hours_passed = random.randint(3, 6)

    problem = f"When the Jones family returned home from a vacation, the temperature in their house was {initial_temp} degrees. They immediately turned up the heat, which will warm the house by {increase_rate} degrees every hour. This is modeled by the equation:<br><br>T = {increase_rate}h + {initial_temp}<br><br>Where T represents the temperature of the Jones' house and h represents the number of hours since they arrived.<br><br>Find the temperature of the Jones' house {hours_passed} hours after turning up the heat."
    temp_after_hours = increase_rate * hours_passed + initial_temp
    answer = f"{temp_after_hours} degrees"
    explanation = f"To find the temperature of the Jones' house after {hours_passed} hours, we can plug h = {hours_passed} into the equation:<br><br>T = {increase_rate}({hours_passed}) + {initial_temp}<br>T = {temp_after_hours}<br><br>So, the temperature of the Jones' house after {hours_passed} hours will be {temp_after_hours} degrees."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/slope_indentify_m_linear_model')
def slope_indentify_m_linear_model():
    initial_blueberries = random.randint(18, 24)
    blueberries_per_pie = round(random.uniform(1.3, 1.7), 1)

    problem = f"A pie shop receives a delivery of {initial_blueberries} pounds of blueberries. Each blueberry pie requires {blueberries_per_pie} pounds of blueberries. Write a linear model in slope-intercept form to model the amount of blueberries on hand in this situation."

    answer = f"y = -{blueberries_per_pie}x + {initial_blueberries}"
    explanation = f"In this situation, the amount of blueberries on hand (y) decreases by {blueberries_per_pie} pounds for each blueberry pie made (x). The initial amount of blueberries is {initial_blueberries} pounds. So the linear model in slope-intercept form is:<br><br>y = -{blueberries_per_pie}x + {initial_blueberries}"

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/linear_model_doughnuts_cost_model')
def linear_model_doughnuts_cost_model():
    fixed_cost = random.randint(1500, 1700)
    cost_per_100_doughnuts = random.randint(10, 20)
    num_batches = random.randint(1, 10)

    problem = f"The cost of operating Mama’s Doughnuts is \\${fixed_cost} per week of fixed costs plus \${cost_per_100_doughnuts} to make each 100 doughnuts. The owner is calculating the total cost each week as more batches of 100 doughnuts are produced. What is the total cost if {num_batches} batches of 100 doughnuts are produced?"

    answer = f"C({num_batches}) = {cost_per_100_doughnuts * num_batches} + {fixed_cost} = \\${cost_per_100_doughnuts * num_batches + fixed_cost}"
    explanation = f"The total cost of operating Mama's Doughnuts consists of a fixed cost of \\${fixed_cost} per week and a variable cost of \${cost_per_100_doughnuts} per 100 doughnuts. Since the cost per 100 doughnuts is constant, this is a linear model. The equation is:<br><br>C(x) = {cost_per_100_doughnuts}x + {fixed_cost}<br><br>where C(x) represents the total cost and x represents the number of batches of 100 doughnuts produced. To find the total cost for {num_batches} batches of 100 doughnuts, we can plug in the value of x:<br><br>C({num_batches}) = {cost_per_100_doughnuts}({num_batches}) + {fixed_cost} = \\${cost_per_100_doughnuts * num_batches + fixed_cost}"

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)

#=================================================================================

import random

@qr_1a1.route('/non_exponential_functions')
def non_exponential_functions():
    exp_base = random.randint(2, 5)
    exp_exponent = random.randint(2, 5)
    exp_func = f"h(x) = {exp_base}^{{x}}"
    
    power_base = random.randint(2, 5)
    power_exponent = random.randint(2, 5)
    power_func = f"g(x) = x^{{{power_exponent}}}"
    
    neg_base = random.randint(2, 5)
    neg_exp_func = f"j(x) = (-{neg_base})^{{x}}"

    coef_base = random.randint(2, 5)
    coef_exp_func = f"f(x) = {coef_base}(x - 2)"
    
    equations = [exp_func, power_func, neg_exp_func, coef_exp_func]
    random.shuffle(equations)

    problem = "Which of the following equations are NOT exponential functions?<br><br>"
    for eq in equations:
        problem += f"${eq}$<br>"

    answer = f"${power_func}, {neg_exp_func}$"
    explanation = f"Expressions\${power_func}$ and\${neg_exp_func}$ are not exponential functions.<br><br>${power_func}$ does not represent an exponential function because the base is a variable and the exponent is a constant. Exponential functions have to have a variable in the exponent.<br><br>${neg_exp_func}$ also does not represent an exponential function because the base, -{neg_base}, is less than 0, and the base b of an exponential function is always a positive constant."
    
    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/exponential_model_melatonin_decay')
def exponential_model_melatonin_decay():
    initial_amount = 10
    half_life = 30
    problem = f"Melatonin is fast-acting and has a half-life of approximately {half_life} minutes. If you take a {initial_amount} milligram tablet, write an exponential equation to model this after t time periods, where t is the number of {half_life} minute time periods."
    
    answer = "M(t) = 10 * (1/2)^(t)"
    explanation = f"The exponential decay model for melatonin is given by the equation: $M(t) = {initial_amount} * \\left(\\frac{{1}}{{2}}\\right)^{{t}}$, where M(t) is the amount of melatonin remaining in the body after t time periods of {half_life} minutes each."
    
    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/simple_interest')
def simple_interest():
    principal = randint(5000, 15000)
    interest_rate = Decimal(randint(5, 15)) / Decimal(100)
    interest_rate = interest_rate.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    time = randint(3, 15)

    interest = principal * interest_rate * time
    balance = round(principal + interest, 2)
    answer = round(balance, 2)
    problem = f"If you deposit \\${principal} into an account that pays {interest_rate * 100}% simple interest, what will the balance be in {time} years?"
    
    explanation = f"The formula for calculating simple interest is: \\[I = P \\times r \\times t\\]"
    explanation += f"\\[I = {principal} \\times {interest_rate} \\times {time}\\]"
    explanation += f"\\[I = {interest}\\]"

    explanation += f"The balance in the account after {time} years will be the principal plus the interest: \\[B = P + I\\]"
    explanation += f"\\[B = {principal} + {interest}\\]"
    explanation += f"\\[B = {balance}\\]"

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
  #=================================================================================

@qr_1a1.route('/simple_interest_rate')
def simple_interest_rate():
    principal = randint(4000, 10000)
    total_owed = randint(principal + 1000, principal + 5000)
    time = randint(1, 5)

    interest = total_owed - principal
    rate = (interest / (principal * time)) * 100

    problem = f"If you take out a loan for \\${principal} and you will owe \\${total_owed} after {time} years, what is the annual rate of simple interest? Round your answer to the nearest tenth of a percent. Do NOT round until you have calculated your final answer."
    answer = round(rate, 1)
    explanation = f"To find the annual rate of simple interest, we can use the formula $r = \\frac{{I}}{{P \\times t}}$, where $r$ is the interest rate, $I$ is the interest, $P$ is the principal, and $t$ is the time in years. In this case, we have $I = {interest}$, $P = {principal}$, and $t = {time}$. Plugging these values into the formula, we get:"
    explanation += "\n$$r = \\frac{" + str(interest) + "}{" + str(principal) + " \\times " + str(time) + "}$$"
    explanation += f"$$r = \\frac{{{interest}}}{{{principal * time}}}$$"
    explanation += f"$$r = {rate:.3f}$$"
    explanation += f"Rounding the interest rate to the nearest tenth of a percent, we get $r \\approx {answer}\\%$."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@qr_1a1.route('/simple_interest_deposit')
def simple_interest_deposit():
    final_amount = randint(1000, 5000)
    interest_rate = randint(3, 11)
    time_years = randint(3, 11)

    problem = f"Sasha's bank account earns {interest_rate}% simple interest. How much must she deposit in the account today if she wants it to be worth\${final_amount} in {time_years} years? Round your answer to the nearest dollar. Do NOT round until you have calculated your final answer."
    principal = round(final_amount / (1 + interest_rate / 100 * time_years))
    answer = round(principal, 0)
    explanation = f"To find the initial deposit required, we can use the formula for simple interest: $A = P(1 + rt)$, where $A$ is the final amount, $P$ is the principal, $r$ is the interest rate, and $t$ is the time in years. In this case, we have $A = {final_amount}$, $r = {interest_rate / 100}$, and $t = {time_years}$. Solving for $P$, we get:"
    explanation += "\n\n"
    explanation += f"\\[P = \\frac{{A}}{{1 + rt}}\\]"
    explanation += "\n\n"
    explanation += f"Plugging in the values, we have $P = \\frac{{{final_amount}}}{{1 + {interest_rate / 100} \\times {time_years}}}$, which gives us an initial deposit of $P = {principal}$. So Sasha must deposit\${principal} in the account today."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/compound_interest_deposit')
def compound_interest_deposit():
    principal = randint(2000, 5000)
    interest_rate = randint(2, 11)
    time_years = randint(2, 11)

    problem = f"You deposit all of your graduation money,\${principal}, into an account earning {interest_rate}% interest, compounded annually. You want to let it sit, no deposits or withdraws, while you are in college for {time_years} years. How much will you have at the end of {time_years} years? Round to the nearest cent."

    # Explanation
    final_amount = round(principal * (1 + interest_rate / 100) ** time_years, 2)
    answer = round(final_amount, 2)
    explanation = f"To find the final amount in the account, we can use the formula for compound interest: $A = P(1 + r)^t$, where $A$ is the final amount, $P$ is the principal, $r$ is the interest rate, and $t$ is the time in years. In this case, we have $P = {principal}$, $r = {interest_rate / 100}$, and $t = {time_years}$. Plugging these values into the formula, we get:"
    explanation += "\n\n"
    explanation += f"\\[A = {principal}(1 + {interest_rate / 100})^{{{time_years}}}\\]"
    explanation += "\n\n"
    explanation += f"Calculating the final amount, we find that $A = {final_amount}$. So at the end of {time_years} years, you will have\${final_amount:.2f} in the account."

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/compound_interest_random')
def compound_interest_random():
    principal = randint(1000, 5000)
    rate = round(uniform(1, 5), 2)
    time = randint(1, 10)
    n = randint(1, 12)  # Random number of times compounded per year

    amount = principal * (1 + rate / 100 / n) ** (n * time)
    final_amount = round(amount, 2)
    answer = round(final_amount, 2)
    problem = f"A bank features a savings account that has an annual percentage rate of {rate}% with interest compounded {n} times a year. Ashley deposits\${principal} into the account. What is the account balance after {time} years? Round your answer to the nearest cent. Do NOT round until you have calculated the final answer."
    #explanation = f"To find the account balance after {time} years, we can use the compound interest formula: $A = P(1 + \\frac{r}{n})^{nt}$, where A is the final amount, P is the principal, r is the interest rate, n is the number of times the interest is compounded per year, and t is the time in years. In this case, we have P =\${principal}, r = {rate}%, n = {n}, and t = {time}. Plugging these values into the formula, we get:"
    explanation = f"To find the account balance after {time} years, we can use the compound interest formula: $A = P(1 + \\frac{{rate}}{n})^{{nt}}$, where A is the final amount, P is the principal, rate is the interest rate, n is the number of times the interest is compounded per year, and t is the time in years. In this case, we have P =\${principal}, rate = {rate}%, n = {n}, and t = {time}. Plugging these values into the formula, we get:"

    explanation += f"\\[A = {principal}(1 + \\frac{{{rate}\\%}}{{{n}}})^{{{n} \\times {time}}}\\]"
    explanation += f"\\[A = {principal}(1 + \\frac{{{rate / 100}}}{{{n}}})^{{{n} \\times {time}}}\\]"
    explanation += f"\\[A = {principal}(1 + {rate / 100 / n})^{{{n} \\times {time}}}\\]"
    explanation += f"\\[A = {principal} \\times {round(1 + rate / 100 / n, 4)}^{{{n} \\times {time}}}\\]"
    explanation += f"\\[A = {principal} \\times {round(1 + rate / 100 / n, 4)}^{n * time}\\]"
    explanation += f"\\[A = \\${final_amount}\\]"

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/credit_card_interest')
def credit_card_interest():
    charged_amount = randint(500, 2000)
    payment = randint(charged_amount // 4, charged_amount // 2)
    remaining_balance = charged_amount - payment
    apr = randint(10, 25)

    problem = f"Erin charged \\${charged_amount} on the current credit card this billing cycle. Erin pays\${payment} towards the balance by the due date, but is unable to pay the remaining\${remaining_balance}. The balance of\${remaining_balance} carries over to the next billing cycle, but he must pay interest on this amount as well. If the APR is {apr}%, how much interest will be added to the payment for the next billing cycle?"

    # Explanation
    monthly_interest_rate = apr / 100 / 12
    interest = round(remaining_balance * monthly_interest_rate, 2)
    answer = round(interest, 2)
    explanation = f"Since the APR is {apr}%, we need to find the monthly interest rate by dividing the APR by 12: \\[\\frac{{APR}}{{12}} = \\frac{{{apr}\\%}}{{12}} = {monthly_interest_rate * 100}\\%\\]"
    explanation += "\n\n"
    explanation += f"To calculate the interest added to the payment for the next billing cycle, we can multiply the remaining balance by the monthly interest rate: \\[Interest = Remaining \\ Balance \\times Monthly \\ Interest \\ Rate\\]"
    explanation += "\n\n"
    explanation += f"\\[Interest = {remaining_balance} \\times {monthly_interest_rate * 100}\\%\\]"
    explanation += "\n\n"
    explanation += f"\\[Interest = {interest}\\]"

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================



@qr_1a1.route('/credit_card_table')
def credit_card_table():
    carryover_balance = randint(500, 2000)
    apr = round(randint(1000, 2500) / 100, 2)
    min_payment_rate = round(randint(200, 1000) / 10000, 4)
    num_months = 3

    problem = f"Mo has a \\${carryover_balance} carryover balance on a credit card that has a {apr}% annual percentage rate. The minimum payment required each month is {min_payment_rate * 100}% of the unpaid balance. Mo makes only the minimum payment each month and makes no new purchases for the first few months. Complete the table for the first {num_months} months."
    problem = f"Mo has a \\${carryover_balance} carryover balance on a credit card that has a {apr}% annual percentage rate. The minimum payment required each month is {min_payment_rate * 100}% of the unpaid balance. Mo makes only the minimum payment each month and makes no new purchases for the first few months. Complete the table for the first {num_months} months."
    problem = f"Mo has a \\${carryover_balance} carryover balance on a credit card that has a {apr}% annual percentage rate. The minimum payment required each month is {min_payment_rate * 100}% of the unpaid balance. Mo makes only the minimum payment each month and makes no new purchases for the first few months. Complete the table for the first {num_months} months."

    results = calculate_credit_card_payments(carryover_balance, apr, min_payment_rate, num_months)

    answer = "<table><tr><th>Month</th><th>Carryover Balance</th><th>Finance Charge</th><th>Ending Balance</th><th>Minimum Payment</th></tr>"
    for result in results:
        answer += f"<tr><td>{result['month']}</td><td>${result['carryover_balance']:.2f}</td><td>${result['finance_charge']:.2f}</td><td>${result['ending_balance']:.2f}</td><td>${result['min_payment']:.2f}</td></tr>"
    answer += "</table>"

    explanation = "<table><tr><th>Month</th><th>Carryover Balance</th><th>Finance Charge</th><th>Ending Balance</th><th>Minimum Payment</th></tr>"
    for result in results:
        explanation += f"<tr><td>{result['month']}</td><td>${result['carryover_balance']:.2f}</td><td>${result['finance_charge']:.2f}</td><td>${result['ending_balance']:.2f}</td><td>${result['min_payment']:.2f}</td></tr>"
    explanation += "</table>"

    return render_template("problem.html", problem=problem, answer=answer, explanation=explanation)
#=================================================================================

def calculate_credit_card_payments(carryover_balance, apr, min_payment_rate, num_months):
    results = []
    for month in range(1, num_months + 1):
        finance_charge = round(carryover_balance * (apr / 100) / 12, 2)
        ending_balance = round(carryover_balance + finance_charge, 2)
        min_payment = round(ending_balance * min_payment_rate, 2)
        carryover_balance = round(ending_balance - min_payment, 2)

        results.append({
            'month': month,
            'carryover_balance': carryover_balance,
            'finance_charge': finance_charge,
            'ending_balance': ending_balance,
            'min_payment': min_payment
        })

    return results
#=================================================================================

import random
from math import pow

@qr_1a1.route('/total_interest_paid')
def total_interest_paid():
    loan_amount = random.randint(100000, 200000)
    interest_rate = round(random.uniform(3.5, 6.5), 1)
    loan_term = random.randint(15, 40)

    # Calculate the monthly payment using the mortgage formula
    monthly_interest_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    factor = (1 + monthly_interest_rate) ** num_payments
    monthly_payment = loan_amount * (monthly_interest_rate * factor) / (factor - 1)

    total_amount_paid = monthly_payment * num_payments
    interest_paid = total_amount_paid - loan_amount

    problem = f"Hailie is buying a house and has asked the bank for a \\${loan_amount} mortgage. The bank offers her {interest_rate}% interest for {loan_term} years. If Hailie only makes the minimum payment each month, how much will she pay back over the life of the loan? How much of that is interest? Round to the nearest cent."

    answer = f"Hailie will pay back a total of \\${total_amount_paid:,.2f} over the life of the loan. The interest paid is \\${interest_paid:,.2f}."

    explanation = "To calculate the monthly payment, we use the mortgage formula:<br>"
    explanation += "Monthly payment $= P\\frac{r(1+r)^n}{(1+r)^n-1}$<br>"
    explanation += f"Where $P = \\${loan_amount}$, $r = {monthly_interest_rate:.5f}$ (monthly interest rate), and $n = {num_payments}$ (number of payments).<br>"
    explanation += f"Monthly payment $= \\${loan_amount} \\times \\frac{{ {monthly_interest_rate:.5f} }}(1 + {monthly_interest_rate:.5f})^{{ {num_payments} }}{{(1 + {monthly_interest_rate:.5f})^{{ {num_payments} }} - 1}} = \\${monthly_payment:.2f}$<br><br>"
    explanation += "To calculate the total amount paid back over the life of the loan, we multiply the monthly payment by the total number of payments:<br>"
    explanation += f"Total amount paid $= \\textrm{{Monthly payment}} \\times \\textrm{{Number of payments}} = \\${monthly_payment:.2f} \\times {num_payments} = \\${total_amount_paid:,.2f}$<br><br>"
    explanation += "To calculate the interest paid, we subtract the loan amount from the total amount paid:<br>"
    explanation += f"Interest paid $= \\textrm{{Total amount paid}} - \\textrm{{Loan amount}} = \\${total_amount_paid:,.2f} - \\${loan_amount} = \\${interest_paid:,.2f}$<br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@qr_1a1.route('/compare_mortgages')
def compare_mortgages():
    loan_amount = random.randint(50000, 150000)
    term_A = random.randint(10, 20)
    interest_rate_A = round(random.uniform(3.5, 5.5), 1)
    
    term_B = random.randint(25, 35)
    interest_rate_B = round(random.uniform(3, 5), 1)

    r_A = interest_rate_A / 100 / 12
    num_payments_A = term_A * 12
    monthly_payment_A = loan_amount * r_A * (1 + r_A) ** num_payments_A / ((1 + r_A) ** num_payments_A - 1)

    r_B = interest_rate_B / 100 / 12
    num_payments_B = term_B * 12
    monthly_payment_B = loan_amount * r_B * (1 + r_B) ** num_payments_B / ((1 + r_B) ** num_payments_B - 1)

    total_payback_A = monthly_payment_A * num_payments_A
    total_payback_B = monthly_payment_B * num_payments_B

    problem = f"Stephen is comparing two mortgage options for his \\${loan_amount:,} mortgage.<br><br>"
    problem += f"Mortgage A: {term_A} years at {interest_rate_A}% with monthly payments of \\${monthly_payment_A:.2f}<br>"
    problem += f"Mortgage B: {term_B} years at {interest_rate_B}% with monthly payments of \\${monthly_payment_B:.2f}<br><br>"
    problem += "How much is the total payback for each mortgage option?"

    answer = f"The total payback for Mortgage A is \\${total_payback_A:,.2f}, and the total payback for Mortgage B is \\${total_payback_B:,.2f}."

    explanation = f"To calculate the total payback for each mortgage option, we multiply the monthly payment by the total number of payments:<br>"
    explanation += f"<ul><li>Mortgage A: \\${monthly_payment_A:.2f} x {num_payments_A} = \\${total_payback_A:,.2f}</li>"
    explanation += f"<li>Mortgage B: \\${monthly_payment_B:.2f} x {num_payments_B} = \\${total_payback_B:,.2f}</li></ul>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)

#=================================================================================

@qr_1a1.route('/first_payment_balance_reduction')
def first_payment_balance_reduction():
    loan_amount = random.randint(80000, 150000)
    loan_term = random.randint(10, 20)
    interest_rate = round(random.uniform(3.5, 5.5), 1)

    monthly_interest_rate = interest_rate / 100 / 12
    total_payments = loan_term * 12

    # Calculate the correct monthly payment
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**total_payments) / ((1 + monthly_interest_rate)**total_payments - 1)

    interest_paid_month_1 = loan_amount * monthly_interest_rate
    principal_paid_month_1 = monthly_payment - interest_paid_month_1

    problem = f"Gabe and Eugenia bought a house! Their loan is for \\${loan_amount:,}, for {loan_term} years at an annual interest rate of {interest_rate}%. This results in a monthly payment of \\${monthly_payment:.2f}.<br><br>"
    problem += "If only the minimum payment is made in month one, how much of the first payment goes toward reducing their balance?<br><br>"
    problem += "First, let's find the amount of interest they paid in month 1.<br>"
    problem += "Then, find the amount toward reducing the balance.<br><br>"
    problem += "Round to the nearest cent."

    answer = f"In the first month, they paid \\${interest_paid_month_1:,.2f} in interest and reduced the balance by \\${principal_paid_month_1:,.2f}."

    explanation = f"To find the amount of interest paid in month 1, we use the formula:<br>"
    explanation += f"Interest paid $= \\textrm{{Loan amount}} \\times \\textrm{{Monthly interest rate}} = \\${loan_amount} \\times {monthly_interest_rate:.5f} = \\${interest_paid_month_1:,.2f}$<br><br>"
    explanation += f"To find the amount toward reducing the balance, we subtract the interest paid from the total monthly payment:<br>"
    explanation += f"Balance reduction $= \\textrm{{Monthly payment}} - \\textrm{{Interest paid}} = \\${monthly_payment:.2f} - \\${interest_paid_month_1:,.2f} = \\${principal_paid_month_1:,.2f}$"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/monthly_payment')
def monthly_payment():
    principal = random.randint(100000, 500000)  # Mortgage amount (dollars)
    annual_interest_rate = random.uniform(3, 10)  # Annual interest rate (percent)
    years = random.randint(15, 30)  # Loan term (years)

    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = years * 12

    monthly_payment_amount = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**num_payments) / ((1 + monthly_interest_rate)**num_payments - 1)

    # Calculate interest paid in the first month
    interest_paid = principal * monthly_interest_rate

    # Calculate the amount toward reducing the balance
    balance_reduction = monthly_payment_amount - interest_paid

    problem = f"Beth and Bryce sign on a \\${principal:,.2f} mortgage at a {annual_interest_rate:.2f}% annual interest rate for {years} years. This results in a monthly payment of \\${monthly_payment_amount:.2f}<br><br>"
    problem += "If only the minimum payment is made in month one, how much of the first payment goes toward reducing her balance?<br><br>"
    problem += "First, let's find the amount of interest she paid in month 1.<br><br>"
    problem += "Round to the nearest cent.<br><br>"
    problem += "Do this in your Excel sheet / Libre Calc / Google Sheets that you created with the formulas."

    answer = f"Monthly payment: \\${monthly_payment_amount:.2f}, Interest paid in the first month: \\${interest_paid:.2f}, Amount toward reducing the balance in the first month: \\${balance_reduction:.2f}"
    explanation = f"The monthly payment is calculated using the mortgage amount, interest rate, and loan term. In this case, the monthly payment is \\${monthly_payment_amount:.2f}. The interest paid in the first month is calculated as the mortgage amount times the monthly interest rate, which is \\${interest_paid:.2f}. Finally, the amount toward reducing the balance is the difference between the monthly payment and the interest paid, which is \\${balance_reduction:.2f}."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/mortgage_payment_table')
def mortgage_payment_table():
    cost = random.randint(250000, 400000)
    length_of_loan = random.randint(5, 30)
    loan_amount_percentage = random.uniform(0.2, 0.5)
    num_payments_per_year = 12
    annual_interest_rate = random.uniform(4, 9)

    loan_amount = cost * loan_amount_percentage
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = length_of_loan * num_payments_per_year

    monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)

    problem = f"What is the monthly payment for this mortgage, as shown in the table below? Round to the nearest cent.<br><br><table><tr><th>Cost</th><td>\\${cost:,.2f}</td></tr><tr><th>Length of loan</th><td>{length_of_loan} years</td></tr><tr><th>Loan Amount</th><td>{loan_amount_percentage * 100:.2f}% LTV (Loan-to-Value)</td></tr><tr><th>Number of payments per year</th><td>{num_payments_per_year}</td></tr><tr><th>Interest rate</th><td>{annual_interest_rate:.2f}% annually</td></tr></table>"
    problem += "<br><br>"
    problem += "Do this in your Excel sheet / Libre Calc / Google Sheets that you created with the formulas.<br><br>"

    answer = f"The monthly payment for this mortgage is \\${monthly_payment:.2f}."
    explanation = f"The mortgage amount is {loan_amount_percentage * 100:.2f}% of the cost, or \\${loan_amount:,.2f}. To find the monthly payment, we use the loan amount, interest rate, and loan term. In this case, the monthly payment is \\${monthly_payment:.2f}."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/liters_in_quarts')
def liters_in_quarts():
    quarts = random.randint(1, 10)
    liters_per_quart = 0.95

    liters = quarts * liters_per_quart

    problem = f"How many liters are in {quarts} quarts of milk? Round to the nearest tenth if needed. 1 quart = 0.95 liters."
    
    answer = f"There are {liters:.1f} liters in {quarts} quarts of milk."

    explanation = f"To convert quarts to liters, we can use the conversion factor 1 quart = 0.95 liters.<br><br>"
    explanation += f"{quarts} quarts = {quarts} × 0.95 liters = {liters:.1f} liters<br><br>"
    explanation += "Conversion Factors Between U.S. and Metric Systems:<br>"
    explanation += "<table>"
    explanation += "<tr><th>Length</th><th>Mass</th><th>Capacity</th></tr>"
    explanation += "<tr><td>1 yd. = 0.914 m</td><td>1 kg = 2.2 lb.</td><td>1 L = 1.06 qt.</td></tr>"
    explanation += "</table>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/kilometers_to_miles')
def kilometers_to_miles():
    kilometers = random.randint(1000, 8000)
    miles_per_kilometer = 1 / 1.61

    miles = kilometers * miles_per_kilometer

    problem = f"The flight distance from New York City to London is {kilometers} kilometers. Convert the distance to miles and round to the nearest mile. 1 mile = 1.61 kilometers."
    
    answer = f"The distance is approximately {round(miles)} miles."

    explanation = f"To convert kilometers to miles, we can use the conversion factor 1 mile = 1.61 kilometers.<br><br>"
    explanation += f"{kilometers} kilometers = {kilometers} × {miles_per_kilometer:.2f} miles = {miles:.2f} miles ≈ {round(miles)} miles<br><br>"
    explanation += "Conversion Factors Between U.S. and Metric Systems:<br>"
    explanation += "<table>"
    explanation += "<tr><th>Length</th><th>Mass</th><th>Capacity</th></tr>"
    explanation += "<tr><td>1 mi. = 1.61 km</td><td></td><td></td></tr>"
    explanation += "<tr><td>1 m = 3.28 ft.</td><td></td><td></td></tr>"
    explanation += "</table>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/fahrenheit_to_celsius')
def fahrenheit_to_celsius():
    fahrenheit = random.randint(-459, 500)

    celsius = (fahrenheit - 32) * (5 / 9)

    problem = f"Convert the Fahrenheit temperature to degrees Celsius: {fahrenheit}° Fahrenheit."

    answer = f"The temperature is approximately {celsius:.1f}° Celsius."

    explanation = f"To convert Fahrenheit to Celsius, we can use the formula:<br>"
    explanation += "$C = \\frac{5}{9} \\times (F - 32)$<br><br>"
    explanation += f"Where $C$ is the temperature in Celsius and $F$ is the temperature in Fahrenheit.<br><br>"
    explanation += f"In this case, $F = {fahrenheit}°$ Fahrenheit.<br>"
    explanation += f"$C = \\frac{5}{9} \\times ({fahrenheit} - 32) = {celsius:.1f}°$ Celsius"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/pounds_to_kilograms')
def pounds_to_kilograms():
    pounds = random.randint(80000, 100000)

    kilograms = pounds / 2.2
    rounded_kilograms = round(kilograms, -2)

    problem = f"An average American will throw away {pounds} lb of trash over their lifetime. Convert this weight to kilograms. Round to the nearest hundred.<br><br>"
    problem += "Recall that 1kg = 2.2lb.<br><br>"
    problem += "Round to one decimal place."

    answer = f"The weight in kilograms is approximately {rounded_kilograms} kg."

    explanation = f"To convert pounds to kilograms, we can use the formula:<br>"
    explanation += "$\\textrm{Kilograms} = \\frac{\\textrm{Pounds}}{2.2}$<br><br>"
    explanation += f"In this case, Pounds = {pounds}lb.<br>"
    explanation += "Kilograms = $\\frac{" + str(pounds) + "}{2.2} = " + f"{kilograms:.1f} \\textrm{{ kg}}$<br>"
    explanation += f"Rounded to the nearest hundred, the weight in kilograms is {rounded_kilograms} kg."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/meters_to_feet')
def meters_to_feet():
    meters = round(random.uniform(1.5, 2.0), 1)

    centimeters = meters * 100
    inches = centimeters / 2.54
    feet = inches / 12
    rounded_feet = round(feet, 1)

    problem = f"Kathryn is {meters}m tall. Convert the height to feet. Round to the nearest tenth.<br><br>"
    problem += "Recall that 1ft = 12in, 1in = 2.54cm, and 1m = 100cm."

    answer = f"Kathryn's height in feet is approximately {rounded_feet} ft."

    explanation = f"To convert meters to feet, we first convert meters to centimeters, then to inches, and finally to feet:<br>"
    explanation += f"{meters} m = {centimeters} cm = {inches:.2f} in = {rounded_feet} ft<br><br>"
    explanation += "Relevant conversions:<br>"
    explanation += "<table>"
    explanation += "<tr><td>1 ft</td><td>=</td><td>12 in</td></tr>"
    explanation += "<tr><td>1 in</td><td>=</td><td>2.54 cm</td></tr>"
    explanation += "<tr><td>1 m</td><td>=</td><td>100 cm</td></tr>"
    explanation += "</table>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/thermometer_temp_conversion')
def thermometer_temp_conversion():
    fahrenheit = random.randint(50, 100)
    celsius = (fahrenheit - 32) * 5 / 9
    rounded_celsius = round(celsius, 1)

    problem = f"A digital food thermometer is capable of showing both °F to one decimal place in the middle of the screen, and °C to one decimal place in a smaller print at the top right corner of the screen.<br><br>"
    problem += f"If the middle of the screen shows {fahrenheit}°F, what is being displayed at the top right corner of the screen?"

    answer = f"At the top right corner of the screen, it displays {rounded_celsius}°C."

    explanation = f"To convert Fahrenheit to Celsius, we can use the formula:<br>"
    explanation += "$\\textrm{Celsius} = (\\frac{5}{9}) \\times (\\textrm{Fahrenheit} - 32)$<br><br>"
    explanation += f"$C = \\frac{5}{9} \\times ({fahrenheit} - 32) = {celsius:.1f}°$ Celsius"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/celsius_to_fahrenheit')
def celsius_to_fahrenheit():
    celsius = random.randint(-200, 200)
    fahrenheit = celsius * 9 / 5 + 32
    rounded_fahrenheit = round(fahrenheit, 1)

    problem = f"Convert {celsius}°C to F.<br><br>"
    problem += "Round to one decimal place."

    answer = f"The answer is {rounded_fahrenheit}°F."

    explanation = f"To convert Celsius to Fahrenheit, we can use the formula:<br>"
    explanation += "$\\textrm{Fahrenheit} = ((\\frac{9}{5}) \\times \\textrm{Celsius}) + 32$<br><br>"
    explanation += f"$F = \\frac{9}{5} \\times {celsius} + 32 = {rounded_fahrenheit}°F$"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@qr_1a1.route('/kilograms_to_pounds')
def kilograms_to_pounds():
    kilograms = random.randint(50, 120)
    pounds = kilograms * 2.2
    rounded_pounds = round(pounds)

    problem = f"How many pounds are in {kilograms} kilograms? Round your answer to the nearest whole number. Note: There are 2.2lbs in a kg."

    answer = f"There are approximately {rounded_pounds} pounds in {kilograms} kilograms."

    explanation = f"To convert kilograms to pounds, we can use the formula:<br>"
    explanation += "$\\textrm{Pounds} = \\textrm{Kilograms} \\times 2.2$<br><br>"
    explanation += f"In this case, $Kilograms = {kilograms} kg$.<br>"
    explanation += f"Pounds = ${kilograms} \\times 2.2 = {pounds:.1f} \\textrm{{ lb}}$<br>"

    explanation += f"Rounded to the nearest whole number, there are {rounded_pounds} pounds in {kilograms} kilograms."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random

@qr_1a1.route('/miles_to_kilometers')
def miles_to_kilometers():
    miles = random.randint(30, 100)
    kilometers = miles * 1.609
    rounded_kilometers = round(kilometers, 1)

    problem = f"How many kilometers are in {miles} miles? Note: There are 1.609kms in 1mi."

    answer = f"There are approximately {rounded_kilometers} kilometers in {miles} miles."

    explanation = f"To convert miles to kilometers, we can use the formula:<br>"
    explanation += "$\\textrm{Kilometers} = \\textrm{Miles} \\times 1.609$<br><br>"
    explanation += f"In this case, Miles = {miles} mi.<br>"
    explanation += f"Kilometers = ${miles} \\times 1.609 = {kilometers:.1f} \\textrm{{ km}}$<br>"

    explanation += f"Rounded to one decimal place, there are {rounded_kilometers} kilometers in {miles} miles."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/currency_weight_conversion')
def currency_weight_conversion():
    cost_per_kg_gbp = round(random.uniform(1, 3), 2)
    gbp_to_usd = 1 / 0.77  # Conversion rate from GBP to USD
    cost_per_kg_usd = cost_per_kg_gbp * gbp_to_usd
    cost_per_lb_usd = cost_per_kg_usd / 2.2
    rounded_cost_per_lb_usd = round(cost_per_lb_usd, 2)

    problem = f"While shopping in England, Sally notices the cost of bananas is £{cost_per_kg_gbp}/kg. Sally isn't familiar with Great Britain Pounds (GBP) or kilograms, and needs to convert the unit price into dollars per pound. You may assume the conversion rate from dollars to GBP is $1 to £0.77, and there are 2.2lbs to 1kg. Round your answer to the nearest cent."

    answer = f"The cost of bananas in dollars per pound is approximately ${rounded_cost_per_lb_usd}."

    explanation = f"To find the cost in dollars per pound, we need to convert the price from GBP to USD and from kilograms to pounds:<br>"
    explanation += "1. Convert the price from GBP to USD:<br>"
    explanation += "$\\textrm{Cost per kg (USD)} = \\textrm{Cost per kg (GBP)} \\times \\textrm{Conversion rate}$<br>"
    explanation += f"Cost per kg (USD) = £${cost_per_kg_gbp:.2f} \\times ${gbp_to_usd:.2f} = ${cost_per_kg_usd:.2f}$<br><br>"
    explanation += "2. Convert the price from kilograms to pounds:<br>"
    explanation += "$\\textrm{Cost per lb (USD)} = \\frac{\\textrm{Cost per kg (USD)}}{2.2}$<br>"
    explanation += f"Cost per lb (USD) = $\\frac{{${cost_per_kg_usd:.2f}}}{{2.2}} = ${rounded_cost_per_lb_usd}<br><br>"
    
    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/road_trip_cost')
def road_trip_cost():
    distance_miles = random.randint(450, 700)
    miles_per_gallon = random.randint(15, 25)
    cost_per_liter = round(random.uniform(0.8, 1.2), 2)
    liters_per_gallon = 3.79

    total_gallons = distance_miles / miles_per_gallon
    total_liters = total_gallons * liters_per_gallon
    total_cost = total_liters * cost_per_liter
    rounded_total_cost = round(total_cost, 2)

    problem = f"Carly wants to fly to Canada and then drive {distance_miles} miles to visit a relative using a rental truck that gets {miles_per_gallon} miles per gallon. If gas costs ${cost_per_liter} per liter, how much will the road trip cost? There are {liters_per_gallon} liters in 1 gallon. Round your answer to the nearest cent."

    answer = f"The road trip will cost approximately ${rounded_total_cost}."

    explanation = f"<br>To find the cost of the road trip, we need to determine the total number of gallons of gas required, convert that to liters, and then multiply by the cost per liter:<br><br>"
    explanation += "1. Calculate the total number of gallons of gas required:<br>"
    explanation += \
      (
        "$\\textrm{Total gallons} = \\frac{\\textrm{Distance}}{\\textrm{Miles per gallon}} = "
        f"\\frac{{{distance_miles}}}{{{miles_per_gallon}}} = {total_gallons:.2f}$<br>"
      ) 
    
    explanation += "<br>"
    explanation += "2. Convert the total gallons to liters:<br>"
    explanation += f"Total liters = $\\textrm{{Total gallons}} \\times \\textrm{{Liters per gallon}} = {total_gallons:.2f} \\times ${liters_per_gallon} = {total_liters:.2f} Liters<br><br>"
    
    explanation += "3. Calculate the total cost of the road trip:<br>"
    explanation += f"Total cost = $\\textrm{{Total liters}} \\times \\textrm{{Cost per liter}} = {total_liters:.2f} \\times ${cost_per_liter:.2f} = \\${total_cost:.2f} <br><br>"
    explanation += f"Rounded to the nearest cent, the road trip will cost approximately ${rounded_total_cost}.<br><br>"
    
    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

def convert_area_sq_inches_to_sq_feet(area_sq_inches):
    conversion_factor = 144  # There are 144 square inches in a square foot
    area_sq_feet = area_sq_inches / conversion_factor
    return round(area_sq_feet, 2)

@qr_1a1.route('/area_conversion')
def area_conversion():
    area_sq_inches = random.randint(400, 700)

    area_sq_feet = convert_area_sq_inches_to_sq_feet(area_sq_inches)

    problem = f"Convert {area_sq_inches} square inches to square feet. Round your answer to the nearest hundredth."

    answer = f"The area is approximately {area_sq_feet} square feet."

    explanation = f"To convert the area from square inches to square feet, we need to know the conversion factor between the two units. There are 144 square inches in 1 square foot.<br><br>"
    explanation += "Here's the relevant conversion table:<br>"
    explanation += "<table><tr><th>Unit</th><th>Conversion factor</th></tr>"
    explanation += "<tr><td>1 square foot</td><td>12 inches x 12 inches = 144 square inches</td></tr></table><br><br>"
    explanation += "Now, let's calculate the conversion:<br>"
    explanation += "$\\textrm{Area (sq ft)     } = \\frac{\\textrm{Area (sq in)}} {Conversion factor}$<br>"
    explanation +=  f"Area (sq ft) = $\\frac{{{area_sq_inches}}} {{144}} \\textrm{{ sq in}} $<br>"
    explanation += f"Area (sq ft) ≈ {area_sq_feet}<br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

def convert_area_sq_km_to_sq_miles(area_sq_km):
    conversion_factor = 0.386102  # There are 0.386102 square miles in a square kilometer
    area_sq_miles = area_sq_km * conversion_factor
    return round(area_sq_miles, 2)

@qr_1a1.route('/area_conversion_km_to_miles')
def area_conversion_km_to_miles():
    area_sq_km = random.randint(40, 125)

    area_sq_miles = convert_area_sq_km_to_sq_miles(area_sq_km)

    problem = f"Convert {area_sq_km} square kilometers to square miles.<br> There are 0.386102 square miles in 1 square kilometer."

    answer = f"The area is approximately {area_sq_miles} square miles."

    explanation = f"To convert the area from square kilometers to square miles, we need to know the conversion factor between the two units. There are 0.386102 square miles in 1 square kilometer.<br><br>"
    explanation += "Here's the relevant conversion table:<br>"
    explanation += "<table><tr><th>Unit</th><th>Conversion factor</th></tr>"
    explanation += "<tr><td>1 square kilometer</td><td>0.386102 square miles</td></tr></table><br><br>"
    explanation += "Now, let's calculate the conversion:<br>"
    explanation += "Area (sq mi) = Area (sq km) × Conversion factor<br><br>"
    explanation += f"$ \\frac{{({area_sq_km} \\textrm{{ sq km}} \\times 0.386102 \\textrm{{ sq mi}})}}{{1 \\textrm{{ sq km}}}} $<br><br>"
    explanation += f"Area (sq mi) ≈ {area_sq_miles}<br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/medication_dosage')
def medication_dosage():
    weight_lb = random.randint(90, 270)
    dosage_mg_per_kg = random.randint(20, 120)
    doses_per_day = random.randint(1, 3)
    lb_to_kg = 0.453592

    weight_kg = weight_lb * lb_to_kg
    total_daily_dosage_mg = weight_kg * dosage_mg_per_kg
    dosage_per_dose_mg = total_daily_dosage_mg / doses_per_day
    rounded_dosage_per_dose = round(dosage_per_dose_mg)

    problem = f"A patient weighs {weight_lb} lb and is prescribed medication with dosage instructions of {dosage_mg_per_kg} mg/kg/day. The medication is to be given {doses_per_day} times per day in equal dosages. How much should the patient receive per dose?"

    answer = f"The patient should receive {rounded_dosage_per_dose} mg per dose."

    explanation = f"<br>To find the dosage per dose, we need to:<br><br>"
    explanation += "1. Convert the patient's weight to kilograms:<br>"
    explanation += f"$ {weight_lb} \\textrm{{ lb}} \\times {lb_to_kg} \\textrm{{ kg/lb}} = {weight_kg:.2f} \\textrm{{ kg}} $<br><br>"
   
    explanation += "2. Calculate the total daily dosage in milligrams:<br>"
    explanation += f"$ {weight_kg:.2f} \\textrm{{ kg}} \\times {dosage_mg_per_kg} \\textrm{{ mg/kg}} = {total_daily_dosage_mg:.2f} \\textrm{{ mg}} $<br><br>"

    explanation += "3. Divide the total daily dosage by the number of doses per day:<br>"
    explanation += f"$ \\frac{{{total_daily_dosage_mg:.2f} \\textrm{{ mg}}}}{{{doses_per_day}}} = {dosage_per_dose_mg:.2f} \\textrm{{ mg}} $<br><br>"

    explanation += f"Rounded to the nearest milligram, the patient should receive {rounded_dosage_per_dose} mg per dose.<br><br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/medication_volume')
def medication_volume():
    ordered_medication_g = random.randint(3, 15)
    concentration_mg_per_ml = random.randint(12, 45)
    g_to_mg = 1000

    ordered_medication_mg = ordered_medication_g * g_to_mg
    volume_to_be_given_ml = ordered_medication_mg / concentration_mg_per_ml
    rounded_volume_ml = round(volume_to_be_given_ml)

    problem = f"A doctor orders {ordered_medication_g} g of medication to be given. The medication has a concentration of {concentration_mg_per_ml} mg/mL. How many mL should be given to the patient? Round to the nearest whole number."

    answer = f"The patient should receive {rounded_volume_ml} mL of the medication."

    explanation = f"<br>Conversion table:<br>"
    explanation += "<table><tr><td>1 g</td><td>=</td><td>1000 mg</td></tr></table><br><br>"

    explanation += "To find the volume of medication to be given, we need to:<br><br>"
    explanation += "1. Convert the ordered medication amount to milligrams:<br>"
    explanation += f"$ {ordered_medication_g} \\textrm{{ g}} \\times {g_to_mg} \\textrm{{ mg/g}} = {ordered_medication_mg} \\textrm{{ mg}} $<br><br>"

    explanation += "2. Calculate the volume to be given in milliliters:<br>"
    explanation += f"$ \\frac{{{ordered_medication_mg} \\textrm{{ mg}}}}{{{concentration_mg_per_ml} \\textrm{{ mg/mL}}}} = {volume_to_be_given_ml:.2f} \\textrm{{ mL}} $<br><br>"

    explanation += f"Rounded to the nearest whole number, the patient should receive {rounded_volume_ml} mL of the medication.<br><br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/rectangle_area')
def rectangle_area():
    length = random.randint(60, 180)
    width = random.randint(20, 60)
    area = length * width

    rect_width = 180 * (length / (length + width))
    rect_height = 80 * (width / (length + width))

    svg_string = f'''
<svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="{{rect_width}}" height="{{rect_height}}" stroke="black" fill="transparent" stroke-width="2"/>
  <text x="95" y="55" font-size="14" text-anchor="middle">Length: {{length_text}}m</text>
  <text x="95" y="75" font-size="14" text-anchor="middle">Width: {{width_text}}m</text>
</svg>
'''

    problem = f"The length of a rectangle is {length} meters and the width is {width} meters. Find the area. Give your answer without units.<br><br>"
    problem += svg_string.format(rect_width=rect_width, rect_height=rect_height, length_text=length, width_text=width)

    answer = f"The area of the rectangle is {area}."

    explanation = f"<br>To find the area of a rectangle, use the formula:<br>"
    explanation += "$\\textrm{Area} = \\textrm{Length} \\times \\textrm{Width}$<br><br>"
    explanation += f"In this case, the length is {length} meters and the width is {width} meters:<br>"
    explanation += f"$\\textrm{{Area}} = {length} \\times {width} = {area}$<br><br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/rectangle_width')
def rectangle_width():
    length = random.randint(60, 180)
    width = random.randint(20, 60)
    area = length * width

    problem = f"The area of a rectangle is {area} square meters. The length is {length} meters. What is the width? Give your answer without units."

    answer = f"The width of the rectangle is {width} meters."

    explanation = f"<br>To find the width of a rectangle, rearrange the formula for the area of a rectangle:<br>"
    explanation += "$\\textrm{Width} = \\frac{\\textrm{Area}}{\\textrm{Length}}$<br><br>"
    explanation += f"In this case, the area is {area} square meters and the length is {length} meters:<br>"
    explanation += f"$\\textrm{{Width}} = \\frac{{{area}}}{{{length}}} = {width}$<br><br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/circle_area_radius')
def circle_area_radius():
    radius = random.randint(10, 25)

    problem = f"Find the area of a circle with a radius of {radius} inches. Give an exact answer."

    answer = f"$\\textrm{{Area}} = \\pi \\times ({radius})^2 = {radius ** 2} \\pi$ square inches<br>"
    answer += f"The area of the circle is {radius ** 2 * pi:.2f} square inches.<br>"
    
    explanation = f"<br>To find the area of a circle, use the formula:<br>"
    explanation += "$\\textrm{Area} = \\pi \\times \\textrm{Radius}^2$<br><br>"
    explanation += f"In this case, the radius is {radius} inches:<br>"
    explanation += f"$\\textrm{{Area}} = \\pi \\times ({radius})^2 = {radius ** 2} \\pi$ square inches<br><br>"
    explanation += f"As a decimal approximation, the area is {radius ** 2 * pi:.2f} square inches.<br><br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/circle_area_diameter')
def circle_area_diameter():
    diameter = random.randint(5, 15)
    radius = diameter / 2
    pi_approx = 3.14
    area = pi_approx * radius ** 2

    problem = f"Find the area of a circle with a diameter of {diameter} inches. Use 3.14 for pi."

    answer = f"The area of the circle is {area:.2f} square inches."

    explanation = f"<br>To find the area of a circle, use the formula:<br>"
    explanation += "$\\textrm{Area} = \\pi \\times \\textrm{Radius}^2$<br><br>"
    explanation += f"In this case, the diameter is {diameter} inches, so the radius is {radius} inches:<br>"
    explanation += f"$\\textrm{{Area}} = 3.14 \\times ({radius})^2 = {area:.2f}$ square inches<br><br>"

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_1a1.route('/cylinder_volume')
def cylinder_volume():
    diameter = random.randint(20, 60)
    height = random.randint(20, 60)
    radius = diameter / 2
    volume = math.pi * radius ** 2 * height

    cylinder_svg = f'''
    <svg width="200" height="150" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="100" cy="25" rx="50" ry="25" stroke="black" fill="transparent" stroke-width="2"/>
        <ellipse cx="100" cy="125" rx="50" ry="25" stroke="black" fill="transparent" stroke-width="2"/>
        <line x1="50" y1="25" x2="50" y2="125" stroke="black" stroke-width="2"/>
        <line x1="150" y1="25" x2="150" y2="125" stroke="black" stroke-width="2"/>
        <text x="100" y="80" font-size="14" text-anchor="middle">Diameter: {diameter}"</text>
        <text x="100" y="100" font-size="14" text-anchor="middle">Height: {height}"</text>
    </svg>
    '''

    problem = (
        f"Find the volume of the cylinder shown with a diameter of {diameter} inches and a height of {height} inches. "
        "Give the answer in terms of π, and do not include units with your answer.<br>"
    )

    problem += cylinder_svg

    answer = f"The volume of the cylinder is {volume:.2f}π cubic inches."

    explanation = f"<br>To find the volume of a cylinder, use the formula:<br>"
    explanation += "$\\textrm{Volume} = \\pi \\times \\textrm{Radius}^2 \\times \\textrm{Height}$<br><br>"
    explanation += (
        f"In this case, the diameter is {diameter} inches, so the radius is {radius} inches, and the height is {height} inches:<br>"
    )
    explanation += f"$\\textrm{{Volume}} = \\pi \\times ({radius})^2 \\times {height} = {volume:.2f}\\pi$ cubic inches<br><br>"
    
    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

