import time
import rauth
import os



def define_params(location):
    params = {}
    params["term"] = "restaurants"
    params["category_filter"] = "french"
    params["location"] = "{}".format(location)
    params["radius_filter"] = "2000"
    params["limit"] = "20"
    params["sort"] = "2"

    return params

def get_data(params):

    # setting up personal Yelp api keys
    consumer_key = os.environ["YELP_CONSUMER_KEY"]
    consumer_secret = os.environ["YELP_CONSUMER_SECRET"]
    token = os.environ["YELP_ACCESS_TOKEN_KEY"]
    token_secret = os.environ["YELP_ACCESS_TOKEN_SECRET"]

    session = rauth.OAuth1Session(consumer_key=consumer_key,
                                  consumer_secret=consumer_secret,
                                  access_token=token,
                                  access_token_secret=token_secret)

    response = session.get("http://api.yelp.com/v2/search", params=params)

    # transforming the data in JSON format
    data = response.json()
    session.close()

    return data


def main():


    locations = ["boulder"]

    api_data = []
    for location in locations:
        params = define_params(location)
        api_data.append(get_data(params))
        time.sleep(1.0)


    return api_data[0]


# binding the JSON object to a variable called data
data = main()
# data.values() of the JSON object returns a list of dictionaries
# I want the 2nd index of that list to get the business info
data_list = data.values()[2]
# restaurant_list is a list of the restaurant names from the JSON object
# based on searching for the 'name' key in the dict and returning the value
# which is the name of the business/restaurant
restaurant_list = [d['name'] for d in data_list]
print restaurant_list

if __name__ == '__main__':
    main()
