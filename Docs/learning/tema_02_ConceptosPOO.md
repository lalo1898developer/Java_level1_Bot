*¿Qué es un objeto?*

Los lenguajes de programación estructurada como C y COBOL siguen un paradigma de programación muy diferente de los orientados a objetos. El paradigma de programación estructurada está altamente orientado a datos, lo cual significa que usted tiene estructuras de datos por una parte y luego instrucciones del programa que actúan sobre esos datos. Los lenguajes orientados a objetos, como el lenguaje Java, combinan datos e instrucciones del programa en objetos.

Un objeto es una entidad independiente que contiene atributos y comportamientos y nada más. En lugar de tener una estructura de datos con campos (atributos) y pasar esa estructura a toda la lógica del programa que actúa sobre ella (comportamiento), en un lenguaje orientado a objetos, se combinan los datos y la lógica del programa. Esta combinación puede ocurrir en niveles completamente diferentes de granularidad, desde objetos específicos como un Number hasta objetos de aplicación general como un servicio de FundsTransfer en una gran aplicación bancaria.


*Objetos padre e hijo*

Un objeto padre es aquel que sirve como la base estructural para derivar objetos hijos más complejos. Un objeto hijo se parece a su padre pero es más especializado. El paradigma orientado a objetos le permite reutilizar los atributos y comportamientos comunes del objeto padre y le agrega a sus objetos hijos atributos y comportamientos que difieren. (Usted aprenderá más sobre herencia en la siguiente sección de este tutorial).


*Comunicación y coordinación de objetos*

Los objetos se comunican con otros objetos por medio del envío de mensajes (llamadas de método en el lenguaje Java). Además, en una aplicación orientada a objetos, el código del programa coordina las actividades entre objetos para realizar tareas dentro del contexto del dominio de aplicación dado. (En el paradigma Modelo-Vista-Controlador, este código de programa de coordinación es el Controlador. Vea Recursos para aprender más acerca de MVC).


*El objeto* `Person`

Comenzaré con un ejemplo que está basado en escenario común de desarrollo de aplicación: se representa a un individuo con un objeto `Person`.

Volviendo a la definición de un objeto, usted sabe que un objeto tiene dos elementos primarios: atributos y comportamiento. Verá cómo estos se aplican al objeto Person.


*Atributos*

¿Qué atributos puede tener una persona? Algunos atributos comunes incluyen:

- Nombre
- Edad
- Altura
- Peso
- Color de ojos
- Género

Probablemente a usted se le pueden ocurrir más (y siempre puede agregar más atributos más tarde) pero esta lista es un buen comienzo


*Comportamiento*

Una persona real puede hacer todo tipo de actividades pero los comportamientos de los objetos normalmente se relacionan con algún tipo de contexto de aplicación. En un contexto de aplicación de negocio, por ejemplo, puede querer preguntarle a su objeto Person: «¿Qué edad tiene?» Como respuesta, Person le diría el valor de su atributo de Edad.

Una lógica más compleja podría estar oculta dentro del objeto Person pero por ahora suponga que esa Person tiene el comportamiento de responder estas preguntas:

- ¿Cuál es su nombre?
- ¿Qué edad tiene?
- ¿Cuál es su altura?
- ¿Cuánto pesa?
- ¿Cuál es su color de ojos?
- ¿Cuál es su género?


*Estado y cadena*

El _Estado_ es un concepto importante en OOP. El estado de un objeto se representa en cualquier momento por medio del valor de sus atributos.

En el caso de `Person`, su estado se define por sus atributos, tales como nombre, edad, altura y peso. Si usted quisiera presentar una lista de varios de esos atributos, podría hacerlo utilizando una clase de `String`, sobre la cual hablaré más en el tutorial posteriormente.

Juntos, los conceptos de estado y cadena le permiten decirle a Person: cuénteme quién es usted dándome un listado (o una `String`) de sus atributos.


*Video Resumen*
https://www.youtube.com/watch?v=-6BYa_x_QA0