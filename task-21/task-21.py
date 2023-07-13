'''
• Create single word lists for all the different works in the NLTK Shakespeare collection. 
• Check if the Zipf distribution holds for every work in the corpus.
'''

import nltk

nltk.download('punkt')
nltk.download('shakespeare')

from nltk.corpus import shakespeare
import matplotlib.pyplot as plt

for fileid in shakespeare.fileids():
    # Get the tokens from the text
    words = shakespeare.words(fileid)
    
    # Create a frequency distribution of the words
    freq_dist = nltk.FreqDist(words)
    
    # Get the ranks and frequencies for each word
    ranks = range(1, len(freq_dist) + 1)
    frequencies = [freq_dist[word] for word in freq_dist]
    
    # Plot the ranks vs. frequencies on a log-log scale
    plt.loglog(ranks, frequencies, label=fileid)

plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
plt.title('Zipf Distribution of Shakespeare Works')
plt.show()
