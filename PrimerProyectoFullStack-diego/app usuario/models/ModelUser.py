from .entities.User import User # se imposta la clase user del constructor


class ModelUser():

    @classmethod # se crea para poder utilizarlo sin instanciar la clase
    def login(self, db, user): #de la instancia usuario que se recibe
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user 
                    WHERE username = '{}'""".format(user.username) #se obtiene su username, permitiendo saber si el usuario existe en la base de datos
            cursor.execute(sql) #ejecutamos la centencia sql
            row = cursor.fetchone() #row resultante 
            if row != None: #hay algun dato resultante?
                #objeto de tipo usuario, se le pasan los datos que pide el constructor
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                # se importa el id, que se encuentra en row, posicion 0, row 1 username, User.check_password se llama al metodo (User.py) y tambien el pass del usuario para comparar, row 3 es fullname
                return user # se retorna el usuario
            else:
                return None # en el caso de que no hay usuario, retorna none
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id): #recibe el usuario y un id
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname, dni, nombres, tipo, apellido FROM user WHERE id = {}".format(id) # se compara el id, (format para concatenar el id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) #el passwor ya no se compara (none), fullname en posicion 2
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod # se crea para poder utilizarlo sin instanciar la clase
    def registro(self, db, user): #de la instancia usuario que se recibe
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, email FROM user 
                    WHERE email = '{}'""".format(user.email) #se obtiene su username, permitiendo saber si el usuario existe en la base de datos
            cursor.execute(sql) #ejecutamos la centencia sql
            row = cursor.fetchone() #row resultante 
            if row != None: #hay algun dato resultante?
                #objeto de tipo usuario, se le pasan los datos que pide el constructor
                user = User(row[0], row[1], row[2], row[3])
                # se importa el id, que se encuentra en row, posicion 0, row 1 username, User.check_password se llama al metodo (User.py) y tambien el pass del usuario para comparar, row 3 es fullname
                return user # se retorna el usuario
            else:
                return None # en el caso de que no hay usuario, retorna none
        except Exception as ex:
            raise Exception(ex)
