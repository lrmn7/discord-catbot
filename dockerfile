# Menggunakan base image Python official
FROM python:3.11.4

# Set working directory di dalam container
WORKDIR /app

# Copy requirements.txt dan install dependensi
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy semua file aplikasi ke dalam container
COPY . .

# Menjalankan perintah saat container dijalankan
CMD [ "python", "main.py" ]
