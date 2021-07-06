import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root-root21@localhost/imdb')

headers = {"Accept-Language": "en-US, en;q=0.5"}

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []
descriprion = []
director = []

pages = np.arange(1, 1001, 50)

for page in pages:
    page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&start=" + str(page) + "&ref_=adv_nxt", headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    movie_div = soup.find_all('div', class_='lister-item mode-advanced')

    for container in movie_div:
        name = container.h3.a.text
        titles.append(name)

        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)

        runtime = container.p.find('span', class_='runtime').text if container.p.find('span',
                                                                                      class_='runtime').text else '-'
        time.append(runtime)

        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
        metascores.append(m_score)

        nv = container.find_all('span', attrs={'name': 'nv'})

        vote = nv[0].text
        votes.append(vote)

        grosses = nv[1].text if len(nv) > 1 else '-'
        us_gross.append(grosses)

        desc = container.find_all('p', class_='text-muted')[-1].text.lstrip()
        descriprion.append(desc)

        direct = container.find("p", class_="").text.replace("\n", "").split('|')
        director.append(direct[0])


movies = pd.DataFrame({
'movie_name': titles,
'movie_year': years,
'duration': time,
'imdb_rating': imdb_ratings,
'metascore': metascores,
'votes': votes,
'revenue': us_gross,
'movie_description': descriprion,
'director': director
})


movies['movie_year'] = movies['movie_year'].str.extract('(\d+)').astype(int)
movies['duration'] = movies['duration'].str.extract('(\d+)').astype(int)
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['metascore'] = movies['metascore'].str.extract('(\d+)')
movies['metascore'] = pd.to_numeric(movies['metascore'], errors='coerce')
movies['revenue'] = movies['revenue'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['director'] = movies['director'].str.replace('    Directors:', '')
movies['director'] = movies['director'].str.replace('    Director:', '')

sql = '''TRUNCATE movies'''
result = engine.execute(sql)

movies.to_sql("movies", con = engine, if_exists='append', index=False)

