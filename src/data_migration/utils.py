import json

def jsonToColumnar(file):
    """
    Read a json file and aggregate
    fields into a dictionary
    """
    dictionary = {}
    with open(file) as json_data:
        ## load the json files into a dictionary
        data = json.load(json_data)
        ## create a 
        ## loop for all dictionary entries
        for item in data["orders"]:
            for key in item:
                if key in dictionary:
                    dictionary[key].append(item[key])
                else:
                    dictionary[key] = [item[key]]
    ## return a columnar dictionary
    return(dictionary)