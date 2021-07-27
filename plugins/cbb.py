
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Contact Person : 📞<a href='tg://user?id={OWNER_ID}'>Click Here</a></b>",
          disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚙️ Tutor ⚙️ ", callback_data = "tutor"),
                        InlineKeyboardButton("❌ Tutup ❌", callback_data = "close")
                    ]
                ]
            )
        )
                
    elif data == "tutor":
        await query.message.edit_text(
            text = f"<b>Tutor</b>",
          disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Tentang Bot 🤖", callback_data = "about"),
                        InlineKeyboardButton("❌ Tutup ❌", callback_data = "close")
                    ]
                ]
            )
        )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
