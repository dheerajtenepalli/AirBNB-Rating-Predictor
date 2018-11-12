import pandas as pd
df1 = pd.read_csv("nlu_data/save_2.csv")
df2 = pd.read_csv("nlu_data/save_3.csv")
df3 = pd.read_csv("nlu_data/save_4.csv")
df4 = pd.read_csv("nlu_data/save_5.csv")
df5 = pd.read_csv("nlu_data/save_6.csv")
df6 = pd.read_csv("nlu_data/save_7.csv")
df7 = pd.read_csv("nlu_data/save_8.csv")
df8 = pd.read_csv("nlu_data/save_9.csv")
df9 = pd.read_csv("nlu_data/save_10.csv")
df10 = pd.read_csv("nlu_data/save_11.csv")


frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10]

final_data_frame = pd.concat(frames)
f=final_data_frame.iloc[:,1].unique()

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv",header=None)
list_of_lists_train = train["listing_id"].values
list_of_lists_train_nlu = []
for index_main,each_train in enumerate(list_of_lists_train):
    print(1)
    for index,each_final_train in enumerate(final_data_frame.iloc[:,1].values):
        if each_train == each_final_train:
            a = list(final_data_frame.iloc[index,2:].values)
            b = [each_final_train]
            c = list(train.iloc[index_main,1:].values)
            #print(b+a)
            if index%1000 == 0:
                print("haha")
            list_of_lists_train_nlu.append(b+a+c)
            #list_of_lists_train_nlu.append()
            break
    break     

list_of_lists_test = test.iloc[:,0].values

train_model = final_data_frame[final_data_frame.iloc[:,1].isin(list_of_lists_train)]
test_model = final_data_frame[final_data_frame.iloc[:,1].isin(list_of_lists_train)]
for each_listing_id in :
    list_of_lists_train.
    
    