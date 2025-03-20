import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Get bot token from environment variable
TOKEN = os.getenv("7898450424:AAG0ix3u1QSVDeJax96vEQ3IUnOzOHdLpy0")

# Define states for conversation
DATE, HOURS, LINK, PENDING, SKIPPED, CURRENT_TASK, CHALLENGES, RESOLVED_ISSUES, FEEDBACK = range(9)

# Dictionary to store responses
user_data = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Please provide the summary for today's tasks.\n\n📅 What is today's date?")
    return DATE

def get_date(update: Update, context: CallbackContext):
    user_data["date"] = update.message.text
    update.message.reply_text("⏳ How many total hours did you work today?")
    return HOURS

def get_hours(update: Update, context: CallbackContext):
    user_data["hours_worked"] = update.message.text
    update.message.reply_text("🔗 Is the link active? (Yes/No)")
    return LINK

def get_link(update: Update, context: CallbackContext):
    user_data["link_status"] = update.message.text
    update.message.reply_text("📌 What tasks are still pending?")
    return PENDING

def get_pending(update: Update, context: CallbackContext):
    user_data["pending_tasks"] = update.message.text
    update.message.reply_text("❌ What tasks were skipped today?")
    return SKIPPED

def get_skipped(update: Update, context: CallbackContext):
    user_data["skipped_tasks"] = update.message.text
    update.message.reply_text("🛠️ What are you currently working on?")
    return CURRENT_TASK

def get_current_task(update: Update, context: CallbackContext):
    user_data["current_task"] = update.message.text
    update.message.reply_text("🚨 Any challenges/problems you need help with?")
    return CHALLENGES

def get_challenges(update: Update, context: CallbackContext):
    user_data["challenges"] = update.message.text
    update.message.reply_text("✅ Any issues you encountered that you were able to resolv
