FROM python:3-alpine

WORKDIR /app/
VOLUME /app/chatlog
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]

