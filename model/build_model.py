import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import m2cgen as m2c 

# Exemplo de dados históricos (em produção, isso seria coletado de um banco de dados)
data = {
    'age': [7, 14, 21, 28, 7, 14, 21, 28],
    'food_history_fish': [5, 0, 0, 0, 0, 5, 0, 0],
    'food_history_meat': [0, 5, 0, 0, 0, 0, 5, 0],
    'food_history_vegetal': [0, 0, 10, 0, 0, 0, 0, 10],
    'food_history_fruit': [0, 0, 0, 10, 0, 0, 0, 0],
    'walk_frequency': [20, 20, 20, 20, 10, 10, 10, 10],
    'condition': [1, 1, 1, 1, 2, 2, 2, 2],
    'happiness': [50, 60, 70, 80, 50, 60, 70, 80],
    'current_stage': ['Blob', 'Child', 'Teen', 'Adult', 'Blob', 'Child', 'Teen', 'Adult'],
    'next_type': ['Cat', 'Cat', 'Tiger', 'Tiger', 'Dog', 'Dog', 'Wolf', 'Wolf']  # Adicionando o próximo tipo
}

# Converter os dados para um DataFrame
df = pd.DataFrame(data)

# Codificar as variáveis categóricas
df['current_stage'] = df['current_stage'].astype('category').cat.codes
df['next_type'] = df['next_type'].astype('category').cat.codes

# Separar features e labels
X = df.drop(['next_type'], axis=1)
y_type = df['next_type']

# Dividir os dados em treino e teste
X_train_type, X_test_type, y_type_train, y_type_test = train_test_split(X, y_type, test_size=0.2, random_state=42)

# Treinar o modelo para tipo
model_type = RandomForestClassifier()
model_type.fit(X_train_type, y_type_train)

# Avaliar os modelos
accuracy_type = model_type.score(X_test_type, y_type_test)
print(f"Model Type Accuracy: {accuracy_type}")

# Salvar os modelos

with open('blockagotchi_type_model.pkl', 'wb') as f:
    pickle.dump(model_type, f)



# EXPORTS MODEL
#

# - uses m2cgen to convert model to pure python code with zero dependencies
#   obs: generated Python code will define a method called `score(input)`, which computes
#        a numerical score based on an input list where each entry corresponds to one of
#        the model's input features/columns. If the dependent variable is a class with
#        more than 2 categories, then the output of the method will be a list of scores
#        for each category.

modeltype_to_python = m2c.export_to_python(model_type)
# - writes model to file `model.py` in the parent directory (m2cgen/backend)
with open("model_type.py", "w") as text_file:
    print(f"{modeltype_to_python}", file=text_file)

print("Model exported successfully")
