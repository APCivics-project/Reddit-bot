import praw
import multiprocessing
#testing if I can commit.
reddit = praw.Reddit(
    client_id="eBc3hGTBg5RhIKoGyVJPKA",
    client_secret="iDrw30iHOc97ify431znKZSsGvckbw",
    user_agent="<console:BiasScanner:1.0>", )

subreddit_List = ["politics","Coronavirus","Conservative","AntiVaxxers"]


conservative = ["Conservative","trump"]
liberal = ["Trumpvirus","democrats"]
other_subs = ['politics',"Coronavirus","AntiVaxxers","news"]
key_words = ["sterile","microchips","magnetic","mRNA","Covid","vaccine"]
# https://www.reddit.com/r/AntiVaxxers/comments/ovpntm/the_inventor_of_mrna_technology_speaks_out/
def searchSubreddits(sub_list):
    data = [] # data is the following per post: [subreddit,keyphrase found,title,news link]
    for sub in range(len(sub_list)):
        for submission in reddit.subreddit(sub_list[sub]).new(limit=None):
            for words in range(len(key_words)):
                if key_words[words] in submission.title:

                    if submission.link_flair_text != None:
                        print("flair is" + submission.link_flair_text)

                    data.append([sub_list[sub],key_words[words],submission.title,submission.url])
    return data
def searchSubreddit(sub):
    for submission in reddit.subreddit(sub).hot(limit=None):
        for words in range(len(key_words)):
            if key_words[words] in submission.title:
                print(submission.link_flair_text)
                print(submission.title)

def searchComment(submission):
    for comment in submission.comments:
        if hasattr(comment, "body"):
            for words in range(len(key_words)):
                if key_words[words] in comment.body:
                    print(comment.body)
print(searchSubreddits(liberal))