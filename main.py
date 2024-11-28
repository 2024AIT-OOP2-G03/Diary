from diaries.DiarySample import DiarySample
from diaries.IshikawaDiary import IshikawaDiary
from diaries.K23100Diary import K23100Diary
from diaries.TanakaDiary import TanakaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    IshikawaDiary(),
    K23100Diary(),
    TanakaDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
