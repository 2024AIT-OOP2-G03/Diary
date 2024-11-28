from diaries.DiarySample import DiarySample 
from diaries.K23029Diary import K23029Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           K23029Diary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
