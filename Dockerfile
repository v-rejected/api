FROM python:3.6

WORKDIR /usr/src/app

EXPOSE 5000
COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD [ "python", "./api.py" ]
