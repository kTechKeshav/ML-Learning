### Building URL dynamically.
## Variable rule
### Jinja 2 Template Engine.

'''
{{  }} expressions to print output in HTML
{%...%} conditions, for loops
{#...#} this is for comments

'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homePage():
      return render_template('index.html')

@app.route('/about')
def aboutPage():
      return render_template('about.html')

@app.route('/submit', methods=['GET','POST'])
def submitPage():
      if request.method == 'POST':
            name = request.form['name']
            return f"Welcome {name}"
      return render_template('form.html')

# Variable Rule.
@app.route('/marks/<int:marks1>/<int:marks2>')
def sumMarks(marks1, marks2):
      return f"Your marks are => {str(marks1 + marks2)}"

@app.route('/vote/<int:age>')
def canIVote(age):
      return render_template('vote.html', age = age)

@app.route('/result/<int:marks>')
def result(marks):
      res= ""
      if marks < 32:
            res = "FAILED"
      else:
            res = "PASSED"
      exp = {
            'score': marks,
            'res' : res
      }
      return render_template('result1.html', results = exp)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
      total=0
      if request.method == 'POST':
            math=float(request.form['math'])
            phy=float(request.form['phy'])
            che=float(request.form['che'])

            total = (math+phy+che)/3
            return redirect(url_for('result', marks=total))

      return render_template('calculate.html')

if __name__ == '__main__':
      app.run(debug=True)