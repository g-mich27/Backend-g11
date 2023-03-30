from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ManejoUsuario(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, password, tipoUsuario):
        # este metodo se manadara a llamr cuando enla terminal se ponga manage.py createsuperuser
        if not correo:
            raise ValueError('El ususario debe tener un correo')
     
        # normalize_email > sirve para llevar todo el correo a minusculas y ademas le quita espacios en blanco y verifica si los caracteres son validos
        # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
        correo_normalizado = self.normalize_email(correo)

        nuevo_usuario = self.model(correo = correo_normalizado, nombre = nombre, apellido = apellido, tipoUsuario = tipoUsuario)

        # generamos el hash de nuestra password
        # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
        nuevo_usuario.set_password(password)
        # is superuser > indica que el usuario tiene la totalidad de privilegios para hacer lo que desee en el panel administrativo
        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)

    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    # char fields
    # 
    tipo_usuario = models.TextField(choices=[('ADMIN', 'ADMIN'), ('CLIENTE', 'CLIENTE')], db_column='tipo_usuario')

    # campos netamente de auth_user 
    # is_staff > sirve para indicar al panel administrativo que el usuario no pertenece al grupo de usuarios que pueden acceder
    is_staff = models.BooleanField(default=False)
     # is_staff > sirve para indicar que el usuario esta activo y por ende puede ingresar al panel administrativo
    is_active = models.BooleanField(default=True)

    # si queremos ingresar al panel administrstivo tenemos que indicar que columna usara para pedir el nombre de usuario
    USERNAME_FIELD = 'correo'

    # cuando querramos crear un superusuario por la terminal tendremos que indicar que atributos son los que nos debe de solicitar
    # El correo no va porque ya etsa definido en USERNAME_FIELD y si lo volvemos a poner nos dara un error y el password es ya solicitado de manera automatica
    REQUIRED_FIELDS = ['nombre', 'apellido']

    object = ManejoUsuario()
    class Meta:
        db_table = 'usuarios'