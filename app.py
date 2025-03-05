import json
from flask import Flask, render_template
from models import db, TimelineEntry
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-random-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chronicle.db'  # SQLite for now
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialise the database
db.init_app(app)

# Create tables (run once)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my_analysis')
def my_analysis():
    return render_template('my_analysis.html')

@app.route('/chronicle')
def chronicle():
    with open('data.json', 'r') as f:
        data = json.load(f)

    return render_template(
        'chronicle.html',
        data=data,
        entries=data['entries'],
        countries=data['countries'],
        years=data['years'],
    )

@app.template_filter('calc_grid_row')
def calc_grid_row(year):
    start_year = 1900
    return (year - start_year) + 2  # Same calculation as before

if __name__ == '__main__':
    app.run(debug=True)