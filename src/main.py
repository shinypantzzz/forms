from tinydb import TinyDB
from aiohttp import web

from config import DB_PATH, PORT
from handlers import get_form
import validators

app = web.Application()
app['db'] = TinyDB(DB_PATH)
app['validator_sequence'] = validators.ValidatorSequence((
    validators.DateValidator("date"),
    validators.PhoneValidator("phone"),
    validators.EmailValidator("email"),
), "text")

app.add_routes([
    web.post('/get_form', get_form),
])

web.run_app(app, port=PORT)