#   Pull official base image
FROM python:3

#   Set environment variables
ENV PYTHONUNBUFFERED=1

#   Set work directory
WORKDIR /code

#   Install dependencies development
#COPY setup.sh /code/
#RUN /code/setup.sh
#   Install dependencies production
COPY requirements.txt /code/
RUN pip install -r requirements.txt

#   Copy project
COPY . /code/ 