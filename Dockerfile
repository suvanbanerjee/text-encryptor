FROM python:3
RUN pip install pyscript
WORKDIR /app
CMD ["python","-m","http.server","8000"]
EXPOSE 8000