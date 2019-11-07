import os, sys, urllib
import zipfile
import numpy as np
print('numpy version: {}'.format(np.__version__))
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import unidecode

def print_hello():
	print('hello')

def clean_cuebiq_data(df, sample_pct = 1, dow = True):
	df = df.sample(frac = sample_pct).reset_index(drop = True)
	df['timestamp'] = pd.to_datetime(df.timestamp, unit = 's')
	df['hour'] = df.timestamp.apply(lambda x : x.hour)
	if dow:
		df['day_of_week'] = df.timestamp.apply(lambda x : x.dayofweek)
	df['date'] = df.timestamp.apply(lambda x: str(x.date()))
	df.lat.replace(r'\N',np.nan, inplace = True)
	df.lon.replace(r'\N',np.nan, inplace = True)
	df.dropna(inplace = True)
	geoms = [Point(x,y) for x,y in zip(df.lon, df.lat)]
	df = gpd.GeoDataFrame(df, geometry = geoms)
	return(df)

def fetch_GADM_boundaries(country_code, verbose = 1):
    GADM_URL = 'https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_{}_shp.zip'.format(country_code)
    shp_path = os.path.join("data", country_code + "_GADM")
    if not os.path.isdir(shp_path):
        os.mkdir(shp_path)
    zip_path = os.path.join(shp_path, 'GADM.zip')
    
    try:
        urllib.request.urlretrieve(GADM_URL, zip_path)
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(e.args)
    
    myzip = zipfile.ZipFile(zip_path)
    if verbose:
        print("downloaded {} files from {}".format(len(myzip.infolist()), GADM_URL))
        print("extracting to {}: \n".format(shp_path))
        for file in myzip.infolist():
            print(file.filename, file.file_size)
    myzip.extractall(shp_path)

def strip_accents_from_series(series):
	map = {unidecode.unidecode(value): value for value in series.unique()}
	map = {v: k for k, v in map.items()}
	return(series.map(map))
