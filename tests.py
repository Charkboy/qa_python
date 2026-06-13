import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1. Тест добавления книги с валидным названием (короткое)
    def test_add_new_book_valid_short_name(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        assert "Книга" in collector.get_books_genre()

    # 2. Тест добавления книги с названием ровно 40 символов
    def test_add_new_book_valid_max_length_name(self):
        collector = BooksCollector()
        name = "A" * 40
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # 3. Тест добавления дубликата книги (не добавляется повторно)
    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_new_book("Книга")
        assert len(collector.get_books_genre()) == 1

    # 4. Тест добавления книги с названием длиннее 40 символов (не должна добавиться)
    def test_add_new_book_name_too_long_not_added(self):
        collector = BooksCollector()
        long_name = "A" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # 5. (параметризированный), тест установки жанра для книги (все доступные жанры)
    @pytest.mark.parametrize("genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"])
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)
        assert collector.get_book_genre("Книга") == genre

    # 6. Тест установки несуществующего жанра (не должен установиться)
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Роман")
        assert collector.get_book_genre("Книга") == ""

    # 7. Тест получения списка книг определённого жанра
    def test_get_books_with_specific_genre_return_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Ужасы")
        collector.set_book_genre("Книга2", "Комедии")
        books = collector.get_books_with_specific_genre("Ужасы")
        assert books == ["Книга1"]

    # 8. Тест что книга с подходящим жанром попадает в список для детей
    def test_get_books_for_children_includes_suitable_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Детская")
        collector.set_book_genre("Детская", "Комедии")
        children_books = collector.get_books_for_children()
        assert "Детская" in children_books

    # 9. Тест что книга с возрастным рейтингом не попадает в список для детей
    def test_get_books_for_children_excludes_age_rating_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Страшная")
        collector.set_book_genre("Страшная", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Страшная" not in children_books

    # 10. Тест добавления книги в избранное
    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert "Книга" in collector.get_list_of_favorites_books()

    # 11. Тест повторного добавления книги в избранное (не дублируется)
    def test_add_book_in_favorites_duplicate_not_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.get_list_of_favorites_books().count("Книга") == 1

    # 12. Тест удаления книги из избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.get_list_of_favorites_books()

    # 13. Тест получения словаря books_genre
    def test_get_books_genre_returns_correct_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.get_books_genre() == {"Книга1": "Фантастика", "Книга2": ""}
        