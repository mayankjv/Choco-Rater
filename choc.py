import pandas as pd

df= pd.read_csv("chocolate-2.csv")

l=df['Ingredients']

ch=l.isnull()
l=l.tolist()
dic={}

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
df1.to_csv("text.csv", columns=['ingredients'])