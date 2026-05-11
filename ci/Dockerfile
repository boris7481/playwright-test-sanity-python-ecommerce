FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# install playwright browsers
RUN playwright install --with-deps

COPY . .

CMD ["pytest"]