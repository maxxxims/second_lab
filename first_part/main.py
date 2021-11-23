import pandas as pd

file_name = 'transactions.csv'
result_file_name = 'result.txt'
n = 3
file = open(result_file_name, 'w')


df = pd.read_csv(file_name)
################################## FIRST ##################################
t1 = df[df.STATUS == 'OK'].sort_values(by='SUM', ascending=False).head(n)
file.write(t1.to_string())
print(t1)


################################## SECOND ##################################
t2 = df[(df['STATUS'] == 'OK') & (df['CONTRACTOR'] == 'Umbrella, Inc')]
file.write('\n'+'\n'+'Total of all transactions for Umbrella, Inc = '+str(t2.SUM.sum()))
print()
print('Total of all transactions for Umbrella,Inc = ' + str(t2.SUM.sum()))

file.close()