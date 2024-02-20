#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

#Importing Data
Data = pd.read_csv(r"C:\Users\ADMIN\OneDrive\Desktop\Amazon Sale Report.csv")

# To check the dimension of the dataset i.e Number of rows and columns
Data.shape

#To check Top Rows
Data.head()

#To checking the bottom rows
Data.tail()

Data.info()

#To drop unrelated/Blank column
Data.drop(["New", "PendingS"],axis = 1 , inplace = True)

Data.info()

#To check Null Values in Dataset
Data.isna().sum()

#To drop null values
Data.dropna(inplace = True)

Data.shape

#To check column names
Data.columns

#To change the datatype
Data["ship-postal-code"] = Data["ship-postal-code"].astype("int")

Data["Date"] = pd.to_datetime (Data["Date"])

Data.info()

#To rename columns
Data.rename(columns={"Qty": "Quantity"})

#Returns the Description of the data present in the dataframe for numerical columns
Data.describe() 

Data.describe(include = "object")

#To describe specific column
Data[["Qty"]].describe()


df = sns.countplot(x = "Size", data=Data)

# To show the labels on bars (used for loops)
df = sns.countplot(x = "Size", data=Data)
for bars in df.containers:
    df.bar_label(bars)

#From the above graph we can see that most of the people buys M-size

Data.groupby(["Size"], as_index = False)["Qty"].sum().sort_values(by = "Qty", ascending = False)

S_Qty = Data.groupby(["Size"], as_index = False)["Qty"].sum().sort_values(by = "Qty", ascending = False)
sns.barplot(x = "Size", y = "Qty", data = S_Qty)

#The graph above shows that the majority of quantity purchases by M-size in sales

plt.figure(figsize = (10,5))
ax = sns.countplot(data = Data, x = "Courier Status", hue = "Status")
plt.show()

#From the above graph majority of the orders are shipped through the courier

#Histogram
Data.Size.hist()

Data["Category"] = Data["Category"].astype(str)
Category_date = Data["Category"]
plt.figure(figsize = (10,5))
plt.hist(Category_date, bins = 30, edgecolor = "Black")
plt.xticks(rotation = 90)
plt.show()


# From the above graph shows that the most of the buyers are form the T-shirt

B2B_check = Data["B2B"].value_counts()
plt.pie(B2B_check, labels = B2B_check.index, autopct = "%1.1f%%")
plt.show()

#From the above graph we can see that the maximum i.e 99.2% are from retailers and 0.8% are from B2B buyers.

#Scatter Plot
x_data = Data["Category"]
y_data = Data["Size"]
plt.scatter(x_data, y_data)
plt.xlabel("Category")
plt.ylabel("Size")
plt.title("Scatter Plot")
plt.show()

#Count of cities by state
plt.figure(figsize = (10,6))
sns.countplot(data = Data, x= "ship-state")
plt.xlabel("ship-state")
plt.ylabel("count")
plt.xticks(rotation = 90)
plt.show()

#Top 10 states
Top_10_States = Data["ship-state"].value_counts().head(12)
plt.figure(figsize =(12,6))
sns.countplot(data = Data[Data["ship-state"].isin(Top_10_States.index)], x = "ship-state")
plt.xlabel("ship-state")
plt.ylabel("count")
plt.title("Distribution of state")
plt.xticks(rotation = 45)
plt.show()

# From the above graph we can see that the most of the buyers are from Maharashtra state.


# # The Data analysis shows that the company serves a significant number of merchants in Maharashtra State, fulfills orders through the company, experiences a large demand for T-shirts, and appears that M-size is the preferred size among customers.
