from pyrogram import Client, filters
from FUNC.defs import *


@Client.on_message(filters.command("howgp", [".", "/"]))
async def cmd_howgp(Client, message):
    try:
        texta = f"""<b>
PARA AÑADIR ESTE BOT A TU GRUPO -

Requisitos: <b>Tu grupo debe tener al menos 50 miembros.</b>

Pasos para autorizar tu grupo:
➔ Agrega a @RETROCHKBOT a tu grupo como administrador.
➔ Copia el nombre de usuario de tu grupo o el enlace de invitación.
➔ Contacta a @Eretro_7 y envíale el nombre de usuario o el enlace de invitación de tu grupo.

¡Eso es todo! Una vez que esté en línea, aprobare tu grupo! ✅.

</b>"""
        await message.reply_text(texta, message.id)

    except Exception as e:
        import traceback

        await error_log(traceback.format_exc())
