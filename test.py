import pandas as pd
from datetime import date, timedelta
from point import Point
import os
from urllib.error import HTTPError
import county
import numpy as np
from numpy import genfromtxt



final_list= []


# new_county = county.County(county_name= 'Miami-Dade')
# county = new_county.get_name()
# date = new_county.get_date()


# # final_list.append(miami_dade.get_all_values())

# # print(miami_dade.get_labels())
# # final_list = miami_dade.get_data()




# #'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key'
# labels_list = ['Last_Update','FIPS', 'Admin2', 'Province_State', 'Country_Region',   'Confirmed', 'Deaths', 'Recovered', 'Combined_Key']
# init_list = new_county.get_data(labels_list)

# size = len(init_list) 
# idx_list = [idx + 1 for idx, val in
#             enumerate(init_list) if val == '|||'] 
  
  
# res = [init_list[i: j] for i, j in
#         zip([0] + idx_list, idx_list + 
#         ([size] if idx_list[-1] != size else []))] 







# final_df = pd.DataFrame(data = res, columns=labels_list+['|||'] )
# print(final_df)
  
# try:
#     os.remove(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''')
#     print('Old file deleted')
# except FileNotFoundError:
#     print('No file to delete.')
    

# final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''' , index = False, header=True)
# print(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''')




# # print(new_list)
#     # for row in db:
#     #     print(row)




