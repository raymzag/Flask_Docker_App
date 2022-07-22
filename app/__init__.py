import logging

from flask import Flask
from flask_unleash import Unleash

logger = logging.getLogger()

app = Flask(__name__)

app.debug = True

app.config['UNLEASH_URL'] = "https://app.unleash-hosted.com/demo/api"
app.config['UNLEASH_CUSTOM_HEADERS'] = {'Authorization': '56907a2fa53c1d16101d509a10b78e36190b0f918d9f122d'}
app.config['UNLEASH_APP_NAME'] = "flask-gunicorn-unleash"
app.config['UNLEASH_ENVIRONMENT'] = 'staging'

Unleash(app)

h = logging.StreamHandler()
fmt = logging.Formatter(
    fmt='%(asctime)s %(levelname)s (%(name)s) %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)
h.setFormatter(fmt)
logger.addHandler(h)
logger.setLevel(logging.DEBUG)

from app import views


