FROM python:3
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "python", "server.py" ]