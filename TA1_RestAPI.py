from bottle import route, run
import sqlite3
import pandas as pd
from bottle import auth_basic, request, route

# Create your connection.
cnx = sqlite3.connect(':memory:')

# Reading Excel file
movies_db = pd.read_excel("Movies.xlsx")

# Converting to SQL database
movies_db.to_sql(name='Movies',con = cnx)

@route('/getMovie')
@auth_basic(is_authenticated_user)
def getMovieDetails(name):
    details = pd.read_sql("SELECT movie, year, imdb, duration, description FROM Movies WHERE movie='" + name + "'", con = cnx)
    return details.to_string()

@route('/sortBy', method = ['POST', 'GET'])
@auth_basic(is_authenticated_user)
def sortBy(field, type='asc'):
    sorted = pd.read_sql("SELECT movie, year, imdb, duration, description FROM Movies ORDER BY "+field+", movie "+type,con = cnx)
    print(sorted['year'])
    return sorted.to_string()
	
@route('/login', method = ['POST'])
@auth_basic(is_authenticated_user)
def home():
    print(request.auth)
    return ['hooray, you are authenticated! your info is: {}'.format(request.auth)]

@route('/searchBy')
@auth_basic(is_authenticated_user)
def searchBy(field, keyword):
    s = " "
    keyword = s.join(keyword.strip().split('-'))
    results = pd.read_sql("SELECT movie, year, imdb, duration, description FROM Movies WHERE "+field+" LIKE '%"+keyword+"%'", con = cnx)
    print(results)
    return results.to_string()	
	
if __name__  == '__main__':
    route('/getMovie/<name>')(getMovieDetails)
    route('/sortBy/<field>/<type>')(sortBy)
    route('/sortBy/<field>')(sortBy)
    route('/searchBy/<field>/<keyword>')(searchBy)
    route('/login')(home)
    run(host='localhost', port=8080, debug=True)