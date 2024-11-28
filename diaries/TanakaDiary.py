from diaries.AbstractDiary import AbstractDiary

class TanakaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return """今日は、オブジェクト指向プログラミング演習2の第9回グループワーク演習だった。
        出だしで少しつまづいてしまったので追いつくのが大変だった。
        来週からはみんなに迷惑かけないようにしっかり予習していきたいと思う。
        明日いきなりプログラミングの知識が頭に入っていたらどんなに楽だろうか……"""

    def get_author(self):
        return "Tanaka Yasuto"