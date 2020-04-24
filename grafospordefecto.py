impor tensorflow as tf
print(tf.get_default_graph())
grafo1 = tf.Graph()
print (grafo1)
print(tf.get_default_graph())
with grafo1.as_defailt():
	print (grafo1 is tf.get_default_graph()) 
print (grafo1 is tf.get_default_graph()) 