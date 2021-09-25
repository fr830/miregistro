import sys
import logging
import pymysql
import handler

class tramites(handler.lambda_handler):
    def __init__(self, event, context, conn):
        super().__init__(event, context, conn)
    
    def get_all(self, limit):
        # This method get all of tramites inner database
        
        count = 0
        sql = """SELECT T.IdTramite AS ID, T.Dominio AS Dominio, Ct.Nombre AS Categoria, T.Observaciones AS Observaciones
                 FROM tramite T
					JOIN categoriatramite Ct ON Ct.IdCategoriaTramite = T.FkIdCategoria
                 WHERE deleted = 0
                 GROUP BY T.IdTramite
                 ORDER BY T.IdTramite DESC
                 LIMIT {};""".format(limit)
        
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)

                for row in cur:
                    count += 1
                    self.response.append(row)
                    
            self.conn.commit()
            self.body = self.buildBody('GET', 'SUCCESS', self.response, count)
        except:
            self.conn.rollback()
            self.response.append("An error ocurred when you try to commited with an MySql Command!")
            self.body = self.buildBody('GET', 'FAILED', self.response, 0)
    
    def get_tramite(self, id):
        # This method get all of tramites inner database
        
        count = 0
        sql ="""SELECT T.IdTramite AS ID, T.Dominio AS Dominio, Ct.Nombre AS Categoria, T.Observaciones AS Observaciones
                FROM tramite T
				    JOIN categoriatramite Ct ON Ct.IdCategoriaTramite = T.FkIdCategoria
                WHERE T.IdTramite = {id}
                GROUP BY T.IdTramite;""".format(id=id)
        
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)

                for row in cur:
                    count += 1
                    self.response.append(row)
                    
            self.conn.commit()
            self.body = self.buildBody('GET', 'SUCCESS', self.response, count)
        except:
            self.conn.rollback()
            self.response.append("An error ocurred when you try to commited with an MySql Command!")
            self.body = self.buildBody('GET', 'FAILED', self.response, 0)
      
    def delete_tramite(self, id):
        # This method delete specific tramite id
        
        sql = "DELETE FROM tramite WHERE IdTramite = {idTramite};".format(idTramite=id)
        sql_recheckidentity = "ALTER TABLE tramite AUTO_INCREMENT = 1; "
        
            
        try:
            # Execute SQL command
            with self.conn.cursor() as cur:
                cur.execute(sql)
                cur.execute(sql_recheckidentity)
    
            # Commit changes    
            self.conn.commit()
            self.response.append("You delete the register tramite {id}".format(id=id))
            self.body = self.buildBody('DELETE', 'SUCCESS', self.response, 1)
        except:
            self.conn.rollback()
            self.response.append("An error ocurred when you try to commited with an MySql Command!")
            self.body = self.buildBody('DELETE', 'FAILED', self.response, 0)
    
    def put_tramite(self, dominio, id_category, id_empresa, observaciones):
        # This method put tramite inner database tramites

        sql = """INSERT INTO tramite (Dominio, FkIdCategoria, FkIdEmpresa, Fecha, Observaciones)
                VALUES 
                (
                    '{dominio}', 
                    {fkcategoria},
                    {fkempresa},
                    NOW(),
                    '{observaciones}'
                );""".format(dominio=dominio, fkcategoria=id_category, fkempresa=id_empresa, observaciones=observaciones)
        
        try:
            # Execute SQL command
            with self.conn.cursor() as cur:
                cur.execute(sql)

            # Commit changes    
            self.conn.commit()
            self.response.append("You insert {dominio} at date now!".format(dominio=dominio))
            self.body = self.buildBody('PUT', 'SUCCESS', self.response, 1)
        except:
            self.conn.rollback()
            self.response.append("An error ocurred when you try to commited with an MySql Command!")
            self.body = self.buildBody('PUT', 'FAILED', self.response, 0)

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
    hand = tramites(event, context, conn)
    
    routeKey = event['routeKey']
    #requestJSON = event['body']
    
    if routeKey == "GET /tramites":
        limit = event['queryStringParameters']['limit']
        
        hand.get_all(limit)

    if routeKey == "PUT /tramites":
        dominio = event['queryStringParameters']['dominio']
        id_category = event['queryStringParameters']['idcategoria']
        id_empresa = event['queryStringParameters']['idempresa']
        observaciones = event['queryStringParameters']['observaciones']

        hand.put_tramite(dominio=dominio, id_category=id_category, id_empresa=id_empresa, observaciones=observaciones)

    if routeKey == "DELETE /tramites/{id}":
        idTramite = event['pathParameters']['id']
        
        hand.delete_tramite(idTramite)
        
    if routeKey == "GET /tramites/{id}":
        idTramite = event['pathParameters']['id']
        
        hand.get_tramite(idTramite)


    return hand.buildResponse(statusCode=hand.status_code, body=hand.body)