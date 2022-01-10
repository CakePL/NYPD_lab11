import pandas as pd

iris = pd.read_csv("data/iris.csv")
varieties = iris["variety"].unique()
result = [iris[iris["variety"] == var] for var in varieties]

with pd.ExcelWriter("iris2.xlsx") as writer:
    for i in range(len(result)):
        result[i].to_excel(writer, sheet_name=varieties[i])

#świadomie zakładam, że kolumna variety powinna być dalej obecna w tabeli