FROM python:3

ADD Walgreens_appointment_availability.py /

RUN pip install pgeocode

RUN pip install requests

CMD [ "python", "./Walgreens_appointment_availability.py" ]
