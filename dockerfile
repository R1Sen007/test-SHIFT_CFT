FROM python:3.9.7 as python-base
RUN mkdir src
WORKDIR  /src
COPY /pyproject.toml /src
# COPY /poetry.lock /src
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install 
# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
WORKDIR /src/cft_test
CMD [ "poetry", "run", "start" ]