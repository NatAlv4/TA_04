from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func 

#definimos notes como una base de datos que recolctara informacion adicional del usuario 

class note(db.model):
  id = db.column(db.integer, primary_key=True)
  datos = db.column(db.String(10000))
  feha = db.column(db.DateTime(Timezone=True), default=func.now()) 
  #queremos almacenar (notes/"informacion") que un usuario ingresa y asociarla con su respectivo ususario, esto se logra con los foreingKeys que me introducen y asocian una columna de una base de datos, con otra base de datos
  user_id = db.column(db.integer, db.foreingKey('user.id')) 



#definimoS que estructura o esquema que tendrá la tabla que almacenara los datos del login de cada una de las entradas (objetos/usuarios) donde cada una de las entradas de la tabla (columna) podran tener un atributo de su unicidad (en el caso del correo electronico)
class User(db.model, UserMixin):
  id = db.column(db.integer, primary_key=True)
  nombre = db.column(db.String(120))
  apellido = db.column(db.String(120))
  email = db.column(db.String(120), unique=True)
  contaseña1 = db.column(db.String(120))
  conraseña2 = db.column(db.String(120))
  notes = db.relationship('note')

