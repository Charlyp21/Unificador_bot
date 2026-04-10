import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from bot.config import Settings
from bot.utils.data_loader import DataFormatError, load_contacts


LOGGER = logging.getLogger(__name__)


async def contactos_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_message:
        return

    settings = context.application.bot_data.get("settings")
    if not isinstance(settings, Settings):
        await update.effective_message.reply_text(
            "No se pudo cargar la configuracion del bot."
        )
        return

    try:
        contacts = load_contacts(settings.contacts_file)
    except (FileNotFoundError, DataFormatError) as exc:
        LOGGER.warning("Contacts data error: %s", exc)
        await update.effective_message.reply_text(
            "No pude leer los contactos en este momento."
        )
        return

    if not contacts:
        await update.effective_message.reply_text("No hay contactos configurados.")
        return

    lines = ["Links de contacto:"]
    for label, url in contacts.items():
        lines.append(f"- {label}: {url}")

    await update.effective_message.reply_text("\n".join(lines))


def register_contactos_command(application: Application) -> None:
    application.add_handler(CommandHandler("contactos", contactos_command))
