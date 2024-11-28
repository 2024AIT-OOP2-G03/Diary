from diaries.IshikawaDiary import IshikawaDiary
from diaries.K23100Diary import K23100Diary
from diaries.TanakaDiary import TanakaDiary
from diaries.K23029Diary import K23029Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    IshikawaDiary(),
    K23100Diary(),
    TanakaDiary(),
    K23029Diary()
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
