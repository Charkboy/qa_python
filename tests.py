import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1. Тест добавления книги с валидным названием (короткое, 40 символов, дубликат)
    def test_add_new_book_valid_name_length(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_new_book("A" * 40)
        collector.add_new_book("Книга")  # одна и та-же книга не должна добавиться
        assert len(collector.get_books_genre()) == 2

    # 2. Тест добавления книги с названием длиннее 40 символов (не должна добавиться)
    def test_add_new_book_name_too_long_not_added(self):
        collector = BooksCollector()
        long_name = "A" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # 3. (параметризированный), тест установки жанра для книги (все доступные жанры)
    @pytest.mark.parametrize("genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"])
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)
        assert collector.get_book_genre("Книга") == genre

    # 4. Тест установки несуществующего жанра (не должен установиться)
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Роман")
        assert collector.get_book_genre("Книга") == ""

    # 5. Тест получения списка книг определённого жанра
    def test_get_books_with_specific_genre_return_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Ужасы")
        collector.set_book_genre("Книга2", "Комедии")
        books = collector.get_books_with_specific_genre("Ужасы")
        assert books == ["Книга1"]

    # 6. Тест получения книг для детей (без жанров из age_rating)
    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Детская")
        collector.add_new_book("Страшная")
        collector.set_book_genre("Детская", "Комедии")
        collector.set_book_genre("Страшная", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Детская" in children_books
        assert "Страшная" not in children_books

    # 7. Тест добавления книги в избранное
    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert "Книга" in collector.get_list_of_favorites_books()

    # 8. Тест повторного добавления книги в избранное (не дублируется)
    def test_add_book_in_favorites_duplicate_not_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.get_list_of_favorites_books().count("Книга") == 1

    # 9. Тест удаления книги из избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.get_list_of_favorites_books()

    # 10. Тест получения словаря books_genre
    def test_get_books_genre_returns_correct_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.get_books_genre() == {"Книга1": "Фантастика", "Книга2": ""}