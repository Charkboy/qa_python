1. test_add_new_book_valid_name_length - проверяет добавление двух книг (короткое имя и имя из 40 символов), а также дубликат.

2. test_add_new_book_name_too_long_not_added - проверяет, что имя длиннее 40 символов не добавляется.

3. test_set_book_genre_valid_genre - (параметризованный), проверяет установку всех допустимых жанров.

4. test_set_book_genre_invalid_genre_not_set - проверяет, что недопустимый жанр не устанавливается (жанр "Роман" не входит в self.genre).

5. test_get_books_with_specific_genre_return_correct_list - проверяет, что метод возвращает список книг с указанным жанром.

6.test_get_books_for_children_excludes_age_rating_genres - проверяет, что книги с жанрами из age_rating не включаются в список для детей.

7. test_add_book_in_favorites_adds_book - проверяет добавление в избранное.

8. test_add_book_in_favorites_duplicate_not_added_twice - проверяет, что повторное добавление книги не создает дубликат.

9. test_delete_book_from_favorites_removes_book - проверяет удаление книги из избранного.

10. test_get_books_genre_returns_correct_dict - проверяет получение словаря books_genre.