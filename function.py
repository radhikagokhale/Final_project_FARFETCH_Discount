def input_farfetch():
    dct = {'female': [0,1], 'unissex': [1,0], 'exclusive': [1,0,0,0,0,0], 'new season': [0,1,0,0,0,0], 'notag': [0,0,1,0,0,0], 'permanent collection': [0,0,0,1,0,0], 'positively conscious': [0,0,0,0,1,0], 'seasonal pick': [0,0,0,0,0,1]}
    with open('model_dt.pkl', 'rb') as file:
        model_dt = pickle.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file) 
    input_1 = input('brand id: ')
    input_2 = input('similar products: ')
    input_3 = input('merchant id: ')
    input_4 = input('initial price: ')
    input_5 = input('stock total: ')
    input_6 = input('sizes: ')
    input_7 = input('sex: ')
    input_8 = input('label: ')
    numericals = scaler.transform([[input_1,input_2,input_3,input_4,input_5,input_6]])[0]
    new_data = [list(numericals) +dct[input_7] + dct[input_8]]
    prediction = model.predict(new_data)[0]
    if prediction == True:
        print("The item is going to be on sale soon!")
    else: 
        print("The item is not going to be on sale soon!")