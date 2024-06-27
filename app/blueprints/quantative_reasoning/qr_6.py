from flask import Blueprint, render_template, url_for, request

import random
from random import randint, uniform
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import math
from math import pi, pow
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.stats import norm
from sympy import *


qr_6 = Blueprint('qr_6', __name__, template_folder='templates')
#=================================================================================

@qr_6.route('/population_density_skewness')
def population_density_skewness():
    mean = random.randint(100, 200)
    median = random.randint(mean // 2, mean + mean // 2)
    problem = f"A data set of the population densities of 15 U.S. states has a mean \
      of {mean} and a median of {median}. Which of the following is a logical \
        conclusion?<br><br>"
    problem += f"The data are skewed to the left.<br> The data are skewed to the \
      right.<br> The data are symmetrical.<br>"
    
    if mean > median:
        answer = "The data are skewed to the right."
        explanation = "When the mean is greater than the median, it indicates that \
        there are some higher values in the data set that are pulling the mean \
        upwards, causing the data to be skewed to the right."
    elif mean < median:
        answer = "The data are skewed to the left."
        explanation = "When the mean is less than the median, it indicates that \
        there are some lower values in the data set that are pulling the mean \
        downwards, causing the data to be skewed to the left."
    else:
        answer = "The data are symmetrical."
        explanation = "When the mean and median are equal, it indicates that the \
        data is evenly distributed, and there is no skewness in the data set."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_6.route('/skewed_frequency_tables', methods=['GET', 'POST'])
def skewed_frequency_tables():
    tables = generate_random_frequency_tables()
    problem = "Which of the following frequency tables show a skewed data set? Select all answers that apply.<br><br>"
    for idx, table in enumerate(tables):
        problem += f"Table {idx + 1}:<br>"
        problem += "<table><tr>"
        for key in table:
            problem += f"<th>{key}</th>"
        problem += "</tr><tr>"
        for value in table.values():
            problem += f"<td>{value}</td>"
        problem += "</tr></table><br>"
    answer = [idx for idx, table in enumerate(tables) if is_skewed(table)]
    explanation = ""
    for idx, table in enumerate(tables):
        mean, median = calculate_mean_median(table)
        skew_type = "skewed left" if mean < median else "skewed right" if mean > median else "not skewed"
        explanation += f"Table {idx + 1} is {skew_type} with a mean of {mean:.2f} and a median of {median}.<br>"
    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)

def generate_random_frequency_tables():
    def generate_random_table():
        table = {}
        for i in range(1, 6):
            table[i] = random.randint(1, 10)
        return table

    tables = [generate_random_table() for _ in range(3)]
    return tables

def is_skewed(table):
    mean, median = calculate_mean_median(table)
    return mean != median

