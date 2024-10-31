import tensorflow as tf

# Carregue e prepare o conjunto de dados MNIST.
# Converta as amostras de números inteiros em números de ponto flutuante:
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Crie o modelo tf.keras.Sequential empilhando camadas. 
# Escolha uma função otimizadora e de perda para treinamento:
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Treine e avalie o modelo:
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

"""
Resultado esperado:
O classificador de imagem agora é treinado para ~98% de acurácia neste conjunto de dados.

Epoch 1/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 2s 654us/step - accuracy: 0.8564 - loss: 0.4909710
Epoch 2/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 1s 635us/step - accuracy: 0.9550 - loss: 0.1489
Epoch 3/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 1s 639us/step - accuracy: 0.9656 - loss: 0.1106
Epoch 4/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 1s 646us/step - accuracy: 0.9731 - loss: 0.0886
Epoch 5/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 1s 633us/step - accuracy: 0.9758 - loss: 0.0764
313/313   ━━━━━━━━━━━━━━━━━━━━ 0s 383us/step - accuracy: 0.9702 - loss: 0.0978
"""