FROM python:3.9-slim-buster
WORKDIR /myportfolio
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
EXPOSE 5000