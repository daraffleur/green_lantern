FROM python:3.7.5

COPY . app/

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "wsgi.py"]
