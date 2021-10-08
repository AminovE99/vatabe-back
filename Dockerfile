FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /telemed
WORKDIR /telemed
COPY requirements.txt /telemed/

ENV VIRTUAL_ENV=/root/telemed-dev/telemed-be/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /telemed/
COPY ./config/entrypoint.sh /telemed/
ENTRYPOINT ["sh", "./config/entrypoint.sh"]