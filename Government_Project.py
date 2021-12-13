import praw
import wordninja

# testing if I can commit.
reddit = praw.Reddit(
    client_id="eBc3hGTBg5RhIKoGyVJPKA",
    client_secret="iDrw30iHOc97ify431znKZSsGvckbw",
    user_agent="<console:BiasScanner:1.0>", )

subreddit_List = ["politics", "Coronavirus", "Conservative", "AntiVaxxers"]

conservative_subs = ["Conservative"]  # ,"trump" if the bot gets permission
liberal_subs = ["democrats","Trumpvirus"]  # "Trumpvirus",
other_subs = ["Coronavirus",'politics',"Coronavirus","AntiVaxxers","news"]

key_words = ["mRNA", "Covid", "corona virus", "Covid-19", "vaccine"
    , "mask", "autisim", "lockdown", "booster"
    , "omicron", "delta", "CDC", "Fauci"]
news_sources = [("npr", -.11), ("ny", -.19),
                ("hill", -.022), ("cnn", -.20),
                ("whitehouse", 0), ("cnbc", -.04),
                ("newsweek", -.14), ("abc", -.11),
                ("politico", -.15), ("sentinal", -.14),
                ("reuters", -.03), ("ap", -.05),
                ("insider", -.12), ("washington", -.18),
                ("rolling", -.31), ("guardian", -.22),  # all the liberal ones
                ("fox", .34), ("town", .49),
                ("nbc", -.18), ("max", .66),
                ("bart", .40), ("defender", .5),
                ("wire", .33), ("forbes", -.07),
                ("cbs",-.08),("bloomburg",-.06),
                ("yahoo",-.15), ("atlantic",-.23),
                ("msnbc",-.32),("today",-.08)]


def searchSubreddits(sub_list):
    data = []  # data is the following per post: [subreddit,keyphrase found,title,news link]
    one_found = None
    for sub in range(len(sub_list)):
        for submission in reddit.subreddit(sub_list[sub]).new(limit=None):
            words_found = []
            for words in range(len(key_words)):
                if key_words[words].casefold() in submission.title.casefold():
                    words_found.append(key_words[words])  # case fold makes it case insensitive
                    one_found = True
                if words == 12 and one_found == True:
                    data.append([sub_list[sub], words_found, submission.title, submission.url])
                    one_found = False

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
#cons_list = searchSubreddits(conservative_subs)
#other_list = searchSubreddits(other_subs)

def newsfrequency(data):
    biases = []
    for links in range(len(data)):
        split_list = wordninja.split(data[links][3])
        for words in range(len(split_list)):
            for sources in range(len(news_sources)):
              if news_sources[sources][0] in split_list[words]:
                  biases.append(news_sources[sources][1])
    return biases



print(newsfrequency(lib_list))
#for i in range(len(list)):
 #   print(other_subs[i])
