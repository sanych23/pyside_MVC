from model import FormCategory


class Events:
    def categoryNews(self, category):
        data = FormCategory().getNewsCategory(category)
        news_feed = ""
        for new in data:
            news_feed = f"{news_feed}{new}\n"
        self.newsArea.setText(news_feed)