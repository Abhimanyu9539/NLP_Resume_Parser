import utils

# function to read the data
def read_data():
    train=utils.convert_json_to_spacy("D:\\ProjectProd\\Resume_Parser\\input\\train_1.json") # train file

    test=utils.convert_json_to_spacy("D:\\ProjectProd\\Resume_Parser\\input\\test.json")     # test file

    return train,test