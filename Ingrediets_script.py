############ Script to Prepare Data for Visualization using TABLEAU ################

import pandas as pd

df= pd.read_csv("chocolate-2.csv")

print(df.Country.unique())
print(df.Type.unique())
print(df.Flavor.unique())
print(df.Source.unique())
print(df.Strain.unique())

'''l=df['Ingredients']

ch=l.isnull()
l=l.tolist()
dic={}
s=[]
c=1
for i in range(0,len(ch)):
	if ch[i] == True:
		continue
	if type(df.Type[i])== float:
		continue
	s.append(df.Type[i].strip())
s=set(s)
s= list(s)

for i in range(0,len(s)):
	for j in range(0,len(l)):
		if ch[j]==True:
			continue
		if df['Rating'][j]<4:
			continue
		if df['Type'][j] != s[i]:
			continue
		temp=l[j].strip().split(", ")
		for k in temp:
			if k in dic:
				dic[k]=dic[k]+1
			else:
				dic[k]=1
	df1= pd.DataFrame()
	f=[]
	d=[]
	res=[]
	for b in dic:
		if(dic[b]<5):
			continue
		d.append(b)
		f.append(dic[b])
	for b in range(0,len(d)):
		for e in range(0,f[b]):
			res.append(d[b])
	df1['ingredients']=res
	df1.to_csv("ingredients_"+s[i]+ ".csv", columns=['ingredients'])

for j in range(0,len(l)):
	if ch[j]==True:
		continue
	if df['Rating'][j]<4:
		continue
	temp= l[j].strip().split(", ")
	for i in temp:
		if i in dic:
			dic[i]=dic[i]+1
		else:
			dic[i]=1

df1= pd.DataFrame()
f=[]
d=[]
res=[]
for i in dic:
	if(dic[i]<5):
		continue
	d.append(i)
	f.append(dic[i])
for i in range(0,len(d)):
	for j in range(0,f[i]):
		res.append(d[i])
df1['ingredients']=res
df1.to_csv("text.csv", columns=['ingredients'])'''