from diaries.AbstractDiary import AbstractDiary

class IshikawaDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。
githubが難しくて大変。
使いこなせるか心配だ。"""

    def get_author(self):
        return "Ihikawa"