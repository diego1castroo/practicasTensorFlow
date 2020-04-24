impor tensorflow as tf
nodo1 = tf.constant(4)
nodo2 = tf.constant(6)
nodo3 = nodo1 + nodo2
print(nodo3)
with tf.Session() as sesion:
	resultado = sesion.run(nodo3)
print (resultado) 
