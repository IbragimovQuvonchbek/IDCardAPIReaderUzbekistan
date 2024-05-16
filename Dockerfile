FROM python:slim

RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx libgl1-mesa-dri mesa-utils \
    && rm -rf /var/lib/apt/lists/*



WORKDIR app/

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]