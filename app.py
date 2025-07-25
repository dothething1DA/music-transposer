from flask import Flask, render_template, request
from processor import process_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ""
    lowest_note = ""
    output_text = ""

    if request.method == 'POST':
        input_text = request.form['input_text']
        lowest_note = request.form['lowest_note']
        output_text = process_text(input_text, lowest_note)

    return render_template('index.html', input_text=input_text, output_text=output_text, lowest_note=lowest_note)

if __name__=="__main__":
    app.run(debug=True)
