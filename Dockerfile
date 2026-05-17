FROM python:3.12-slim
WORKDIR /Sergienko
COPY . .
RUN pip install googletrans==3.1.0a0
CMD ["python", "gtrans3.py"]