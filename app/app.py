from flask import Flask, render_template, request
import random

from blueprints.quantative_reasoning.qr_1a1 import qr_1a1
from blueprints.quantative_reasoning.qr_6 import qr_6
from blueprints.openstax.prealgebra_2e import prealgebra_2e
from blueprints.openstax.elementary_algebra_2e import elementary_algebra_2e

app = Flask(__name__)

app.register_blueprint(qr_1a1, url_prefix='/qr-1a1')
app.register_blueprint(qr_6, url_prefix='/qr-6')
app.register_blueprint(prealgebra_2e, url_prefix='/prealgebra_2e')
app.register_blueprint(elementary_algebra_2e, url_prefix='/elementary_algebra_2e')


#=================================================================================

@app.route('/')
def index():
    return render_template('index.html')
#=================================================================================

@app.route('/quantative_reasoning')
def quantative_reasoning():
    return render_template('quantative_reasoning.html')
#=================================================================================

@app.route('/prealgebra_2e')
def prealgebra_2e():
    return render_template('prealgebra_2e.html')
#=================================================================================

@app.route('/elementary_algebra_2e')
def elementary_algebra_2e():
    return render_template('elementary_algebra_2e.html')
#=================================================================================


@app.route('/base_forms')
def base_forms():
    problem_title = "Customizable Problem"
    problem_description = "Enter the values you want to use for this problem."
    fields = {
        "Value 1": 10,
        "Value 2": 20,
    }
    return render_template('base_forms.html', problem_title=problem_title, problem_description=problem_description, fields=fields)
#=================================================================================

@app.route('/quadratic')
def quadratic():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    problem = f"${a}x^2 + {b}x + {c} = 0$"
    answer = f"$x = \\frac{{-{b} \\pm \\sqrt{{{b}^2-4{a}{c}}}}}{{2{a}}}$"
    return render_template('problem.html', problem=problem, answer=answer)
#=================================================================================  

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
#=================================================================================   
