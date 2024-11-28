from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "頭がこんがらがった"

    def get_author(self):
        return "Sample"
