import pandas as pd
from datetime import date, timedelta


sdate = date(2020, 3, 22)   # start date
edate = date.today() - timedelta(days=1)  # end date || currently set to yesterday's date because it turned to midnight and I was getting an error cause JHU did not publish it yet for 3/28


delta = edate - sdate       # as timedelta

new_list = []


for i in range(delta.days + 1):
    date = sdate + timedelta(days=i)

    month = date.month
    if len(str(month))<2:
        month = '0'+str(month)
        

    day = date.day
    if len(str(day))<2:
        day = '0'+str(day)

    url = f'''https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{month}-{day}-2020.csv'''
    db = pd.read_csv(url, error_bad_lines=False)
    df = pd.DataFrame(db)
    # print(url)
    
    location = df.loc[df['Admin2']=='Miami-Dade'].index[0]
    print(location)
    cell = df['Confirmed'][location]
    print(cell)



    # for row in db:
    #     print(row)





