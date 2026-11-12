from flask import Flask, jsonify, request
import psycopg2 # Este es el motor

app = Flask(__name__) # La creación del servidor

# Vamos a conectar nuestro servidor (API) con la BD
# Debes tener instalado psycop2 => PostgreSQL
#                       mysqlclient => MySQL
# pip install psycopg2

# CONEXIÓN
# Vamos a crear una función para poder conectarnos a nuestra BD
# Informacón o los datos que vas a envoar son los siguientes:
# host     => Es el lugar dónde está alojado tu bd (localhost, 157.15.65.68)
# database => Es el nombre de la bd a la que quieres conectarte
# user     => El usuario de tu bd (postgres)
# password => La contraseña de tu bd (root)
# port     => Es el puerto dónde corre la bd (5432)
def get_db_conection():
    conexión = psycopg2.connect(
                        host='localhost',
                        database='canciones',
                        user='postgres',
                        password='73papafrita404',
                        port='5432'
                    )
    
    return conexión

@app.route("/api/artistas", methods=["GET"])
def get_artistas():
    # 01. Conectarte a la BD
    conn = get_db_conection() # Me conecto y guardo la conexión
    # 02. Cear un cursor => Donde podesmos ejecutar SQL
    cur = conn.cursor()
    # 03. Vamos a ejecutar la consulta SQL
    cur.execute("SELECT * FROM artistas")
    # 04. Guardar la respuesta
    filas = cur.fetchall()
    # 05. Vamos a cerrar el cursor y la conexión
    cur.close() # Cierro el cursor
    conn.close() # Cierro la conexión
    # 06. Formateo
    resultados_transformados = []
    for elmt in filas:
        formato = {
            "id": elmt[0],
            "nombre": elmt[1],
            "genero": [2],
            "pais_origen": [3],
            "activo": [4]
        }
        resultados_transformados.append(formato)

    # 07. Retornar info. o responder
    # SIEMPRE debe retornar una respuesta
    # El formato de la respuesta debe ser en JSON
    # Para transformar la respuesta en JSON debes de importar
    # from flask jsonify (va en la arte superior)
    return jsonify(resultados_transformados)

# RETO 01:
# Crear un endpoint del tipo GET, llamado /api/canciones
# Este endpoint debe devolver todas las canciones de la tabla
# canciones
# La respuesta debe ser todas las canciones en JSON

@app.route("/api/canciones", methods=["GET"])
def get_canciones():
    conn = get_db_conection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM canciones")
    filas = cur.fetchall()
    print(filas)
    cur.close()
    conn.close()

    resultados_transformados = []
    for elmt in filas:
        formato = {
            "id": elmt[0],
            "titulo": elmt[1],
            "album": elmt[2],
            "duracion": elmt[3],
            "artista_id": elmt[4]
        }
        resultados_transformados.append(formato)
    return  jsonify(resultados_transformados)

# Necesitamos que se devuelva a un solo artista
# Se cree un endpoint el cual devuelva a un artista según el id
# /api/artistas/<id>
# Debe de ser del tipo GET

@app.route("/api/artistas/<int:id>", methods=["GET"])
def get_single_artist(id):
    conn = get_db_conection()
    cur = conn.cursor()
    # cur.execute(f"SELECT * FROM artistas WHERE id = {id}")
    cur.execute("SELECT * FROM artistas WHERE id = %s", (id,))
    fila = cur.fetchone()
    cur.close()
    conn.close()

    if fila is None:
        return {
            "msg": "Artista no encontrado"
        }, 404

    return {
        "id": fila[0],
        "nombre": fila[1],
        "genero": fila[2],
        "pais_origen": fila[3],
        "activo": fila[4]
    }

# Nesecitamos que se registre la info. de los artistas
# Se solicita que se cree un endpoint => /api/add-artistas
# Tiene que ser del tipo POST => insertar info.
@app.route("/api/add-artistas", methods=["POST"])
def add_artistas():
    # Vas a capturar el JSON que te va a enviar el fronted
    # Para capturar el JSON
    # Se debe de importar
    # from flask import request
    # 01. Capturar la info.
    data = request.json
    # 02. Validaciones
    # El JSON este vacío
    if not data:
        return {
            "msg": "Debes de enviar la información"
        }

    if "nombre" not in data:
        return {
            "msg": "Debes de enviar el nombre del artista"
        }

    if "genero" not in data:
        return {
            "msg": "Debes de enviar el genero"
        }
    # 03. Vamos a conectarnos y crear el cursor
    conn = get_db_conection()
    cur = conn.cursor()
    # 04. Ejecutar tu insercción y grabar
    cur.execute("""INSERT INTO artistas (nombre, genero, pais_origen) 
                   VALUES (%s, %s, %s)""",
                   (data["nombre"], data["genero"], data["pais_origen"]))

    conn.commit() # Graba tu insercción en la bd

    cur.close()
    conn.close()

    return {
        "msg": "Creacion exitosa"
    }, 201

# RETO 02:
# Necesitamos que se registre informacion en las canciones
# Se solicita que se cree un endpoint => "/api/add-canciones"
# Este tiene que ser del tipo POST
# {
#   titulo: "No te vayas",
#   album: "Rafaga",
#   duracion_segundos: 230,
#   anio_lanzamiento: 2016,
#   artista_id: 9
# }

@app.route("/api/add-canciones", methods=["POST"])
def add_canciones():
    data = request.json
    if not data:
        return {
            "msg": "Debes de enviar la información"
        }
    
    if "titulo" not in data:
        return {
            "msg": "Debes de enviar el titulo del artista"
        }
    
    if "album" not in data:
        return {
            "msg": "Debes de enviar el album"
        }
    if "duracion_segundos" not in data:
        return {
            "msg": "Debes de enviar la duración en segundos"
        }
    if "anio_lanzamiento" not in data:
        return {
            "msg": " Debes de enviar el año de lanzamiento"
        }
    conn = get_db_conection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO canciones (titulo, album, duracion_segundos, anio_lanzamiento) 
                       VALUES (%s, %s, %s)""",
                       (data["titulo"], data["album"], data["duracion_segundos"], data["anio_lanzamiento"]))
    conn.commit()
    cur.close()
    conn.close()
    return {
        "msg": "Creacion exitosa"
    }, 201

# Encendiendo el servidor
# Buscas evitar prender y apagar el servidor por cada cambio
# Debes usar debug=True
# El servidor se reiniciará solo cuando vea un camio
# también nos indica los errores que existieran
app.run(debug=True)