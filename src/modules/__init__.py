import os
from dotenv import load_dotenv

from modules.core.logging.logger import Logger

# Xác định môi trường hiện tại ("development" hoặc "production")
current_env = os.environ.get('ENVIRONMENT')

# Tải các biến môi trường từ tệp .env tương ứng với môi trường hiện tại
if current_env == 'development':
    load_dotenv('.env.development')
elif current_env == 'production':
    load_dotenv('.env.production')
else:
    load_dotenv('.env.development')

print("____ ENV ____")
for key, value in os.environ.items():
    # Kiểm tra nếu tên biến môi trường bắt đầu bằng PYSTOCK_
    if key.startswith("PS_"):
        print(f"{key}: {value}")
print("_____________")
