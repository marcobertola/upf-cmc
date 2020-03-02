import numpy as np
from gensim.models import KeyedVectors
from itertools import repeat

#model loading
print('Wait for model to be loaded..')
model_glove = KeyedVectors.load_word2vec_format('./words2midi/glove.6B.50d_word2vec.txt')


def find_range(point, range_limits):
    n_limits = len(range_limits)
    for limit in range(n_limits - 1):
        if (point > range_limits[limit]) and (point < range_limits[limit + 1]):
            return limit
    raise ValueError


def colapse_into_10(space_50d):
    ndim = space_50d.ndim
    if ndim == 1:  # If a word embedding
        space_10d = np.zeros(10)
        for idx in range(10):
            space_10d[idx] = np.sum(space_50d[idx*5:(idx+1)*5])
    else:
        space_10d = np.zeros([space_50d.shape[0], 10])
        for idx in range(10):
            space_10d[idx] = np.sum(space_50d[idx*5:(idx+1)*5],)
    return space_10d


def embspace_to_midi(word_embedding, n_words):
    """
        word_embedding: The 50dim vector resulting of difference between multiple words embedding
        n_words: Number of words used to create the word_embedding
    """
    embedding = np.load('./words2midi/mappings.npy')
    reduced_10 = colapse_into_10(embedding)
    maxs = np.max(reduced_10, axis=0)*n_words
    mins = np.min(reduced_10, axis=0)*n_words
    steps = (maxs - mins) / 129
    mappings = np.array(list((map(np.arange, mins, maxs, steps))))

    reduced_embedding = colapse_into_10(word_embedding)
        
    midi = np.zeros(10)
    for dimension in range(10):
        midi[dimension] = find_range(reduced_embedding[dimension], mappings[dimension])
    return midi

def difference_word(input_words, nb_words):
    #todo: loop in case more than 2 words are received 
    diffwords = model_glove[input_words[0]] - model_glove[input_words[1]]
    dist = embspace_to_midi(diffwords, nb_words)
    print('Distance: {}'.format(dist))
    return dist
