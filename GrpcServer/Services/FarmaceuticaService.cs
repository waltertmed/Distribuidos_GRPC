using Grpc.Core;
using Microsoft.Extensions.Logging;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GrpcServer.Services
{
    
    public class FarmaceuticaService : Farmaceutica.FarmaceuticaBase
    {   //creo un string que contenga los datos de la conexion a bd para no repetirlos cada vez que hay que conectar
        string myConnectionString = "Database=grcp_bd;Data Source=localhost;User Id=root;Password=root";
        public MySqlConnection conexion(string myConnectionString)
        {
            MySqlConnection cnx = new MySqlConnection(myConnectionString);
            return cnx;
        }


        private readonly ILogger<FarmaceuticaService> _logger;

        public FarmaceuticaService(ILogger<FarmaceuticaService> logger)
        {
            _logger = logger;
        }
        //**************************************************************************************
        public override Task<Confirmacion> AltaTipoMedicamento(Tipo request, ServerCallContext context)
        {
            Confirmacion output = new Confirmacion();

            AgregarTipoMedicamento(request);
            output.Confirmacion_ = "El Tipo de medicamento:" + request.TipoMedicamento+" fue dado de alta" ;
            return Task.FromResult(output);
        }
        //**************************************************************************************
        public override Task<Confirmacion> AltaMedicamento(Medicamento request, ServerCallContext context)
        {
            Confirmacion output = new Confirmacion();

            AgregarMedicamento(request);
            output.Confirmacion_ = "El Medicamento:"+ request.NombreComercial+" fue dado de alta";
            return Task.FromResult(output);
        }
        //**************************************************************************************
        public override Task<Confirmacion> BajaTipoMedicamento(Tipo request, ServerCallContext context)
        {
            Confirmacion output = new Confirmacion();

            DarDeBajaTipoMedicamento(request);
            output.Confirmacion_ = "El tipo de medicamento:" + request.TipoMedicamento + " fue dado de baja";
            return Task.FromResult(output);
        }


        //**************************************************************************************
        public override Task<ListaMedicamentos> ConsultaMedicamentoPorTipo(ConsultaTipo request, ServerCallContext context)
        {
            ListaMedicamentos output = new ListaMedicamentos();
            output = ConsultarMedicamentoXTipo(request);

            return Task.FromResult(output);
        }

        //**************************************************************************************
        public override Task<RespuestaCodigo> EsPrioritario(ConsultaTipo request, ServerCallContext context)
        {

            RespuestaCodigo output = new RespuestaCodigo();
            output.Respuesta = TipoEsPrioritario(request);
            return Task.FromResult(output);
        }
        //**************************************************************************************
        public override Task<RespuestaCodigo> Verificar(ConsultaTipo request, ServerCallContext context)
        {

            RespuestaCodigo output = new RespuestaCodigo();
            output.Respuesta = Verificado(request);
            return Task.FromResult(output);
        }


        public override Task<ListaMedicamentos> ConsultaMedicamentoPorNombreComercial(ConsultaTipo request, ServerCallContext context)
        {

            ListaMedicamentos output = new ListaMedicamentos();
            output = ConsultarMedicamentoXNombre(request);
            return Task.FromResult(output);
        }
        //*************************************************************************************
        public override Task<ListaMedicamentos> ListaProductos(Nulo request, ServerCallContext context)
        {
            ListaMedicamentos output = new ListaMedicamentos();
            output = traerListaMedicamentos();

            return Task.FromResult(output);
        }




        //**************************************************************************************
        public void AgregarTipoMedicamento(Tipo request)
        {
            Console.WriteLine("-------");
            Console.WriteLine("Agregar Tipo de Medicamento");
            Console.WriteLine("Nombre Tipo: " + request.TipoMedicamento);
            Console.WriteLine("Activo: " + request.Activo);
            Console.WriteLine("-------");
            MySqlConnection cnx = new MySqlConnection(myConnectionString);
            cnx.Open();
            string myInsertQuery = "INSERT INTO Tipo(Tipo_Medicamento, Activo) values(?NombreTipo, ?Activo);";
            MySqlCommand commando = new MySqlCommand(myInsertQuery, cnx);
            commando.Parameters.AddWithValue("?NombreTipo", request.TipoMedicamento);
            commando.Parameters.AddWithValue("?Activo", request.Activo);
            commando.ExecuteNonQuery();
            commando.Connection.Close();


        }
        //**************************************************************************************
        public void DarDeBajaTipoMedicamento(Tipo request)
        {

            Console.WriteLine("-------");
            Console.WriteLine("Dar de baja Tipo de Medicamento");
            Console.WriteLine("Nombre Tipo: " + request.TipoMedicamento);
            Console.WriteLine("-------");

            MySqlConnection cnx = conexion(myConnectionString);
            cnx.Open();

            MySqlCommand consultaQuery = cnx.CreateCommand();
            consultaQuery.CommandText = "SELECT IdTipo FROM Tipo WHERE Tipo_Medicamento= ?TipoMedicamento;";
            consultaQuery.Parameters.AddWithValue("?TipoMedicamento", request.TipoMedicamento);
            var reader = consultaQuery.ExecuteReader();
            reader.Read();
            var idTipo = reader.GetValue(0);
            consultaQuery.Connection.Close();

            string actualizarQuery = "UPDATE Tipo SET Activo = 0 WHERE IdTipo = ?IdTipo";
            cnx.Open();
            MySqlCommand commando = new MySqlCommand(actualizarQuery, cnx);
            commando.Parameters.AddWithValue("?IdTipo", idTipo);
            commando.ExecuteNonQuery();
            commando.Connection.Close();

        }

        //**************************************************************************************
        public void AgregarMedicamento(Medicamento request)
        {

            Console.WriteLine("-------");
            Console.WriteLine("Agregar Medicamento");
            Console.WriteLine("Codigo " + request.Codigo);
            Console.WriteLine("Nombre comercial: " + request.NombreComercial);
            Console.WriteLine("Droga: " + request.Droga);
            Console.WriteLine("Tipo Medicamento: " + request.TipoMedicamento.TipoMedicamento);
            Console.WriteLine("-------");

            // llamo a la clase de mysql conexion
            MySqlConnection cnx = conexion(myConnectionString);
            // abro la conexion con el nombre cnx
            cnx.Open();
            // en base a esa conexion creo un comando llamado consulta query
            MySqlCommand consultaQuery = cnx.CreateCommand();
           // determino mi query
            consultaQuery.CommandText = "SELECT IdTipo FROM Tipo WHERE Tipo_Medicamento= ?TipoMedicamento;";
           // al parametro creadp "?TipoMedicamento" que le paso a la query le tengo que asignar un valor
            consultaQuery.Parameters.AddWithValue("?TipoMedicamento", request.TipoMedicamento.TipoMedicamento);
            // ejecuto execute reader para que levante el select en la bd
            var reader = consultaQuery.ExecuteReader();
            // reader.Read() va al proximo resultado
            reader.Read();
            // en idTipo guardo el valor del reader
            var idTipo = reader.GetValue(0);
            // cierro la conexion de la consulta para iniciar la query del insert sino no te deja,**** se puede hacer todo en una misma conexion?
            consultaQuery.Connection.Close();
            // creo la query para insertar
            string myInsertQuery = "INSERT INTO Medicamento(Nombre_Comercial, Codigo, Droga, Tipo_idTipo) values( ?NombreComercial , ?Codigo  , ?Droga , ?TipoMedicamento );";
            // abro conexion
            cnx.Open();
            // creo un comando que contenga la query y la conexion abierta
            MySqlCommand commando = new MySqlCommand(myInsertQuery, cnx);
            // agrego en cada parametro creado con el"?" los datos que llegan del request
            commando.Parameters.AddWithValue("?NombreComercial", request.NombreComercial);
            commando.Parameters.AddWithValue("?Codigo", request.Codigo);
            commando.Parameters.AddWithValue("?Droga", request.Droga);
            // idTipo viene de la consulta reader
            commando.Parameters.AddWithValue("?TipoMedicamento", idTipo );
            // ejecuto la query, aca si no cerraba la conexion o el reader de arriba, tiraba error de que habia que cerrar antes la otra consulta
            commando.ExecuteNonQuery();
            // cierro conexion
            commando.Connection.Close();
        }

        //**************************************************************************************

        public bool TipoEsPrioritario (ConsultaTipo request)
        {
           bool respuesta = false;

            Console.WriteLine("-------");
            Console.WriteLine("Consultar prioridad de medicamento");
            Console.WriteLine("Codigo: " + request.Confirmacion);
            Console.WriteLine("-------");

            //MySqlConnection cnx = conexion(myConnectionString);
            //cnx.Open();
            //MySqlCommand consultaQuery = cnx.CreateCommand();
            //consultaQuery.CommandText = ("SELECT IdMedicamento FROM Medicamento WHERE (Codigo LIKE 'P%' OR codigo LIKE 'W%') AND Codigo =?Codigo;");
            //consultaQuery.Parameters.AddWithValue("?Codigo", request.Confirmacion);
            //var reader = consultaQuery.ExecuteReader();

            //while (reader.Read()) {

            //    var Codigo = reader.GetString(0);
            //    if (Codigo == null)
            //    {
            //        respuesta = false;
            //    }
            //    else
            //    {
            //        respuesta = true;
            //    }
            //}

            string Codigo = request.Confirmacion.Substring(0,1);

            Console.WriteLine("CODIGO:"+Codigo);
            List<string> list = new List<string>(new[] {"P","p","W","w" });


            if (!list.Contains(Codigo))
                {
                respuesta = false;
                }else
                   {
                    respuesta = true;
                    }
           

            return respuesta;
        }

        //**************************************************************************************

        public bool Verificado(ConsultaTipo request)
        {

            bool respuesta = false;

            Console.WriteLine("-------");
            Console.WriteLine("Verificar digito");
            Console.WriteLine("Codigo: " + request.Confirmacion);
            Console.WriteLine("-------");

            int primerPosicion = request.Confirmacion.IndexOf("-")+1;
            int segundaPosicion = request.Confirmacion.LastIndexOf("-");
            string StringAVerificar = request.Confirmacion.Substring(primerPosicion, segundaPosicion - primerPosicion);
            
         
            //    MySqlConnection cnx = conexion(myConnectionString);
            //    cnx.Open();
            //    MySqlCommand consultaQuery = cnx.CreateCommand();
            //    consultaQuery.CommandText = ("");
            //    consultaQuery.Parameters.AddWithValue("?Codigo", request.Confirmacion);
            //    var reader = consultaQuery.ExecuteReader();

            //    while (reader.Read())
            //    {
            //        var Codigo = reader.GetString(0);
            //        int primerPosicion = Codigo.IndexOf("-");
            //        int segundaPosicion = Codigo.IndexOf("-");
            //        string StringAVerificar = Codigo.Substring(primerPosicion, segundaPosicion - primerPosicion);
            //        prueba = StringAVerificar;

            //    }

            int devolucion = sumarElementos(StringAVerificar);

      
            string codigoVerificador = request.Confirmacion.Substring(segundaPosicion + 1);

   

            if (devolucion== Int32.Parse(codigoVerificador))
            {
                respuesta = true;
            }


            return respuesta;
        }

        //**************************************************************************************
        public int sumarElementos(string var)
        {
            int respuesta = 0;
            int numero = Int32.Parse(var);
            List<int> lista = new List<int>();
            List<int> lista2 = new List<int>();
            while (numero > 0)
            {
               int agregar = numero % 10;
                numero = numero / 10;
                lista.Add(agregar);
                Console.WriteLine(agregar);
            }
            int sumar=0;
         
            for(int i = 0; i < lista.Count; i++)
            {

                sumar += lista[i];
                Console.WriteLine("Suma:" + sumar);
            }
            if (sumar > 10)
            {
                int agregar2 = sumar % 10;
                int cociente = sumar / 10 ;
                Console.WriteLine("Agregar2:" + agregar2);
                Console.WriteLine("Cociente:" + cociente);
                lista2.Add(agregar2);
                lista2.Add(cociente);
                int sumaFinal = 0;
                for (int i = 0; i < lista2.Count; i++)
                {
                    sumaFinal += lista2[i];
                    Console.WriteLine("Suma:" + i +" :"+ sumaFinal);
                }
                Console.WriteLine("SumaFinal:" + sumaFinal);
                respuesta = sumaFinal;
            }
            else
            {
                respuesta = sumar;

            }

            return respuesta;

        }
        //**************************************************************************************
        public ListaMedicamentos ConsultarMedicamentoXTipo(ConsultaTipo request)
        {

            ListaMedicamentos lista = new ListaMedicamentos();

            Console.WriteLine("-------");
            Console.WriteLine("Consultar por Tipo de Medicamento");
            Console.WriteLine("Nombre Tipo: " + request.Confirmacion);
            Console.WriteLine("-------");

            MySqlConnection cnx = conexion(myConnectionString);
            cnx.Open();

            MySqlCommand consultaQuery = cnx.CreateCommand();
            consultaQuery.CommandText = "SELECT IdTipo FROM Tipo WHERE Tipo_Medicamento= ?TipoMedicamento;";
            consultaQuery.Parameters.AddWithValue("?TipoMedicamento", request.Confirmacion);
            var reader = consultaQuery.ExecuteReader();


            reader.Read();
            
            int idTipo = reader.GetInt32(0);
      
            

            consultaQuery.Connection.Close();

            cnx.Open();
            MySqlCommand segundaQuery = cnx.CreateCommand();
            segundaQuery.CommandText = "SELECT Nombre_Comercial, Codigo, Droga FROM Medicamento WHERE Tipo_IdTipo= ?IdTipo";
            segundaQuery.Parameters.AddWithValue("?IdTipo", idTipo);
            var segundoReader = segundaQuery.ExecuteReader();

            while (segundoReader.Read())
            {
                Medicamento nombre = new Medicamento(); 
                nombre.NombreComercial = (string)segundoReader.GetValue(0);
                nombre.Codigo = (string)segundoReader.GetValue(1);
                nombre.Droga = (string)segundoReader.GetValue(2);
                List<Medicamento> lst = new List<Medicamento>();

                lst.Add(nombre);
                foreach(var nombres in lst)
                {
                    lista.LstMedicamentos.Add(nombres);
                }
               
            }
            segundaQuery.Connection.Close();
            return lista;
        }

        //**************************************************************************************

        public ListaMedicamentos ConsultarMedicamentoXNombre (ConsultaTipo request)
        {
            Console.WriteLine("-------");
            Console.WriteLine("Consultar por Nombre comercial del Medicamento");
            Console.WriteLine("Nombre Medicamento: " + request.Confirmacion);
            Console.WriteLine("-------");

            ListaMedicamentos lista = new ListaMedicamentos();

            MySqlConnection cnx = conexion(myConnectionString);
            cnx.Open();

            MySqlCommand consultaQuery = cnx.CreateCommand();


            consultaQuery.CommandText = "SELECT Nombre_Comercial, Codigo, Droga FROM Medicamento WHERE Nombre_Comercial LIKE ?Nombre_Comercial";
            consultaQuery.Parameters.Add("?Nombre_Comercial", MySqlDbType.VarChar).Value = request.Confirmacion + "%";

            var reader= consultaQuery.ExecuteReader();

            while (reader.Read())
            {
                Medicamento nombre = new Medicamento();
                nombre.NombreComercial = (string) reader.GetValue(0);
                nombre.Codigo = (string)reader.GetValue(1);
                nombre.Droga = (string)reader.GetValue(2);
                List<Medicamento> lst = new List<Medicamento>();

                lst.Add(nombre);

                foreach(var nombres in lst)
                {
                    lista.LstMedicamentos.Add(nombres);
                }
            }
            consultaQuery.Connection.Close();
            return lista;

        }

        public ListaMedicamentos traerListaMedicamentos()
        {

            ListaMedicamentos lista = new ListaMedicamentos();

            MySqlConnection cnx = conexion(myConnectionString);

            cnx.Open();

            MySqlCommand consultaQuery = cnx.CreateCommand();
            consultaQuery.CommandText = "SELECT Nombre_Comercial, Codigo, Droga FROM Medicamento;";
            var reader = consultaQuery.ExecuteReader();

            while (reader.Read())
            {
                Medicamento nombre = new Medicamento();
                nombre.NombreComercial = (string)reader.GetValue(0);
                nombre.Codigo = (string)reader.GetValue(1);
                nombre.Droga = (string)reader.GetValue(2);
                List<Medicamento> lst = new List<Medicamento>();

                lst.Add(nombre);
                foreach (var nombres in lst)
                {
                    lista.LstMedicamentos.Add(nombres);
                }


            }

            return lista;
        }

    }


}