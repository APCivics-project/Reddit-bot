import praw
import multiprocessing
reddit = praw.Reddit(
    client_id="eBc3hGTBg5RhIKoGyVJPKA",
    client_secret="iDrw30iHOc97ify431znKZSsGvckbw",
    user_agent="<console:BiasScanner:1.0>", )

subreddit_List = ["politics","Coronavirus","Conservative","AntiVaxxers"]
key_words = ["sterile","microchips","magnetic","mRNA"]
# https://www.reddit.com/r/AntiVaxxers/comments/ovpntm/the_inventor_of_mrna_technology_speaks_out/
def searchSubreddits():
    for sub in range(len(subreddit_List)):
        for submission in reddit.subreddit(subreddit_List[sub]).new(limit=None):
            for words in range(len(key_words)):
                if key_words[words] in submission.title:
                    print(subreddit_List[sub])
                    print(submission.title)


def searchComment(submission):
    for comment in submission.comments:
        if hasattr(comment, "body"):
            for words in range(len(key_words)):
                if key_words[words] in comment.body:
                    print(comment.body)
searchSubreddits()