# Stripe test task

Задание
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price) 
API с двумя методами:
GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
Пример реализации можно посмотреть в пунктах 1-3 тут
Залить решение на Github, описать запуск в Readme.md
Опубликовать свое решение чтобы его можно было быстро и легко протестировать. 
Решения доступные только в виде кода на Github получат низкий приоритет при проверке.


How to run project:

cd to dir with docker files

sudo docker-compose up -d --build

sudo docker-compose exec web python main/manage.py makemigrations

sudo docker-compose exec web python main/manage.py migrate

sudo docker-compose exec web python main/manage.py createsuperuser
