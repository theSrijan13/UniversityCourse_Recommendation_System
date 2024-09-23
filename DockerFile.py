# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR 

# Step 3: Copy the requirements.txt file to the container
COPY requirements.txt .

# Step 4: Install dependencies in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the FastAPI app to the container
COPY . .

# Step 6: Expose the port that FastAPI will run on (default is 8000)
EXPOSE 8000

# Step 7: Command to run FastAPI using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
