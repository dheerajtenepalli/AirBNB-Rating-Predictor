#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:56:54 2018

@author: reddy
"""
import pandas as pd
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end

asheville_listings_csv =pd.read_csv("asheville/listings.csv")

austin_listings_csv = pd.read_csv("austin/listings.csv")

boston_listings_csv = pd.read_csv("boston/listings.csv")

chicago_listings_csv = pd.read_csv("chicago/listings.csv")

denver_listings_csv = pd.read_csv("denver/listings.csv")

losangeles_listings_csv = pd.read_csv("losangeles/listings.csv")

nasheville_listings_csv = pd.read_csv("nasheville/listings.csv")

neworleans_listings_csv = pd.read_csv("neworleans/listings.csv")

newyork_listings_csv = pd.read_csv("newyork/listings.csv")

oakland_listings_csv = pd.read_csv("oakland/listings.csv")

portland_listings_csv = pd.read_csv("portland/listings.csv")

sandiego_listings_csv = pd.read_csv("sandiego/listings.csv")

sanfrancisco_listings_csv = pd.read_csv("sanfrancisco/listings.csv")

santacruz_listings_csv = pd.read_csv("santacruz/listings.csv")

seattle_listings_csv = pd.read_csv("seattle/listings.csv")

washingtondc_listings_csv = pd.read_csv("washingtondc/listings.csv")

model_train_with_listings_analysis = pd.read_csv("model_train.csv")
frames = [asheville_listings_csv, austin_listings_csv, boston_listings_csv, chicago_listings_csv, denver_listings_csv, losangeles_listings_csv, nasheville_listings_csv, neworleans_listings_csv, newyork_listings_csv, oakland_listings_csv, portland_listings_csv, sandiego_listings_csv, sanfrancisco_listings_csv, santacruz_listings_csv, seattle_listings_csv, washingtondc_listings_csv]

final_data_frame = pd.concat(frames)

final_data_frame = final_data_frame.sort_values(['id'])
final_data_frame = final_data_frame.loc[:, final_data_frame.isnull().mean() < .2]
all_listings_df = final_data_frame.drop(['calendar_updated','calendar_last_scraped','listing_url','scrape_id','last_scraped','picture_url','host_id','host_url','host_name','host_thumbnail_url','host_picture_url'],axis = 1)

#Number of amenities count
#all_listings_df["amenities"].values[0].split(",")
Range = list(range(final_data_frame.values.shape[0]))
list_of_num_amenities = []

for index_main in Range:
   list_of_num_amenities.append(len(all_listings_df["amenities"].values[index_main].split(",")))
   if index_main % 1000 == 0:
       print(index_main,"Hellp")

all_listings_df["amenities_c"] = list_of_num_amenities
all_listings_df = all_listings_df.drop("amenities",axis =1)

bed_type = pd.get_dummies(all_listings_df["bed_type"])

all_listings_df = pd.concat([all_listings_df,bed_type],axis =1)
all_listings_df = all_listings_df.drop("bed_type",axis =1)
all_listings_df.columns
####################################################
#Cancellation Policy
cancel_pol= pd.get_dummies(all_listings_df["cancellation_policy"])
all_listings_df = pd.concat([all_listings_df,cancel_pol],axis =1)
all_listings_df = all_listings_df.drop("cancellation_policy",axis =1)
all_listings_df = all_listings_df.drop("country",axis =1)
all_listings_df = all_listings_df.drop(["country_code","description","experiences_offered","host_listings_count","host_location","host_neighbourhood","host_since","market","name","neighbourhood","neighbourhood_cleansed","smart_location","street","summary"],axis =1)
####################################################
#City drop ----,extra_people
all_listings_df = all_listings_df.drop("city",axis =1)
state = pd.get_dummies(all_listings_df["state"])
all_listings_df = pd.concat([all_listings_df,state],axis =1)
all_listings_df = all_listings_df.drop("state",axis =1)
all_listings_df = all_listings_df.drop(["extra_people","host_verifications"],axis =1)

#######################################################
#Remaining Dummy Variables
superhost = pd.get_dummies(all_listings_df["host_is_superhost"])
all_listings_df = pd.concat([all_listings_df,superhost],axis =1)
all_listings_df = all_listings_df.drop("host_is_superhost",axis =1)


room_type = pd.get_dummies(all_listings_df["room_type"])
all_listings_df = pd.concat([all_listings_df,room_type],axis =1)
all_listings_df = all_listings_df.drop("room_type",axis =1)

property_type = pd.get_dummies(all_listings_df["property_type"])
all_listings_df = pd.concat([all_listings_df,property_type],axis =1)
all_listings_df = all_listings_df.drop("property_type",axis =1)

all_listings_df = all_listings_df.drop(['host_identity_verified','instant_bookable',"is_location_exact",'require_guest_phone_verification',"requires_license","require_guest_profile_picture"],axis =1)
all_listings_df = all_listings_df.drop(["host_has_profile_pic"],axis =1)

all_listings_df["price"] = all_listings_df["price"].str.replace("$","")
all_listings_df["price"] = pd.to_numeric(all_listings_df["price"],errors="coerce")

all_listings_df = pd.DataFrame(all_listings_df.values)
model_train_list = list(range(model_train_with_listings_analysis.values.shape[0]))
list_of_lists_of_listings  = []

for index_main in model_train_list:
    print(index_main)
    index_found = binary_search(all_listings_df.iloc[:,11].values,model_train_with_listings_analysis.iloc[:,2][index_main])
    if index_found != -1:
        print(index_found)
        list_of_lists_of_listings.append(all_listings_df.iloc[index_found,:])

    else:
        print("Not found")
        break
listings_final_data_frame = pd.DataFrame(list_of_lists_of_listings)
listings_final_data_frame = listings_final_data_frame.drop(listings_final_data_frame.columns[11],axis=1)

model_train_with_listings_analysis = model_train_with_listings_analysis.drop("superhost",axis=1)
model_train_with_listings_analysis = model_train_with_listings_analysis.iloc[:,2:]


train = pd.concat([ pd.DataFrame(listings_final_data_frame.values), pd.DataFrame(model_train_with_listings_analysis.values)],axis=1)
train.columns = list(range(124))
train.to_csv("model_train_version_3.csv")
