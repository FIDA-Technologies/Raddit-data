import numpy as np
import matplotlib.pyplot as plt
import csv
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

# Read
# with open('GME_post+return.csv', newline='') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#      for row in spamreader:
#          print(', '.join(row))
sid = SentimentIntensityAnalyzer()

x1=[]
x2=[]
y1=[]
y2=[]
# Read and Write
with open('GME_post+return.csv', newline='', encoding = 'utf-8') as csvfile:
    with open('GME_post+return+sentiment.csv', 'w', newline='') as csvfile2:
        spamwriter = csv.writer(csvfile2, delimiter=',')
        reader = csv.DictReader(csvfile)
        for row in reader:
            ss = sid.polarity_scores(row['title'])
            for k in ss:
                print('{0}:{1},'.format(k,ss[k]), end='')
                if k == 'compound':
                    x1.append(row['Post_Time'])
                    x2.append(row['Post_Time'])
                    y1.append(row['return']*100)
                    y2.append(ss[k])
                    spamwriter.writerow((row['Post_Time'], row['return'],ss[k]))

print('x1----------------------')
print(x1)
print('y1----------------------')
print(y1)
print('y2----------------------')
print(y2)
print('correlation-----------------------')
# TODO: print("correlation:", np.corrcoef(np.array(y1).astype(np.float), np.array(y2).astype(np.float)))

##### Visualization
# line 1 points
# x1 = [10,20,30]
# y1 = [20,40,10]
# plotting the line 1 points 
plt.plot(x1, y1, label = 'Return - line 1')
# line 2 points
# x2 = [10,20,30]
# y2 = [25,30,40]
# plotting the line 2 points 
plt.plot(x2, y2, label = 'Sentiment - line 2')
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()