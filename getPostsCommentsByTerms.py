import praw

#main menu
def main():   
    print(
        """Welcome to my proprietary Reddit reader!
There are a few default settings you can tweak.
Let's run through them now:\n""")
    userInput = str(input("""Enter 'T' to enter new Terms to lookup.
Enter 'S' to enter new Subreddits to search.
Enter 'J' to use existing values and proceed.
Enter 'Q' to quit.\n"""))
    if userInput.lower() == 't':
        newTerms()
        main()
    if userInput.lower() == 's':
        newSubreddits()
        main()
    if userInput.lower() == 'j':
        redditSearch(termList, subredditList)
        main()
    if userInput.lower() == 'q':
        quit()
    else:
         print("Entry invalid. Now you get to go back.")
         main()

#define new terms to lookup or check old terms    
def newTerms():
    global termList
    print("Right now, the listed terms are: " + str(termList))
    userInput = str(input("Do you want to search up the default terms? (Y/N) \n"))
    if userInput.lower() == 'n':
        termList = []
        userInput = input("Old terms deleted (temporary). Please enter new comma-separated terms.\n")
        termList = userInput.split(',')
        print("Your new list of terms is " + str(termList))
        return(termList)
    if userInput.lower() == 'y':
        print("Will use old terms.")
        return(termList)
    else:
        print("Entry invalid. Now you get to go back.")
        newTerms()

#define new subreddits to lookup or check existing list
def newSubreddits():
    global subredditList
    print("Right now, the listed subreddits are: " + str(subredditList))
    userInput = str(input("Do you want to search in the default subreddits? (Y/N) \n"))
    if userInput.lower() == 'n':
        termList = []
        userInput = input("Old subreddits deleted (temporary). Please enter new comma-separated subreddits.\n")
        subredditList = userInput.replace(' ', '').split(',')
        print("Your new list of subreddits is " + str(subredditList))
        return(subredditList)
    if userInput.lower() == 'y':
        print("Will use old terms.")
        return(subredditList)
    else:
        print("Entry invalid. Now you get to go back.")
        newSubreddits()

#search listed subreddits for listed terms
def redditSearch(terms, subreddits):
    print("You will be searching " + str(len(subreddits)) + " subreddits for " + str(len(terms)) + " terms.")
    for sub in subreddits:
        subredditName = reddit.subreddit(str(sub))
        print("Searching {} posts & comments for terms.".format(subredditName))
        try:
            for submission in subredditName.new(limit=5):
                for term in terms:
                    if term in submission.title:
                        print("\nMATCH FOUND IN POST TITLE:")
                        print(submission.title)
                        print(submission.url)
                    submission.comments.replace_more(limit=None)
                    for comment in submission.comments.list():
                        if term in comment.body:
                            print("\nMATCH FOUND IN COMMENT BODY:")
                            print("www.reddit.com{}".format(comment.permalink))
        except UnicodeEncodeError:
            print("End of posts")
    print("\nEnd of new posts. Returning to main menu.\n")

#build reddit instance and bind to 'reddit'
reddit = praw.Reddit(client_id='', #client id provided by reddit dev
                     client_secret='', #client secret provided by reddit dev
                     user_agent='') #'my program' by 'my account name'

#confirm connection status in console
print("Connection status: " + str(reddit.read_only))

#globals
termList = [''] #put your terms here (comma separated)
subredditList = [''] #put your subreddits here (comma separated)

main()
