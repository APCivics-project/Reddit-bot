import praw
import multiprocessing
#testing if I can commit.
reddit = praw.Reddit(
    client_id="eBc3hGTBg5RhIKoGyVJPKA",
    client_secret="iDrw30iHOc97ify431znKZSsGvckbw",
    user_agent="<console:BiasScanner:1.0>", )

subreddit_List = ["politics","Coronavirus","Conservative","AntiVaxxers"]


conservative_subs = ["Conservative","trump"]
liberal_subs = ["Trumpvirus","democrats"]
other_subs = ['politics',"Coronavirus","AntiVaxxers","news"]
key_words = ["sterile","microchips","magnetic","mRNA"
            ,"Covid","corona virus","Covid-19","vaccine"
            ,"mask","autisim","lockdown","booster"]

def searchSubreddits(sub_list):
    data = [] # data is the following per post: [subreddit,keyphrase found,title,news link]
    for sub in range(len(sub_list)):
        for submission in reddit.subreddit(sub_list[sub]).new(limit=None):
            for words in range(len(key_words)):
                if key_words[words].casefold() in submission.title.casefold(): #case fold makes it case insensitive

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
print(searchSubreddits(liberal_subs))
print(searchSubreddits(conservative_subs))
print(searchSubreddits(other_subs))
# ADD 0 TO 1 THING OWEN
