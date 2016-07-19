# Implement a simple bookstore using OOP.
# The BookStore should implement a special search_books method.
# This method should accept two optional parameters, either title to search
# by book title or author, to search by author's name.
# Example:
#     store = BookStore()
#     # Authors
#     poe = Author(name="Edgar Allan Poe", nationality="American")
#     doyle = Author(name="Arthur Conan Doyle", nationality='British')
#     # Books
#     raven = Book(title="The Raven", author=poe)
#     study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)
#     store.add_book(raven)
#     store.add_book(study_in_scarlet)
#     store.search_books(title='raven')  # [raven]
#     store.search_books(author='doyle')  # [study_in_scarlet]


import unittest


class BookStore(object):

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, title=None, author=None):
        if title:
            search_val = title.lower()
            search_list = [book.title.lower() for book in self.books]
        elif author:
            search_val = author.lower()
            search_list = [book.author.name.lower() for book in self.books]
        else:
            raise AttributeError
        return [book for i, book in enumerate(self.books) if search_val in search_list[i]]


class Author(object):

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book(object):

    def __init__(self, title, author):
        self.title = title
        self.author = author


class BookstoreTestCase(unittest.TestCase):

    def test_class_relationships(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        self.assertEqual(store.books, [raven, study_in_scarlet])

        self.assertEqual(raven.author, poe)
        self.assertEqual(study_in_scarlet.author, doyle)

    def test_search_books_by_title(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        results = store.search_books(title='raven')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], raven)

    def test_search_books_by_authors_name(self):
        store = BookStore()

        # Authors
        poe = Author(name="Edgar Allan Poe", nationality="American")
        doyle = Author(name="Arthur Conan Doyle", nationality='British')

        # Books
        raven = Book(title="The Raven", author=poe)
        study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

        # main
        store.add_book(raven)
        store.add_book(study_in_scarlet)

        results = store.search_books(author='doyle')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], study_in_scarlet)

    def test_search_without_title_or_author_raises_error(self):
        store = BookStore()
        with self.assertRaises(AttributeError):
            store.search_books()