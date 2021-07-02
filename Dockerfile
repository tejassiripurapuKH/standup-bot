FROM python:3.8-slim

LABEL maintainer="Tejas Siripurapu <tejas97siripruapu@gmail.com>"

COPY . .
RUN ls && pip install -r requirements.txt

EXPOSE 8000

# CMD gunicorn -b 0.0.0.0:8000 main:app

CMD python main.py
