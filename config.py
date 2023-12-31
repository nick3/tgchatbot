import os
WEB_HOOK = os.environ["WEB_HOOK"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get('PORT', '8080'))
NICK = os.environ.get('NICK', None)
API = os.environ.get('API', None)
API4 = os.environ.get('API4', None)
PASS_HISTORY = (os.environ.get('PASS_HISTORY', "False") == "False") == False
USE_GOOGLE = (os.environ.get('USE_GOOGLE', "True") == "False") == False
if os.environ.get('GOOGLE_API_KEY', None) == None and os.environ.get('GOOGLE_CSE_ID', None) == None:
    USE_GOOGLE = False
temperature = float(os.environ.get('temperature', '0.5'))
DEFAULT_SEARCH_MODEL = os.environ.get('DEFAULT_SEARCH_MODEL', 'gpt-3.5-turbo-16k')
SEARCH_USE_GPT = (os.environ.get('SEARCH_USE_GPT', "True") == "False") == False
GPT_ENGINE = os.environ.get('GPT_ENGINE', 'gpt-3.5-turbo')
API_URL = os.environ.get('API_URL', 'https://api.openai.com/v1/chat/completions')