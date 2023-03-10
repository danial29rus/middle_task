# middle_task
cd middle_task

docker build -t myimage .

docker run -d --name mycontainer -p 80:80 myimage

Deploy тут - https://task-middle-test.onrender.com/docs
