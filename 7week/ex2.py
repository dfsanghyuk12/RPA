import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2024_seoul_data.csv', encoding='utf-8')
df2 = df.fillna(method='ffill')

df2.rename(columns={'일강수량':'rain'}, inplace=True)
df2.head(1)

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 강수량 변화')
plt.plot(df2['일시'], df2 ['rain'], label='일강수량', c='g')
plt.xlabel('날짜')
plt.ylabel('일강수량')
plt.legend()
plt.show()