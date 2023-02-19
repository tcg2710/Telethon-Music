import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "2917991"))
    API_HASH = os.environ.get("API_HASH", "7f64363978199cb4b7c8675968583fcd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6010197666:AAFgoxOrkDtzd5y0794BOSslmI7G4h9SDVY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKwBu1c2bFAmW5Oziz0Zc6TkNPA0CopGUyCWHotSfVli96jlAyTOGjMcojtrAh0vdW4utn9O3UuEvJnmIM-QB1ExmCsrZbHNFva-q6ZuQAUrerpJbv3zTKVONuokIzbV_oAfmDo9CLs5StJiLU61Nhggg9T0XcVQaxHCm4UG0P7Bjsb8Eq0K5E6mC6Z131TElaxvjUhUG9Cnp0AjaSgGmpNIREu0xHDVrSq4Boqdlv86D9IV5Gzg5rQ5toG-ZbhH5KK3WaslLnBwdmtaronE8hg1CmVAnuq3uREo2Hy-MXz6NRWZ_iHYatvpbfKcIoBSLolhf0zHUO4r2NSCkaDcWLcc89w=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Dndsuperbot")
    SUPPORT = os.environ.get("SUPPORT", "jeewallh") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "rockstar_remix") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/15cbf0b312145f7d49233.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/15cbf0b312145f7d49233.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1976526522")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "60")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
