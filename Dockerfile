FROM python:3.9.15-alpine
RUN mkdir /usr/src/stripe_test_task
WORKDIR /usr/src/stripe_test_task
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
