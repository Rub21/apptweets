import psycopg2
from datetime import datetime
import time
from sys import argv
import json
import codecs
import os

conn = psycopg2.connect(database="dbtwitter21", user="postgres",password="rub212106tkm")
cursor = conn.cursor()
filepath = '/home/rub21/Dropbox/Public/'

geojson = { "cant": [], "fech": [] }
query = "select count, fecha from get_estats;"
cursor.execute(query)
resultados = cursor.fetchall()
for stats in resultados:
	
	geojson['cant'].append(float(stats[0]))
	arr_fech =stats[1].split('-')

	geojson['fech'].append(arr_fech[2]+'-'+arr_fech[1])


cursor.close()
conn.close()
json.dump(geojson, open(os.path.join(filepath,'statstwitter21.js'), 'w'))
   



