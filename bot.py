import praw
import random
import datetime
import time


# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "The [FIRST] transport [JOB] told MP [LASTNAME] that a new £[NUMBER] Integrated Rail Plan for the north and the Midlands will instead deliver [UNIQUE] train journeys both earlier and cheaper than the original HS2 plans would have done. "
    "[NY] [JOB] General [LASTNAME] estimated that [NUMBER] of Americans’ identities were stolen and used in spam campaigns that support [CAMPAIGN]. My research found at least [NUMBER] [FAKE] [CAMPAIGN] comments, with suspicions about many more. You should check into the campaigns before accepting them.",
    "Don't forget your [BANDANA]. If you signed up [ONLINE] and still need to pick up your [BANDANA], don't worry -- we will have them there! (You can also pick up your [BANDANA] at [LOCATION], or any night mission). This is your last chance though, so enjoy!", 
    "There were likely multiple other campaigns in [NY] aimed at injecting what may total [NUMBER] [CAMPAIGN] comments into the system. It’s highly likely that more than [NUMBER] percent of the truly [UNIQUE] comments were in favor of keeping [CAMPAIGN].",
    "If I wanted to do the analysis without having to set up the tools and infrastructure typically used for “[CAMPAIGN],” I needed to break down the [NUMBER] comments and 60GB+ worth of text data and metadata into smaller pieces. The [FIRST] and largest cluster of [CAMPAIGN] documents was especially [UNIQUE]. ",
    "If even a quarter of these [CAMPAIGN] in [NY] comments are found to have been [FAKE], that would still result in more than [NUMBER] faked [CAMPAIGN] comments, each with an email address attached. Further verification [SHOULD] be done on the email addresses used to submit these likely [FAKE] comments.",
    ]

replacements = {
    'NY' : ['NY', 'LA', 'GA', 'AZ', 'MA'],
    'NUMBER' : ['1.3 million', 'hundred thousand', '10', '2 million'],
    'LASTNAME' : ['Phillips', 'Washington', 'Ahn', 'Feldman', 'Carmel'],
    'CAMPAIGN' : ['net neutrality', 'environmental cleanup', 'saving the turtles', 'big brother'],
    'JOB' : ['District Attorney', 'Governor', 'street sweeper', 'dentist'],
    'FAKE' : ['fake', 'real', 'terrible', 'false', 'incorrect', 'spam'],
    'BANDANA'  : ['hats', 'bandanas', 'beanie', 'flags'],
    'ONLINE' : ['online', 'on the web', 'on the computer'],
    'LOCATION' : ['the home', 'store', 'conference room'],
    'UNIQUE' : ['unique', 'special', 'one of  a kind', 'singular', 'distinct', 'notable'],
    'FIRST' : ['first', 'first and foremost', 'earliest', 'initial'],
    'SHOULD' : ['should', 'must', 'ought to', 'need to'],
    'PROGRAMMER' : ['programmer', 'developer', 'pythonista', 'software engineer'],
    'LEARN' : ['learn', 'master', 'study'],
    }


def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    sentence = random.choice(madlibs)
    for key in replacements.keys():
        sentence = sentence.replace('['+key+']',random.choice(replacements[key])) 
    return sentence 

# connect to reddit 
reddit = praw.Reddit('bot2', user_agent='newbotnat')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown/comments/qxnpbo/text_submission_for_lecture_bot/?'
#submission_url = 'https://old.reddit.com/r/BotTown/comments/qzwqwq/check_3/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once


while True:
    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    #submission.comments.replace_more(limit=None)
    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = submission.comments.list()
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'newbotnat':
            not_my_comments.append(comment)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    """
    for comment in not_my_comments:
            print("comment author: ", str(comment.author))
    print('len(not_my_comments)=',len(not_my_comments))
    """

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print ("has not comment: ", has_not_commented)
    
    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies =[]

        for comment in not_my_comments:
            authors = []
            for reply in comment.replies:
                authors.append(str(reply.author))
            if "newbotnat" in authors:
                pass
            else: 
                comments_without_replies.append(comment)
        # for comment in comments_without_replies:
            # print("comment: ", comment)
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        
        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIException: 
            print("not replying to a comment that has been deleted")
          
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit("BotTown").hot(limit=5)))
    # We sleep just for 1 second at the end of the while loop.

    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)