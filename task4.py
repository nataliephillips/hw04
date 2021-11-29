import praw
import time

reddit = praw.Reddit('bot')

count = 0
for submission in reddit.subreddit("liberalstupidity").hot(limit=300):
    a = submission.title
    b = submission.url
    try:
        reddit.subreddit('BotTown2').submit(a, url=b)
    except AttributeError:
        pass
    count+=1
    print("reposted comments = ", count)
    time.sleep(20)
