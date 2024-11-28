import pandas as pd
from sklearn.model_selection import train_test_split

w = pd.read_csv("ch5-1.csv")
x_data = w.iloc[:,2:5].values##독립변수
y_data = w.iloc[:,1].values##종속변수

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)  ##train_test_split 중요
#train은 학습, test는 예측, r2에선 test와 predict를 비교해서 검증
from sklearn.neural_network import MLPRegressor
model_mlp = MLPRegressor().fit(x_train, y_train)##MLPRegressor().fit
y_pred_mlp = model_mlp.predict(x_test) ##model_mlp.predict(x_test)

df_x_test = pd.DataFrame(x_test, columns=['egg_weight','movement','acc_food'])
df_y_pred = pd.DataFrame(y_pred_mlp, columns=['predict'])
df_y_test = pd.DataFrame(y_test , columns=['real'])
df = pd.concat([df_x_test, df_y_test, df_y_pred], axis=1)
print(df, end='\n\n')

from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_pred_mlp)##채점
print("R2 = ", R2, end='\n\n')##채점