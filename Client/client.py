import grpc

import servicio_pb2_grpc 
import servicio_pb2 




from flask import Flask, render_template, request

app = Flask(__name__)


##
##	404 error

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


##
##	HOME


@app.route('/')
def home():
	return render_template("home.html")

##
##	ALTA DE TIPO


@app.route('/altaTipo_form')
def altaTipo_form():
	return render_template("altaTipo_form.html")

@app.route('/altaTipo_msg', methods=['POST'])
def altaTipo_msg():
	tipo_medicamento = request.form['tipo_medicamento']
	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001',credentials) 
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)
	response = stub.AltaTipoMedicamento(servicio_pb2.Tipo(tipo_medicamento=tipo_medicamento, activo = 1))#alta
	msg = "Msg from server: " + response.confirmacion
	return render_template("altaTipo_msg.html", msg = msg)


##	BAJA LOGICA DE TIPO
##

@app.route('/bajaTipo_form')
def bajaTipo_form():
	return render_template("bajaTipo_form.html")

@app.route('/bajaTipo_msg', methods=['POST'])
def bajaTipo_msg():
	tipo_medicamento = request.form['tipo_medicamento']
	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001', credentials)
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)
	response = stub.BajaTipoMedicamento(servicio_pb2.Tipo(tipo_medicamento=tipo_medicamento, activo = 0))#baja
	msg = "Msg from server: " + response.confirmacion
	return render_template("bajaTipo_msg.html", msg = msg)

##
##	ALTA MEDICAMENTO
##
@app.route('/altaMed_form')
def altaMed_form():
	return render_template("altaMed_form.html")


@app.route('/altaMed_msg', methods=['POST'])
def altaMed_msg():

	nombre_comercial = request.form['nombre_comercial']
	codigo = request.form['codigo']
	droga = request.form['droga']
	tipo_medicamento = request.form['tipo_medicamento']

	tipo_medicamento_type = servicio_pb2.Tipo(tipo_medicamento=tipo_medicamento, activo = True)
	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001',credentials)
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)
	response = stub.AltaMedicamento(servicio_pb2.Medicamento(nombre_comercial=nombre_comercial, codigo= codigo, droga= droga, tipo_medicamento= tipo_medicamento_type))
	msg = "Msg from server: " + response.confirmacion
	
	return render_template("altaMed_msg.html", msg = msg)

##
##	CONSULTA POR TIPO
##

@app.route('/consTipo_form')
def consTipo_form():
	return render_template("consTipo_form.html")

@app.route('/consTipo_msg', methods=['POST'])
def consTipo_msg():
	tipo_medicamento = request.form['tipo_medicamento']
	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001',credentials)
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)
	response = stub.ConsultaMedicamentoPorTipo(servicio_pb2.ConsultaTipo(confirmacion=tipo_medicamento))#baja
	msg = response.lst_medicamentos
	return render_template("consTipo_msg.html", msg = msg)



##
##	CONSULTA POR NOMBRE COMERCIAL
##

@app.route('/consNombComerc_form')
def consNombComerc_form():
	return render_template("consNombComerc_form.html")

@app.route('/consNombComerc_msg', methods=['POST'])
def consNombComerc_msg():
	nombre_comercial = request.form['nombre_comercial']
	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001',credentials)
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)
	response = stub.ConsultaMedicamentoPorNombreComercial(servicio_pb2.ConsultaTipo(confirmacion = nombre_comercial)) #viaja al server y trae respuesta
	msg = response.lst_medicamentos
	return render_template("consNombComerc_msg.html", msg = msg)


##
##	CONSULTA DE CODIGOS
##

@app.route('/consCodigo_form')
def consCodigo_form():
	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001',credentials)
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)

	response = stub.ListaProductos(servicio_pb2.Nulo()) #viaja al server y trae respuesta
	msg = response.lst_medicamentos
	return render_template("consCodigo_form.html", msg = msg)

@app.route('/consCodigo_msg', methods=['POST'])
def consCodigo_msg():

	codigo_geografico_prioridad = request.form['codigo_geografico_prioridad']

	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001',credentials)
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)

	response = stub.EsPrioritario(servicio_pb2.ConsultaTipo(confirmacion= codigo_geografico_prioridad)) #viaja al server y trae respuesta
	flag = response.respuesta

	if flag == 1:
		msg =" El codigo es prioritario = True"
	else:
		 msg =" El codigo es prioritario = False"

	return render_template("consCodigo_msg.html", msg = msg)

@app.route('/consCodigoVerif_msg', methods=['POST'])
def consCodigoVerif_msg():

	codigo_geografico_verificador = request.form['codigo_geografico_verificador']

	with open('C:/Users/Admin/Desktop/Certificado.cer', 'rb') as f : credentials = grpc.ssl_channel_credentials(f.read())
	channel = grpc.secure_channel('localhost:5001',credentials)
	stub = servicio_pb2_grpc.FarmaceuticaStub(channel)

	response = stub.Verificar(servicio_pb2.ConsultaTipo(confirmacion= codigo_geografico_verificador))
	flag = response.respuesta

	if flag == 1:
		msg =" El codigo verificador es correcto = True"
	else:
		msg =" El codigo verificador es correcto = False"

	return render_template("consCodigo_msg.html", msg = msg)



if __name__ == "__main__" :
    #serve()
    app.run(debug= True)
