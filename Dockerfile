FROM python:3.11.5
WORKDIR /AnimalsBot
COPY requirements.txt /AnimalsBot/
RUN pip install -r requirements.txt
COPY . /AnimalsBot/
CMD python bot.py