def calculate_mean_median(table):
    values = list(table.values())
    mean = sum(values) / len(values)
    median = sorted(values)[len(values) // 2]
    return mean, median
#=================================================================================

@qr_6.route('/mean_median_skewness', methods=['GET', 'POST'])
def mean_median_skewness():
    median = random.randint(5, 25)
    mean = random.choice([random.randint(1, median - 1), random.randint(median + 1, 50)])
    problem = f"If the median of a data set is {median} and the mean is {mean}, which of the following is most likely?<br><br>"
    problem += "The data are skewed to the left.<br> The data are skewed to the right.<br> The data are symmetrical.<br>"
    answer = "The data are skewed to the left." if mean < median else "The data are skewed to the right."
    explanation = f"Since the mean ({mean}) is {'less' if mean < median else 'greater'} than the median ({median}), the data is most likely skewed to the {'left' if mean < median else 'right'}."
    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

@qr_6.route('/salary_skewness', methods=['GET', 'POST'])
def salary_skewness():
    data = sorted([random.randint(30, 50) for _ in range(7)] + [random.randint(90, 120) for _ in range(3)])    
    mean = statistics.mean(data)
    median = statistics.median(data)
    problem = f"The following data set represents salaries at a company (in thousands of dollars):<br>{', '.join(map(str, data))}<br>"
    problem += "Determine if the following data set represents a distribution which is skewed left, skewed right, or symmetric.<br>"
    if mean < median:
        answer = "The data are skewed to the left."
    elif mean > median:
        answer = "The data are skewed to the right."
    else:
        answer = "The data are symmetrical."
    explanation = f"Since the mean ({mean:.1f}) is {'less' if mean < median else ('greater' if mean > median else 'equal to')} the median ({median}), the data is {'skewed to the left' if mean < median else ('skewed to the right' if mean > median else 'symmetrical')}."
    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=================================================================================

import random
import os
from flask import Flask, render_template, url_for
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def is_skewed(data):
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    skew_left = any(x < lower_bound for x in data)
    skew_right = any(x > upper_bound for x in data)

    return skew_left or skew_right

@qr_6.route('/box_and_whisker_plots')
def box_and_whisker_plots():
    data_sets = generate_random_box_and_whisker_data()

    for i, data in enumerate(data_sets):
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.boxplot(data, vert=False)
        plt.savefig(os.path.join('static', 'images', f'box_and_whisker_{i}.png'))
        plt.close()

    correct_answers = [i for i, data in enumerate(data_sets) if is_skewed(data)]
    correct_answer_str = ", ".join(str(x) for x in correct_answers)

    problem = f"Which of the following box-and-whisker plots shows a skewed data set? Select all answers that apply.<br><br>"
    for i in range(4):
        image_url = url_for('static', filename=f'images/box_and_whisker_{i}.png')
        problem += f'<div style="display:inline-block; margin-right: 20px;"><img src="{image_url}" alt="Box and whisker plot {i}"><br>Plot {i}</div>'

    explanation = f"A skewed box-and-whisker plot is characterized by an asymmetrical distribution of the data, where the median (the middle line inside the box) is not in the center of the box, and the whiskers have unequal lengths. The skewed box-and-whisker plots are: {correct_answer_str}."
    
    return render_template('problem.html', problem=problem, answer=correct_answer_str, explanation=explanation)
#=================================================================================


def generate_random_box_and_whisker_data():
    data_sets = []
    for _ in range(4):
        data = [random.randint(10, 50) for _ in range(10)]
        if random.choice([True, False]):
            data.extend([random.randint(70, 100) for _ in range(3)])
        random.shuffle(data)
        data_sets.append(data)
    return data_sets

if __name__ == '__main__':
    app.run()
#=====================================================================

@qr_6.route('/iq_score_problem')
def iq_score_problem():
    mean = random.randint(90, 110)
    std_dev = random.randint(10, 20)
    iq = random.randint(mean + 5, mean + 30)

    # Calculate the z-score
    z_score = (iq - mean) / std_dev

    # Determine if the IQ is above or below the mean
    if z_score > 0:
        position = "above"
    else:
        position = "below"

    # Determine if the IQ is unusual
    if abs(z_score) > 3:
        unusual = "is"
    else:
        unusual = "is not"

    problem = f"IQ Scores have an average of {mean} with a standard deviation of {std_dev}. Assume IQ scores are normally distributed. For an IQ score of {iq}, answer the following questions:<br>" \
              "a. What is the z-score?<br>" \
              "b. An IQ of {iq} is _______ standard deviation(s) _________ (above or below) the mean.<br>" \
              "c. An IQ of {iq} ______ (is or is not) unusual because the z-score _______ (is or is not) more than three standard deviations _____ (above or below) the mean."

    answer_a = f"{z_score:.2f}"
    answer_b = f"{abs(z_score):.2f} standard deviation(s) {position} the mean"
    answer_c = f"An IQ of {iq} {unusual} unusual because the z-score {unusual} more than three standard deviations {position} the mean"

    explanation = f"a. The z-score is {answer_a}.<br>" \
                  f"b. {answer_b}.<br>" \
                  f"c. {answer_c}."

    answer = explanation

    explanation += (f"The z-score is calculated by subtracting the mean ({mean}) from the given IQ score ({iq}) "
                    f"and then dividing the result by the standard deviation ({std_dev}).<br><br>"
                    f"z = (IQ - Mean) / Standard Deviation<br>"
                    f"z = ({iq} - {mean}) / {std_dev}<br>"
                    f"z = {z_score:.2f}<br><br>"
                    f"An IQ of {iq} is {z_score:.2f} standard deviation(s) {position} the mean. "
                    f"An IQ of {iq} {unusual} unusual because the z-score "
                    f"{unusual} more than three standard deviations {position} the mean.")


    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)

#=====================================================================

