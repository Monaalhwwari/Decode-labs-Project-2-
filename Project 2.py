import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Dataset_for_Data_Analytics.xlsx")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

df.columns = df.columns.str.strip()

df["OrderID"]=df["OrderID"].astype(str).str.lower().str.strip()
df["Date"]=pd.to_datetime(df["Date"])
df["CustomerID"]=df["CustomerID"].astype(str).str.lower().str.strip()
df["Product"]=df["Product"].astype(str).str.lower().str.strip()
df["Quantity"]=pd.to_numeric(df["Quantity"])
df["UnitPrice"]=pd.to_numeric(df["UnitPrice"])
df["ShippingAddress"]=df["ShippingAddress"].astype(str).str.lower().str.strip()
df["PaymentMethod"]=df["PaymentMethod"].astype(str).str.lower().str.strip()
df["OrderStatus"]=df["OrderStatus"].astype(str).str.lower().str.strip()
df["TrackingNumber"]=df["TrackingNumber"].astype(str).str.lower().str.strip()
df["ItemsInCart"]=pd.to_numeric(df["ItemsInCart"])
df["CouponCode"]=df["CouponCode"].astype(str).str.lower().str.strip()
df["ReferralSource"]=df["ReferralSource"].astype(str).str.lower().str.strip()
df["TotalPrice"]=pd.to_numeric(df["TotalPrice"])

df = df.dropna(subset=["OrderID","Date","CustomerID","Product","Quantity","UnitPrice","ShippingAddress","PaymentMethod","OrderStatus","TrackingNumber","ItemsInCart","CouponCode","ReferralSource","TotalPrice"
])

#analysis

med_quantity = df["Quantity"].median()
med_unit = df["UnitPrice"].median()
med_itemsincart=df["ItemsInCart"].median()
med_totalprice = df["TotalPrice"].median()

max_quantity = df["Quantity"].max()
max_unit = df["UnitPrice"].max()
max_itemsincart = df["ItemsInCart"].max()
max_totalprice = df["TotalPrice"].max()

min_quantity = df["Quantity"].min()
min_unit = df["UnitPrice"].min()
min_itemsincart = df["ItemsInCart"].min()
min_totalprice = df["TotalPrice"].min()

std_quantity = df["Quantity"].std()
std_unit = df["UnitPrice"].std()
std_itemsincart = df["ItemsInCart"].std()
std_totalprice = df["TotalPrice"].std()

mean_quantity = df["Quantity"].mean()
mean_unit = df["UnitPrice"].mean()
mean_itemsincart = df["ItemsInCart"].mean()
mean_totalprice = df["TotalPrice"].mean()

# Analysis Summary

print("Exploratory Data Analysis Summary")
print(f"Quantity  min:{min_quantity}, median:{med_quantity}, mean:{mean_quantity:.2f}, max:{max_quantity}, std:{std_quantity:.2f}")
print(f"UnitPrice  min:{min_unit}, median:{med_unit}, mean:{mean_unit:.2f}, max:{max_unit}, std:{std_unit:.2f}")
print(f"ItemsInCart  min:{min_itemsincart}, median:{med_itemsincart}, mean:{mean_itemsincart:.2f}, max:{max_itemsincart}, std:{std_itemsincart:.2f}")
print(f"TotalPrice  min:{min_totalprice}, median:{med_totalprice}, mean:{mean_totalprice:.2f}, max:{max_totalprice}, std:{std_totalprice:.2f}")


# histogram for Quantity
df["Quantity"].hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.savefig("quantity_Hist.png")
plt.close()

# histogram for UnitPrice
df["UnitPrice"].hist(bins=20, color="skyblue", edgecolor="black")
plt.title("UnitPrice histogram")
plt.savefig("unitprice_Hist.png")
plt.close()

# histogram for totalprice
df["TotalPrice"].hist(bins=20, color="skyblue", edgecolor="black")
plt.title("TotalPrice histogram")
plt.savefig("totalprice_Hist.png")
plt.close()

# boxplot for UnitPrice
sns.boxplot(x=df["UnitPrice"], color="lightgreen")
plt.title("UnitPrice Boxplot")
plt.savefig("unitprice_Box.png")
plt.close()

# boxplot for totalrpice
sns.boxplot(x=df["TotalPrice"], color="lightgreen")
plt.title("TotalPrice Boxplot")
plt.savefig("TotalPrice_Box.png")
plt.close()

# boxplot for quantity
sns.boxplot(x=df["Quantity"], color="lightgreen")
plt.title("Quantity Boxplot")
plt.savefig("Quantity_Box.png")
plt.close()


correlation_Items_and_TotalPrice= df[["ItemsInCart","TotalPrice"]].corr()
correlation_quantity_and_UnitPrice = df[["Quantity","UnitPrice"]].corr()

# heatmap for correlation_quantity_and_UnitPrice

plt.figure(figsize=(8,6))
sns.heatmap(correlation_quantity_and_UnitPrice, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("correlation_quantity_and_UnitPrice.png")
plt.close()

# heatmap for correlation_Items_and_TotalPrice

plt.figure(figsize=(8,6))
sns.heatmap(correlation_Items_and_TotalPrice, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("correlation_Items_and_TotalPrice.png")
plt.close()
