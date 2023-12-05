FROM python:3.8
WORKDIR /app
COPY oficinaprojeto/ /app/oficinaprojeto/
COPY venv/ /app/venv/
COPY requirements.txt /app/
RUN python -m venv venv
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "oficinaprojeto/manage.py", "runserver", "0.0.0.0:8000"]
