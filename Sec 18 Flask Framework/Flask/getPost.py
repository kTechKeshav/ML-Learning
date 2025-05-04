from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homePage():
      return render_template('index.html')

@app.route('/about')
def aboutPage():
      return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def formPage():
      if request.method == 'POST':
            name = request.form['name']
            return f"Welcome {name}"
      return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submitPage():
      if request.method == 'POST':
            name = request.form['name']
            return f"Welcome {name}"


if __name__ == '__main__':
      app.run(debug=True)