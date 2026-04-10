import logging
from datetime import datetime

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from bot.config import Settings
from bot.utils.calendar_client import get_next_events


LOGGER = logging.getLogger(__name__)


def _format_event_start(event_start: dict[str, str]) -> str:
    if "dateTime" in event_start:
        try:
            dt = datetime.fromisoformat(event_start["dateTime"].replace("Z", "+00:00"))
            return dt.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            return event_start["dateTime"]

    if "date" in event_start:
        return f"{event_start['date']} (todo el dia)"

    return "Sin fecha"


async def eventos_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_message:
        return

    settings = context.application.bot_data.get("settings")
    if not isinstance(settings, Settings):
        await update.effective_message.reply_text("No se pudo cargar la configuracion del bot.")
        return

    if not settings.google_calendar_api_key or not settings.google_calendar_id:
        await update.effective_message.reply_text(
            "Falta configurar Google Calendar. Revisa GOOGLE_CALENDAR_API_KEY y GOOGLE_CALENDAR_ID en .env"
        )
        return

    try:
        events = get_next_events(
            api_key=settings.google_calendar_api_key,
            calendar_id=settings.google_calendar_id,
            max_results=5,
        )
    except Exception as exc:
        LOGGER.exception("Google Calendar request failed", exc_info=exc)
        await update.effective_message.reply_text(
            "No pude consultar el calendario en este momento."
        )
        return

    if not events:
        await update.effective_message.reply_text("No hay eventos proximos.")
        return

    lines = ["Proximos 5 eventos:"]
    for index, event in enumerate(events, start=1):
        start = _format_event_start(event.get("start", {}))
        title = event.get("summary", "Sin titulo")
        lines.append(f"{index}. {title} - {start}")

    await update.effective_message.reply_text("\n".join(lines))


def register_eventos_command(application: Application) -> None:
    application.add_handler(CommandHandler("eventos", eventos_command))
