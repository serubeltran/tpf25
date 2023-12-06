# Documentación Trabajo Final Python - Django - MySQL
## Nombre del Proyecto:
### `Tienda 25`
## Nombre del equipo: 
`Grupo Nº 25`

## Integrantes:
- `Marian de los Angeles Chirinos Noguera.`
- `Elvio Villegas.`
- `Sergio Beltran.`
- `Tamara Chaizaz Valenzuela.`

## Estructura del Proyecto
```
TPF25
├──  mitienda
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── nosotros.html
│   │   ├── plantilla.html
│   │   ├── principal.html
│   │   ├── productos.html
│   │   └── productoModificar.html
│   ├── urls.py
│   └── views.py
├── manage.py
│   
└── tpCrud
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── views.py
    └── wsgi.py
```
## Documentación de las URLs de Django

El archivo `url.py` define las URLs de la aplicación utilizando el framework Django.

## Configuración

Asegúrate de tener Django instalado antes de ejecutar la aplicación:

```bash
pip install django
```
## Estructura de Archivos
- `urls.py`: Archivo que define las URL de la aplicación.
- `views.py`: Archivo que contiene las funciones de vista asociadas a cada URL.
# URLs
## Administrador Django
- Ruta: `/admin/`
- Descripción: Acceso al panel de administración de Django.
- Método de Vista: Django Admin Site
- Nombre: `admin`
## Página Principal
- Ruta: `/ `
- Descripción: Página principal de la aplicación.
- Método de Vista: views.principal
- Nombre: `principal`
## Página de Productos
- Ruta: `/productos`
- Descripción: Página que muestra la lista de productos.
- Método de Vista: views.productos
- Nombre: `productos`
## Guardar Producto
- Ruta: `/productos/guardar`
- Descripción: Guarda un nuevo producto.
- Método de Vista: views.guardar
- Nombre: `guardar`
## Eliminar Producto
- Ruta: `/productos/eliminar/<int:id>`
- Descripción: Elimina un producto específico.
- Método de Vista: views.eliminar
- Nombre: `eliminar`
## Modificar Producto
- Ruta: `/productos/modificar/<int:id>`
- Descripción: Muestra el formulario para modificar un producto.
- Método de Vista: views.modificar
- Nombre: `modificar`
## Editar Producto
- Ruta: `/productos/editar`
- Descripción: Guarda las modificaciones de un producto.
- Método de Vista: views.editar
- Nombre: `editar`
## Nosotros
- Ruta: `/nosotros`
- Descripción: Página que muestra información sobre nosotros.
- Método de Vista: views.nosotros
- Nombre: `nosotros`


# Documentación del Modelo Django

El archivo `models.py` define el modelo de datos para la aplicación utilizando el framework Django.

## Modelo: Producto

### Atributos

- `id` (AutoField): Identificador único del producto (clave primaria).
- `nombre` (CharField): Nombre del producto con una longitud máxima de 30 caracteres.
- `descripcion` (TextField): Descripción detallada del producto con una longitud máxima de 100 caracteres.
- `precio` (DecimalField): Precio del producto con un máximo de 9 dígitos y 2 decimales.

### Métodos

#### `__str__(self) -> str`
Devuelve una representación de cadena del objeto Producto.

```python
def __str__(self):
    return f"Producto: {self.nombre} - Descripción: {self.descripcion}"
```
### Uso del Modelo
El modelo `Producto` se utiliza para representar los productos en la base de datos.

# Documentación de las Vistas Django

El archivo `views.py` define las vistas de la aplicación utilizando el framework Django.

## Funciones de Vista

### `principal(request) -> HttpResponse`
- Descripción: Muestra la página principal de la aplicación.
- Método HTTP: GET
- Plantilla: `principal.html`

### `productos(request) -> HttpResponse`
- Descripción: Muestra la lista de productos almacenados en la base de datos.
- Método HTTP: GET
- Plantilla: `productos.html`
- Contexto: `{'productos': productos}`

### `guardar(request) -> HttpResponse`
- Descripción: Guarda un nuevo producto en la base de datos.
- Método HTTP: POST
- Redirección: A la vista de productos
- Mensaje de éxito: "Producto agregado"

### `eliminar(request, id) -> HttpResponse`
- Descripción: Elimina un producto específico de la base de datos.
- Método HTTP: GET (o POST)
- Redirección: A la vista de productos
- Mensaje de éxito: "Producto eliminado"

### `modificar(request, id) -> HttpResponse`
- Descripción: Muestra la página para modificar un producto específico.
- Método HTTP: GET
- Plantilla: `productoModificar.html`
- Contexto: `{'producto': producto}`

### `editar(request) -> HttpResponse`
- Descripción: Guarda las modificaciones de un producto en la base de datos.
- Método HTTP: POST
- Redirección: A la vista de productos
- Mensaje de éxito: "Producto actualizado"

### `nosotros(request) -> HttpResponse`
- Descripción: Muestra la página "Nosotros" de la aplicación.
- Método HTTP: GET
- Plantilla: `nosotros.html`


