import cx_Oracle

def main():

    ip = '10.1.71.21'
    port = 1521
    SID = 'hom'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)


    con = cx_Oracle.connect('unikvp', 'unikvp.1234', dsn_tns)
    print con.version
    
    con.close()
    
if __name__ == '__main__':
    main()