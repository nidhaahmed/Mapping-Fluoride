from flask import Flask, render_template, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Load your data
data_path = 'data_updated.json'
with open(data_path) as f:
    data = json.load(f)

# Convert the station data to a DataFrame
stations_df = pd.DataFrame(data['stations'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Return the station data as JSON
    return jsonify(stations_df.to_dict(orient='records'))

@app.route('/bar-chart')
def bar_chart():
    district_counts = stations_df['District'].value_counts()
    return jsonify(district_counts.to_dict())

@app.route('/pie-chart')
def pie_chart():
    fluoride_levels = pd.cut(stations_df['Fluoride'], bins=[-1, 0.5, 1.0, float('inf')], labels=['Low', 'Medium', 'High'])
    level_counts = fluoride_levels.value_counts()
    return jsonify(level_counts.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
