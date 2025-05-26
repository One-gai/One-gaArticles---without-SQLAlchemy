from lib.models.articles import Article


articles = Article.find_by_author_id(1)



for article in articles:
    print(article.title)


 
