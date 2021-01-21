*Encapsulamiento*

Recuerde que un objeto es, sobre todo, diferenciado o independiente. Este es el principio de encapsulamiento en funcionamiento. Ocultación es otro término que a veces se usa para expresar la naturaleza independiente y protegida de los objetos.

Sin tener en cuenta la terminología, lo que es importante es que el objeto mantiene un límite entre su estado y comportamiento y el mundo exterior. Como los objetos del mundo real, los objetos usados en la programación de computadora tienen diversos tipos de relaciones con diferentes categorías de objetos en las aplicaciones que los utilizan.

En la plataforma Java, puede usar especificadores de acceso (los que presentaré más adelante en el tutorial) para variar la naturaleza de las relaciones de los objetos desde lo público a lo privado. El acceso público tiene una gran apertura, mientras que el acceso privado significa que los atributos del objeto son accesibles solo dentro del objeto mismo.

El límite entre lo público y lo privado hace cumplir el principio orientado a objetos de encapsulamiento. En la plataforma Java, usted puede variar la fortaleza de ese límite sobre una base de objeto a objeto, al depender de un sistema de confianza. El encapsulamiento es una potente función del lenguaje Java.


*Herencia*

En la programación estructurada, es común copiar una estructura, darle un nombre nuevo y agregar o modificar los atributos que hacen que la nueva identidad (por ejemplo, un registro de Cuenta) sea diferente de su fuente original. Con el tiempo, este abordaje genera una gran cantidad de códigos duplicados, que pueden crear problemas de mantenimiento.

OOP presenta el concepto de herencia, por el cual los objetos especializados, — sin ningún código adicional, — pueden «copiar» los atributos y el comportamiento de los objetos de origen en los que se especializan. Si alguno de esos atributos o comportamientos necesitan modificarse, entonces simplemente modifíquelos temporalmente. Solo modifique lo que necesite modificar para crear objetos especializados. Como ya sabe desde la sección Lo que sigue, el objeto origen se llama el padre y la especialización nueva se llama el hijo.

*Herencia en funcionamiento*

Suponga que está escribiendo una aplicación de recursos humanos y quiere usar el objeto Person como base para un objeto nuevo llamado Employee. Al ser el hijo de Person, el Employee tendría todos los atributos de un objeto Person, junto con los adicionales, tales como:

Número de identificación del contribuyente
Fecha de contratación
Salario
La herencia hace que sea fácil crear la nueva clase de Employee del objeto sin necesidad de copiar manualmente todo el código de Person o mantenerlo.


*Polimorfismo*

El polimorfismo es un concepto más difícil de entender que el encapsulamiento o la herencia. Básicamente, significa que los objetos que pertenecen a la misma ramificación de una jerarquía, cuando se envía el mismo mensaje (es decir, cuando se le indica que realice lo mismo), pueden manifestar ese comportamiento de modo diferente.

Para entender cómo el polimorfismo se aplica a un contexto de aplicación de negocio, regrese al ejemplo de Person. ¿Recuerda indicarle a Person que formatee sus atributos en una String? El polimorfismo hace que sea posible para Person representar sus atributos en una variedad de formas, dependiendo del tipo de Person que sea.

El polimorfismo es uno de los conceptos más complejos con los que se encontrará en OOP en la plataforma Java y no dentro del ámbito de un tutorial introductorio. Vea Recursos si quiere aprender más acerca del polimorfismo.