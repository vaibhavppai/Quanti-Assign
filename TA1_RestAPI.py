from bottle import route, run
import sqlite3
import pandas as pd
from bottle import auth_basic, request, route

# Authentication
def is_authenticated_user(user, password):
    if user == 'User' and password == 'pass@123' :
        return True
    return False

# Create your connection.
cnx = sqlite3.connect(':memory:')

# Reading Excel file
movies_db = pd.read_excel("Movies.xlsx")

# Converting to SQL database
movies_db.to_sql(name='Movies',con = cnx)