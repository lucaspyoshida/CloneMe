import os
import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import uuid
import asyncio

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def generate_session_id():
    return str(uuid.uuid4())

model = "gemini-2.0-flash-lite-001"
SESSION_ID  = generate_session_id()
APP_NAME = "batepapo"
USER_ID = "user123"

session_service = InMemorySessionService()

session = asyncio.run(session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
))


root_agent = Agent(
   name=APP_NAME,
   model=model,  
   description="Agent to answer questions and talk like a good frind",
   instruction="You are a friendly and helpful assistant. Always provide accurate and concise answers to the user's questions."
)

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)



async def conversa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assunto = update.message.text
    content = types.Content(
        role="user",
        parts=[types.Part(text=assunto)]
    )

    loop = asyncio.get_event_loop()
    events = await loop.run_in_executor(
        None,
        lambda: runner.run(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=content
        )
    )

    final = next(
        e for e in events
        if e.is_final_response()
    )
    resposta = final.content.parts[0].text

    await update.message.reply_text(resposta)



# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# # set higher logging level for httpx to avoid all GET and POST requests being logged
# logging.getLogger("httpx").setLevel(logging.WARNING)

# logger = logging.getLogger(__name__)
logging.getLogger("google_adk").setLevel(logging.WARNING)
logging.getLogger("telegram.ext").setLevel(logging.WARNING)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, conversa))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    main()