import pandas as pd

train_csv = pd.read_csv("train.csv")
train_csv.info()
describe_train = train_csv.describe()

test_csv = pd.read_csv("test.csv")
test_csv.info()

train_csv_temp = train_csv[train_csv.review_scores_rating] 

#Making a data frame from all listings from all locations 
asheville_listings_csv = pd.read_csv("asheville/listings.csv")

if "is_business_travel_ready" in asheville_listings_csv.columns:
    asheville_listings_csv = asheville_listings_csv.drop("is_business_travel_ready",axis=1)

austin_listings_csv = pd.read_csv("austin/listings.csv")

if "is_business_travel_ready" in austin_listings_csv.columns:
    austin_listings_csv = austin_listings_csv.drop("is_business_travel_ready",axis=1)


boston_listings_csv = pd.read_csv("boston/listings.csv")

if "is_business_travel_ready" in boston_listings_csv.columns:
    boston_listings_csv = boston_listings_csv.drop("is_business_travel_ready",axis=1)


chicago_listings_csv = pd.read_csv("chicago/listings.csv")

if "is_business_travel_ready" in chicago_listings_csv.columns:
    chicago_listings_csv = chicago_listings_csv.drop("is_business_travel_ready",axis=1)


denver_listings_csv = pd.read_csv("denver/listings.csv")

if "is_business_travel_ready" in denver_listings_csv.columns:
    denver_listings_csv = denver_listings_csv.drop("is_business_travel_ready",axis=1)


losangeles_listings_csv = pd.read_csv("losangeles/listings.csv")

if "is_business_travel_ready" in losangeles_listings_csv.columns:
    losangeles_listings_csv = losangeles_listings_csv.drop("is_business_travel_ready",axis=1)


nasheville_listings_csv = pd.read_csv("nasheville/listings.csv")

if "is_business_travel_ready" in nasheville_listings_csv.columns:
    nasheville_listings_csv = nasheville_listings_csv.drop("is_business_travel_ready",axis=1)


neworleans_listings_csv = pd.read_csv("neworleans/listings.csv")

if "is_business_travel_ready" in neworleans_listings_csv.columns:
    neworleans_listings_csv = neworleans_listings_csv.drop("is_business_travel_ready",axis=1)


newyork_listings_csv = pd.read_csv("newyork/listings.csv")

if "is_business_travel_ready" in newyork_listings_csv.columns:
    newyork_listings_csv = newyork_listings_csv.drop("is_business_travel_ready",axis=1)


oakland_listings_csv = pd.read_csv("oakland/listings.csv")

if "is_business_travel_ready" in oakland_listings_csv.columns:
    oakland_listings_csv = oakland_listings_csv.drop("is_business_travel_ready",axis=1)


portland_listings_csv = pd.read_csv("portland/listings.csv")

if "is_business_travel_ready" in portland_listings_csv.columns:
    portland_listings_csv = portland_listings_csv.drop("is_business_travel_ready",axis=1)


sandiego_listings_csv = pd.read_csv("sandiego/listings.csv")

if "is_business_travel_ready" in sandiego_listings_csv.columns:
    sandiego_listings_csv = sandiego_listings_csv.drop("is_business_travel_ready",axis=1)


sanfrancisco_listings_csv = pd.read_csv("sanfrancisco/listings.csv")

if "is_business_travel_ready" in sanfrancisco_listings_csv.columns:
    sanfrancisco_listings_csv = sanfrancisco_listings_csv.drop("is_business_travel_ready",axis=1)


santacruz_listings_csv = pd.read_csv("santacruz/listings.csv")

if "is_business_travel_ready" in santacruz_listings_csv.columns:
    santacruz_listings_csv = santacruz_listings_csv.drop("is_business_travel_ready",axis=1)


seattle_listings_csv = pd.read_csv("seattle/listings.csv")

if "is_business_travel_ready" in seattle_listings_csv.columns:
    seattle_listings_csv = seattle_listings_csv.drop("is_business_travel_ready",axis=1)


washingtondc_listings_csv = pd.read_csv("washingtondc/listings.csv")

if "is_business_travel_ready" in washingtondc_listings_csv.columns:
    washingtondc_listings_csv = washingtondc_listings_csv.drop("is_business_travel_ready",axis=1)


#list1 = losangeles_listings_csv.columns
#list2 = nasheville_listings_csv.columns

#for index,each_string in enumerate(list1):
#    if each_string != list2[index]:
#        print(each_string,"  ***  ",list2[index])     
frames = [asheville_listings_csv, austin_listings_csv, boston_listings_csv, chicago_listings_csv, denver_listings_csv, losangeles_listings_csv, nasheville_listings_csv, neworleans_listings_csv, newyork_listings_csv, oakland_listings_csv, portland_listings_csv, sandiego_listings_csv, sanfrancisco_listings_csv, santacruz_listings_csv, seattle_listings_csv, washingtondc_listings_csv]
concatenated_data_frame = pd.concat(frames,ignore_index = True)
all_listings_df = asheville_listings_csv
#Data Preprocess 
all_listings_df = all_listings_df.drop(['listing_url','scrape_id','last_searched','last_scraped','thumbnail_url','medium_url','picture_url','xl_picture_url','host_id','host_url','host_name','host_thumbnail_url','host_picture_url','license','region_id','region_parent_id','calculated_host_listings_count'],axis = 1)
all_listings_df.describe()