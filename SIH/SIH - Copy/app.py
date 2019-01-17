from flask import Flask, redirect,url_for, request, render_template, session, abort
import os
#from tabledef import *
import numpy as np
import pandas as pd
from bokeh.plotting import figure,output_file,show
from bokeh.resources import CDN
from bokeh.embed import components
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import datetime

app=Flask(__name__)
'''@app.route('/')
def main():
	if request.method=='POST':
		return render_template('user.html')
	return render_template('dashboard.html')
'''
@app.route('/sample')
def get_data():
   if request.method=='POST':
               first_name=request.form['sID']
               last_name=request.form['review']
               typeofmeal=request.form.get("country")
               rating = request.form.get("star")
               connection = mysql.get_db()
               cursor = connection.cursor()
               query="INSERT INTO names_tb2(studID,review,Meal,rate) VALUES(%s,%s,%s,%s)"
               cursor.execute(query,(first_name,last_name,typeofmeal,rating))
               connection.commit()
   return render_template("sample.html")


@app.route('/b')

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
 #-------
 print('mess')
 print(mess0df.head())
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
 #--------
 wastestatsB1=wastagedf_B.groupby('Meal_1')['Wastage_1'].sum()
 wastestatsB2=wastagedf_B.groupby('Meal_2')['Wastage_2'].sum()
 wastestatsB3=wastagedf_B.groupby('Meal_3')['Wastage_3'].sum()

 wastestatsL1=wastagedf_L.groupby('Meal_1')['Wastage_1'].sum()
 wastestatsL2=wastagedf_L.groupby('Meal_2')['Wastage_2'].sum()
 wastestatsL3=wastagedf_L.groupby('Meal_3')['Wastage_3'].sum()

 wastestatsD1=wastagedf_D.groupby('Meal_1')['Wastage_1'].sum()
 wastestatsD2=wastagedf_D.groupby('Meal_2')['Wastage_2'].sum()
 wastestatsD3=wastagedf_D.groupby('Meal_3')['Wastage_3'].sum()

 print("wastage for Breakfast Menu1,2,3")
 print(wastestatsB1)
 print(wastestatsB2)
 print(wastestatsB3)

 wastage_concated_df=pd.concat([wastestatsB1,wastestatsB2,wastestatsB3])
 wastage_concated_df1=pd.concat([wastestatsL1,wastestatsL2,wastestatsL3])
 wastage_concated_df2=pd.concat([wastestatsD1,wastestatsD2,wastestatsD3])
 print("hello")
 print(wastage_concated_df)
 minimun_breakfast_wastage=wastage_concated_df.idxmin(axis=0)
 maximum_breakfast_wastage=wastage_concated_df.idxmax(axis=0)
 minimun_lunch_wastage=wastage_concated_df1.idxmin(axis=0)
 maximum_lunch_wastage=wastage_concated_df1.idxmax(axis=0)
 minimun_dinner_wastage=wastage_concated_df2.idxmin(axis=0)
 maximum_dinner_wastage=wastage_concated_df2.idxmax(axis=0)
 print("hi")
 print(minimun_breakfast_wastage)
 minimun_breakfast_wastage=' Least wasted item in last 7 days for Breakfast :: {:s}'.format(minimun_breakfast_wastage)
 maximum_breakfast_wastage=' Maximum wasted item in last 7 days for Breakfast :: {:s}'.format(maximum_breakfast_wastage)


 minimun_lunch_wastage=' Least wasted item in last 7 days for Lunch :: {:s}'.format(minimun_lunch_wastage)
 maximum_lunch_wastage=' Maximum wasted item in last 7 days for Lunch :: {:s}'.format(maximum_lunch_wastage)


 minimun_dinner_wastage=' Least wasted item in last 7 days for Dinner :: {:s}'.format(minimun_dinner_wastage)
 maximum_dinner_wastage=' Maximum wasted item in last 7 days for Dinner :: {:s}'.format(maximum_dinner_wastage)







 

 #wastage_breakfast=



 # Return the webpage
 return render_template('vis.html',script0=script0, div0=div0,script1=script1, div1=div1,script2=script2, div2=div2,script3=script3, div3=div3,div4=div4,script4=script4,minimun_breakfast_wastage=minimun_breakfast_wastage,maximum_breakfast_wastage=maximum_breakfast_wastage,minimun_lunch_wastage=minimun_lunch_wastage, maximum_lunch_wastage=maximum_lunch_wastage,minimun_dinner_wastage=minimun_dinner_wastage,maximum_dinner_wastage=maximum_dinner_wastage,bokeh_css=CDN.render_css(),bokeh_js=CDN.render_js())
