from python:3
VOLUME /app
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["python","/app/main.py","2","3","4"]
