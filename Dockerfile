FROM python:3.12.3-slim
ENV DEBUG_ENABLED=false
ENV APP_DATA_LOCATION=data
ENV APP_DATA_SRC=file_system
ENV APP_PORT=8000
WORKDIR /app
COPY src src
COPY data data
COPY requirements.txt ./
COPY run_app.sh ./

RUN pip install -r requirements.txt
LABEL site.anuraj.json.resume.version=1
LABEL site.anuraj.is.beta=true

#CMD ["fastapi","run","src/app.py"]
CMD ["/bin/bash","run_app.sh"]
EXPOSE $APP_PORT
