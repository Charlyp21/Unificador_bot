from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


HELP_TEXT = "\n".join(
    [
        "Comandos disponibles:",
        "/ayuda - Lista de comandos",
        "/contactos - Links de contacto utiles",
        "/comunidad - Links de grupos de la fraternidad",
        "/horario # - Envia la imagen del horario por semestre",
        "/eventos - Muestra los proximos 5 eventos del calendario",
    ]
)


async def ayuda_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_message:
        return

    await update.effective_message.reply_text(HELP_TEXT)


def register_ayuda_command(application: Application) -> None:
    application.add_handler(CommandHandler("ayuda", ayuda_command))
