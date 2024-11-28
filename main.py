from diaries.k23059_Diary import k23059_Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    k23059_Diary(),
    ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
