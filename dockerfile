FROM python:3.9.7 as base
RUN mkdir src
WORKDIR  /src
COPY /pyproject.toml /src
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install

FROM base as test
WORKDIR /src/cft_test
CMD [ "poetry", "run", "pytest" ]

FROM base as production
WORKDIR /src/cft_test
CMD [ "poetry", "run", "start" ]