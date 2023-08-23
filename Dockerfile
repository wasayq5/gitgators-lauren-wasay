FROM python:3.9-slim-buster
WORKDIR /gitgators-lauren-wasay
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
EXPOSE 5000
