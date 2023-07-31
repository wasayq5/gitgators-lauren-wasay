FROM quay.io/centos/centos:stream8
RUN dnf install -y python3.9
RUN python3.9 -m ensurepip
RUN python3.9 -m pip install --upgrade pip
WORKDIR /myportfolio
COPY . .
RUN pip install click==8.0.1
RUN pip install cryptography==37.0.2
RUN pip install Flask==2.0.1
RUN pip install itsdangerous==2.0.1
RUN pip install Jinja2==3.0.1
RUN pip install MarkupSafe==2.0.1
RUN pip install peewee==3.14.10
RUN pip install pycparser==2.21
RUN pip install PyMySQL==1.0.2
RUN pip install python-dotenv==0.17.1
RUN pip install Werkzeug==2.0.1
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000