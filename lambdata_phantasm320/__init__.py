def calculate(data, target, feature_1, feature_2):
    '''
    Returns a dictionary of a columns unique
    names/values as a percentage with respect to the target
    -------------------------------------------------------------------
    data(pandas dataframe): is the name of your training data frame
    target(pandas dataframe): is the name of your test data frame
    feature_1(string): Column from data that you want to turn into a percentage
    feature_2(string): Column from target that you want to test
    '''
    import numpy as np
    import pandas as pd

    # create an empty dictionary to store percentages
    organize = {} 
    # Iterate through each unique name in the column
    for i in data[feature_1].value_counts().index:
        # Save and find the index for all instances of the unique name
        index_feature = data[data[feature_1] == i].index
        # Search df_target for the index and return instances for each target
        percentages = target.loc[index_feature][feature_2].value_counts().values
        # Add the name and highest instance into the dictionary
        # as a percentage 
        organize[i] = round(percentages[0] / percentages.sum(), 3)
    return organize
