# test_kamtor
Test task for SHIFT CFT

## Task: 

Реализуйте REST-сервис просмотра текущей зарплаты и даты следующего
повышения. Из-за того, что такие данные очень важны и критичны, каждый
сотрудник может видеть только свою сумму. Для обеспечения безопасности, вам
потребуется реализовать метод где по логину и паролю сотрудника будет выдан
секретный токен, который действует в течение определенного времени. Запрос
данных о зарплате должен выдаваться только при предъявлении валидного токена.
Требования к решению
Обязательные технические требования:
● код размещен и доступен в публичном репозитории на GitLab;
● оформлена инструкция по запуску сервиса и взаимодействию с проектом
(Markdown файл с использованием конструкций разметки от GitLab по
необходимости);
● сервис реализован на FastAPI.
Необязательные технические требования (по возрастанию трудоемкости):
● зависимости зафиксированы менеджером зависимостей poetry;
● написаны тесты с использованием pytest;
● реализована возможность собирать и запускать контейнер с сервисом в Docker.


## How to install:
### 1) Clone repository
```
git clone https://github.com/R1Sen007/test_kamtor.git
cd test_kamtor
```
### 2) Create & activate virtual environment 
```
python -m venv venv
```
If your platform is Windows:
```
Set-ExecutionPolicy Unrestricted
venv/Scripts/activate.ps1
```
If you have Unix/Linux:
```
sourse venv/bin/activate
```
### 3) Clone important libraries 
```
pip install -r requirements.txt
```
## How to run:
```
python main.py
```