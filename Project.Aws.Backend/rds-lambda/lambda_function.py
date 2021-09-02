import sys
import logging
import rds_config
import pymysql

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

    result = []
    item_count = 0
    sql = "SELECT * from usuario LIMIT 100"
    
    with conn.cursor() as cur:
        cur.execute(sql)

        for row in cur:
            item_count += 1
            logger.info(row)
            result.append(row)
        
        print(result)
        conn.commit()
        cur.close()

    return result

def main(event, context):
    handler(event)

main("", "")