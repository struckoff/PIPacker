FROM python:3
MAINTAINER Alexey Struckov <struckov@protonmail.com>
#RUN apt-get update
#RUN apt-get install -y python python-pip build-essential
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
# ENTRYPOINT ["kill"]
# CMD ["-9 1"]