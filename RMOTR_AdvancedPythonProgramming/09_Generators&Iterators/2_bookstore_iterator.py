# Convert the search_books method of the Bookstore class you implemented in the previous unit so it has an iterator-like interface.
# Instead of returning a list with the results,
# create a generator/iterator that behaves with the Iterator API:
#     store = BookStore()
# Both these pieces of code should work and be equivalent:
#     # Using a for loop
#     results = store.search_books(title="raven")
#     for book in results:
#         print(book)
#     # Invoking next directly
#     results = store.search_books(title="raven")
#     print(next(result))
#     print(next(result))


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
        for book in [book for i, book in enumerate(self.books) if search_val in search_list[i]]:
            yield book


class Author(object):

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __eq__(self, other):
        return self.name == other.name and self.nationality == other.nationality


class Book(object):

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class BookStoreTestCase(unittest.TestCase):
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


class ObjectsComparisonTestCase(unittest.TestCase):
    def test_compare_books(self):
        """Books with same author and title should be equal"""
        poe = Author(name="Edgar Allan Poe", nationality="American")

        b1 = Book(title="The Raven", author=poe)
        b2 = Book(title="The Raven", author=poe)
        self.assertEqual(b1, b2)

    def test_compare_authors(self):
        """Authors with same name and nationality should be equal"""
        a1 = Author(name="Edgar Allan Poe", nationality="American")
        a2 = Author(name="Edgar Allan Poe", nationality="American")

        self.assertEqual(a1, a2)


class BookGeneratorTestCase(unittest.TestCase):

    def test_search_books_by_title_returns_generator(self):
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

        results_generator = store.search_books(title='raven')
        self.assertEqual(next(results_generator), raven)
        with self.assertRaises(StopIteration):
            next(results_generator)

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

        results_generator = store.search_books(author='doyle')

        self.assertEqual(next(results_generator), study_in_scarlet)
        with self.assertRaises(StopIteration):
            next(results_generator)

    def test_search_without_title_or_author_raises_error(self):
        store = BookStore()
        with self.assertRaises(AttributeError):
            next(store.search_books())