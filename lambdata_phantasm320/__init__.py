def calculate(df_train, df_target, feature):
    '''
    Function that returns a dictionary of the columns features
    as a percentage to the target
    -------------------------------------------------------------------
    df_train(pandas dataframe): is the name of your training data frame
    df_target(pandas dataframe): is the name of your test data frame
    feature(column from df_train): is the column from df_train that you want to
    turn into a percentage
    '''
    import numpy as np
    import pandas as pd

    # create an empty dictionary to store percentages
    organize = {} 
    # Iterate through each unique name in the column
    for i in df_train[feature].value_counts().index:
        # Save and find the index for all instances of the unique name
        index_feature = df_train[df_train[feature] == i].index
        # Search df_target for the index and return instances for each target
        percentages = df_target.loc[index_feature]['status_group'].value_counts().values
        # Add the name and highest instance into the dictionary
        # as a percentage 
        organize[i] = round(percentages[0] / percentages.sum(), 3)
    return organize
