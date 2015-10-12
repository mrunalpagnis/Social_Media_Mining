from tweepy import StreamListener
import time

class listener(StreamListener):
 
    def __init__(self, start_time, time_limit=180):
 
        self.time = start_time
        self.limit = time_limit
 
    def on_data(self, data):
 
        while (time.time() - self.time) < self.limit:
 
            try:
 
                saveFile = open('C:\\Users\\mpagnis\\Documents\\personal\\SMM\\Social_Media_Mining\\raw_tweets.json', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
 
                return True
 
 
            except BaseException, e:
                print 'failed to stream data, ', str(e)
                time.sleep(10)
                pass
 
        exit()
 
    def on_error(self, status):
 
        print status