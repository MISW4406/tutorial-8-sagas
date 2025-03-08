
class DatoProcesadoRegistrado():
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    tipo_processed_data = TipoCliente
    fecha_creacion = Long()

class DatoProcesadoValidado():
    id = String()
    fecha_validacion = Long()

class DatoProcesadoDesactivado():
    id = String()
    fecha_desactivacion = Long()