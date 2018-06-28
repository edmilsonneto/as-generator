import cx_Oracle, os
from jinja2 import Environment, FileSystemLoader
from Campo import Campo

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def makeConection():

    ip = '10.1.71.21'
    port = 1521
    SID = 'hom'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)

    return cx_Oracle.connect('unikvp', 'unikvp.1234', dsn_tns)

def main():

    #readTable("T_LOJA")
    writeClass("T_RESPROCDOCAGENDADO")
   
def writeClass(tableName):

    campos = readTable(tableName)

    j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)

    print j2_env.get_template('javaClass.tpl').render(tableName=tableName, campos=campos)

def parseType(columnName,tipo, dataLenght, dataPrecision, dataScale):

    if tipo == 'VARCHAR2' :
        return "String"
    elif tipo == 'NUMBER' and (dataScale == 0 or not dataScale ):
        return "Integer"
    elif tipo == 'NUMBER' and dataScale == 4:
        return "BigDecimal"

def readTable(tableName):
    campos = []

    con = makeConection()
    cur = con.cursor()

    cur.execute("SELECT COLUMN_NAME, DATA_TYPE, DATA_LENGTH, DATA_PRECISION, DATA_SCALE FROM user_tab_cols WHERE TABLE_NAME = :tableName", {"tableName":tableName})
    for result in cur.fetchall():
       campos.append(Campo(result[0], parseType(result[0], result[1], result[2], result[3], result[4])))

    cur.close()
    con.close()

    return campos

if __name__ == '__main__':
    main()