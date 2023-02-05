
class UsuarioRegistrado():
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    tipo_cliente = TipoCliente
    fecha_creacion = Long()

class UsuarioValidado():
    id = String()
    fecha_validacion = Long()

class UsuarioDesactivado():
    id = String()
    fecha_desactivacion = Long()