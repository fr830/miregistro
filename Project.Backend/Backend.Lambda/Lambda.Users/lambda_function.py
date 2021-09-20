import sys
import logging
import rds_config
import pymysql
import handler

class users(handler.lambda_handler):
    def __init__(self, event, context, conn):
        super().__init__(event, context, conn)
    
    def get_all(self,empresa_location):
        # This method get all of users in a register
        
        item_count = 0
        sql = """SELECT U.IdUsuario, P.IdPerfil,  U.Usuario, U.Email, U.activo, P.Nombre, P.Apellido, P.nick, Er.nombre
                 FROM usuario U
                 JOIN perfil P ON P.IdPerfil = U.FkIdPerfil
                 JOIN empleado E ON E.FkIdUsuario = U.IdUsuario
                 JOIN empresa Er ON Er.IdEmpresa = E.FkIdEmpresa
                 WHERE Er.nombre = '{empresa_name}';""".format(empresa_name=empresa_location)
        
        with self.conn.cursor() as cur:
            cur.execute(sql)

            for row in cur:
                item_count += 1
                self.response.append(row)
                
        self.conn.commit()
        self.response.append(item_count)

        self.body = self.buildBody('GET', 'SUCCESS', self.response, item_count)
        
    def get_user(self, idUser, nameUser):
        # This method get specific user
        
        item_count = 0

        sql = """SELECT U.IdUsuario, P.IdPerfil,  U.Usuario, U.Email, U.activo, P.Nombre, P.Apellido, P.nick, Er.nombre
                 FROM usuario U
                 JOIN perfil P ON P.IdPerfil = U.FkIdPerfil
                 JOIN empleado E ON E.FkIdUsuario = U.IdUsuario
                 JOIN empresa Er ON Er.IdEmpresa = E.FkIdEmpresa
                 WHERE U.IdUsuario = {id} AND U.usuario = '{usuario}';""".format(id=idUser, usuario=nameUser)
        
        #sql = "SELECT * from usuario WHERE IdUsuario={id} AND usuario='{name}'".format(id = idUser, name=nameUser)

        with self.conn.cursor() as cur:
            cur.execute(sql)

            for row in cur:
                item_count = item_count + 1
                self.response.append(row)
                
        self.conn.commit()
        
        #print(self.response)
        self.body = self.buildBody('GET', 'SUCCESS', self.response, item_count)
    
#rds settings
rds_host  = "instance-aws-free-tier.c9qdfbtzelbq.us-east-2.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
        
def handler(event, context):    
    hand = users(event, context, conn)
    
    routeKey = event['routeKey']
    requestJSON = event['body']
    queryStringParameters = event['queryStringParameters']
    
    if routeKey == "GET /user":
        empresaLocation = queryStringParameters['location']
        hand.get_all(empresaLocation)
        
    if routeKey == "GET /user/{id}":
        idUser = event['pathParameters']['id']
        nameUser = queryStringParameters['name_usuario']
        hand.get_user(idUser, nameUser)
    
    return hand.buildResponse(statusCode=hand.status_code, body=hand.body)