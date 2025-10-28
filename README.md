# Enunciado con respuestas. Se usan mis palabras.

### Apartado 1: Crear un chatbot que tenga las siguientes funcionalidades:

**Una interfaz, por ejemplo la interfaz de chatbot de Gradio.**
**Se han de ingestar varios documentos PDF largos para usarlos como base de conocimiento de un RAG. Se ha de usar una base de datos vectorial a elección. Se valorará positivamente,:**  
**Que alguno de los documentos contenga imágenes y éstas sean indexadas para poder preguntar por ellas.**  
**Que de alguno de los documentos se haga una extracción estructurada de su información (por ejemplo, un formulario con nombre, apellidos, fecha de nacimiento....). Esta extracción de información no tiene por qué guardarse en la base de datos vectorial.**  
**Se ha de implementar una memoria dinámica que mantenga la conversación y que cuando esta pase de X tokens se resuma de forma automática.**  
**La implementación ha de estar basada en LangChain/LangGraph.**  
**Si se detecta una pregunta que lo necesite el modelo ha de ser capaz de implementar y ejecutar código python.** 


Respuesta:
Se desarrolla un sistema basado en Gradio (chat), LangGraph (Orquestador), SQLiteVec (Base de datos vectorial) y Docling (Multimodal-OCR). Se ingesta un pdf de las páginas que sean a elección del usuario y se añade a la base de datos vectorial. Tras esto se inicialize un sencillo grafo en el que, en funcion de la entrada, te busca los vectores similares (se basa en la distancia por defecto de la librería empleada) y los devuelve. Esto se expone mediante GradioChat para que se pueda interactuar con el flujo diseñado en LangGraph. 
Con el hardware necesario, los siguientes pasos se resuelven añadiendo nodos al grafo para comprobar longitud de tokens del historial de chats y ejecutando una consulta LLM para resumirlo cuando se alcance el límite. Todo debe estar en contacto con una base de datos de baja latencia para ofrecer funcionalidades de cache y memoria a corto plazo. Para el nodo que ejecuta código python se podría emplear PythonREPL. 

La parte técnica ha quedado definida pero hay que darle la importancia que tiene a la parte de negocio. Con qué hay que integrar? 'prompt engineering'? validar flujos, comportamientos...?

![Esquema solución propuesta](/images/schema.png)

*Figura 1 – Esquema solución propuesta.*


![Esquema solución propuesta en Azure con más tiempo y recursos](/images/schema-prod.png)

*Figura 2 – Esquema solución propuesta en Azure con más tiempo y recursos*


### Apartado 2: Dar respuesta a los siguientes puntos de forma teórica, sin necesidad de desarrollarlos, que guardan relación con las tecnologías utilizadas en el primer apartado:

- **Diferencias entre 'completion' y 'chat' models** 

El modelo LLM es el mismo y se ha entrenado en tareas de 'completion'. Hablando de APIs, completion es respuesta sin mayor contexto que el prompt. 'chat' model implementa una capa de complejidad para mantener histórico de mensajes, es decir, contexto de conversación.

- **¿Qué diferencias hay entre un modelo de razonamiento y un modelo generalista?**

El modelo de razonamiento tiene la 'capacidad de pensar'. Esto se consigue empleando flujos de respuesta que ejecutan tantos prompts como esté definido hasta que se otorga la respuesta al usuario. 

- **¿Cómo forzar a que el chatbot responda 'si' o 'no'? ¿Cómo parsear la salida para que siga un formato determinado?** 

Se puede hacer mediante instrucciones de systema + guardarailes (nodos de flujo que comprueban si la respuesta cumple una o varias condiciones y actua en consecuencia, por ejemplo, montando otro prompt para consultar al llm o haciendo un replace)

- **RAG vs fine-tuning: ¿para qué sirve cada uno, y qué ventajas e inconvenientes tienen?**

Un RAG es una manera sencilla de hacer que un modelo tenga en cuenta información almacenada en una base de datos. El finetuning consiste en entrenar ciertas capas del LLM con datos etiquetados para conseguir un funcionamiento determinado. El primero es más sencillo y permite agregar a los prompt información de cualquier tipo. El segundo es muy caro y por experiencia tiene que ser una tarea muy específica y contar con datos suficientes (muchisimos), en general menos aconsejable.

