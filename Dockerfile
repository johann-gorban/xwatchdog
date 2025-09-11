FROM python:3.12

RUN pip install --upgrade pip

WORKDIR /bot

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN playwright install
RUN playwright install-deps

CMD ["python3", "-u", "bot/main.py"]