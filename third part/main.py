import pandas as pd
import matplotlib.pyplot as plt

file_names = ['results_ejudge.html', 'students_info.xls', 'result.txt']

data_html = pd.read_html(file_names[0])
data_xls = pd.read_excel(file_names[1])

df = data_html[0].merge(data_xls, left_on='User', right_on='login')

df1 = df.groupby('group_faculty')['Solved'].mean()
df2 = df.groupby('group_out')['Solved'].mean()



fig1, ax1 = plt.subplots()
ax1.bar(df1.index, df1.values)
ax1.set_title('Среднне кол-во решенных задач по факультетским группам')
ax1.set_xlabel('номер факультетской группы')
ax1.set_ylabel('среднее значение')
ax1.grid(axis='y')
plt.ylim([0,8])
plt.savefig('mean_per_faculty.png')

fig2, ax2 = plt.subplots()
ax2.bar(df2.index, df2.values)
ax2.set_title('Среднне кол-во решенных задач по распределённым группам')
ax2.set_xlabel('номер группы по информатике')
ax2.set_ylabel('среднее значение')
ax2.grid(axis='y')
plt.ylim([0,8])
plt.savefig('mean_per_out.png')

plt.show()


file = open(file_names[2], 'w')
result = df[(df.G >= 10) | (df.H >= 10)]

print(result[['group_faculty', 'group_out']])
file.write(result[['group_faculty', 'group_out']].to_string())
file.close()