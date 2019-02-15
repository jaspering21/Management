FROM python:3
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
WORKDIR /code
COPY  . /code/
ADD manage.py /
RUN pip3 --no-cache-dir install -r requirements.txt
CMD [ "python3", "./manage.py" ]