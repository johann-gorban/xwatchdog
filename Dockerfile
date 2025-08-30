FROM python:3.12

RUN pip install --upgrade pip

WORKDIR /xwatchdog

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN playwright install
RUN playwright install-deps

COPY . .

CMD ["python", "bot/main.py"]