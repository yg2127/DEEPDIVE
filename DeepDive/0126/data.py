# pandas
# matplotlib, Seaborn 안함
# plotly를 활용한 데이터 시각화

import numpy as np
import pandas as pd
np.random.seed(0)
arr = np.random.randint(10, size = (2,2)) # 2,2 짜리 랜덤 arr 생성
print(arr)

# copy true는 원본 데이터 (여기선 arr) 수정해도 인스턴스 변경 안됨
# False는 원본 데이터가 수정될 경우 그대로 판다스 df에 반영됨
df1 = pd.DataFrame(arr, copy = False)
df2 = pd.DataFrame(arr, copy = True)
arr[0,0] = 99
print(df1)
print(df2)

