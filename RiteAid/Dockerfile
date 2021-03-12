FROM python:3

ADD RiteAid_appointment_availability.py /

RUN pip install pgeocode

RUN pip install requests

CMD [ "python", "./RiteAid_appointment_availability.py" ]