- **¿Qué es un agente?**

PAra mi es lo mismo que se ha montado (o que se debería haber montado) en esta prueba. Es un sistema orquestado por un flujo que emplea LLMs y se integra con herramientas mediante APIs para dar respuesta a un problema/necesidad/oportunidad... 

- **¿Cómo evaluar el desempaño de un bot de Q&A? ¿Cómo evaluar el desempeño de un RAG? ¿Cómo evaluar el desempeño de una app de IA Generativa, en general: herramientas y métricas?**

Crear un set de prueba y lanzarlo con el sistema. Esto permite evaluar las respuestas contra un set conocido y la posibilidad de sacar métricas como Accuracy, F1 o Recall. 

El desempeño del RAG se mide primero desde un punto de vista técnico, viendo latencias principalmente. También hay que ver cómo afecta lo añadido al prompt desde el RAG a la respuesta dada por el sistema. 

Todo lo anterior aplica para una herramienta de IA Generativa. Para mi la evaluación más valiosa sería la de las personas que van a emplear el sistema compartiendo pequeños sets o publicando demos o MVPs para que se conozca y se controles expectativas. 
Las APIs se protegerían ante ataques como cualquier API. Las respuestas de los modelos (para evitar terminos malsonantes u ofensivos) se controlan con la propia herramienta de AI seafty que tiene Azure. Es importante también medir parte latencias, disponibilidad y demas temnas de infraestructura. Muy importante llevar una trazabilidad perfecta de id de usuario, prompt de entrada, respuesta, hora... Con esta información se puede mejorar el sistema y monitorear todo el comportamiento.


### Apartado 3 (Opcional): Servicio local para detección de objetos. El objetivo es disponer de un servicio que tenga como entrada una imagen y que como salida proporcione un JSON con detecciones de coches y personas. Se han de cumplir los siguientes puntos:

- **No hay necesidad de entrenar un modelo. Se pueden usar preentrenados.**
- **El servicio ha de estar conteinerizado. Es decir, una imagen docker que al arrancar exponga el servicio.**
- **La petición al servicio se puede hacer desde Postman o herramienta similar o desde código Python.**
- **La solución ha de estar implementada en Python.**

Respuesta: 
1. Ir a hugging face para buscar posibles modelos candidatos que hagan la tarea propuesta.
2. Implementar/buscar imagen docker base.
3. Seleccionar herramientas (en principio usario KServe para levantar api y exponer modelo).
4. Desarrollar el Dockerfile correspondiente (y YAML file para desplegar en Kubernetes si se tiene infra) iniciando el script y  exponiendo el servicio al exterior (abriendo puerto).
5. Levantarlo y lanzar requests hasta que funcione, que nunca es a la primera. Habría que iterar.


### Además, plantear cuales serían los pasos necesarios para entrenar un modelo de detección con categorías no existentes en los modelos preentrenados. Los puntos en los que centrar la explicación son:

**Pasos necesarios a seguir.**
**Descripción de posibles problemas que puedan surgir y medidas para reducir el riesgo.**
**Estimación de cantidad de datos necesarios así como de los resultados, métricas, esperadas.**
**Enumeración y pequeña descripción (2-3 frases) de técnicas que se pueden utilizar para mejorar el desempeño, las métricas del modelo en tiempo de entrenamiento y las métricas del modelo en tiempo de inferencia.**

Respuesta: 
1. Usar modelo preentrenado en detección de imagenes para hacer transfer learning. 
2. Tener un dataset con calidad suficiente (tamaño aceptable y calidad de imagenes buena).
3. Dependiendo del modelo se podría plantear cargar los pesos y lanzar unas epochs más o hacer finetuning de ciertas capas.
4. Desarrollar el Dockerfile correspondiente (y YAML file para desplegar en Kubernetes si se tiene infra) iniciando el script y  exponiendo el servicio al exterior (abriendo puerto).
5. En cuanto a medir desempeño, conozco algunas métricas más específicas de CV como IoU y mAP. Pero yo por desconocimiento en principio empezaría usando las clasicas (curva ROC hablando de detección, Accuracy, Precision, Recall...)