# Add this route in your Python file
@qr_6.route('/z_score_probability')
def z_score_probability():
    z_score_a = round(random.uniform(-3, 3), 2)
    z_score_b = round(random.uniform(-3, 3), 2)

    # Compute the probabilities
    probability_a = norm.cdf(z_score_a)
    probability_b = 1 - norm.cdf(z_score_b)

    problem = f"Find the answers to a) and b) using the table below. Do not round, and include a leading zero for a decimal answer.<br>" \
              f"a) Compute the probability of the z-score less than {z_score_a}.<br>" \
              f"b) What is the area to the right of the z-score {z_score_b} on the normal curve?"

    answer_a = f"{probability_a:.4f}"
    answer_b = f"{probability_b:.4f}"

    explanation = f"z = (IQ - Mean) / Standard Deviation<br>" \
                  f"a) The probability of the z-score less than {z_score_a} is {answer_a}.<br>" \
                  f"b) The area to the right of the z-score {z_score_b} on the normal curve is {answer_b}.<br><br>" \
                  f"The z-score represents the number of standard deviations a data point is away from the mean in a normal distribution. In this context, the z-score is used to find the probability of a data point being less than or greater than a specific value. The cumulative distribution function (CDF) of a normal distribution is used to calculate the probability for a given z-score. The area under the curve to the left of the z-score is equal to the probability."

    return render_template('problem.html', problem=problem, answer=f"{answer_a}, {answer_b}", explanation=explanation)
#=====================================================================

import random
from fractions import Fraction

# Add this route in your Python file
@qr_6.route('/marble_probability')
def marble_probability():
    green_marbles = random.randint(1, 10)
    red_marbles = random.randint(1, 10)
    blue_marbles = random.randint(1, 10)
    total_marbles = green_marbles + red_marbles + blue_marbles

    # Calculate the probabilities
    probability_red = Fraction(red_marbles, total_marbles)
    probability_green = Fraction(green_marbles, total_marbles)

    problem = f"You have a bag with {green_marbles} green marbles, {red_marbles} red marbles, and {blue_marbles} blue marbles. "\
              "You reach into the bag (no peeking!) and choose one marble at random. Give your answer as a simplified fraction.<br>"\
              "c. What is the probability the marble is red?<br>"\
              "d. What is the probability the marble is green?"

    answer_c = f"{probability_red}"
    answer_d = f"{probability_green}"

    explanation = f"c. The probability the marble is red is {answer_c}. "\
                  f"To find the probability, divide the number of red marbles by the total number of marbles: {red_marbles}/{total_marbles} = {probability_red}.<br>"\
                  f"d. The probability the marble is green is {answer_d}. "\
                  f"To find the probability, divide the number of green marbles by the total number of marbles: {green_marbles}/{total_marbles} = {probability_green}."

    return render_template('problem.html', problem=problem, answer=f"{answer_c}, {answer_d}", explanation=explanation)
#=====================================================================

@qr_6.route('/dice_probability')
def dice_probability():
    total_faces = 6
    odd_numbers = [1, 3, 5]
    target_number = 2

    # Calculate the probability
    successful_outcomes = len(odd_numbers) + (1 if target_number not in odd_numbers else 0)
    probability = Fraction(successful_outcomes, total_faces)

    problem = f"What is the probability of rolling an odd number or rolling a 2 on a fair six-sided die? Write your answer as a simplified fraction."

    answer = f"{probability}"

    explanation = f"The probability of rolling an odd number or rolling a 2 is {answer}. "\
                  f"There are 3 odd numbers (1, 3, and 5) and 1 even number (2). "\
                  f"Therefore, there are 4 successful outcomes out of a total of 6 possible outcomes: "\
                  f"{successful_outcomes}/{total_faces} = {probability}."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=====================================================================

@qr_6.route('/rain_probability')
def rain_probability():
    rain_prob = round(random.uniform(0.1, 0.9), 2)
    no_rain_prob = round(1 - rain_prob, 2)

    problem = f"The probability that it will rain tomorrow is {rain_prob}. What is the probability that it does not rain?"
    answer = f"{no_rain_prob}"
    explanation = f"The probability of an event not occurring is equal to 1 minus the probability of the event occurring. In this case, the probability of it not raining tomorrow is 1 - {rain_prob} = {no_rain_prob}."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=====================================================================

