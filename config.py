
'''curl -H Metadata-Flavor:Google 169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token

chmod 600 C:/Users/skvor/mykey

ssh -i C:/Users/skvor/mykey student@158.160.129.26

'''



HOME_DIR = r'C:/Users/skvor/PycharmProjects/pythonProject2'  # путь к папке с проектом
LOGS = f'{HOME_DIR}/logs.txt'  # файл для логов
DB_FILE = f'{HOME_DIR}/messages.db'  # файл для базы данных

IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'  # файл для хранения iam_token
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'  # файл для хранения folder_id
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'  # файл для хранения bot_token


MAX_USERS = 3
MAX_GPT_TOKENS = 120  #
COUNT_LAST_MSG = 4

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10
MAX_USER_TTS_SYMBOLS = 5000
MAX_USER_GPT_TOKENS = 2000

SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]