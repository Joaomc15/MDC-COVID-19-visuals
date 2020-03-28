# import pandas as pd
# from datetime import date, timedelta
# from point import Point
# import os
# from urllib.error import HTTPError


# sdate = date(2020, 3, 22)   # start date || this is the first day that JHU posted data for MDC
# edate = date.today()   # end date || currently set to yesterday's date because it turned to midnight and I was getting an error cause JHU did not publish it yet for 3/28


# delta = edate - sdate       # as timedelta

# new_list = []

# county = 'Miami-Dade'

# for i in range(delta.days + 1):
#     date = sdate + timedelta(days=i)
#     printable_date = str(date)

#     month = date.month
#     if len(str(month))<2:
#         month = '0'+str(month)
        

#     day = date.day
#     if len(str(day))<2:
#         day = '0'+str(day)

#     url = f'''https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{day}-2020.csv'''
    
#     try:
#         db = pd.read_csv(url, error_bad_lines=False)
#         df = pd.DataFrame(db)
#     except HTTPError:
#         print(f'''There is no file for {month}/{day} yet so it was skipped.''') 
#         continue
#     # print(url)
    
#     county = 'Sacramento'

#     location = df.loc[df['Admin2']==county].index[0]
#     # print(location)
#     cell = df['Confirmed'][location]
#     # print(cell)
#     # point1 = Point(printable_date, f'''Confirmed cases: {cell}''')
#     point1 = Point(printable_date, cell)
#     new_list.append(point1.get_point())
    

# final_df = pd.DataFrame(data = new_list, columns= ('Date', 'Number of cases'))
# print(final_df)

# try:
#     os.remove(f'''D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''')
#     print('Old file deleted')
# except FileNotFoundError:
#     print('No file to delete.')
    

# final_df.to_csv ( f'''D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''' , index = False, header=True)
# print(f'''New file created at: D:\Programming Projects\MDC-COVID-19\{county}-COVID.csv''')
# # print(new_list)
#     # for row in db:
#     #     print(row)