@qr_6.route('/blood_type_probability')
def blood_type_probability():
    a_rh_negative = random.randint(20, 100)
    b_rh_negative = random.randint(20, 100)
    ab_rh_negative = random.randint(10, 50)
    o_rh_negative = random.randint(20, 100)
    a_rh_positive = random.randint(20, 100)
    b_rh_positive = random.randint(20, 100)
    ab_rh_positive = random.randint(10, 50)
    o_rh_positive = random.randint(20, 100)

    total_a = a_rh_negative + a_rh_positive
    total_b = b_rh_negative + b_rh_positive
    total_ab = ab_rh_negative + ab_rh_positive
    total_o = o_rh_negative + o_rh_positive
    total_negative = a_rh_negative + b_rh_negative + ab_rh_negative + o_rh_negative
    total_positive = a_rh_positive + b_rh_positive + ab_rh_positive + o_rh_positive
    total_donors = total_a + total_b + total_ab + total_o

    problem = (f"Use the table below to find the probabilities. Round to four decimals as needed.<br>"
               f"a) Find the probability of choosing a donor with type A and Rh-Negative Blood.<br>"
               f"b) Find the probability of choosing a donor with type O blood.<br>"
               f"c) Find the probability of choosing a donor with Rh-Positive or type AB blood.<br>"
               f"d) Given type B blood has been chosen, find the probability the blood is Rh-Positive.<br><br>"
               f"<table border='1'><tr><th></th><th>A</th><th>B</th><th>AB</th><th>O</th><th>Total</th></tr>"
               f"<tr><td>Rh-Negative</td><td>{a_rh_negative}</td><td>{b_rh_negative}</td><td>{ab_rh_negative}</td><td>{o_rh_negative}</td><td>{total_negative}</td></tr>"
               f"<tr><td>Rh-Positive</td><td>{a_rh_positive}</td><td>{b_rh_positive}</td><td>{ab_rh_positive}</td><td>{o_rh_positive}</td><td>{total_positive}</td></tr>"
               f"<tr><td>Total</td><td>{total_a}</td><td>{total_b}</td><td>{total_ab}</td><td>{total_o}</td><td>{total_donors}</td></tr></table>")

    a_rh_negative_prob = a_rh_negative / total_donors
    o_blood_prob = total_o / total_donors
    rh_positive_ab_prob = (total_positive + total_ab) / total_donors
    b_rh_positive_given_b = b_rh_positive / total_b

    answer_a = f"{a_rh_negative_prob:.4f}"
    answer_b = f"{o_blood_prob:.4f}"
    answer_c = f"{rh_positive_ab_prob:.4f}"
    answer_d = f"{b_rh_positive_given_b:.4f}"

    explanation = (f"a) Probability of choosing a donor with type A and Rh-Negative Blood: {answer_a}<br>"
                   f"b) Probability of choosing a donor with type O blood: {answer_b}<br>"
                   f"c) Probability of choosing a donor with Rh-Positive or type AB blood: {answer_c}<br>"
                   f"d) Given type B blood has been chosen, find the probability the blood is Rh-Positive: {answer_d}")

    return render_template('problem.html', problem=problem, answer=f"{answer_a}, {answer_b}, {answer_c}, {answer_d}", explanation=explanation)
#=====================================================================

@qr_6.route('/painter_preferences')
def painter_preferences():
    flat_gray = round(random.uniform(0.01, 0.1), 2)
    flat_tan = round(random.uniform(0.01, 0.1), 2)
    eggshell_gray = round(random.uniform(0.2, 0.3), 2)
    eggshell_tan = round(random.uniform(0.1, 0.2), 2)
    satin_gray = round(random.uniform(0.1, 0.2), 2)
    satin_tan = round(1 - (flat_gray + flat_tan + eggshell_gray + eggshell_tan + satin_gray), 2)

    problem = f"A group of house painters were asked if they prefer to paint interior homes with flat, eggshell or satin paint and if they prefer shades of gray or tan. The percentage of painters who responded is listed in the table. Enter your responses as a decimal.<br><br>" \
              f"<table border='1'><tr><th></th><th>Gray Tone</th><th>Tan Tone</th></tr>" \
              f"<tr><td>flat</td><td>{flat_gray}</td><td>{flat_tan}</td></tr>" \
              f"<tr><td>eggshell</td><td>{eggshell_gray}</td><td>{eggshell_tan}</td></tr>" \
              f"<tr><td>satin</td><td>{satin_gray}</td><td>{satin_tan}</td></tr></table><br>" \
              f"a) What is the probability that a painter prefers a gray shade of eggshell paint?<br>" \
              f"b) What is the probability a painter prefers satin and tan tone paint?"

    answer_a = f"{eggshell_gray}"
    answer_b = f"{satin_tan}"

    explanation = f"a) The probability that a painter prefers a gray shade of eggshell paint is {answer_a}.<br>" \
                  f"b) The probability a painter prefers satin and tan tone paint is {answer_b}."

    return render_template('problem.html', problem=problem, answer=f"{answer_a}, {answer_b}", explanation=explanation)

