################################################Main MySQL#########################################
###-------------- Run pip install -r requirements.txt before using!######################
######## HUSK at ændre password! Er i bunden af rapporten.########################
# Bruges til at importere de forskellige biblioteker
from h11 import Data
import mysql.connector
from mysql.connector import Error
import dash
from dash import html
from dash import dcc
from dash import Dash, dash_table
from IPython.display import display
import pandas as pd
import numpy as np
import plotly.express as px

# MySQL connection til databasen. Her skal password tastes ind fra opgaven
# NB Husk at ændre password! Er i bunden af rapporten
db_connection = mysql.connector.connect(
    host="mysql4delivery5.mysql.database.azure.com",
    user="Righthereismyusername",
    port="3306",
    password="TYPEPASSWORDHERE",
    database="measure",
)
# Her kigger vi efter databaser på SQL-serveren. Det bruges da vi ikke skal skrive noget til filen. 
# MySQL cursor er kun read only. 
db_cursor = db_connection.cursor()

# Her læser vi tabellen anonmeasure ind i vores variabel df
df = pd.read_sql('SELECT * FROM anonmeasure', con=db_connection)

# Her viser vi vores data mellem measureDate og hjernebølgen Cz. 
fig_histo = px.histogram(data_frame=df, x ='MeasureDate', y ='Cz')
# Her viser vi blot ovenstående graf. 
fig_histo.show()




