from github3 import login, GitHub
import time
g = login('user', password='password')


anon = GitHub()
followers = g.followers()
# Follow all user followers
for follower in followers:
    print("following: " + str(follower))
    print(g.follow(follower))
    time.sleep(120)
