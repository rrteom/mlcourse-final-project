FROM python:3.10

WORKDIR /workdir

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app/ /workdir/
COPY pickles/ /pickles/

ENTRYPOINT ["python", "./server.py"]