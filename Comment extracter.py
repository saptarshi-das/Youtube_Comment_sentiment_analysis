# Python program for extracting YouTube comments using YouTube API  
# import all the required libraries  
import os  
from googleapiclient.discovery import build  
from google.oauth2.credentials import Credentials
from nltk.sentiment import SentimentIntensityAnalyzer
# imports for the visuals
import webbrowser
from flask import Flask, render_template
from flask import request


# Get credentials  
credentials = Credentials(
    token=None,  # No need for this field
    client_id='145945614300-m432pq7ilg45uup1esslhqj1ccksj43d.apps.googleusercontent.com',
    client_secret='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',
    refresh_token='1//03axh6coRlLL4CgYIARAAGAMSNwF-L9IrBxsBMDobnr6Jn8IyY2Mz9PGlfkiiTNAfhHYmYbC2kRqM8Lrz-bELwwzKh_-8ynBNEAY',
    token_uri='https://accounts.google.com/o/oauth2/token',
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
)
  
# Create YouTube API client
youtube = build('youtube', 'v3', credentials = credentials)  
  
# Set video ID  
video_id = 'kffacxfA7G4'
  
# Call the API to get comments  
comments = []
results = youtube.commentThreads().list(  
    part = 'snippet',  
    videoId = video_id,  
    textFormat = 'plainText',  
    ).execute()  
  
# Loop through each comment and append to comments list  
while results:  
    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']  
        comments.append(comment)  
          
    # Check if there are more comments and continue iterating  
    if 'nextPageToken' in results:  
        results = youtube.commentThreads().list(  
            part = 'snippet',  
            videoId = video_id,  
            textFormat = 'plainText',  
            pageToken = results['nextPageToken']  
        ).execute()  
    else:  
        break  

response_video = youtube.videos().list(
    part='snippet',
    id=video_id
).execute()

for item in response_video['items']:
    video_title = item['snippet']['title']
    print(f"Video Title: {video_title}")



sentimentScore=[]
#The setntiment analysis part of the code.
sia = SentimentIntensityAnalyzer()
for i in range(0,len(comments)):
    sentiment_eachcomment=sia.polarity_scores(comments[i])
    sentimentScore.append(sentiment_eachcomment)



# Calculate the overall sentiment score
overall_sentiment_score = 0
for sentiment in sentimentScore:
    overall_sentiment_score += sentiment['compound']
overall_sentiment_score = overall_sentiment_score / len(sentimentScore)

#
# 
#  Scaling the data for higher looking value
if overall_sentiment_score >= 0:
    overall_sentiment_score= overall_sentiment_score**(1/1.5)
else:
    overall_sentiment_score= (-1)*(abs(overall_sentiment_score)**(1/1.5))

# Print the results
print("Overall sentiment score: ", overall_sentiment_score)


# 
# 
# 
# trying to start the server
app = Flask(__name__)

@app.route('/')
def index():
    value_from_python = round(overall_sentiment_score,2)
    return render_template('index.html',value_from_python=value_from_python, video_title=video_title)

if __name__ == '__main__':
    import threading

    # Start the Flask app in a separate thread
    server_thread = threading.Thread(target=app.run)
    server_thread.start()

    # Open the page in the web browser
    url = "http://127.0.0.1:5000/"
    webbrowser.open(url, new=0, autoraise=True)

