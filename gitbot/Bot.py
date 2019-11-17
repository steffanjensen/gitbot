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
        
    def unlimited_commits(self):
        ''' Make Unlimited commits'''
        with open("rockstar.py", "w+") as f:
            randoms = random.randint(100, 400)
            f.write(str(randoms))
        os.system("git add rockstar.py")
        os.system("git commit -m 'fun'")

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

    def follow_repo_contributes(self, username):
        ''' Follow a users followers '''
        repos = self.g.repositories_by(username)
        x = 0
        for repo in repos:
            if x < 20:
                repo = str(repo)
                repo = repo.split("/")
                print(repo[1])
                followers = self.g.repository(repo[0], repo[1])
                followers = (set(followers.contributors()))
                print(followers)
                for follower in followers:
                    if not self.g.is_following(follower):
                        print("following: " + str(follower))
                        print(self.g.follow(follower))
                        print("sleeping " + str(self.delay) + " seconds")
                        time.sleep(self.delay)
                    else:
                        print("Already following this user")
                        time.sleep(self.delay)

    def unfollow_non_followers(self):
        ''' unfollow all non mutal followers '''
        followings = self.g.following()
        for following in followings:
            print(self.g.unfollow(following))
            print("unfollowed " + str(following))
            time.sleep(self.delay)
        else:
            pass

    def star_followers_repo(self, username):
        ''' Star followers repos '''
        followers = self.g.followers_of(username)
        for follower in followers:
            repos = self.g.repositories_by(follower)
            x = 0
            for repo in repos:
                if x < 2:
                    print("Starring " + str(follower) + " " + str(repo))
                    repo = str(repo)
                    repo = repo.split("/")
                    print(repo[1])
                    print(self.g.star(follower, repo[1]))
                    time.sleep(self.delay)
                    x += 1
                else:
                    print("Liking next profile")

            else:
                pass

    def unstar_repos(self, username):
        starred = self.g.starred_by(username)
        for star in starred:
            star = str(star)
            star = star.split("/")
            print("Unstar " + str(star))
            print(self.g.unstar(star[0], star[1]))
            time.sleep(self.delay)
            
    def unlimited_contributions(username, password, repo):
        while True:
            rock_it_bro = RockStar(days=300)
            rock_it_bro.make_me_a_rockstar()
            os.system("git clone https://github.com/" + username + "/" + repo + ".git")
            os.system("git push https://" + username + ":" + password + " @github.com/" + username + "/" + repo + ".git --all")
