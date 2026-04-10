from telegram.ext import Application

from bot.commands.ayuda import register_ayuda_command
from bot.commands.comunidad import register_comunidad_command
from bot.commands.contactos import register_contactos_command
from bot.commands.eventos import register_eventos_command
from bot.commands.horario import register_horario_command
from bot.commands.start import register_start_command


def register_command_handlers(application: Application) -> None:
    register_start_command(application)
    register_ayuda_command(application)
    register_contactos_command(application)
    register_comunidad_command(application)
    register_horario_command(application)
    register_eventos_command(application)
