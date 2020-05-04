class NewsSource:
    """
    Newssource class to define newssource objects
    """
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country



class Article:

    def __init__(self, title, description, url, urlToImage, publishedAt):
        self.title =title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

        