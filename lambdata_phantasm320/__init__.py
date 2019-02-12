def calculate(df_train, df_target, feature):
    '''Function that returns a dictionary of the columns features
       as a percentage to the target
       ----------------------------------------------------------
       df_train: is the name of your training data frame
       df_target: is the name of your test data frame
       feature: is the column from df_train that you want to
                turn into a percentage
    '''

    organize = {}
    for i in df_train[feature].value_counts().index:
        index_feature = df_train[df_train[feature] == i].index
        percentages = df_target.loc[index_feature]['status_group'].value_counts().values  
        organize[i] = round(percentages[0] / percentages.sum(), 3)
    return organize
