FROM python
WORKDIR /app

COPY . . 
RUN pip install -r req.txt
 # __ current dir of image, _ current dir of image
#to run during build time
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


