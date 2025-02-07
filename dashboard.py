import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the fluoride data (JSON/CSV)
data = pd.read_json('data_updated.json')  # Modify the path as needed

# Normalize the data for easier analysis
stations_data = pd.json_normalize(data['stations'])

# Function to categorize risk levels based on fluoride concentration
def categorize_risk(fluoride):
    if fluoride <= 0.5:
        return 'Low Risk'
    elif fluoride <= 1.0:
        return 'Medium Risk'
    else:
        return 'High Risk'

# Add risk category to the stations_data
stations_data['Risk Level'] = stations_data['Fluoride'].apply(categorize_risk)

# Bar Chart - Comparing fluoride levels across districts
def bar_chart_by_district():
    district_avg = stations_data.groupby('District')['Fluoride'].mean().reset_index()
    fig = px.bar(district_avg, x='District', y='Fluoride', title="Average Fluoride Levels by District")
    fig.write_html('bar_chart.html')  # Save the figure as HTML

# # Pie Chart - Percentage of stations by fluoride level
def pie_chart_by_fluoride_level():
    def categorize_fluoride(fluoride):
        if fluoride <= 0.5:
            return 'Low (<= 0.5 mg/L)'
        elif fluoride <= 1.0:
            return 'Medium (0.5 - 1.0 mg/L)'
        else:
            return 'High (> 1.0 mg/L)'

    stations_data['Fluoride Category'] = stations_data['Fluoride'].apply(categorize_fluoride)
    fluoride_counts = stations_data['Fluoride Category'].value_counts().reset_index()
    fluoride_counts.columns = ['Fluoride Category', 'count']  # Rename columns

    fig = px.pie(fluoride_counts, names='Fluoride Category', values='count',
                 title="Fluoride Concentration Distribution")
    fig.write_html('pie_chart.html')  # Save the figure as HTML

# Data Table - Showing fluoride data in a table
def data_table():
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(stations_data.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[stations_data[col] for col in stations_data.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.update_layout(title="Fluoride Data Table")
    fig.write_html('data_table.html')  # Save the figure as HTML

# Call the functions to display the charts
bar_chart_by_district()
pie_chart_by_fluoride_level()
data_table()