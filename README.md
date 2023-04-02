# verge_webscraper
A web scraper to read articles off theverge.com using Python
- Read the headline, get the link of the article, the author, and the date of each of the articles found on "theverge.com"
- Store these in a CSV file titled `ddmmyyy_verge.csv`, with the following header `id, URL, headline, author, date`.
- Create an SQLite database to store the same data, and make sure that the id is the primary key
- Run this script on a cloud service (Pythonanywhere)
- Save the articles (and de-duplicate them) daily on the server in a SQL Database.
