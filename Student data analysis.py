#importing libraries
import pandas as pd

#Sample Student data
data={ 
        "Name":["Akash","John","Mina","Roy","Jack"],
        "Python":[96,89,91,76,87],
        "SQL":[94,88,75,86,91],
        "ML":[89,91,82,79,90]
}
df=pd.DataFrame(data)

#Calculate average marksk
df["Average"]=df[["Python", "SQL", "ML"]].mean(axis=1)

#Find topper
topper=df.loc[df["Average"].idxmax()]

print("Student data\n")
print(df)

print("topper:")
print(topper)