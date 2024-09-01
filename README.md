# Roll App
Una aplicación simple creada en Python con utilidades para ayudar en TTRPGs.

La aplicación se divide en 3 categorías (Accesibles moviendo el ratón a la izquierda de la App):
  - Any System: Son funciones útiles para cualquier partida
    - Nombre Aleatorio: Genera un Nombre aleatorio siguiendo las reglas de “Mythic game master Emulator”
    - Lugar Aleatorio: Crea un nombre y una descripción usando una mezcla entre las reglas de “Mythic” y “The Perilous Wilds”
    - Personaje Aleatorio: Crea un Nombre, Apariencia, Personalidad y Descripción para un NPC. Basado en las reglas de “Mythic”
    - Distancia / Peso: Son un par de Conversores de Feet+Inches / Metros y Pound+Ounces / Kilogramos
    - Volumen / Temperatura: Conversor de Cantidad de Líquido (Galón / Litros) y Conversor de Temperatura (Fahrenheit / Celsius)
    - Tiempo de Guardía: Calcula el total de tiempo necesario para permitir la Horas de Sueño indicadas a cada personaje
  - SWADE: Son funciones útiles al jugar a Savage World Adventurer edition
    - Probabilidad de Dado Swade: Devuelve la probabilidad de llegar a X valor usando un par de dados “Explosivos”
    - Atributo como Dado Salvage: Esta herramienta está pensada para modificar automáticamente una ficha de Foundry VTT del sistema SWADE cambiando el Dado salvaje de cada        Habilidad por la de su Atributo correspondiente.
    - Poner habilidades Base: Esta herramienta está pensada para modificar automáticamente una ficha de Foundry VTT del sistema SWADE añadiendo la lista de habilidades            básicas, tanto a NPC como a PJ, para facilitar su creación. Incluye una opción para Cambiar el Dado Salvaje como en la Herramienta Anterior
    - Aumentos por Rango: Esta utilidad está diseñada para modificar el sistema SWADE para Foundry VTT en el ordenador que ejecuta la app. Cambiado el Número de Aumentos          necesarios para cambiar de Rango (Se puede indicar 0 para volver al valor por defecto de SWADE)
  - D&D: Son funciones útiles al jugar a D&D 5e (Y juegos similares)
    - Puntos de Vida: Indica la Cantidad de Puntos de Vida máximos que debe tener un Personaje. Se pueden elegir varias clases, Modificadores que afecten por nivel (Tanto         de personaje como de Clase), modificadores estáticos. Y elegir valor que se toma para el Hit Dice
    - Velocidades: Muestra una tabla con velocidades comunes y permite indicar una velocidad para hacer la convención entre Viajes de Larga Distancia y Combates Tacticos.

Se ha utilizado una versión reducida de las tablas propias de los sistemas “Mythic game master Emulator” y “The Perilous Wilds” para evitar problemas de Copyright, por lo que no hay mucha variedad de resultados.
Esas tablas se encuentran el el fichero “configuracion.py” para mas posibilidades, ya sea añadiendo las restantes del sistema u otras propias.
