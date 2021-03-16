from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
Gua Bot Musik Yang Dapat Menemani Kegabutan Kalian Semua.
Cara Penggunaan Cukup Mudah! Klik Saja Tombol Dibawah Maka Kan Ada Tutorialnya.
JANGAN LUPA SUPPORT DIBAWAH! JANGAN MALAS MEMBACA!!!.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📖 Panduan Pengguna", url="https://telegra.ph/ʜɪʟᴇʀ-ʙʀ-03-16"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/storyangkasa"
                    ),
                    InlineKeyboardButton(
                        "🔎 SPACE-BOT", url="https://github.com/AngkasaBoy/Space-Bot"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
