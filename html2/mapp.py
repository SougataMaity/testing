
from flask import Flask, render_template, request
import analysis

app = Flask('__name__')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pred', methods = ['POST'])
def pred():
    v1 = request.form.get('v1')
    v2 = request.form.get('v2')
    v3 = request.form.get('v3')
    v4 = request.form.get('v4')
    output = [v1,v2,v3,v4]
    return render_template('pred.html', pred_text = 'Mean of the Output {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)