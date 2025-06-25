from waitress import serve
from app import wsr_app

serve(wsr_app, host='0.0.0.0', port=8080)