#generates table for all 4 messes for last 3 meals for each mess.
@app.route('/generatetable')
def generatetable():
    df=pd.read_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\sihnewdata.csv')
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
    #print dfnew.head()
    return dfnew.to_html()

@app.route('/predict',methods=['GET','POST'])
def predict():
	global quantitydf
	menudf=pd.read_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\Menu_planner.csv')
	consumptiondf=pd.read_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\consumption.csv')
	now=datetime.datetime.now()
	
	daytoday=now.weekday()
	print(daytoday)
	print(menudf.iloc[daytoday,:])
	menutoday=pd.Series(menudf.iloc[daytoday,:])
	print("blah blah")
	print("menu")
	print(menutoday)
	print(type(menutoday))




	data={}
	if request.form:
		form_data=request.form
		data['form']=form_data
		predict_class=form_data['predict_class']
		predict_age=form_data['predict_age']
		predict_sibsp=form_data['predict_sibsp']

		if predict_class=='Exam':
			Special_Occasion_Exam=1
			Special_Occasion_Fest=0
			Special_Occasion_Regular=0
			Special_Occasion_Other_Holidays=0
			Special_Occasion_Sem_Break=0
		
		elif predict_class=='Fest':
			Special_Occasion_Exam=0
			Special_Occasion_Fest=1
			Special_Occasion_Regular=0
			Special_Occasion_Other_Holidays=0
			Special_Occasion_Sem_Break=0
		else:
			Special_Occasion_Exam=0
			Special_Occasion_Fest=0
			Special_Occasion_Regular=1
			Special_Occasion_Other_Holidays=0
			Special_Occasion_Sem_Break=0

		if predict_age=='B':
			Type_Of_Meal_B=1
			Type_Of_Meal_L=0
			Type_Of_Meal_D=0
			menutoday=menutoday[:3]

		
		elif predict_age=='L':
			Type_Of_Meal_B=0
			Type_Of_Meal_L=1
			Type_Of_Meal_D=0
			menutoday=menutoday[3:6]
		else:
			Type_Of_Meal_B=0
			Type_Of_Meal_L=0
			Type_Of_Meal_D=1
			menutoday=menutoday[6:]
		print(menutoday)


			

		if predict_sibsp=='Today':
			now=datetime.datetime.now()

			weekday1=now.weekday()
			print("what weekday")
			print(weekday1)
			if weekday1==0:
				weekday_0=1
				weekday_1=0
				weekday_2=0
				weekday_3=0
				weekday_4=0
				weekday_5=0
				weekday_6=0

			elif weekday1==1:
				weekday_0=0
				weekday_1=1
				weekday_2=0
				weekday_3=0
				weekday_4=0
				weekday_5=0
				weekday_6=0

			else:
				weekday_0=0
				weekday_1=0
				weekday_2=1
				weekday_3=0
				weekday_4=0
				weekday_5=0
				weekday_6=0
		if predict_sibsp=='Today':
			now=datetime.datetime.now()

			month=now.month
			if month!=12:
				month_01=1
				month_02=0
				month_03=0
				month_04=0
				month_05=0
				month_06=0
				month_07=0
				month_08=0
				month_09=0
				month_10=0
				month_11=0
				month_12=0
			else:
				month_12=1
				month_01=0
				month_02=0
				month_03=0
				month_04=0
				month_05=0
				month_06=0
				month_07=0
				month_08=0
				month_09=0
				month_10=0
				month_11=0
				

		input_data=np.array([Special_Occasion_Exam,Special_Occasion_Fest,Special_Occasion_Other_Holidays,Special_Occasion_Regular,Special_Occasion_Sem_Break,Type_Of_Meal_B,Type_Of_Meal_D,Type_Of_Meal_L,weekday_0,
			weekday_1,weekday_2,weekday_3,weekday_4,weekday_5,weekday_6,month_01,month_12,month_02,month_03,month_04,month_05,month_06,month_07,month_08,month_09,month_10,month_11])

		#Special_Occasion,Date,No_of_Students_in_Hostel,No_of_Actual_Diners,Mess_No,New_Menu,Food_Prepared_By1,Food_Prepared_By2,Food_Prepared_By3,Meal_1,Wastage_1,Meal_2,Wastage_2,Meal_3,Wastage_3,Type_Of_Meal,Total Wastage
		'''[u'Special_Occasion_Exam', u'Special_Occasion_Fest',
       u'Special_Occasion_Other-Holidays', u'Special_Occasion_Regular',
       u'Special_Occasion_Sem-Break', u'Type_Of_Meal_B', u'Type_Of_Meal_D',
       u'Type_Of_Meal_L', u'weekday_0', u'weekday_1', u'weekday_2',
       u'weekday_3', u'weekday_4', u'weekday_5', u'weekday_6', u'month_01',
       u'month_02', u'month_03', u'month_04', u'month_05', u'month_06',
       u'month_07', u'month_08', u'month_09', u'month_10', u'month_11',
       u'month_12'],'''
		prediction=int(regr.predict(input_data.reshape(1,-1)))
		data['prediction']='{:d} Number of students expected to dine'.format(prediction)
		for i in range(len(consumptiondf)):
			if consumptiondf.iloc[i,0]==menutoday[0]:
				I1q=consumptiondf.iloc[i,2]*prediction
				I2q=consumptiondf.iloc[i,4]*prediction
				I3q=consumptiondf.iloc[i,6]*prediction
			elif consumptiondf.iloc[i,0]==menutoday[1]:
				I1q=consumptiondf.iloc[i,2]*prediction
				I2q=consumptiondf.iloc[i,4]*prediction
				I3q=consumptiondf.iloc[i,6]*prediction
			else :
				I1q=consumptiondf.iloc[i,2]*prediction
				I2q=consumptiondf.iloc[i,4]*prediction
				I3q=consumptiondf.iloc[i,6]*prediction
		print(I1q)
		print(I2q)
		print(I3q)

		list1=[[consumptiondf.iloc[i,1],I1q],[consumptiondf.iloc[i,3],I2q],[consumptiondf.iloc[i,5],I3q]]
		
		print list1

		#global quantitydf
		quantitydf=pd.DataFrame(list1)
		quantitydf.columns=['Ingredient','Quantity to Be used']
		quantitydf.to_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\q.csv',index=False)
		#print(quantitydf) 






	return render_template('titanic_finished.html',data=data)
	month=[]
	for i in range(len(df)):
		month.append(df.iloc[i,1].split('-')[1])

