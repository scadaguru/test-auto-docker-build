FROM python:3.12-alpine

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

COPY *.py /src

EXPOSE 5000

CMD ["python", "-u", "/src/main.py" ]