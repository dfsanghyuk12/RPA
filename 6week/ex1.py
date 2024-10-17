import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

hat = pd.read_csv('ch4-2.csv')

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

#히스토그램 그리기

plt.figure(figsize=(10, 17))
plt.subplot(1, 2, 1)
plt.hist(hat.weight, bins = 7)
plt.title('B 부회장 병아리 무게 분포 근황', fontsize = 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')

sns.displot(hat.weight) #라인 히스토그램으로 보기
#plt.show()

print(hat.describe(), end="\n\n")
#상자 그림 그리기
#plt.figure(figsize=(8, 10))
plt.subplot(1, 2, 2)
plt.boxplot(hat.weight)
#plt.title('B hatchery chick weight bos', fontsize =17)
#plt.ylabel('weigh(g)')
plt.show()