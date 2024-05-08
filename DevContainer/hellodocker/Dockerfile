FROM python:3.12

LABEL maintainer="aq98123@gmail.com"

WORKDIR /code

COPY . /code/

RUN pip install poetry 

RUN poetry config virtualenvs.create fasle

RUN poetry install

CMD ["poetry", "run", "uvicorn", "hellodocker.main:app", "--host", "0.0.0.0" ]