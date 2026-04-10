from pathlib import Path
import logging
import asyncio

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, ContextTypes

from bot.commands import register_command_handlers
from bot.config import Settings


LOGGER = logging.getLogger(__name__)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    LOGGER.exception("Unhandled error while processing an update", exc_info=context.error)

    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "Ocurrio un error inesperado. Intenta de nuevo en unos minutos."
        )


def build_application(settings: Settings) -> Application:
    application = Application.builder().token(settings.telegram_token).build()
    application.bot_data["settings"] = settings

    register_command_handlers(application)
    application.add_error_handler(error_handler)
    return application


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    load_dotenv(base_dir / ".env")

    settings = Settings.from_env(base_dir)

    logging.basicConfig(
        level=getattr(logging, settings.log_level, logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    LOGGER.info("Starting bot polling")
    app = build_application(settings)

    # Python 3.14 no longer creates a default loop in the main thread.
    # PTB 21.x expects one when calling run_polling().
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
