# middle_task

# Тестовое задание на позицию Middle Python Developer

Необходимо было создать 3 ручки:

- 1я принимает x, y, один из операторов ['+', '-', '/', '*']
На выходе отдает id задачи

- 2я принимает id задачи и выдает ответ

- 3я Отдает список всех задач с их статусами

Надо было покрыть тестами, деплой, docker



Для запуска 

git clone https://github.com/danial29rus/middle_task.git

cd middle_task

docker build -t myimage .

docker run -d --name mycontainer -p 80:80 myimage

Deploy тут - https://task-middle-test.onrender.com/docs
