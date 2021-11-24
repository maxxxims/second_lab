import pandas as pd
import matplotlib.pyplot as plt


file_name='flights.csv'
df = pd.read_csv(file_name)
count = df['CARGO'].value_counts()
groups = df.groupby('CARGO')[['PRICE', 'WEIGHT']].sum()


fig1, ax1 = plt.subplots()
ax1.bar(count.index, count.values)
ax1.set_title('Количество рейсов')
ax1.grid(axis='y')
plt.savefig('result1.png')

fig2, ax2 = plt.subplots()
ax2.bar(groups.index, groups.PRICE / 1000)
ax2.set_title('Выручка')
ax2.set_ylabel('тыс. руб.')
ax2.grid(axis='y')
plt.savefig('result2.png')

fig3, ax3 = plt.subplots()
ax3.bar(groups.index, groups.WEIGHT)
ax3.set_title('Полный вес перевезённого груза')
ax3.set_ylabel('кг', rotation = 90)
ax3.grid(axis='y')
plt.savefig('result3.png')

plt.show()