#=====================================================================


@qr_6.route('/food_allergy_test_problem')
def food_allergy_test_problem():
    positive_disease = random.randint(100, 200)
    negative_disease = random.randint(1, 10)
    total_disease = positive_disease + negative_disease

    positive_no_disease = random.randint(1, 10)
    negative_no_disease = random.randint(250, 350)
    total_no_disease = positive_no_disease + negative_no_disease

    total_positive = positive_disease + positive_no_disease
    total_negative = negative_disease + negative_no_disease
    grand_total = total_disease + total_no_disease

    problem = f"A veterinarian wants to determine if a new brand of test is effective in detecting whether or not dogs have food allergies. Use the table below to determine the probability that the test… <br>a) gives a false negative result.  b) gives a false positive<br><br> Enter your answer as a simplified fraction." \
              f"<table border='1'><tr><th></th><th>Disease</th><th>No Disease</th><th>Total</th></tr>" \
              f"<tr><td>Positive Test</td><td>{positive_disease}</td><td>{positive_no_disease}</td><td>{total_positive}</td></tr>" \
              f"<tr><td>Negative Test</td><td>{negative_disease}</td><td>{negative_no_disease}</td><td>{total_negative}</td></tr>" \
              f"<tr><td>Total</td><td>{total_disease}</td><td>{total_no_disease}</td><td>{grand_total}</td></tr></table>"

    false_negative_prob = Fraction(negative_disease, grand_total).limit_denominator()
    false_positive_prob = Fraction(positive_no_disease, grand_total).limit_denominator()

    answer_a = f"{false_negative_prob}"
    answer_b = f"{false_positive_prob}"

    explanation = f"To calculate the probabilities, we need to divide the desired count by the total count.<br><br>" \
                  f"a) To find the probability that the test gives a false negative result, we use the count of false negatives ({negative_disease}) divided by the grand total count ({grand_total}).<br>" \
                  f"False Negative Probability = {negative_disease}/{grand_total} = {answer_a}<br><br>" \
                  f"b) To find the probability that the test gives a false positive result, we use the count of false positives ({positive_no_disease}) divided by the grand total count ({grand_total}).<br>" \
                  f"False Positive Probability = {positive_no_disease}/{grand_total} = {answer_b}"

    return render_template('problem.html', problem=problem, answer=f"{answer_a}, {answer_b}", explanation=explanation)
#=====================================================================

@qr_6.route('/students_major_problem', methods=['GET'])
def students_major_problem():
    total_students = random.randint(120, 200)
    total_freshman = random.randint(60, total_students - 50)
    total_sophomore = total_students - total_freshman
    total_undecided = random.randint(20, total_students - 60)

    # Variables to find
    freshman_undecided = random.randint(1, total_undecided - 1) # a
    freshman_declared = total_freshman - freshman_undecided # b
    sophomore_declared = total_sophomore - (total_undecided - freshman_undecided) # c
    total_declared = total_students - total_undecided # d

    answer_e = Fraction(freshman_undecided, total_freshman)
    answer_f = Fraction(sophomore_declared, total_declared)
    answer_g = Fraction(total_undecided - freshman_undecided, total_students)
    answer_h = Fraction(total_declared + total_freshman - freshman_undecided, total_students)

    problem = f"""Complete the table below and then find the probabilities. Write your answers as simplified fractions.
    <table border='1'>
    <tr><th></th><th>Freshman</th><th>Sophomore</th><th>Total</th></tr>
    <tr><td>Undecided Major</td><td>a)</td><td>{total_undecided - freshman_undecided}</td><td>{total_undecided}</td></tr>
    <tr><td>Declared Major</td><td>b)</td><td>c)</td><td>d)</td></tr>
    <tr><td>Total</td><td>{total_freshman}</td><td>{total_sophomore}</td><td>{total_students}</td></tr>
    </table><br>
    e) What is the probability that a randomly chosen student is an undecided major, given that they are a freshman?<br><br>
    f) What is the probability that a randomly chosen student is a sophomore, given that they have a declared major?<br><br>
    g) What is the probability a randomly selected student is a sophomore and has an undecided major?<br><br>
    h)  What is the probability a randomly selected student has declared a major or is a freshman?"""

    explanation = f"""
    a) Number of Freshman Undecided Major students: {freshman_undecided}<br>
    b) Number of Freshman Declared Major students: {freshman_declared}<br>
    c) Number of Sophomore Declared Major students: {sophomore_declared}<br>
    d) Total Number of Declared Major students: {total_declared}<br>
    e) P(Undecided | Freshman) = {freshman_undecided}/{total_freshman} = {answer_e}<br>
    f) P(Sophomore | Declared) = {sophomore_declared}/{total_declared} = {answer_f}<br>
    g) P(Sophomore and Undecided) = {total_undecided - freshman_undecided}/{total_students} = {answer_g}<br>
    h) P(Declared or Freshman) = {total_declared + total_freshman - freshman_undecided}/{total_students} = {answer_h}"""

    return render_template('problem.html', problem=problem, answer=f"{answer_e}, {answer_f}, {answer_g}, {answer_h}", explanation=explanation)
