import pandas as pd
from datetime import date, timedelta
from point import Point
import os
from urllib.error import HTTPError
import county
import numpy as np
from numpy import genfromtxt



final_list= []

miami_dade = county.County(county_name= 'Miami-Dade', final_list=final_list)
county = miami_dade.get_name()


# final_list.append(miami_dade.get_all_values())

# print(miami_dade.get_labels())
# final_list = miami_dade.get_data()

labels_list = ['Last_Update', 'FIPS', 'Admin2', 'Province_State', 'Country_Region',  'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key']
init_list = miami_dade.get_data(labels_list)

size = len(init_list) 
idx_list = [idx + 1 for idx, val in
            enumerate(init_list) if val == '|||'] 
  
  
res = [init_list[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))] 







final_df = pd.DataFrame(data = res, columns=labels_list+['|||'] )
print(final_df)
  
# try:
#     os.remove(f'''D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''')
#     print('Old file deleted')
# except FileNotFoundError:
#     print('No file to delete.')
    

final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\{county}-COVID-19.csv''' , index = False, header=True)
print(f'''New file created at: D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''')

pic_array = genfromtxt(f'''{county}-COVID-19.csv ''', delimiter=',')


# print(new_list)
    # for row in db:
    #     print(row)




