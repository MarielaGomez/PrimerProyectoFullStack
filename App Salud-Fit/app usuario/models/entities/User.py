from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin # para saber si el usuario esta activo

 
class User(UserMixin): #hereda UserMixin, en este caso es para saber si esta activo

    def __init__(self, id, username, password, dni="", fullname="", tipo="", email="", nombres="" ) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.dni = dni                
        self.fullname = fullname
        self.tipo = tipo
        self.email = email
        self.nombres = nombres
        

        
        
#ingresa pasword y sale el pass encriptado
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    



#print(generate_password_hash("admin"))
