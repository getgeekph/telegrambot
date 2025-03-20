from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Define conversation states
DATE, HOURS, LINK, PENDING, SKIPPED, CURRENT_TASK, CHALLENGES, RESOLVED_ISSUES, FEEDBACK = range(9)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Please provide the summary for today's tasks.\n\nDate (YYYY-MM-DD):")
    return DATE

def date(update: Update, context: CallbackContext) -> int:
    context.user_data['date'] = update.message.text
    update.message.reply_text("Total Hours Worked:")
    return HOURS

def hours(update: Update, context: CallbackContext) -> int:
    context.user_data['hours'] = update.message.text
    update.message.reply_text("Is the link active? (Yes/No):")
    return LINK

def link(update: Update, context: CallbackContext) -> int:
    context.user_data['link'] = update.message.text
    update.message.reply_text("Any pending tasks?")
    return PENDING

def pending(update: Update, context: CallbackContext) -> int:
    context.user_data['pending'] = update.message.text
    update.message.reply_text("Any tasks skipped?")
    return SKIPPED

def skipped(update: Update, context: CallbackContext) -> int:
    context.user_data['skipped'] = update.message.text
    update.message.reply_text("What are you currently working on?")
    return CURRENT_TASK

def current_task(update: Update, context: CallbackContext) -> int:
    context.user_data['current_task'] = update.message.text
    update.message.reply_text("Are there any challenges/problems that you need help with?")
    return CHALLENGES

def challenges(update: Update, context: CallbackContext) -> int:
    context.user_data['challenges'] = update.message.text
    update.message.reply_text("Any issues you encountered that you were able to resolve?")
    return RESOLVED_ISSUES

def resolved_issues(update: Update, context: CallbackContext) -> int:
    context.user_data['resolved_issues'] = update.message.text
    update.message.reply_text("Any feedback/suggestions?")
    return FEEDBACK

def feedback(update: Update, context: CallbackContext) -> int:
    context.user_data['feedback'] = update.message.text
    
    # Log the data (can be stored in Google Sheets, a database, or a local file)
    summary = (f"Task Summary:\n"
               f"Date: {context.user_data['date']}\n"
               f"Total Hours Worked: {context.user_data['hours']}\n"
               f"Link Active: {context.user_data['link']}\n"
               f"Pending: {context.user_data['pending']}\n"
               f"Skipped: {context.user_data['skipped']}\n"
               f"Current Task: {context.user_data['current_task']}\n"
               f"Challenges: {context.user_data['challenges']}\n"
               f"Resolved Issues: {context.user_data['resolved_issues']}\n"
               f"Feedback: {context.user_data['feedback']}")
    
    update.message.reply_text("Thank you for submitting your report!\n\n" + summary)
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Task summary submission canceled.")
    return ConversationHandler.END

def main():
    updater = Updater("YOUR_BOT_TOKEN")
    dispatcher = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            DATE: [MessageHandler(Filters.text & ~Filters.command, date)],
            HOURS: [MessageHandler(Filters.text & ~Filters.command, hours)],
            LINK: [MessageHandler(Filters.text & ~Filters.command, link)],
            PENDING: [MessageHandler(Filters.text & ~Filters.command, pending)],
            SKIPPED: [MessageHandler(Filters.text & ~Filters.command, skipped)],
            CURRENT_TASK: [MessageHandler(Filters.text & ~Filters.command, current_task)],
            CHALLENGES: [MessageHandler(Filters.text & ~Filters.command, challenges)],
            RESOLVED_ISSUES: [MessageHandler(Filters.text & ~Filters.command, resolved_issues)],
            FEEDBACK: [MessageHandler(Filters.text & ~Filters.command, feedback)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
