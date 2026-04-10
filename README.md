# Unificador_bot
Bot de telegram con diversas utilidades enfocado en el uso por parte de la comunidad de la licenciatura en neurociencias.

## Stack
- Python 3.10+
- python-telegram-bot
- python-dotenv
- google-api-python-client

## Estructura del proyecto
```
.
├── assets/
│   └── horarios/
├── bot/
│   ├── commands/
│   │   ├── ayuda.py
│   │   ├── comunidad.py
│   │   ├── contactos.py
│   │   ├── eventos.py
│   │   ├── horario.py
│   │   └── start.py
│   ├── utils/
│   │   ├── calendar_client.py
│   │   └── data_loader.py
│   ├── config.py
│   └── main.py
├── data/
│   ├── comunidad.json
│   └── contactos.json
├── .env.example
├── .gitignore
└── requirements.txt
```

## Instalacion
1. Crear o activar entorno virtual.
2. Instalar dependencias:
	```bash
	pip install -r requirements.txt
	```
3. Crear `.env` a partir de `.env.example` y colocar el token real.

## Variables de entorno
- `TELEGRAM_TOKEN`: token del bot generado con BotFather.
- `LOG_LEVEL`: nivel de logs (`INFO`, `DEBUG`, etc.).
- `CONTACTS_FILE`: ruta al JSON de contactos (default: `data/contactos.json`).
- `COMMUNITY_FILE`: ruta al JSON de comunidad (default: `data/comunidad.json`).
- `GOOGLE_CALENDAR_API_KEY`: API key de Google Cloud para Calendar API.
- `GOOGLE_CALENDAR_ID`: ID del calendario a consultar.

## Ejecucion
```bash
python -m bot.main
```

## Comandos implementados
- `/start`: mensaje de bienvenida.
- `/ayuda`: lista de comandos.
- `/contactos`: muestra links desde `data/contactos.json`.
- `/comunidad`: muestra links desde `data/comunidad.json`.
- `/horario #`: envia una imagen de horario segun el semestre.
- `/eventos`: devuelve los proximos 5 eventos de Google Calendar.

## Estado de /horario
El comando `/horario` ya esta activo y usa un diccionario condicional con formato:
- clave: numero de semestre (`2`, `4`, `6`)
- valor: ruta del asset correspondiente

Ejemplo de uso esperado:
```text
/horario 4
```

Semestres soportados en la configuracion actual: 2, 4 y 6.

## Estado de /eventos
El comando `/eventos` usa Google Calendar API y devuelve los proximos 5 eventos del calendario configurado en `.env`.

## Como agregar un nuevo comando
1. Crear un archivo en `bot/commands/`.
2. Definir la funcion del comando y su `register_*`.
3. Registrar el comando en `bot/commands/__init__.py`.
