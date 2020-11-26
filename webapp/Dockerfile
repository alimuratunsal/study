FROM python:3.8-alpine3.10

MAINTAINER Ali Murat Unsal "alimuratunsal@gmail.com"

COPY . /webapp
WORKDIR /webapp

RUN pip install -r requirements.txt

#Application Port Expose
EXPOSE 11130

CMD [ "python", "./hello.py" ]
