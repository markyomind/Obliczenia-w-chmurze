FROM python:3.9
 
RUN apt-get update
RUN apt-get install vim -y
RUN mkdir -p /home/neighbor
 
RUN pip install matplotlib
 
COPY sasiad.py /home/neighbor/sasiad.py
WORKDIR /home/neighbor 

CMD ["python","/home/neighbor/sasiad.py"]


