from flask import Flask, render_template
app = Flask(__name__)
# after @ an instance of a flask class is provided, .route the method of this class
@app.route('/') # when you are in the root url the function home is activated
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)