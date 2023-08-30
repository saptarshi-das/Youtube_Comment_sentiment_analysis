# Youtube_Comment_sentiment_analysis

**Project overview**
Understanding the sentiment behind user comments is crucial for video creators, as it allows them to gauge the reception of their content and engage with their audience effectively.
Businesses and advertisers can utilize sentiment analysis to evaluate the impact of their promotional campaigns and tailor their strategies accordingly.
Manually analyzing a large number of comments is time-consuming and impractical.

**Model**
Youtube comments were scraped using Scrapper to extract every comment on a specific video.
VADER model to map each comment with VADER to obtain individual sentimental scores ranging from -1 to 1
The average sentimental score of all comments is taken to be the entire video’s sentimental score.
A meter visualising the score on a scale of -1 to 1 will be the expected output.

