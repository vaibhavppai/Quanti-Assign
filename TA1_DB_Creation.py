import pandas as pd
from bs4 import BeautifulSoup
from requests import get
from time import sleep
from time import time
import random
from warnings import warn
from IPython.core.display import clear_output

# Lists to store scraped data in
names = []
imdb_ratings = []
years = []
durations = []
descriptions = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0

pages = [str(i) for i in range(1, 250, 50)]

# For every page
for page in pages:

    # Make a get request
    response = get('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=' + page)

    # Pause the loop
    # sleep(random.randint(8, 15))

    # Monitor the requests
    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))
    clear_output(wait=True)

    # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    # Break the loop if the number of requests is greater than expected
    if requests > 5:
        warn('Number of requests was greater than expected.')
        break

    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')

    # Select all the 50 movie containers from a single page
    movie_containers = page_html.find_all('div', class_='lister-item mode-advanced')

    # Extracting data from each movie container
    for container in movie_containers:
        # The Name
        name = container.h3.a.text
        names.append(name)
        # The Year
        year = int((container.h3.find('span', class_='lister-item-year text-muted unbold').text.split(' ')[-1])[1:-1])
        years.append(year)

        # The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        # The Duration
        duration = int(container.p.find('span', class_="runtime").text.split(' ')[0])
        durations.append(duration)

        # The Description
        desc = container.find_all('p', class_="text-muted")[1].text.strip()
        descriptions.append(desc)

# Storing into a DataFrame
movies_db = pd.DataFrame({'movie': names,
                          'year': years,
                          'imdb': imdb_ratings,
                          'duration': durations,
                          'description': descriptions
                          })

print(movies_db.info())
print(movies_db.head(10))

# Writing dataframe to excel
movies_db.to_excel("Movies.xlsx", index="False")
