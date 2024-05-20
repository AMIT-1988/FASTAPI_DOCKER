# i choice a image of python templete
FROM python:3.9
#i select a working derectory
WORKDIR /code
#i copy my project requirements into my docker espace
#i work in my container
COPY ./requirements.txt /code/requirements.txt
# i install library into my container
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#i copy my project into container
COPY ./App /code/App
#i run my app into my container
CMD ["fastapi","run","App/main.py","--port","80"]