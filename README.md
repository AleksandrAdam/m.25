(Задание 25.3.1):
Написать тест, который проверяет, что на сайте PetFriends (https://petfriends.skillfactory.ru/) на странице со списком питомцев пользователя (https://petfriends.skillfactory.ru/my_pets):
1) Присутствуют все питомцы.
2) Хотя бы у половины питомцев есть фото.
3) У всех питомцев есть имя, возраст и порода.
4) У всех питомцев разные имена.
5) В списке нет повторяющихся питомцев.

(Задание 25.5.1.)
1) В тесте (проверка карточек всех питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст).
2) В тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.

В файле "Conftest.py" находится фикстура, открывающая браузер Google Chrome. Также представленая настройка размера окна и закрытие браузера после прохождения теста.

Файл "test_selenium_petfriends.py" содержит два теста.
1) Тест "test_show_all_pets()" проверяет карточки всех питомцев на главной странице сайта и содержит неявные ожидания всех элементов.
2) Тест "test_show_my_pets()" проверяет карточки всех питомцев пользователя на странице пользователя и содержит явные ожидания.



