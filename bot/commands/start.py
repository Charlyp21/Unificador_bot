from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_message:
        return

    await update.effective_message.reply_text(
        "Bienvenido al Unificador Bot. Usa /ayuda para ver los comandos disponibles."
    )


def register_start_command(application: Application) -> None:
    application.add_handler(CommandHandler("start", start_command))
