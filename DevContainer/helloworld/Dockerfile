FROM python:3.12
LABEL maintainer="aq98123@gmail.com"
WORKDIR /code
RUN pip install poetry 
ADD ./pyproject.toml /code/
ADD ./helloworld /code/helloworld/
RUN poetry install
CMD ["poetry", "run", "uvicorn", "helloworld.main:app", "--host", "0.0.0.0" ]