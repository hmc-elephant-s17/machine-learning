import pickle

pkl_file = open('data.pkl', 'rb')
stocks = pickle.load(pkl_file)
pkl_file.close()

