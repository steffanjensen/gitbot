from github3 import login, GitHub
import time


class github(object):
    # Initizilate the start
    def __init__(
        self,
        username,
        password,
        max_limit=100,
        delay=10,
        proxy=None
        ):
        self.username = username
        self.password = password
        self.max_limit = max_limit
        self.delay = delay
        self.g = login(username=username, password=password)
        self.anon = GitHub()
        print("Logged in ")

    def follow_users_followers(self, username):
        ''' Follow a users followers '''
        followers = self.g.followers_of(username)
        for follower in followers:
            if not self.g.is_following(follower):
                print("following: " + str(follower))
                print(self.g.follow(follower))
                print("sleeping " + str(self.delay) + " seconds")
                time.sleep(self.delay)
            else:
                print("Already following this user")

    def unfollow_non_followers(self):
        ''' unfollow all non mutal followers '''
        followings = self.g.following()
        for following in followings:
            print(self.g.unfollow(following))
            print("unfollowed " + str(following))
            time.sleep(self.delay)
        else:
            pass



