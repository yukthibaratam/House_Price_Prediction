import pickle
import json
import numpy as np
import warnings

__locations = None
__data_columns = None
__model = None

def get_estimated_prices(location,sqft,bhk,bath):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            loc_index = __data_columns.index(location.lower())
        except:
            loc_index = -1

        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

# def load_saved_artifacts():
#     print("loading saved artifacts...start")
#     global __data_columns
#     global __locations
#     global __model
#     with open("./server/artifacts/columns.json", 'r') as f:
#         __data_columns = json.load(f)['data_columns']
#         __locations = __data_columns[3:]
#     if __model is None:
#         with open("./server/artifacts/banglore_home_prices_model.pickle", 'rb') as f:
#             model = pickle.load(f)
#     print("loading saved artifacts")
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
        print("locations:", __locations)
        print("_____DONE________")
    global __model
    if __model is None:
        with open('./server/artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            print("using banglore_home_prices_model.pickle")
            __model = pickle.load(f)
    print("loading saved artifacts...done")



if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_prices('1st Phase JP Nagar', 1000, 3, 3))

    print(get_estimated_prices('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_prices('Kalhalli', 1000, 2, 2))
    print(get_estimated_prices('Ejipura', 1000, 2, 2))
