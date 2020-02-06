from azure.storage.blob import BlockBlobService
from os.path import join, isfile
from os import listdir
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import numpy as np


def read_tweets_from_local(local_path):
    all_tweets = []
    for file in listdir(local_path):
        if not isfile(join(local_path, file)):
            continue
        else:
            candidate_df = pd.read_csv(join(local_path, file))
            candidate_df['candidate'] = file[:-4]
            all_tweets.append(candidate_df)

    all_tweets_df = pd.concat(all_tweets, ignore_index=True)
    return all_tweets_df


def filter_texts_by_candidate(dataframe, candidate):
    texts = list(dataframe[dataframe.candidate == candidate]['processed_text'])
    return texts


def show_similar_tweets(query, centroid, tweets, candidate, d_min=0.2, n=3):
    D = linear_kernel(query, centroid)
    ind = np.argsort(D[0], axis=-1)[::-1]
    candidate_tweets = tweets[tweets.candidate == candidate]
    shown_tweets_count = 0
    for i in ind[:n]:
        if D[0][i] >= d_min:
            print(i, '@' + candidate + ': ' + candidate_tweets['tweet'].iloc[i], '\n')
            shown_tweets_count += 1
    if shown_tweets_count < 1:
        print('WARNING: Any tweet from %s was found for the given query within a distance of %s' % (candidate, d_min))