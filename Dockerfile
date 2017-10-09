FROM frolvlad/alpine-python3
RUN apk add --no-cache sqlite
WORKDIR /src
ADD . .
EXPOSE 80
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
ENTRYPOINT python3 manage.py runserver 0.0.0.0:80
