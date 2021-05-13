FROM python:3.9

COPY / /

WORKDIR /

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "freddy"]