from diaries.AbstractDiary import AbstractDiary

class K23100Diary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return """今日はGitHubを初めて使った。説明についていけなくてかなり頭がこんがらがってしまった。
    これから使っていくものなのでちゃんと理解しておきたい。
    次の授業ではコードが渡されてそれを読んでするらしいので予習しておきたい。"""

    def get_author(self):
        return "Sample"
