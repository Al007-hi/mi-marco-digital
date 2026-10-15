MI MARCO DIGITAL — PERSONALIZADO PARA IPAD MINI 2
Versión 1.0 · interfaz en español · diseñado para Safari/iOS antiguo

IMPORTANTE, SIN PROMESAS FALSAS
Este paquete es una aplicación web progresiva (PWA), no una app nativa firmada por Apple. Para instalarla como icono y que el navegador pueda guardar su interfaz para uso sin conexión, el primer acceso debe hacerse desde una dirección HTTPS válida (o en localhost). El servidor.py de este paquete sirve para pruebas en la red local, pero el HTTP por IP puede NO habilitar el modo instalable/offline en Safari. No borres datos de Safari ni reinstales la app sin respaldar tus fotos originales.

QUÉ HACE
- Importa múltiples imágenes desde Fotos/Archivos en iPad o desde el selector del ordenador.
- Guarda imágenes en IndexedDB local del navegador, no en una nube.
- Pase automático, 5/8/12/20/30/60 segundos, aleatorio, fundido o corte.
- Modo foto completa o llenar pantalla, reloj opcional, aspecto cálido/oscuro/claro.
- Interfaz adaptable a horizontal y vertical.

PRIMERA PRUEBA (red local; puede requerir el ordenador durante la prueba)
1. Extrae la carpeta completa.
2. En Windows, abre la carpeta y escribe cmd en la barra de dirección.
3. Ejecuta: python server.py
4. Abre en Safari del iPad la dirección impresa por el programa.
5. Prueba importar fotos y presentar. El navegador debe permanecer en la misma dirección para conservar los datos.

PARA EL USO REAL SIN ORDENADOR
La aplicación necesita servirse una vez desde HTTPS para que Safari permita instalarla en la pantalla de inicio y cachear sus archivos. Una vez instalada correctamente, el pase y las fotos guardadas son locales; no hace falta Internet para la presentación. Este paquete no incluye alojamiento HTTPS, certificado ni firma de aplicación nativa. El primer uso mediante HTTP local no garantiza el modo sin conexión en iOS 12.

PRIVACIDAD Y LÍMITES
Las fotos se guardan en el almacenamiento local de Safari/PWA en este dispositivo. No se suben a ningún servidor por el código de esta app. Si iOS limpia el almacenamiento, si se borra Safari o si el sistema se queda sin espacio, pueden perderse; conserva siempre los originales en Fotos/Archivos/ordenador. La pantalla puede bloquearse por los ajustes de Auto-bloqueo de iOS: configura Ajustes > Pantalla y brillo > Bloqueo automático, si la opción está disponible.
