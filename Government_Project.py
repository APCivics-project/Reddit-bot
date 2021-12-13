import praw
import requests
from bs4 import BeautifulSoup
import wordninja

# testing if I can commit.
reddit = praw.Reddit(
    client_id="eBc3hGTBg5RhIKoGyVJPKA",
    client_secret="iDrw30iHOc97ify431znKZSsGvckbw",
    user_agent="<console:BiasScanner:1.0>", )

subreddit_List = ["politics", "Coronavirus", "Conservative", "AntiVaxxers"]

conservative_subs = ["Conservative"]  # ,"trump" if the bot gets permission
liberal_subs = ["democrats"]  # "Trumpvirus",
other_subs = ["Coronavirus"]  # 'politics',"Coronavirus","AntiVaxxers","news"

key_words = ["mRNA", "Covid", "corona virus", "Covid-19", "vaccine"
    , "mask", "autisim", "lockdown", "booster"
    , "omicron", "delta", "CDC", "Fauci"]
news_sources = [(["npr"], -.11), (["ny", "times"], -.19),
                (["hill"], -.022), (["cnn"], -.20),
                (["whitehouse"], 0), (["cnbc"], -.04)
                (["newsweek"], -.14), (["abc"], -.11),
                (["politico"], -.15), (["sun", "sentinal"], -.14),
                (["reuters"], -.03), (["ap"], -.05),
                (["insider"],-.12),(["washington","post"],-.18),
                (["rolling","stone"],-.31),(["guardian"],-.22)]


def searchSubreddits(sub_list):
    data = []  # data is the following per post: [subreddit,keyphrase found,title,news link]
    for sub in range(len(sub_list)):
        for submission in reddit.subreddit(sub_list[sub]).new(limit=None):
            for words in range(len(key_words)):
                if key_words[words].casefold() in submission.title.casefold():  # case fold makes it case insensitive

                    # if submission.link_flair_text != None:
                    # print("flair is" + submission.link_flair_text)

                    data.append([sub_list[sub], key_words[words], submission.title, submission.url])
                    break
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


lib_list = searchSubreddits(liberal_subs)


# cons_list = searchSubreddits(conservative_subs)
# other_list = searchSubreddits(other_subs)
def newsfrequency(data):
    for links in range(len(data)):
        print(wordninja.split(data[links][3]))


newsfrequency(lib_list)
