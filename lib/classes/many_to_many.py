class Article:
    all = []  # tests expect this

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")

        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

      
    def add_article(self, magazine, title):
        """Create and return a new Article for this author"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return a list of categories for all magazines this author has articles in"""
        categories = {mag.category for mag in self.magazines()}
        return list(categories) if categories else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    
    def article_titles(self):
        """Return a list of titles of all articles in this magazine"""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    
    def contributing_authors(self):
        """Return authors who have written more than 2 articles for this magazine"""
        from collections import Counter
        author_counts = Counter(article.author for article in self.articles())
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None
