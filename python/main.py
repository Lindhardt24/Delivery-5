##############################################Main.py###########################################
###############---------------------Bruges til data fra MongoDB-----------------------#########
#########-------------- Run pip install -r requirements.txt before using!######################

# Importerer de forskellige biblioteker
from random import uniform
import pymongo
from pymongo import MongoClient
import dash
from dash import html
from dash import dcc
from dash import Dash, dash_table
from IPython.display import display
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Pymongo hjælper os med at hive databasen ned Atlas clusteren.
# NB Husk at ændre password fra Extern-password fil tilsendt.
myclient = pymongo.MongoClient("mongodb+srv://Righthereismyusername:TYPEPASSWORD HERE@clusterdelivery5.0nc0d.mongodb.net/?retryWrites=true&w=majority")

# Dash appen startes and the magic starts to happen
app = Dash(__name__)

# Her peger vi på databasen Account som pymongo har puttet ned i variablen myclient
mydb = myclient["Account"]

# Vores collection User peges der her på
mycol = mydb["User"]


# Pandas bruges til at omdanne dataen til noget vi kan arbejde med gennem varialblen data.
# Metoden find bruges til at finde alt mycol, som er vores collection i Account databasen
data = pd.DataFrame(list(mycol.find()))


# Vores figur laves gennem plotly og er her hentet som plotly as go. 
# I cells=dict sætter vi de values ind vi vil bruge i vores figur. 
fig = go.Figure(data=[go.Table(
    header=dict(values=list(data.columns),
                fill_color='green',
                align='left'),
    cells=dict(values=[data.Name, data.Address, data.Mail, data.Name],
                fill_color='lavender',
                align='left'))
])


# App layoutet er med til at give dashboardet et større overblik.
app.layout = html.Div(children=[
    html.H1(children='Dette er Delivery 5'),

    html.Div(children='''
        Denne tabel er over Users gennem MongoDB
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


# Dette sørger for at serveren bliver ved med at køre
if __name__ == '__main__':
    app.run_server(debug=True)
