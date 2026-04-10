from pathlib import Path

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets" / "horarios"
SEMESTER_ASSET_MAP = {
    2: "2.png",
    4: "4.png",
    6: "6.png",
}


def _usage_text() -> str:
    return (
        "Uso: /horario #\n"
        "Semestres disponibles: 2, 4 y 6.\n"
        "Ejemplo: /horario 4"
    )


async def horario_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_message:
        return

    if not context.args:
        await update.effective_message.reply_text(_usage_text())
        return

    semester_arg = context.args[0].strip()
    if not semester_arg.isdigit():
        await update.effective_message.reply_text(
            "Debes indicar un numero de semestre.\n" + _usage_text()
        )
        return

    semester = int(semester_arg)
    asset_name = SEMESTER_ASSET_MAP.get(semester)
    if not asset_name:
        await update.effective_message.reply_text(
            "No tengo horario para ese semestre.\n" + _usage_text()
        )
        return

    asset_path = ASSETS_DIR / asset_name
    if not asset_path.exists():
        await update.effective_message.reply_text(
            "No encontre la imagen configurada para ese semestre."
        )
        return

    with asset_path.open("rb") as photo_file:
        await update.effective_message.reply_photo(
            photo=photo_file,
            caption=f"Horario de semestre {semester}",
        )


def register_horario_command(application: Application) -> None:
    application.add_handler(CommandHandler("horario", horario_command))
