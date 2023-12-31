from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_input', methods=['POST'])
def check_input():
    user_input = request.form['userInput']
    is_thala_fan = False

    if user_input.isdigit():
        # Check if the input is a pure number
        digit_sum = sum(map(int, str(user_input)))
        is_thala_fan = digit_sum == 7
    elif len(user_input) == 7:
        # Check if the input is a pure string of length 7
        is_thala_fan = True

    return render_template('result.html', is_thala_fan=is_thala_fan)

if __name__ == '__main__':
    app.run(debug=True)
