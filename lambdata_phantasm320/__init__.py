def calculate(df_train, df_target, feature):
    organize = {}
    for i in df_train[feature].value_counts().index:
        index_feature = df_train[df_train[feature] == i].index
        percentages = df_target.loc[index_feature]['status_group'].value_counts().values  
        organize[i] = round(percentages[0] / percentages.sum(), 3)
    return organize
