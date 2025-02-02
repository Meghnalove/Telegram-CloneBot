import os
import json
from distutils.util import strtobool as stb

# --------------------------------------
BOT_TOKEN = "1721730854:AAFNNLlJtbY8F8Hy_K1YT5Ozpn4fYe_mw1Q"
GDRIVE_FOLDER_ID = "https://drive.google.com/folderview?id=1KA28OavCxOhNBR_tcbJRR81OWURM0FxB"
# Default folder id.
OWNER_ID = 930652019
# Example: OWNER_ID = 619418070
AUTHORISED_USERS = [930652019]
# Example: AUTHORISED_USERS = [63055333, 100483029, -1003943959]
INDEX_URL = "postgres://zqmodpdyyxtslp:29113587c5cde7670c631a80549503e8947b2cb3382401c24029bb461b0fb065@ec2-3-89-0-52.compute-1.amazonaws.com:5432/d2haso7bfraj44"
IS_TEAM_DRIVE = True
USE_SERVICE_ACCOUNTS = True
# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))
