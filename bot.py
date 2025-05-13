import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /start"""
    user = update.effective_user
    await update.message.reply_html(
        f"Привет {user.mention_html()}! Я твой первый бот.",
        reply_markup=None
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /help"""
    await update.message.reply_text("Чем я могу помочь? Просто напиши мне что-нибудь.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Эхо-ответ на текстовые сообщения"""
    await update.message.reply_text(update.message.text)

def main() -> None:
    """Запускает бота"""
    application = Application.builder().token("7282724004:AAEV-3rebVWQ4nL8jg0ESQzd_upMf6odnrg").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
