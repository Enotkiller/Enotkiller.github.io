FROM python:3.13-slim


RUN pip install --no-cache-dir uv

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости через uv С ФЛАГОМ --system
RUN uv pip install --system -r requirements.txt

# Копируем код и данные
COPY . .

CMD ["python", "main.py"]
