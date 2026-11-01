from django.db import models
# Create your models here.


class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    fecha_creacion = models.DateField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.nombre_rol


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.nombre_categoria


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50, db_column='contraseña')
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_registro = models.DateField(null=True, blank=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='id_rol')

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    id_publicaciones = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')

    class Meta:
        db_table = 'publicaciones'

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    id_comentario = models.IntegerField(primary_key=True)
    contenido_comentario = models.TextField(null=True, blank=True)
    fecha_comentario = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        db_table = 'comentarios'

    def __str__(self):
        return f"Comentario {self.id_comentario} de {self.id_usuario}"


class Chat(models.Model):
    id_chats = models.IntegerField(primary_key=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')

    class Meta:
        db_table = 'chats'

    def __str__(self):
        return f"Chat {self.id_chats} - Publicación {self.id_publicacion}"


class Mensaje(models.Model):
    id_mensajes = models.IntegerField(primary_key=True)
    contenido_mensaje = models.TextField(null=True, blank=True)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, db_column='id_chat')

    class Meta:
        db_table = 'mensajes'

    def __str__(self):
        return f"Mensaje {self.id_mensajes} en Chat {self.id_chat}"
