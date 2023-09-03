from learn import *
import os

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def clear_screen():
    os.system('cls')



while True :

    print("-----------------Diabetes-Detector----------------\n\n")

    age = input("Age : ")
    insulin = input("Insulin level : ")
    bp = input("Blood Preasure : ")
    bmi = input("Body Mass Index (BMI) : ")
    dpf = input("DPF : ")
    glucose = input("Glucose level : ")
    st = input("Skin Thickness : ")
    preg = input("Number of childrens : ")

    new_info = (preg,glucose,bp,st,insulin,bmi,dpf,age)

    new_info = (11,143,94,33,146,36.6,0.254,51)

    info_arr = np.asarray(new_info)
    update_arr = info_arr.reshape(1,-1)
    final_data = scaler.transform(update_arr)
    result = myML.predict(final_data)


    if result[0] == 1:
        print('DIABETICS DETECTED !!!')
    else:
        print('DIABETICS NOT DETECTED !!!')

    print("test again : Y/N")
    key = input()
    if key == 'Y':
        clear_screen()
    elif key == 'N':
        clear_screen()
        input('Press any key to close')
        break