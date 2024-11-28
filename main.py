from diaries.DiarySample import DiarySample
from diaries.K23100Diary import K23100Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           K23100Diary(),
             ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
