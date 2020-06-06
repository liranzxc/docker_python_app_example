FROM python:3

ADD . /

RUN pip install -r requirements.txt

ENV MYVAR 7

CMD [ "python", "./app.py" ]
