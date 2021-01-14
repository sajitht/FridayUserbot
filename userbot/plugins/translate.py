""" Google Translate
Available Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

import emoji
from deep_translator import GoogleTranslator
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
from langdetect import detect


@friday.on(friday_on_cmd("tr ?(.*)"))
@friday.on(sudo_cmd("tr ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "gu"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await edit_or_reply(event, "`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    try:
        
        lmao = detect(text)
        after_tr_text = lmao
        to_translate = text

        translated = GoogleTranslator(source='auto', target=lan).translate(to_translate)
      
        output_str = """**Translated By FridayUserbot** 
         Source **( {} )**
         Translation **( {} )**
         {}""".format(
            after_tr_text, lan, translated
        )
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_or_reply(event, str(exc))


