# Import required packages
from dash.dependencies import Input, Output, State
from dash import no_update
import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import mysql.connector
from mysql.connector import Error
from dash import no_update


def create_db_connection(host_name, user_name, user_password, db_name):
    """this function automatically connect to db of interest which we have already created"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def read_query(connection, query):
    """executes a querry and retrieve data from the database"""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

pw = " " # IMPORTANT! Put your MySQL Terminal password here.

db = "DataMinded" 

connection = create_db_connection("localhost", "root", pw, db)

#Accesing database

q5 = """
SELECT *
FROM Pollutant;
"""
results = read_query(connection, q5)

from_db = []

for result in results:
    
    result = list(result)
    
    from_db.append(result)
    
columns = ["data_id", "country", "city", "sourceType", "location", "mobile", "unit", "local date", "value", "parameter"]

df = pd.DataFrame(from_db, columns=columns)

df.sort_values(by='local date', ascending=True, axis=0, inplace=True)

df['local date'] = pd.to_datetime(df['local date'])

df_TP = df[['local date', 'value']]

# Line plot Creation
fig = px.line(df_TP, x='local date', y='value', title='Hourly variation of NO2', markers=True)
fig.update_layout(
yaxis = dict(
tickfont = dict(size=25)),
xaxis = dict(
tickfont = dict(size=25)))

# Create a dash application
app = dash.Dash(__name__)

app.config.suppress_callback_exceptions = True

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.

app.layout = html.Div(children=[
    html.H1(
        children='Air Quality Data Dashboard', 
       style = {'textAlign':'center',
               'color':'#503D36',
               'font-size':40}
    ),
    # Create dropdown
    dcc.Dropdown(id='input-type', 
            options=[
            {'label': 'West-Vlaanderen', 'value': 'West-Vlaanderen'},
            {'label': 'Antwerp', 'value': 'Antwerp'},
            {'label': 'Brussels', 'value': 'Brussels'}
        ],
         placeholder="Select a city",
         style={'width':'80%', 'padding':'3px', 'font-size': '20px', 'text-align-last' : 'center'}
    ),
    # Bar graph
    html.Div(
         html.Div(children = [dcc.Graph(id='plot1',figure=fig, style={'width': '120vh', 'height': '70vh','display': 'flex'})]))
])

#html.Div(children = [dcc.Graph(id='plot1',figure=fig, style={'width': '120vh', 'height': '70vh','display': 'flex'})])
"""
@app.callback(
    Output("plot1", "figure"), 
    Input('input-type', 'value'))
def get_figure(city):
    if city == 'West-Vlaanderen':
        fig = px.line(df_TP, x='local date', y='value', title='Hourly variation of NO2', )
    else:
        fig = px.line(df_TP, x='local date', y='value', title='Hourly variation of NO2', )
    
    return [dcc.Graph(figure=fig)]
"""
# Run the application                   
if __name__ == '__main__':
    app.run_server()