import pandas as pd
import sqlite3
import glob

# CSV 파일 경로 (본인 경로에 맞게 수정)
csv_files = glob.glob('./소상공인시장진흥공단_상가(상권)정보_20251231/*.csv')

# DB 연결 (없으면 자동 생성)
conn = sqlite3.connect('상권분석.db')

# CSV 파일을 하나씩 읽어서 하나의 테이블로 합치기
dfs = []
for f in csv_files:
    df = pd.read_csv(f, encoding='utf-8')
    dfs.append(df)

combined = pd.concat(dfs, ignore_index=True)
combined.to_sql('상가업소정보_201912', conn, if_exists='replace', index=False)

conn.close()
print("완료!")