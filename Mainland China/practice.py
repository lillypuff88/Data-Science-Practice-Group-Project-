# https://www.geeksforgeeks.org/how-to-read-multiple-data-files-into-pandas/
import matplotlib.pyplot as plt 
import pandas as pd 



file_list=['01-22-2020.csv','01-23-2020.csv','01-24-2020.csv','01-25-2020.csv','01-26-2020.csv','01-27-2020.csv','01-28-2020.csv','01-29-2020.csv','01-30-2020.csv','01-31-2020.csv','02-01-2020.csv','02-02-2020.csv','02-03-2020.csv','02-04-2020.csv','02-05-2020.csv','02-06-2020.csv','02-07-2020.csv','02-08-2020.csv','02-09-2020.csv','02-10-2020.csv','02-11-2020.csv','02-12-2020.csv','02-13-2020.csv','02-14-2020.csv','02-15-2020.csv','02-16-2020.csv','02-17-2020.csv','02-18-2020.csv','02-19-2020.csv','02-20-2020.csv','02-21-2020.csv','02-22-2020.csv','02-23-2020.csv', '02-24-2020.csv','02-25-2020.csv','02-26-2020.csv','02-27-2020.csv','02-28-2020.csv','02-29-2020.csv','03-01-2020.csv'] 
  
allChina = pd.DataFrame()

for i in range (1, len(file_list)):
    
   
    df = pd.read_csv(file_list[i], usecols= ["Country/Region","Last Update","Confirmed", "Deaths", "Recovered"])
    rslt_df = df.loc[df['Country/Region'] == "Mainland China"]
    date=file_list[i].rsplit(".",maxsplit=1)[0]
    date=date.rsplit("-")
    a = date[0]
    b = date[1]
    date[0] = b
    date[1] = a
    date = date[0] + "-" + date[1] + "-" + date[2]
    rslt_df = rslt_df.assign(Date = date)
    allChina = pd.concat([rslt_df, allChina])
    print(rslt_df)

new_csv_data = allChina.to_csv('new.csv', index = True) 
print('\nCSV String:\n', new_csv_data) 

gr = pd.read_csv("new.csv")
confirmed1 = gr.groupby("Date")["Confirmed"].sum() 

gr1 = pd.read_csv("new.csv")
recovered1 = gr1.groupby("Date")["Recovered"].sum()

gr2 = pd.read_csv("new.csv")
death1 = gr2.groupby("Date")["Deaths"].sum()



lf = pd.read_csv("Daily Confirmed and Recovered.csv")
lf.plot(x = "Date", kind = "bar", stacked = False)
plt.ylabel("Number of People")
plt.figure(figsize=(10,6)) 
plt.show()


lf = pd.read_csv("Daily Deaths.csv")
lf.plot(x = "Date", kind = "bar", stacked = False)
plt.ylabel("Number of People")
plt.figure(figsize=(10,6)) 
plt.show()