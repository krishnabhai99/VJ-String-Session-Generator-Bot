from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "14050586"))
API_HASH = environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7434920209:AAFyKq35cGt-ZxWWqIYO_NVrBQSkU3rBhp0")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "5446367898")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "Animes_India_bot")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
