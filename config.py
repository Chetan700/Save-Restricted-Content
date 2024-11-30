import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24068626"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "de2781dce723aa9a68ba4948b9e7044f")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chetan3:W7AxgWL7T9Cvtv3r@cluster1.bht6e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
