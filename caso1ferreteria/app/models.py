# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleta(models.Model):
    id_boleta = models.IntegerField(primary_key=True)
    fecha_boleta = models.DateField()
    neto_boleta = models.IntegerField()
    iva_boleta = models.IntegerField()
    total_boleta = models.IntegerField()
    id_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_compra')
    rut_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='rut_cliente')
    id_medio = models.ForeignKey('MedioPago', models.DO_NOTHING, db_column='id_medio')

    class Meta:
        managed = False
        db_table = 'boleta'


class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    nombre_cargo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cliente(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    correo_cliente = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class CompraProveedor(models.Model):
    id_compra = models.IntegerField(primary_key=True)
    fecha_compra = models.DateField()
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'compra_proveedor'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=50)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class CostoEnvio(models.Model):
    id_costoenvio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'costo_envio'


class Despacho(models.Model):
    id_despacho = models.IntegerField(primary_key=True)
    id_detalle = models.ForeignKey('DetalleOrden', models.DO_NOTHING, db_column='id_detalle')
    id_estado = models.ForeignKey('EstadoDespacho', models.DO_NOTHING, db_column='id_estado')
    rut_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='rut_empleado')
    fecha_envio = models.DateField()
    fecha_recepcion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'despacho'


class DetalleOrden(models.Model):
    id_detalle = models.BigIntegerField(primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    id_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=100)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cliente')
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'direccion'


class Empleado(models.Model):
    rut_empleado = models.CharField(primary_key=True, max_length=10)
    nombres_empleado = models.CharField(max_length=50)
    apellidos_empleado = models.CharField(max_length=50)
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'empleado'


class Empresa(models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50)
    rut_empresa = models.CharField(max_length=10)
    id_tipo = models.ForeignKey('TipoEmpresa', models.DO_NOTHING, db_column='id_tipo')
    correo_empresa = models.CharField(max_length=50)
    rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class EstadoDespacho(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_despacho'


class EstadoRecepcion(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_recepcion'


class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    fecha_factura = models.DateField()
    neto_factura = models.IntegerField()
    iva_factura = models.IntegerField()
    total_factura = models.IntegerField()
    id_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_compra')
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    id_medio = models.ForeignKey('MedioPago', models.DO_NOTHING, db_column='id_medio')

    class Meta:
        managed = False
        db_table = 'factura'


class FamiliaProducto(models.Model):
    id_familia = models.IntegerField(primary_key=True)
    nombre_familia = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'familia_producto'


class MedioPago(models.Model):
    id_medio = models.IntegerField(primary_key=True)
    nombre_medio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'medio_pago'


class OrdenCompra(models.Model):
    id_compra = models.BigIntegerField(primary_key=True)
    fecha_orden = models.DateField()
    descuento = models.IntegerField(blank=True, null=True)
    rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_empleado', blank=True, null=True)
    id_tipocom = models.ForeignKey('TipoCompra', models.DO_NOTHING, db_column='id_tipocom')
    id_costoenvio = models.ForeignKey(CostoEnvio, models.DO_NOTHING, db_column='id_costoenvio')

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_familia = models.ForeignKey(FamiliaProducto, models.DO_NOTHING, db_column='id_familia')
    fecha_vencimiento = models.DateField(blank=True, null=True)
    id_tipo = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo')
    descripcion = models.CharField(max_length=100)
    precio_clp = models.IntegerField()
    precio_usd = models.IntegerField()
    stock = models.IntegerField()
    foto = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoProveedor(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    id_compra = models.ForeignKey(CompraProveedor, models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'producto_proveedor'


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=50)
    rut_proveedor = models.CharField(max_length=10)
    celular = models.BigIntegerField()
    correo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class RecepcionProducto(models.Model):
    id_recepcion = models.IntegerField(primary_key=True)
    id_estado = models.ForeignKey(EstadoRecepcion, models.DO_NOTHING, db_column='id_estado')
    rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_empleado')
    id_compra = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'recepcion_producto'


class Region(models.Model):
    id_region = models.CharField(primary_key=True, max_length=4)
    nombre_region = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'region'


class ResumenProductos(models.Model):
    id_respro = models.IntegerField(primary_key=True)
    mes_anno = models.IntegerField()
    id_producto = models.BigIntegerField()
    nombre_producto = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50)
    familia_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resumen_productos'


class Rubro(models.Model):
    id_rubro = models.IntegerField(primary_key=True)
    nombre_rubro = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rubro'


class RubroProveedor(models.Model):
    id_proveedor = models.OneToOneField(Proveedor, models.DO_NOTHING, db_column='id_proveedor', primary_key=True)
    id_rubro = models.ForeignKey(Rubro, models.DO_NOTHING, db_column='id_rubro')

    class Meta:
        managed = False
        db_table = 'rubro_proveedor'
        unique_together = (('id_proveedor', 'id_rubro'),)


class TipoCompra(models.Model):
    id_tipocom = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_compra'


class TipoEmpresa(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre_tipo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_empresa'


class TipoProducto(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre_tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoUsuario(models.Model):
    id_tipousu = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=64)
    id_tipousu = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipousu')

    class Meta:
        managed = False
        db_table = 'usuario'
