import html
import random
import time

import zerotwobot.modules.fun_strings as fun_strings
from zerotwobot import dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from zerotwobot.modules.helper_funcs.chat_status import is_user_admin
from zerotwobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext


def characters(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF BALBLA\n\n/xiao - ABOUT XIAO\n/ganyu - ABOUT GANYU",
    )
   
CHARACTERS_HANDLER = DisableAbleCommandHandler("characters", characters, run_async=True)
  
dispatcher.add_handler(CHARACTERS_HANDLER)
