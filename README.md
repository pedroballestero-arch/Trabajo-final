
<h1 align="center">🍀PRESTAGO </h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/422a1acf-9822-4f8b-978d-02a41f4628c7" width="500">
</p>

---


## Licencia

## Integrantes

### Pedro Ballestero
- Soy una persona responsable y enfocada que siempre busca aprender cosas nuevas, por eso el paso por la programación me emociona mucho porque me va a ayudar a descubrir y desarrollar habilidades que antes no tenia

### Edwin Avila
- Soy una 

---

## Vínculos académicos y descripción

### 🍀Pedro Ballestero

**Programa:**
- Ingeniería Industrial

**Habilidades:**
- Comunicación asertiva  
- Adaptabilidad frente a cambios y nuevos retos  
- Aprendizaje rápido  
- Planificación de las tereas  

**Fortalezas:**
- Empático con los demás  
- Paciente  
- Responsable  
- Carismático  


### 🍀Edwin Avila

**Programa:**
- Ingeniería Industrial

**Habilidades:**
- Pensamiento analítico  
- Creatividad para enfrentar nuevos retos  
- Trabajo en equipo  
- Organización y planificación de tareas y de tiempo  
- Creatividad para proponer ideas y soluciones  

**Fortalezas:**
- Perseverancia para cumplir mir objetivos  
- Actitud positiva  
- Colaborador  
- Responsabilidad  

---

## 🍀Nombre del proyecto y detalles


PrestaGO es un programa de consola en Python diseñado para gestionar el préstamo de objetos personales de manera organizada y eficiente. Este sistema permitirá a MJ llevar un control claro de su inventario y de los artículos que presta, facilitando el seguimiento de cada préstamo y evitando pérdidas de información.

El sistema permite registrar usuarios, consultar la disponibilidad de ítems, crear y gestionar préstamos, registrar devoluciones, generar certificados y emitir facturas en caso de incumplimiento en los tiempos establecidos. Además, controla automáticamente las condiciones de préstamo y venta según las reglas definidas.

<p align="center">
  <img src="https://github.com/user-attachments/assets/422a1acf-9822-4f8b-978d-02a41f4628c7" width="500">
</p>

---

## Reporte de visión

El sistema Gestor de Préstamos (PrestaGo) es una solución tecnológica diseñada para optimizar la administración de préstamos de objetos personales de MJ, facilitando el control de inventario, usuarios y transacciones. Más que un simple registro, el software funciona como una herramienta integral que permite gestionar de manera organizada y automatizada los préstamos, devoluciones y ventas de artículos.

el sistema busca facilitar los registros de prestamos que hace MJ y asi tener un control e inventario de todo, ofreciendo un proceso claro, confiable y eficiente para el manejo de la información. Además, permite centralizar los datos en archivos planos, facilitando su consulta, almacenamiento y exportación.



Objetivos

- Ofrecer un sistema de registro y administración de usuarios, con validación de datos  
- Permitir el registro y control de ítems, incluyendo categoría, estado e identificación única  
- Gestionar los préstamos de objetos, asegurando control de fechas y disponibilidad  
- Automatizar el proceso de devoluciones, generando certificados correspondientes  
- Implementar la generación automática de ventas cuando se superen los tiempos establecidos  
- Proporcionar notificaciones y recordatorios para la recuperación de objetos  
- Permitir la consulta del estado general de los préstamos mediante estadísticas básicas  
- Garantizar una experiencia de usuario mediante una interfaz de consola clara, intuitiva y estructurada  



Beneficios

- Facilita el control de préstamos sin necesidad de llevar registros manuales  
- Reduce errores asociados a la pérdida de información o mala memoria  
- Mejora la organización y trazabilidad de los objetos prestados  
- Permite generar documentos como certificados y facturas automáticamente  
- Brinda acceso rápido a la información mediante almacenamiento en archivos planos  
- Permite obtener datos estadísticos sobre préstamos, devoluciones y ventas  
- Ofrece una solución adaptable a futuras mejoras, como interfaces gráficas o bases de datos  
- Garantiza disponibilidad inmediata de la información para consultas en tiempo real  

---

<h2 align="center">Requisitos PrestaGo</h2>

### Requisitos Funcionales

#### 1. Gestión de usuarios
- El sistema debe permitir registrar usuarios con:  
  - Nombre (mínimo 3 letras, sin números)  
  - Apellido (mínimo 3 letras, sin números)  
  - Documento (entre 3 y 15 dígitos, solo números)  
  - Correo electrónico válido (@ y .com)  
  - Tiempo de préstamo (solo 5, 10, 15 o 30 días)  

#### 2. Gestión de ítems
- El sistema debe permitir registrar ítems con:  
  - Nombre (mínimo 3 caracteres)  
  - Categoría (videojuegos, libros, música y video, herramientas, dinero, misceláneo)  
  - Precio de compra  
  - ID único alfanumérico basado en la categoría  
  - Estado del ítem usando lógica difusa  

#### 3. Gestión de préstamos
- Permitir registrar préstamos solo a usuarios existentes  
- Permitir seleccionar ítems por ID  
- Validar disponibilidad del ítem  
- Registrar fecha de préstamo  
- Mostrar mensaje si el usuario no existe  

#### 4. Gestión de devoluciones
- Permitir devolver solo préstamos activos  
- Validar si el usuario tiene préstamos  
- Generar certificado de devolución en archivo de texto  
- Incluir:  
  - Datos del usuario  
  - ID del ítem  
  - Fecha de devolución  

#### 5. Gestión de ventas
- Generar venta automática si el préstamo supera 30 días  
- Calcular:  
  - Subtotal  
  - Impuesto del 23%  
  - Total a pagar  
- Generar factura en archivo de texto o PDF

#### 6. Notificaciones
- Generar recordatorios después de 20 días  
- Notificar solicitud de devolución  

#### 7. Consultas
- Mostrar estado general de préstamos  
- Ordenar por cantidad de días  
- Leer información desde archivos planos  

#### 8. Administración
- Permitir acceso con usuario y contraseña  
- Mostrar:  
  - Total de préstamos  
  - Total de devoluciones  
  - Total de ventas  
  - Total pagado  
  - Lista de usuarios  
  - Usuario con más y menos préstamos  

---

### Requisitos No Funcionales

#### 1. Usabilidad
- Interfaz en consola clara y fácil de usar  
- Menú organizado  
- Mensajes de error comprensibles  

#### 2. Rendimiento
- El sistema debe responder rápidamente a las operaciones  
- Manejo eficiente de archivos planos  

#### 3. Seguridad
- Validación de usuario y contraseña en módulo administrador  
- Validación de datos ingresados (evitar errores o datos inválidos)  

#### 4. Fiabilidad
- El sistema debe evitar pérdida de información  
- Manejo de errores en entradas incorrectas  

#### 5. Persistencia
- Almacenamiento de datos en archivos planos  
- Exportación de datos a formato CSV  

---

## Plan proyecto

## Presupuesto

### Pedro Ballestero
- Inversión por semana (10 horas): $72.950  
- Inversión total del trabajo (16 semanas): $1.167.200  

### Edwin Ávila
- Inversión por semana (10 horas): $72.950  
- Inversión total del trabajo (16 semanas): $1.167.200  

### Inversión grupal
- Inversión por semana (20 horas): $145.900  
- Inversión total del trabajo (16 semanas): $2.334.400  


