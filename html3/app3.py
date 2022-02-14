from flask import Flask, render_template,request
app2 = Flask(__name__)

@app2.route('/')
def home():
    return render_template('index.html')

@app2.route('/', methods = ['POST'])
def pred():
    v1 = request.form.get('v1')
    v2 = request.form.get('v2')
    return render_template('index.html', price_prediction = 'Price is {}'.format(v1) )

if __name__ == '__main__':
    app2.run(debug=True)

