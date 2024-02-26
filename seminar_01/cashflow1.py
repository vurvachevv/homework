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

#проверка введенного месяца
if month not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
    if year not in [str(x) for x in range(1960, 2024 + 1)]:
        print("Введен неправильный год!")
    print("Введен неправильный месяц!")
    exit()
if year not in [str(x) for x in range(1960, 2024 + 1)]:
    print("Введен неправильный год!")
    exit()

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