FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /Users/user/Desktop/freelance_projects/Jocars

COPY requirements.txt /Users/user/Desktop/freelance_projects/requirements.txt
RUN pip install -r /Users/user/Desktop/freelance_projects/requirements.txt

COPY . /Users/user/Desktop/freelance_projects/Jocars

