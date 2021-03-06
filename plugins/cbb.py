
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"š Bahasa pemrograman : <b><code>Python3</code></b>\nš Contact Person : <b><a href='tg://user?id={OWNER_ID}'>Owner Bot</a></b>\nš¦ø Creator <b><a href='t.me/lullaby330'>Lullaby</a></b>\nBot Ini Dibuat Dengan ā¤ļø Selamat menikmati š¤",
          disable_web_page_preview = True,

            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Tutor āļø ", callback_data = "tutor"),
                        InlineKeyboardButton("Pesan Bot š¦ø", url="t.me/fybadmin")
                    ],
                    [
                        InlineKeyboardButton("Tutup ā", callback_data = "close")
                    ]
                ]
            )
        )

    elif data == "tutor":
        await query.message.edit_text(
            text = f"<b>Tutorial Pemakaian</b>\n\n<b>āļø Jika Sudah Join Channel Atau Group</b>\nKalian Hanya Perlu Mendapatkan Link Dari Channel Atau Group Kemudian Tekan Tombol 'Start' Di Bot\n\n<b>ā Jika Belum Join Channel Atau Group</b>\n Kalian Wajib Join Agar Video Dapat Di Akses\n\n Jika Video Tidak Muncul Hubungi <b><a href='tg://user?id={OWNER_ID}'>Owner Bot</a></b>",
          disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Tentang Bot š¤", callback_data = "about"),
                        InlineKeyboardButton("Tutup ā", callback_data = "close")
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
