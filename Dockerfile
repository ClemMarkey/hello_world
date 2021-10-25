FROM python:3.8.6
WORKDIR /usr/src/app
RUN pip install Flask
RUN pip install mysql-connector-python
COPY . .
CMD ["app.py"]
ENTRYPOINT [ "python" ]