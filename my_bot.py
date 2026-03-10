from secret import my_username

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  standardized_message = user_message.lower().strip().replace(".", "")
  if "robot" in standardized_message:
    return True
  elif "what is 7 + 5" in standardized_message:
    return True
  elif "what planet are we on" in standardized_message:
    return True
  elif "who wrote romeo and juliet" in standardized_message:
    return True
  elif "what is 9 + 10" in standardized_message:
    return True
  elif "what do bees make" in standardized_message:
    return True
  elif "what gas do humans breathe" in standardized_message:
    return True
  elif "how long is a day" in standardized_message:
    return True
  elif "where was this bot made" in standardized_message:
    return True
  elif "where do fish live" in standardized_message:
    return True
  elif "what does not grow on trees" in standardized_message:
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  standardized_message = user_message.lower().strip().replace(".", "")
  if "robot" in standardized_message:
    return f"""you said my name!!
  {user_message.replace("robot", user_name)}"""
  elif "what is 7 + 5" in standardized_message:
    return f"""Its 12, {user_name}"""
  elif "what planet are we on" in standardized_message:
    return f""" Earth, {user_name}"""
  elif "who wrote romeo and juliet" in standardized_message:
    return f"""Shakespear,{user_name}"""
  elif "what is 9 + 10" in standardized_message:
    return f"""21,{user_name}"""
  elif "what do bees make" in standardized_message:
    return f"""honey,{user_name}"""
  elif "what gas do humans breathe" in standardized_message:
    return f"""oxygen,{user_name}"""
  elif "how long is a day" in standardized_message:
    return f"""24 hours,{user_name}"""
  elif "where was this bot made" in standardized_message:
    return f"""Kehillah,{user_message}"""
  elif "where do fish live" in standardized_message:
    return f"""The ocean,{user_name}"""
  elif "what does not grow on trees" in standardized_message:
    return f"""Money,{user_name}"""
  else:
    return False


  