@app.route('/tablequant')
def tablequant():
	quantitydf=pd.read_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\q.csv')
	#global quantitydf
	print(quantitydf)
	return quantitydf.to_html()

if __name__=='__main__':

	titanic_df=pd.read_csv('C:\Users\sunil\OneDrive\Documents\SIH\static\sihnewdata.csv')
	#quantitydf=titanic_df
	print("hi")
	print(titanic_df.head())
	df=titanic_df.iloc[:,[0,1,2,15]]
	import datetime
	df['weekday']=pd.to_datetime(df['Date']).apply(lambda x:x.weekday())
	month=[]
	for i in range(len(df)):
		month.append(df.iloc[i,1].split('-')[1])
	df['month']=month
	print(df.head())
	dummies1=pd.get_dummies(df['Special_Occasion'],prefix='Special_Occasion',prefix_sep='_')
	dummies2=pd.get_dummies(df['Type_Of_Meal'],prefix='Type_Of_Meal',prefix_sep='_')
	dummies3=pd.get_dummies(df['weekday'],prefix='weekday',prefix_sep='_')
	dummies4=pd.get_dummies(df['month'],prefix='month',prefix_sep='_')
	
	dffin=pd.concat([dummies1,dummies2,dummies3,dummies4],axis=1)
	print("dffin values")
	print(dffin.columns)
	target=df['No_of_Students_in_Hostel']
	from sklearn import linear_model
	print('model_build_print')
	regr=linear_model.LogisticRegression()
	regr.fit(dffin,target)
	app.secret_key=os.urandom(12)
	app.run(host='0.0.0.0',port=7000)	


				








