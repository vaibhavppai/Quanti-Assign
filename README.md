# Quantify Capital Techincal Asignment 1

Setup Instructions

Clone this repository
`https://github.com/vaibhavppai/Quanti-Assign.git` 

The req.txt file contains all the packages required to run this project.
install dependencies <br>
`pip install -r req.txt` 

Scrape https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt and generate database containing name, release date, rating, duration and description of the Top 250 IMDB Movies. <br>
`python3 TA1_DB_Creation.py`

Start Bottle server on localhost where the required routes are implemented: <br>
`python3 TA1_RestAPI.py`

Run the query application user interface: <br>
`python3 TA1_Query.py`
