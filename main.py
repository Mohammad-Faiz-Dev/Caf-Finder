from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Regexp
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# ---- FORM CLASS ----
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired()])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕' * i for i in range(1, 6)], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=['💪' * i for i in range(1, 6)], validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Rating', choices=['🔌' * i for i in range(1, 6)], validators=[DataRequired()])
    submit = SubmitField('Submit')

# ---- ROUTES ----
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes():
    cafes_list = []
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Store header separately
        for row in csv_reader:
            cafes_list.append(row)
    return render_template('cafes.html', header=header, cafes=cafes_list)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open_time.data,
                form.close_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_rating.data
            ])
        return redirect(url_for('cafes'))
    else:
        print(form.errors)  # DEBUG: See why it failed
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
