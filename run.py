from gitbot import Bot

# Example on how to run this bot
bot = Bot.github("yourusername", "yourpassword", delay=30)
bot.unfollow_non_followers()
bot.follow_users_followers("reliefs")
