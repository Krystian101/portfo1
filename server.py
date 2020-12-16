from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)


@app.route('/index.html')
def my_home():
    return render_template(r'./index.html')


@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)


def storing_data_csv(data):
    filename = "./database.csv"
    file_stats = os.stat(filename)
    file_size = file_stats.st_size
    try:
        with open('./database.csv', mode='a+', newline='') as database_file:
            field_names = list(data.keys())
            writer = csv.DictWriter(database_file, field_names)
            if file_stats.st_size > 0:
                writer.writerow(data)
            else:
                writer.writeheader()
                writer.writerow(data)

    except IOError:
        print("I/O error")


def storing_data_txt(data):
    try:
        with open('./database.txt', mode='a+') as database_file2:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            file = database_file2.write(f'\n{email},{subject},{message}')

    except IOError:
        print("I/O error")


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        storing_data_txt(data)
        storing_data_csv(data)
        return redirect('/thankyounote.html')
    else:
        return 'something went worng'
