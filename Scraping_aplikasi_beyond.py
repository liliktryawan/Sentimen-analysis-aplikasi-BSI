#Ambil 10000 data ulasan aplikasi beyond dari playstore

from google_play_scraper import app, reviews_all, Sort
import pandas as pd

review_apps = reviews_all(
    'co.id.bankbsi.superapp',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=10000,
)

df = pd.DataFrame(review_apps)
df.to_csv('review_beyond_apps.csv', index=False)