import praw
import random
import datetime
import time
from textblob import TextBlob
import prawcore
from re import sub
'''
Have your bot upvote any comment or submission that mentions your favorite candidate (or downvote submission mentioning a candidate you do not like). 
I recommend creating a separate python file for performing the upvotes, and you must be able to upvote comments contained within any submission in the class subreddit.

You may earn an additional two points if you use the TextBlob sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate. 
If the comment/submission has positive sentiment, then upvote it; if the comment/submission has a negative sentiment, then downvote it.

This extra credit is "grayhat" since it may violate reddit's TOS if not done correctly.
You must up/downvote at least 100 submissions and 500 comments for the full extra credit.
'''

commentcount = 0
submissioncount = 0
polcount = 0

reddit = praw.Reddit('bot2')
for submission in list(reddit.subreddit("BotTown2").new(limit=None)):
    print("one submission is being processed")
    submission.comments.replace_more(limit=None, threshold=0)
    blob = TextBlob(str(submission.title))
    pop = blob.sentiment.polarity
    not_my_comments = []
    if 'Biden' in submission.title:
        if str(submission.author) == 'natthebot':
            print("my submission")
            pass
        else:
            print("one submission with biden and not mine is being processed")
            if pop > 0:
                submission.downvote()
                submissioncount+=1
                print("Downvoting submission", submissioncount)
            if pop <= 0:
                submission.upvote()
                submissioncount+=1
                print("Upvoting comment", submissioncount)
            else:
                pass
    for comment in submission.comments:
        if str(comment.author) != 'natthebot':
            not_my_comments.append(comment)
    for comment in not_my_comments:
        blob = TextBlob(str(comment.body))
        try:
            if 'biden' in comment.body:
                if blob.sentiment.polarity > 0:
                    comment.downvote()
                    commentcount+=1
                    print("Downvoting comment", commentcount)
                if blob.sentiment.polarity <= 0:
                    comment.upvote()
                    commentcount+=1
                    print("Upvoting comment", commentcount)   
            else:
                pass
        except prawcore.exceptions.NotFound:
            print("comment deleted")
            pass
    print("one submission checked")
    
    submission_url = reddit.subreddit("BotTown2")
    x = list(submission_url.hot(limit=None))
    submission = random.choice(x)