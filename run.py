# Importing necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Read the CSV file
df = pd.read_csv('education.csv')  # Make sure the CSV file is in the same directory as this script

# Create visualizations for EDA
fig_gender = px.bar(df, x='gender', color='Class', title='Gender Distribution Across Classes')
fig_stage = px.bar(df, x='StageID', color='Class', title='Educational Stage Distribution Across Classes')

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Student Performance Prediction Dashboard"),
    
    # Data Overview
    html.Div([
        html.H2("Data Overview"),
        dcc.Graph(id='data-overview-table', 
                  figure=px.scatter(df.sample(100), x='raisedhands', y='VisITedResources', color='Class').update_traces(marker=dict(size=8, opacity=0.5))
                  .update_layout(title='Sample Data (100 random points)'))
    ], style={'width': '48%', 'display': 'inline-block'}),
    
    # EDA Section
    html.Div([
        html.H2("Exploratory Data Analysis"),
        dcc.Graph(id='gender-distribution', figure=fig_gender),
        dcc.Graph(id='stage-distribution', figure=fig_stage)
    ], style={'width': '48%', 'display': 'inline-block'})
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
