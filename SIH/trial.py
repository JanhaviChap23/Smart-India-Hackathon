
import numpy as np # Import the numpy numerical library
import pandas as pd # Import your pet panda
#from waitress import serve
# Build the dataframe
from flask import Flask, render_template
app = Flask(__name__)
from bokeh.plotting import figure,output_file,show
from bokeh.resources import CDN
from bokeh.embed import components
import pandas as pd

@app.route("/")
def visualisation():
 # Build the dataframe
 df=pd.read_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\sihnewdata.csv')
 #print df.head(10)
 #for mess 0
 mess0df=df[df['Mess_No']==0]
 mess0df=df.iloc[-21:,:]
 li=[]
 for i in range(0,len(mess0df)):
     li.append(i)    

 #source = ColumnDataSource(df)
 # Create the plot
 plot = plot = figure(plot_width=590, plot_height=120)
 #plot.multi_line(x=[li, df['No_of_Students_in_Hostel']] , y=[li, df['No_of_Actual_Diners']], color=['red','green'])
 plot.line(x=li,y=mess0df['No_of_Actual_Diners'],color='green')
 plot.line(x=li,y=mess0df['No_of_Students_in_Hostel'],color='red')
 #show(plot)
 # Generate the script and HTML for the plot
 script0, div0 = components(plot)
 
 #-------------
  #for mess 1
 mess1df=df[df['Mess_No']==1]
 mess1df=mess1df.iloc[-21:,:]
 li=[]
 for i in range(0,len(mess1df)):
     li.append(i)    

 #source = ColumnDataSource(df)
 # Create the plot
 plot1  = figure(plot_width=590, plot_height=120)
 plot1.line(x=li,y=mess1df['No_of_Actual_Diners'],color='green')
 plot1.line(x=li,y=mess1df['No_of_Students_in_Hostel'],color='red')
 #show(plot)
 # Generate the script and HTML for the plot
 script1, div1 = components(plot1)
 #----------------
 #for mess 2
 mess2df=df[df['Mess_No']==2]
 mess2df=mess2df.iloc[-21:,:]
 li=[]
 for i in range(0,len(mess2df)):
     li.append(i)    

 #source = ColumnDataSource(df)
 # Create the plot
 plot2  = figure(plot_width=590, plot_height=120)
 plot2.line(x=li,y=mess2df['No_of_Actual_Diners'],color='green')
 plot2.line(x=li,y=mess2df['No_of_Students_in_Hostel'],color='red')
 #show(plot)
 # Generate the script and HTML for the plot
 script2, div2 = components(plot2)
 #----------------
  #for mess 3 or use a group by(better way to do it but this is okay for basic version-will enhance later)
 mess3df=df[df['Mess_No']==3]
 mess3df=mess3df.iloc[-21:,:]
 li=[]
 for i in range(0,len(mess3df)):
     li.append(i)    

 #source = ColumnDataSource(df)
 # Create the plot
 plot3  = figure(plot_width=590, plot_height=120)
 plot3.line(x=li,y=mess3df['No_of_Actual_Diners'],color='green')
 plot3.line(x=li,y=mess3df['No_of_Students_in_Hostel'],color='red')
 #show(plot)
 # Generate the script and HTML for the plot
 script3, div3 = components(plot3)

#------------

 wastagedf_B=mess0df[mess0df.Type_Of_Meal=='B']
 wastagedf_B=wastagedf_B.iloc[-7:,:]
 print("wastage")
 print(wastagedf_B)
 wastagedf_L=mess0df[mess0df.Type_Of_Meal=='L']
 wastagedf_L=wastagedf_L.iloc[-7:,:]
 wastagedf_D=mess0df[mess0df.Type_Of_Meal=='D']
 wastagedf_D=wastagedf_D.iloc[-7:,:]

 plot_wastage  = figure(plot_width=590, plot_height=120)
 plot_wastage.line(x=[1,2,3,4,5,6,7],y=wastagedf_B['Total Wastage'],color='green')
 plot_wastage.line(x=[1,2,3,4,5,6,7],y=wastagedf_L['Total Wastage'],color='red')
 plot_wastage.line(x=[1,2,3,4,5,6,7],y=wastagedf_D['Total Wastage'],color='blue')
 #show(plot)
 #Generate the script and HTML for the plot
 script4, div4 = components(plot_wastage)

#---------
 wastestatsB1=wastagedf_B.groupby('Meal_1')['Wastage_1'].sum()
 wastestatsB2=wastagedf_B.groupby('Meal_2')['Wastage_2'].sum()
 wastestatsB3=wastagedf_B.groupby('Meal_3')['Wastage_3'].sum()

 print("wastage for Breakfast Menu1,2,3")
 print(wastestatsB1)
 print(wastestatsB2)
 print(wastestatsB3)
 # Return the webpage

 return render_template('vis.html',script0=script0, div0=div0,script1=script1, div1=div1,script2=script2, div2=div2,script3=script3, div3=div3,bokeh_css=CDN.render_css(),bokeh_js=CDN.render_js())
#generates table for all 4 messes for last 3 meals for each mess.
@app.route('/generatetable')
def generatetable():
    df=pd.read_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\sihdata.csv')
    #print df.head()
    dfnew=df[['Mess_No','Date','Type_Of_Meal','No_of_Students_in_Hostel','No_of_Actual_Diners']]
    dfnew['Students in Hostel']=dfnew['No_of_Students_in_Hostel']
    dfnew['Actual Diners']=dfnew['No_of_Actual_Diners']
    dfnew['Meal Type']=dfnew['Type_Of_Meal']
    dfnew=dfnew.drop('No_of_Actual_Diners',axis=1)
    dfnew=dfnew.drop('No_of_Students_in_Hostel',axis=1)
    dfnew=dfnew.drop('Type_Of_Meal',axis=1)
    dfnew=dfnew.iloc[-12:]
    #print dfnew.head()
    return dfnew.to_html()
    #return render_template('vis.html',tables=[dfnew.to_html()],titles = ['na', 'Female surfers'])
   #return render_template('content.html', text=df)
@app.route('/t')
def t():
	return render_template('vis.html')
if __name__ == "__main__":
 app.run(debug=True)
 #serve(app)