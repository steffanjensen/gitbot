from gitbot import Bot

# Example on how to run this bot
bot = Bot.github("yourusername", "yourpassword", delay=20)

bot.star_followers_repo("reliefs")
bot.unfollow_non_followers()
bot.follow_users_followers("reliefs")
bot.unlimited_contributions("username", "password", "repo")
