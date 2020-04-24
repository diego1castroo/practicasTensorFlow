impor tensorflow as tf
tensor = tf.random_uniform((5,5),0,1)
variable = tf.Variable(initial_value = tensor)
print variable
inicializador = tf.global_variables_initializer()
with tf.Session() as sesion:
	sesion.run(inicializador)
	print(sesion.run(variable))
print (resultado) 
incognitas = tf.placeholder()
print(incognitas)
