import sys
import logging
import rds_config
import pymysql
import json

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

def handler(event):    
    #This function fetches content from MySQL RDS instance

    response = []
    item_count = 0
    sql = "SELECT * from usuario LIMIT 100"
    
    with conn.cursor() as cur:
        cur.execute(sql)

        for row in cur:
            item_count += 1
            response.append(row)
            
    conn.commit()
    
    body = buildBody('GET', 'SUCCESS', response)
    
    return buildResponse(200, body)

def buildBody(operation, message, item):
    return {
      'Operation': operation,
      'Message': message,
      'Item': item
    }

def buildResponse(statusCode, body):
    return {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(body) 
    }  
    
def main(event, context):
    return handler(event)