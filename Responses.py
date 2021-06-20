from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"

    if user_message in ("irupc", "user", "hept",):
        return "Join @iruPC for more Updates"   

    if user_message in ("time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(datetime)

    return "I dont Understand"
