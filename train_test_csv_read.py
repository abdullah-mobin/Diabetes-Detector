from necessery_pkgs import *

diabetis_dataset = pd.read_csv("dataset/KaggleDataS1.csv")

X = diabetis_dataset.drop(columns='Outcome', axis=1)
Y = diabetis_dataset['Outcome']

scaler = StandardScaler()
scaler.fit(X)

scaled_data = scaler.transform(X)
X = scaled_data

X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=0.35, stratify=Y, random_state=2)

print("Splited shape : ", X_train.shape, X_test.shape)