import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures

poly= PolynomialFeatures(degree=2)

reg=RandomForestRegressor(max_depth=2,random_state=0)

df= pd.read_csv("chocolate-2.csv", names=['_BarId','Bar_Name','Maker','Country','Type','Flavor','Source','Strain','Rating','Type_More_Info','Strain_More_Info','Source_More_Info','Flavor_More_Info','Style','Appearance_Rating','Appearance_Overall','Appearance_Color','Appearance_Surface','Appearance_Temper','Appearance_Snap','Aroma_Rating','Aroma_Overall','Mouthfeel_Rating','Mouthfeel_Overall','Mouthfeel_Texture','Mouthfeel_Melt','Flavor_Rating','Flavor_Overall','Quality_Rating','Quality_Overall','Ingredients'])
#print(df.head())

##### country type flavor source strain  ########
le =LabelEncoder()

print("::::::::::::::::::::::REFER THE BELOW COUNTRY CODES::::::::::::::::::")
t=list(df['Country'])
le.fit(t)
has=[]
count=[]
dfc= pd.DataFrame()
#country=list(le.classes_)
country=le.transform(df['Country'])
for i in range(1,len(country)):
	if country[i] in has:
		continue
	else:
		count.append(t[i])
		has.append(country[i])
dfc['country']=count
dfc['code']=has
dfc=dfc.sort_values('code')
print(dfc)


print("::::::::::::::::::::::REFER THE BELOW TYPE CODES::::::::::::::::::")
t=list(df['Type'])
le.fit(list(df['Type']))
has=[]
count=[]
dft= pd.DataFrame()
#typ=list(le.classes_)
typ=le.transform(list(df['Type']))
for i in range(1,len(typ)):
	if typ[i] in has:
		continue
	else:
		count.append(t[i])
		has.append(typ[i])
dft['Type']=count
dft['code']=has
dft=dft.sort_values('code')
print(dft)



print("::::::::::::::::::::::REFER THE FLAVOR COUNTRY CODES::::::::::::::::::")
t=list(df['Flavor'])
le.fit(list(df['Flavor']))
has=[]
count=[]
dff= pd.DataFrame()
#flavor=list(le.classes_)
flavor=le.transform(list(df['Flavor']))
for i in range(1,len(flavor)):
	if flavor[i] in has:
		continue
	else:
		count.append(t[i])
		has.append(flavor[i])
dff['Flavour']=count
dff['code']=has
dff=dff.sort_values('code')
print(dff)


print("::::::::::::::::::::::REFER THE BELOW SOURCE CODES::::::::::::::::::")
t=list(df['Source'])
le.fit(list(df['Source']))
has=[]
count=[]
dfs= pd.DataFrame()
#flavor=list(le.classes_)
source=le.transform(list(df['Source']))
for i in range(1,len(source)):
	if source[i] in has:
		continue
	else:
		count.append(t[i])
		has.append(source[i])
dfs['Source']=count
dfs['code']=has
dfs=dfs.sort_values('code')
print(dfs)


print("::::::::::::::::::::::REFER THE BELOW STRAIN CODES::::::::::::::::::")
t=list(df['Strain'])
le.fit(list(df['Strain']))
has=[]
count=[]
dfS= pd.DataFrame()
#flavor=list(le.classes_)
strain=le.transform(list(df['Strain']))
for i in range(1,len(strain)):
	if strain[i] in has:
		continue
	else:
		count.append(t[i])
		has.append(strain[i])
dfS['Strain']=count
dfS['code']=has
dfS=dfS.sort_values('code')
print(dfS)


df1= pd.DataFrame()
df1['country']=country[1:]
df1['typ']=typ[1:]
df1['flavor']=flavor[1:]
df1['source']=source[1:]
df1['strain']=strain[1:]

rate=[]
temp=list(df['Rating'])
for i in temp:
	if i=='Rating':
		continue
	rate.append(float(i))
	df2= pd.DataFrame()
print("Enter Country Code:", end="")
df2['country']=[int(input())]
print("Enter Type Code:", end="")
df2['typ']=[int(input())]
print("Enter Flavor Code:", end="")
df2['flavor']=[int(input())]
print("Enter Source Code:", end="")
df2['source']=[int(input())]
print("Enter Strain Code:", end="")
df2['strain']=[int(input())]

reg.fit(df1,rate)
pred=reg.predict(df2)

print("The Rating of the chocolate bar with the Provided credentials is ",pred[0])