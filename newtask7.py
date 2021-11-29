from typing import Text
import praw
import random
import datetime
import time
from textblob import TextBlob

reddit = praw.Reddit('bot')

reddit_debate_url = 'https://www.reddit.com/r/BotTown2/comments/r4ptwu/aoc_challenges_trump_to_release_his_college/'
submission = reddit.submission(url=reddit_debate_url)

commentcount = 0
submissioncount = 0
polcount = 0

while True:
    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = submission.comments.list()

    # upvote comment fav
    for comment in all_comments:
        if 'biden' in comment.body.lower():
            comment.upvote()
            commentcount+=1
            print('commentcount = ', commentcount)
    # downvote comment opp
    for comment in all_comments:
        if 'trump' in comment.body.lower():
            comment.downvote()
            commentcount+=1
            print('commentcount = ', commentcount)
    # upvote submission fav
    if 'biden' in submission.title.lower():
        submission.upvote()
        submissioncount+=1
        print('submissioncount = ', submissioncount)
        # downvote submission opp
    if 'trump' in submission.title.lower():
        submission.downvote()
        submissioncount+=1
        print('submissioncount = ', submissioncount)
    # up/down vote polarity
    for comment in all_comments:
        blob = TextBlob(str(comment.body))
        if 'biden' in comment.body.lower():
            if blob.sentiment.polarity >= 0:
                comment.upvote()
                polcount+=1
                print('polcount = ', polcount)
            if blob.sentiment.polarity < 0:
                comment.downvote()
                polcount+=1
                print('polcount = ', polcount)
    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=None)))