#=====================================================================

@qr_6.route('/snail_pace')
def snail_pace():
    # standard deviation, mean and the z scores for 68%, 95%, 99.7% 
    std_dev = random.randint(1, 5)
    mean = random.randint(10, 50)
    z_68 = 1
    z_95 = 2
    z_99 = 3

    # calculate the ranges
    range_68 = (mean - z_68 * std_dev, mean + z_68 * std_dev)
    range_95 = (mean - z_95 * std_dev, mean + z_95 * std_dev)
    range_99 = (mean - z_99 * std_dev, mean + z_99 * std_dev)

    problem = f"A researcher found that the average pace of a snail is {mean} inches per hour, with a standard deviation of {std_dev} inches per hour. Assuming the data is normally distributed fill in the blanks.<br>\
                a) 68% of the data is between ____ and ____ inches per hour.<br>\
                b) 95% of the data is between ____ and ____ inches per hour.<br>\
                c) 99.7% of the data is between ____ and ____ inches per hour."

    answer = f"{range_68[0]} and {range_68[1]}, {range_95[0]} and {range_95[1]}, {range_99[0]} and {range_99[1]}"

    explanation = f"The rule is also called the empirical rule or the 68-95-99.7 rule, which is a shorthand used to remember the percentage of values that lie within a band around the mean in a normal distribution with a width of two, four and six standard deviations, respectively.<br>\
                    68% of the data is between (mean - std_dev) and (mean + std_dev).<br>\
                    95% of the data is between (mean - 2std_dev) and (mean + 2std_dev).<br>\
                    99.7% of the data is between (mean - 3std_dev) and (mean + 3std_dev)."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)
#=====================================================================

from random import choices
@qr_6.route('/co2_levels')
def co2_levels():
    mean = randint(400, 600)
    std_dev = randint(50, 100)

    z_score_lower = choices([1, 2, 3], weights=[0.5, 0.3, 0.2], k=1)[0]
    z_score_upper = choices([1, 2, 3], weights=[0.2, 0.3, 0.5], k=1)[0]

    lower_range = mean - int(z_score_lower*std_dev)
    upper_range = mean + int(z_score_upper*std_dev)

    # Decide the percentage to be used for the problem
    if z_score_upper <= 1:
        percentage = 68
    elif z_score_upper <= 2:
        percentage = 95
    else:
        percentage = 99.7

    problem = f"A random sample of CO2 levels in a school has a sample mean of x={mean} ppm and sample standard deviation of s={std_dev} ppm. Use the Empirical Rule to determine the approximate percentage of CO2 levels that lie between {lower_range} and {upper_range} ppm."
    answer = f"{percentage}%"
    explanation = f"The range from {lower_range} to {upper_range} ppm corresponds to approximately {-z_score_upper} to {z_score_upper} standard deviations from the mean. According to the Empirical Rule, approximately {percentage}% of all data in a normal distribution falls within this range."

    return render_template('problem.html', problem=problem, answer=answer, explanation=explanation)

#=====================================================================



