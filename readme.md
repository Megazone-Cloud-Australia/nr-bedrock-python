Start the flask server in a docker container.

Build the container using
docker build -t flask-app .

Run container with
docker run -p 80:80 -e AWS_ACCESS_KEY_ID={your access key id} -e AWS_SECRET_ACCESS_KEY={ your secret access key } flask-app

freeze dependencies with
pip freeze > requirements.txt
