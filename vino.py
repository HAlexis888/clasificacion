# arbol_vino_simple.py
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import tree

# Cargar datos
wine = load_wine()
X, y = wine.data, wine.target

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Arbol con max_depth=2
tree1 = DecisionTreeClassifier(max_depth=2, random_state=42)
tree1.fit(X_train, y_train)
rules1 = export_text(tree1, feature_names=wine.feature_names)
print("Reglas:")
print(rules1)
print(f"Precisión con dos de profundidad: {tree1.score(X_test, y_test):.4f}")

# Arbol con max_depth=None
tree2 = DecisionTreeClassifier(max_depth=None, random_state=42)
tree2.fit(X_train, y_train)
print(f"Precisión sin limite de profundidad: {tree2.score(X_test, y_test):.4f}")
print(f"Profundidad real: {tree2.get_depth()}")
print(f"Número de hojas: {tree2.get_n_leaves()}")
