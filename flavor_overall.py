import pandas as pd

df= pd.read_csv("chocolate-2.csv")
dic={'appearance':0.0,'aroma':0.0,'mouthfeel':0.0,'flavor':0.0,'quality':0.0}

app=list(df['Appearance_Rating'])
ch_app= pd.isnull(app)
aroma=list(df['Aroma_Rating'])
ch_aroma= pd.isnull(aroma)
mouthfeel=list(df['Mouthfeel_Rating'])
ch_mouthfeel= pd.isnull(mouthfeel)
flavor=list(df['Flavor_Rating'])
ch_flavor= pd.isnull(flavor)
quality=list(df['Quality_Rating'])
ch_quality= pd.isnull(quality)
rate =list(df['Rating'])
ch_rate= pd.isnull(rate)

for i in range(0,len(rate)):
	if rate[i] <4 :
		continue
	if ch_app[i] ==False and ch_rate[i]==False:
		dic['appearance']= dic['appearance']+abs(rate[i]-app[i])
	if ch_aroma[i] ==False and ch_rate[i]==False:
		dic['aroma']= dic['aroma']+ abs(rate[i]-aroma[i])
	if ch_mouthfeel[i] ==False and ch_rate[i]==False:
		dic['mouthfeel']= dic['mouthfeel']+ abs(rate[i]-mouthfeel[i])
	if ch_flavor[i] ==False and ch_rate[i]==False:
		dic['flavor']= dic['flavor']+ abs(rate[i]-flavor[i])
	if ch_quality[i] ==False and ch_rate[i]==False:
		dic['quality']= dic['quality']+ abs(rate[i]-quality[i])

df1= pd.DataFrame()
df1['attribute']=[i for i in dic]
temp=[]
for i in dic:
	temp.append(dic[i])
df1['diff']=temp
df1=df1.sort_values(by=['diff'])
l= list(df1['diff'])
l.reverse()
df1['diff']=l
df1.to_csv("top_attributes.csv", index=None)