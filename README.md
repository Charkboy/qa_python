1. test_add_new_book_valid_short_name - Проверяет добавление книги с коротким валидным названием.

2. test_add_new_book_valid_max_length_name - Проверяет добавление книги с названием длиной ровно 40 символов.

3. test_add_new_book_duplicate_not_added - Проверяет, что повторное добавление той же книги не увеличивает количество записей.

4. test_add_new_book_name_too_long_not_added - Проверяет, что название длиннее 40 символов не добавляется в словарь.

5. test_set_book_genre_valid_genre - (параметризированный) Проверяет установку жанров (Фантастика, Ужасы, Детективы, Мультфильмы, Комедии).

6. test_set_book_genre_invalid_genre_not_set - Проверяет, что несуществующий жанр не устанавливается.

7. test_get_books_with_specific_genre_return_correct_list - Проверяет, что метод возвращает список книг только с указанным жанром.

8. test_get_books_for_children_includes_suitable_genre - Проверяет, что книга с жанром без возрастного рейтинга попадает в список для детей.

9. test_get_books_for_children_excludes_age_rating_genre - Проверяет, что книга с жанром из списка `genre_age_rating` (например, "Ужасы") не попадает в детский список.

10. test_add_book_in_favorites_adds_book - Проверяет добавление книги в список избранного.

11. test_add_book_in_favorites_duplicate_not_added_twice - Проверяет, что повторное добавление той же книги не создаёт дубликат.

12. test_delete_book_from_favorites_removes_book - Проверяет удаление книги из избранного.

13. test_get_books_genre_returns_correct_dict - Проверяет, что метод возвращает полный словарь `books_genre` с корректными данными.
