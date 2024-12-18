import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha = 'center')
        
df = pd.read_csv('singer_youtube.csv') # hat 변수에 데이터셋 입력
print(df.head(), end="\n\n") # 위에서 부터 5개 데이터 확인     

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(15, 10))
plt.bar(df['name'], df['youtube count'], color = ('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'black', 'white', 'gray'))####중요
plt.title('youtube count by singer')
plt.xlabel('group')
plt.ylabel('youtube count')   

addtext(df['name'], df['youtube count'])   

plt.show()   