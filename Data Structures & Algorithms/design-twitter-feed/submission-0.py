class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId → [(time, tweetId)]
        self.following = defaultdict(set)    # userId → {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}
        
        for uid in users:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                t, tid = tweets[idx]
                heapq.heappush(heap, (-t, tid, uid, idx - 1))
        
        res = []
        while heap and len(res) < 10:
            t, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            if idx >= 0:    # push next tweet from same user
                nt, ntid = self.tweets[uid][idx]
                heapq.heappush(heap, (-nt, ntid, uid, idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)