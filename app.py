from flask import Flask, render_template, request
from processor import process_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ""
    output_text = ""

    if request.method == 'POST':
        input_text = request.form['input_text']
        output_text = process_text(input_text)

    return render_template('index.html', input_text=input_text, output_text=output_text)

if __name__=="__main__":
    app.run(debug=True)
