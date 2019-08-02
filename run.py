from github3 import login, GitHub
import time
g = login('user', password='password')


anon = GitHub()
followers = g.followers()
# Follow all user followers
for follower in followers:
    if not g.is_following(follower):
        print("following: " + str(follower))
        print(g.follow(follower))
        time.sleep(220)
