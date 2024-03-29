
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = pd.read_excel("miuul_gezinomi.xlsx")


def check_data(dataframe,head=10,tail=10):
    """
    It gives information about shape of the dataframe, type of its variables, first 5 observations, last 5 observations, total number of missing observations.
    Parameters
    ----------
    dataframe : dataframe
        The dataframe whose properties will be defined
    head : int,optional
       Refers to the number of observations that will be displayed from the beginning and end
    tail : int,optional

    Returns
    -------
     None

    Examples
    -------
    check_data(df,10,10)

     Notes
     -------
        The number of observations to be viewed from the end is the same as the number of observations to be observed from the beginning.
    """

    print("####### Head #######")
    print(dataframe.head())
    print("####### Types #####")
    print(dataframe.dtypes)
    print("###### Shape ######")
    print(dataframe.shape)
    print("####### NA #######")
    print(dataframe.isnull.sum())
    print("####### Tail ########")
    print(dataframe.tail())
    
for col in df.columns:
    print(check_data(df,col))

a=df["SaleCityName"].nunique()
b=df["SaleCityName"].value_counts()

df["ConceptName"].nunique()
x=df["ConceptName"].value_counts()

df.groupby("SaleCityName").agg({"Price":"sum"})
df.groupby("ConceptName").agg({"Price":"sum"})
df.groupby("SaleCityName").agg({"Price":"mean"})
df.groupby("ConceptName").agg({"Price": "mean"})
df.groupby(["SaleCityName", 'ConceptName']).agg({"Price": "mean"})

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)


df.groupby(["SaleCityName","ConceptName","EB_Score"]).agg({"Price": ["mean","count"]})
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

agg_df=df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price",ascending=False)

agg_df.reset_index(inplace=True)
agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

agg_df.sort_values(by="Price")

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]




