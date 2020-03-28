from datetime import date, timedelta
import pandas as pd
from point import Point
import os
from urllib.error import HTTPError
import datetime
import numpy as np




class County:
    def __init__(self, county_name, final_list):      #( county_list, data_list, label_list):
        self.name = county_name
        self.county_list= county_list =[county_name]
       

    def get_data(self, labels_list):
        sdate = datetime.date(2020, 3, 22)   # start date || this is the first day that JHU posted data for MDC
        edate = datetime.date.today()   # end date || currently set to yesterday's date because it turned to midnight and I was getting an error cause JHU did not publish it yet for 3/28

        delta = edate - sdate       # as timedelta
        
      
        county = self.name
        big_list = []
        values_list =[]
        x = []
        # labels_list = ['FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key']
        # labels_list = [ 'Last_Update', 'Confirmed', 'Deaths',  'Combined_Key']
        
        # big_list += labels_list + ['|||']

        for i in range(delta.days + 1):
            date = sdate + timedelta(days=i)
            printable_date = str(date)

            month = date.month

            
            if len(str(month))<2:
                month = '0'+str(month)
                
            day = date.day
            if len(str(day))<2:
                day = '0'+str(day)
            url = f'''https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{day}-2020.csv'''
                
            try:
                db = pd.read_csv(url, error_bad_lines=False)
                df = pd.DataFrame(db)
            except HTTPError:
                print(f'''There is no file for {month}/{day} yet, so it was skipped.''') 
                continue

            values_list.clear()
            x.clear()

            for item in labels_list:
                        

                if item =='Last_Update':
                    location = df.loc[df['Admin2']==county].index[0]
            
                    cell_value = df[item][location]

                    values_list.insert(0,cell_value)

                    continue

               
                location = df.loc[df['Admin2']==county].index[0]
            
                cell_value = df[item][location]
                
                values_list.append(cell_value)
            
            break_value ="|||"
            
            x.append(values_list)

            
            
            
            # print (values_list)
            big_list += values_list
            big_list.append(break_value)
            


        # print(big_list)
        # print(big_list)
        
                # point1 = Point(printable_date, cell_value)
                # new_list.append(point1.get_point())
                

       
        
        return big_list



    def get_all_values(self):
        sdate = datetime.date(2020, 3, 22)   # start date || this is the first day that JHU posted data for MDC
        edate = datetime.date.today()   # end date || currently set to yesterday's date because it turned to midnight and I was getting an error cause JHU did not publish it yet for 3/28

        delta = edate - sdate       # as timedelta

      
        county = self.name
        values_list =[]

        for i in range(delta.days + 1):
            date = sdate + timedelta(days=i)
            printable_date = str(date)

            month = date.month

            
            if len(str(month))<2:
                month = '0'+str(month)
                
            day = date.day
            if len(str(day))<2:
                day = '0'+str(day)

            url = f'''https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{day}-2020.csv'''
            
            try:
                db = pd.read_csv(url, error_bad_lines=False)
                df = pd.DataFrame(db)
            except HTTPError:
                print(f'''There is no file for {month}/{day} yet, so it was skipped.''') 
                continue
     
            location = df.loc[df['Admin2']==county].index[0]
          
            row_values = df.loc[location]
            values_list.append(row_values)
        return values_list


    def get_labels(self):
        labels_list=[]

        # url = f'''https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-27-2020.csv'''
    
        # db = pd.read_csv(url, error_bad_lines=False)
        # df = pd.DataFrame(db)
       
        # location = df.loc[df['Admin2']=='Admin2']
          
        # row_values = df.iloc[location]
        labels_list.extend(['FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key'])
        return labels_list

    def get_name(self):
        return self.name


# final_df = pd.DataFrame(data = new_list, columns= ('Date', 'Number of cases'))
# print(final_df)

# try:
#     os.remove(f'''D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''')
#     print('Old file deleted')
# except FileNotFoundError:
#     print('No file to delete.')
    

# final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''' , index = False, header=True)
# print(f'''New file created at: D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''')


# print(new_list)
    # for row in db:
    #     print(row)





