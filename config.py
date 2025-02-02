import os

class Config:
    AWS_ACCESS_KEY_ID = os.getenv('aws_access_key_id')
    AWS_SECRET_ACCESS_KEY = os.getenv('aws_secret_access_key')
    REGION_NAME = os.getenv('region_name')
    UPLOAD_FOLDER = 'uploads'

