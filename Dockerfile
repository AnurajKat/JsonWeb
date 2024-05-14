FROM python:3.12.3-slim
ENV APP_ME=anuraj
WORKDIR /app
COPY src src
COPY data data
COPY requirements.txt ./
COPY .env ./
COPY run_app.sh ./

RUN pip install -r requirements.txt
LABEL site.anuraj.json.resume.version=1
LABEL site.anuraj.is.beta=true

#CMD ["fastapi","run","src/app.py"]
CMD ["/bin/bash","run_app.sh"]
EXPOSE 8000
