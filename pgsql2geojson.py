import psycopg2
from datetime import datetime
import time
from sys import argv
import json
import codecs
import os

conn = psycopg2.connect(database="dbtwitter21", user="postgres",password="rub212106tkm")
cursor = conn.cursor()
geojson = { "type": "FeatureCollection", "features": [] }
filepath = '/home/rub21/Dropbox/Public/'

query = "SELECT id_t, text_t, created_at, source, latitud, longitud, imagen, id_u, name_u, screen_name, profile_image_url FROM get_data;"
cursor.execute(query)
#print query
#print len(cursor.fetchall())
resultados = cursor.fetchall()
for tweet in resultados:
	print tweet  
	data = {
        "type": "Feature",
        "geometry": {
        "type": 'Point',
        "coordinates": []
 	},
    	"properties": { }
 	} 
	print type(tweet[8])
	#print type(tweet[5])
	
	data['geometry']['coordinates'].append(float(tweet[5]))
	data['geometry']['coordinates'].append(float(tweet[4]))
	if(float(tweet[5]) == 0 and float(tweet[4]) == 0):
		data['geometry']='None'
	data['properties']['id_t']=tweet[0]
	data['properties']['text_t']=tweet[1]	
	data['properties']['created_at']=tweet[2]
	data['properties']['source']=tweet[3]
	data['properties']['imagen']=tweet[6]
	data['properties']['id_u']=tweet[7]
	data['properties']['name_u']=tweet[8]
	data['properties']['screen_name']=tweet[9]
	data['properties']['profile_image_url']=tweet[10]
	geojson['features'].append(data)

cursor.close()
conn.close()
#json.dump(geojson, open('datatwitter.js', 'w'))    
json.dump(geojson, open(os.path.join(filepath,'datatwitter21.js'), 'w'))


