FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /Users/user/Desktop/freelance_projects/Jocars

COPY requirements.txt /Users/user/Desktop/freelance_projects/requirements.txt
RUN pip install -r /Users/user/Desktop/freelance_projects/requirements.txt

COPY . /Users/user/Desktop/freelance_projects/Jocars

EXPOSE 8000
#CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]