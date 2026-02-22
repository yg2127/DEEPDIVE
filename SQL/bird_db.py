import pandas as pd
import sqlite3

# DB 연결 (없으면 자동 생성)
conn = sqlite3.connect('./SQL/bird.db')

# bird_tracking_devices.csv (7건 - 새 기기 정보)
devices = pd.read_csv('./SQL/bird_tracking_devices.csv')
devices.to_sql('bird_tracking_devices', conn, if_exists='replace', index=False)
print(f"bird_tracking_devices: {len(devices)}건 완료")

# bird_tracking.csv (61,920건 - GPS 추적 기록)
tracking = pd.read_csv('./SQL/bird_tracking.csv')
tracking.to_sql('bird_tracking', conn, if_exists='replace', index=False)
print(f"bird_tracking: {len(tracking)}건 완료")

conn.close()
print("마이그레이션 완료!")
