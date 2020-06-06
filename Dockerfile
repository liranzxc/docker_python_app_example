FROM python:3

WORKDIR /tmp

ADD . /tmp

RUN pip install -r /tmp/requirements.txt

ENV PORT 3000
EXPOSE $PORT

ENV MYVAR 7

CMD [ "python", "/tmp/app.py" ]
