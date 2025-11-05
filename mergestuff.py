import json
import pandas as pd

# raw contour data
with open('./contours_20220505.json') as F: t_contours = json.load(F)
# UDL channels, beam, RF data
t_udl = pd.read_json('./udl_merged_no_contours.json')
# merge contour
t_udl['contour'] = t_udl['idBeam'].apply( lambda X: t_contours.get(X,None) )