import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('month', type=str)
parser.add_argument('year', type=str)

args = parser.parse_args()
month = args.month
year = args.year

outcome_data = pd.read_excel(rf"C:\Users\vurva\Downloads\outcome_{month}.{year}.xlsx")
outcome_data["День"] = [int(x.split()[0]) for x in outcome_data["Дата"]]

fig, ax = plt.subplots(constrained_layout=True)
sns.lineplot(
    data = outcome_data,
    x = "День",
    y = "Сумма",
    hue = "Категория",
    ax = ax
)

ax.legend()
plt.show()

fig, ax = plt.subplots(constrained_layout=True)
sns.barplot(
    data = outcome_data,
    y = "Категория",
    x = "Сумма",
    hue = "Категория",
    orient = "h",
    estimator = "sum",
    errorbar = None,
    ax = ax
)

plt.title(f"{month}.{year}.", fontdict={'fontname': 'sans-serif', 'fontsize': 10})
plt.show()