#This Code gets all the reviews and it's sentiment,emotion analysis using IBM Watson NLU Service.
"""Note Data for this application is available online as open source by Airbnb"""
import pandas as pd

def process_data_frame(path):
    review_csv = pd.read_csv(path)
    df = review_csv["listing_id"]
    dictionary = {}
    for index in range(df.values.shape[0]):
        if  df[index] in  dictionary.keys() :
            dictionary[df[index]] = str(dictionary[df[index]]) + " " + str(review_csv["comments"][index]).replace(","," ")
        else :
            dictionary[df[index]] =  str(review_csv["comments"][index]).replace(","," ")
    return  dictionary


path_1 ="asheville/reviews_asheville.csv"
dictionary_1 = process_data_frame(path_1)

path_2 ="austin/reviews_austin.csv"
dictionary_2 = process_data_frame(path_2)

path_3 ="boston/reviews_boston.csv"
dictionary_3 = process_data_frame(path_3)

path_4 ="chicago/reviews_chicago.csv"
dictionary_4 = process_data_frame(path_4)

path_5 ="denver/reviews_denver.csv"
dictionary_5 = process_data_frame(path_5)

path_6 ="losangeles/reviews_losangeles.csv"
dictionary_6 = process_data_frame(path_6)

path_7 ="nasheville/reviews_nasheville.csv"
dictionary_7 = process_data_frame(path_7)

path_8 ="neworleans/reviews_neworleans.csv"
dictionary_8 = process_data_frame(path_8)

path_9 ="newyork/reviews_newyork.csv"
dictionary_9 = process_data_frame(path_9)

path_10="oakland/reviews_oakland.csv"
dictionary_10 = process_data_frame(path_10)

path_11="portland/reviews_portland.csv"
dictionary_11 = process_data_frame(path_11)

path_12="sandiego/reviews_sandiego.csv"
dictionary_12 = process_data_frame(path_12)

path_13="sanfrancisco/reviews_sanfrancisco.csv"
dictionary_13 = process_data_frame(path_13)

path_14="santacruz/reviews_santacruz.csv"
dictionary_14 = process_data_frame(path_14)

path_15="seattle/reviews_seattle.csv"
dictionary_15 = process_data_frame(path_15)

path_16="washingtondc/reviews_washingtondc.csv"
dictionary_16 = process_data_frame(path_16)

df1 = pd.DataFrame.from_dict(list(dictionary_1.items()))
df2 = pd.DataFrame.from_dict(list(dictionary_2.items()))
df3 = pd.DataFrame.from_dict(list(dictionary_3.items()))
df4 = pd.DataFrame.from_dict(list(dictionary_4.items()))
df5 = pd.DataFrame.from_dict(list(dictionary_5.items()))
df6 = pd.DataFrame.from_dict(list(dictionary_6.items()))
df7 = pd.DataFrame.from_dict(list(dictionary_7.items()))
df8 = pd.DataFrame.from_dict(list(dictionary_8.items()))
df9 = pd.DataFrame.from_dict(list(dictionary_9.items()))
df10 = pd.DataFrame.from_dict(list(dictionary_10.items()))
df11 = pd.DataFrame.from_dict(list(dictionary_11.items()))
df12 = pd.DataFrame.from_dict(list(dictionary_12.items()))
df13 = pd.DataFrame.from_dict(list(dictionary_13.items()))
df14 = pd.DataFrame.from_dict(list(dictionary_14.items()))
df15 = pd.DataFrame.from_dict(list(dictionary_15.items()))
df16 = pd.DataFrame.from_dict(list(dictionary_16.items()))

frames1 = [df1,df2,df3,df4]
frames2 = [df5,df6,df7,df8]
frames3 = [df9,df10,df11,df12]
frames4 =  [df13,df14,df15,df16]


final_data_1 = pd.concat(frames1)
final_data_2 = pd.concat(frames2)
final_data_3 = pd.concat(frames3)
final_data_4 = pd.concat(frames4)


final_data_1.to_csv("final_data_1.csv")
final_data_2.to_csv("final_data_2.csv")
final_data_3.to_csv("final_data_3.csv")
final_data_4.to_csv("final_data_4.csv")

train = pd.read_csv("train.csv")
df = train["listing_id"]
unique3 = list(set(df.values))
test = pd.read_csv("test.csv")


asheville_listings_csv = pd.read_csv("asheville/reviews_asheville.csv")
df = asheville_listings_csv["listing_id"]
unique = list(set(df.values))

asheville_listings_csv = pd.read_csv("asheville/listings.csv")
df = asheville_listings_csv["id"]
unique2 = list(set(df.values))

for value in unique2:
    if value not in unique and value in unique3:
        print(value)

austin_listings_csv = pd.read_csv("austin/reviews.csv")

boston_listings_csv = pd.read_csv("boston/reviews.csv")

chicago_listings_csv = pd.read_csv("chicago/reviews.csv")

denver_listings_csv = pd.read_csv("denver/reviews.csv")

losangeles_listings_csv = pd.read_csv("losangeles/reviews.csv")

nasheville_listings_csv = pd.read_csv("nasheville/reviews.csv")

neworleans_listings_csv = pd.read_csv("neworleans/reviews.csv")

newyork_listings_csv = pd.read_csv("newyork/reviews.csv")

oakland_listings_csv = pd.read_csv("oakland/reviews.csv")

portland_listings_csv = pd.read_csv("portland/reviews.csv")

sandiego_listings_csv = pd.read_csv("sandiego/reviews.csv")

sanfrancisco_listings_csv = pd.read_csv("sanfrancisco/reviews.csv")

santacruz_listings_csv = pd.read_csv("santacruz/reviews.csv")

seattle_listings_csv = pd.read_csv("seattle/reviews.csv")

washingtondc_listings_csv = pd.read_csv("washingtondc/reviews.csv")

mframes = [asheville_listings_csv, austin_listings_csv, boston_listings_csv, chicago_listings_csv, denver_listings_csv, losangeles_listings_csv, nasheville_listings_csv, neworleans_listings_csv, newyork_listings_csv, oakland_listings_csv, portland_listings_csv, sandiego_listings_csv, sanfrancisco_listings_csv, santacruz_listings_csv, seattle_listings_csv, washingtondc_listings_csv]

for each_location_df_review in frames:
    list_of_lists = []
    length_of_dataframe = (each_location_df_review.values).shape[0]
    for index in range(length_of_dataframe):
        print(each_location_df_review['listing_id'][index],nlu.get_text_analysis( each_location_df_review['comments'][index] ) )
        break
    break
