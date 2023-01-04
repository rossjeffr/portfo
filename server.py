#first lines imported from flask documentation

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', 'a') as database:
        name = data['name'] #this works because the data is a dictionary
        email = data['email']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        name = data['name'] #this works because the data is a dictionary
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('http://127.0.0.1:5000/')
        except:
            return 'did not save to database'
    else:
        return "something went wrong"