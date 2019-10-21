FROM python:3
ADD main.py /
ADD LeftRotation.py /
ENTRYPOINT ["python", "main.py"]
