import pandas as pd
from datetime import date, timedelta
from point import Point
import os
from urllib.error import HTTPError
import numpy as np
from numpy import genfromtxt
import FIPS
import test
import county

final_list= []

input_type = input('\n\nWould you like to search by name(1) or by FIPS(0)? >')



if input_type == '1':
    
    new_name = input('''\nWhat is the exact name of the county you would like searched up 
                        \nPlease enter the county name without ( -county) at the end and in title format with the first letter of each new word capitalized. 
                        \nFor example, Miami-Dade County should be entered as "Miami-Dade". 
                        \nNow please enter your county name. >''')

    new_county = county.County(county_name= new_name)
    county = new_county.get_name()
    date = new_county.get_date()


    # final_list.append(miami_dade.get_all_values())

    # print(miami_dade.get_labels())
    # final_list = miami_dade.get_data()


    #'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key'
    labels_list = ['Last_Update','FIPS', 'Admin2', 'Province_State', 'Country_Region',   'Confirmed', 'Deaths', 'Combined_Key']
    init_list = new_county.get_data(labels_list)

    size = len(init_list) 
    idx_list = [idx + 1 for idx, val in
                enumerate(init_list) if val == '|||'] 
    
    
    res = [init_list[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))] 


    final_df = pd.DataFrame(data = res, columns=labels_list+['|||'] )
    print(final_df)
    
    if county == 'Miami-Dade':
        try:
            os.remove(f'D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\Miami-Dade\03-March\{date}-{county}-COVID-19_Update.csv')
            print('Old file deleted')
        except FileNotFoundError:
            print('No file to delete.')

        # final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\Miami-Dade\3-March\{date}-{county}-COVID-19_Update.csv''' , index = False, header=True)
        final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''' , index = False, header=True)
        print(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\Miami-Dade\03-March{date}-{county}-COVID-19_Update.csv''')

    else:
        try:
            os.remove(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''')
            print('Old file deleted')
        except FileNotFoundError:
            print('No file to delete.')

        final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''' , index = False, header=True)
        print(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''')




    # print(new_list)
        # for row in db:
        #     print(row)








elif input_type == '0':

    new_FIPS = int(input('\nWhat is the FIPS number that you would like to search up? >'))

    new_county = FIPS.County(FIPS= new_FIPS)
    county = new_county.get_name()
    date = new_county.get_date()


    # final_list.append(miami_dade.get_all_values())

    # print(miami_dade.get_labels())
    # final_list = miami_dade.get_data()



    #'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key'
    labels_list = ['Last_Update', 'FIPS', 'Admin2', 'Province_State', 'Country_Region',   'Confirmed', 'Deaths', 'Combined_Key']
    init_list = new_county.get_data(labels_list)

    size = len(init_list) 
    idx_list = [idx + 1 for idx, val in
                enumerate(init_list) if val == '|||'] 
    
    
    res = [init_list[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))] 



    final_df = pd.DataFrame(data = res, columns=labels_list+['|||'] )
    print(final_df)
    
   
        
#TODO Make python create a new path for each new county searched up so that the files are stored better.

    if county == 'Miami-Dade':
        try:
            os.remove(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\Miami-Dade\03-March\{date}-{county}-COVID-19_Update.csv''')
            print('Old file deleted')
        except FileNotFoundError:
            print('No file to delete.')

        # final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\Miami-Dade\03-March\{date}-{county}-COVID-19_Update.csv''' , index = False, header=True)
        final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''' , index = False, header=True)
        print(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\Miami-Dade\03-March{date}-{county}-COVID-19_Update.csv''')

    else:
        try:
            os.remove(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''')
            print('Old file deleted')
        except FileNotFoundError:
            print('No file to delete.')

        final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''' , index = False, header=True)
        print(f'''D:\Programming Projects\MDC-COVID-19\Git\MDC-COVID-19-visuals\CSV_file\March\{date}-{county}-COVID-19_Update.csv''')



    # print(new_list)
        # for row in db:
        #     print(row)

else:
    print("Invalid Input: not 1 or 0\nNow Closing...")









