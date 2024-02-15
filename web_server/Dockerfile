FROM python:slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w4", "--bind", "0.0.0.0:80", "flask_app:launch()"]