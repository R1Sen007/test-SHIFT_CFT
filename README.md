# test-SHIFT_CFT
Test task for SHIFT CFT

## Task: 

Реализуйте REST-сервис просмотра текущей зарплаты и даты следующего
повышения. Из-за того, что такие данные очень важны и критичны, каждый
сотрудник может видеть только свою сумму. Для обеспечения безопасности, вам
потребуется реализовать метод где по логину и паролю сотрудника будет выдан
секретный токен, который действует в течение определенного времени. Запрос
данных о зарплате должен выдаваться только при предъявлении валидного токена.

### Требования к решению

Обязательные технические требования:<br />
● код размещен и доступен в публичном репозитории на GitLab;<br />
● оформлена инструкция по запуску сервиса и взаимодействию с проекто<br />
(Markdown файл с использованием конструкций разметки от GitLab по
необходимости);<br />
● сервис реализован на FastAPI.<br />

Необязательные технические требования (по возрастанию трудоемкости):<br />
● зависимости зафиксированы менеджером зависимостей poetry;<br />
● написаны тесты с использованием pytest;<br />
● реализована возможность собирать и запускать контейнер с сервисом в Docker.<br />


## How to install:
### 1) Clone repository
```
git clone https://github.com/R1Sen007/test-SHIFT_CFT.git
```
### 2) Installation (need docker on your PC) 
```
cd test-SHIFT_CFT
```
Image для тестов:
```
docker build -t cft-docker-tests --target test .
```
Image для старта сервера:
```
docker build -t cft-docker --target production . 
```
## How to run:
### Для старта сервера:
Запускаем контейнер:
```
docker run -d --name cft-dockercontainer -p 8000:8000 cft-docker
```
Переходим в браузер и набираем:
```
http://0.0.0.0:8000/docs
```
### Для прохода тестов:
Запускаем контейнер:
```
docker run -d --name cft-dockercontainer-tests cft-docker-tests
```
Смотрим логи:
```
docker logs cft-dockercontainer-tests
```
