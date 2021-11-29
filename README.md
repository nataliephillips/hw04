# hw_04

[The assignment](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04)

1. What I have to do:
    1. Your completed `bot.py` file (but not your `praw.ini` file!!!) - this is attached above
    1. A `README.md` file, properly formatted with markdown syntax, that:
        1. Clearly states which politician your bot is supporting or opposing.
            1. I AM SUPPORTING BIDEN AND I OPPOSE TRUMP
        1. Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it.
            1. [my favorite thread](https://www.reddit.com/r/BotTown2/comments/r4nmic/biden_campaign_to_hammer_trump_over_pandemic/hmhxgyz/?context=3)
            1. ![Screen Shot 2021-11-28 at 10.55.35 PM.png](https://github.com/nataliephillips/hw04.github.io/blob/main/Screen%20Shot%202021-11-28%20at%2010.55.35%20PM.png)
            1. It's my favorite, because my bots are socializing. They are my children.
        1. Includes the output of running the `bot_counter.py` file on your bot to count how many comments you've created.
           The output of this command must be inside of a markdown code block (i.e. use the triple backticks notation).
            1.'''Natalies-MacBook-Pro-5:reddit nataliephillips$ python3 bot_counter.py --username=natthebot
                Version 7.4.0 of praw is outdated. Version 7.5.0 was released Sunday November 14, 2021.
                len(comments)= 738
                len(top_level_comments)= 105
                len(replies)= 633
                len(valid_top_level_comments)= 54
                len(not_self_replies)= 616
                len(valid_replies)= 593
                ========================================
                valid_comments= 647
                ========================================
                NOTE: the number valid_comments is what will be used to determine your extra credit'''
        1. Explains what you believe your score should be.
           1. I should recieve a 30/20 because I completed these:
            <li> 1. Each task in `bot.py` is worth 3 points. (6 tasks * 3 points/task = 18 points) +18 </li>
            <li> 2. The github repo is worth 2 points. +2 </li>
            <br>
            <li> 1. Getting at least 100 valid comments posted. +2 </li>
            <li> 2. Getting at least 500 valid comments posted. +2 </li>
            <li> 4. Make your bot create new submission posts instead of just new comments. +2 </li>
            <li> 7. upvote any comment or submission using TextBlob +4 </li>