from waitress import serve
from personal_info.logger import logger
from personal_info.app import create_app

serve(create_app(config_filename="config.py"), host='0.0.0.0', port=2323, threads = 10)