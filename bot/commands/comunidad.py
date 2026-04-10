import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from bot.config import Settings
from bot.utils.data_loader import DataFormatError, load_community


LOGGER = logging.getLogger(__name__)


async def comunidad_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_message:
        return

    settings = context.application.bot_data.get("settings")
    if not isinstance(settings, Settings):
        await update.effective_message.reply_text(
            "No se pudo cargar la configuracion del bot."
        )
        return

    try:
        community = load_community(settings.community_file)
    except (FileNotFoundError, DataFormatError) as exc:
        LOGGER.warning("Community data error: %s", exc)
        await update.effective_message.reply_text(
            "No pude leer la comunidad en este momento."
        )
        return

    if not community:
        await update.effective_message.reply_text("No hay links configurados.")
        return

    lines = ["Links de la fraternidad:"]
    for label, url in community.items():
        lines.append(f"- {label}: {url}")

    await update.effective_message.reply_text("\n".join(lines))


def register_comunidad_command(application: Application) -> None:
    application.add_handler(CommandHandler("comunidad", comunidad_command))