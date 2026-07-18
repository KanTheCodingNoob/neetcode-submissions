class Twitter:

    def __init__(self):
        self.tweets = {} # userId, stack of (order, tweet)
        self.follows = {}
        self.countId = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.countId, tweetId))
        self.countId += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        results = []
        totalTweets = []
        
        # User own tweets
        if userId in self.tweets:
            userTweets = self.tweets[userId]
            for t in userTweets:
                totalTweets.append(t)
        # Follower's tweets
        if userId in self.follows:
            listOfFollowee = self.follows[userId]
            for f in listOfFollowee:
                listOfTweets = self.tweets[f]
                for t in listOfTweets:
                    totalTweets.append(t)
        
        heapq.heapify_max(totalTweets)

        for i in range(10):
            if len(totalTweets) == 0:
                break
            results.append(heapq.heappop_max(totalTweets)[1])

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if (followerId not in self.follows):
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if (followerId in self.follows):
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)

