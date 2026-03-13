<h1>📌 Calculadora de Ahorro Programado 
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" width="60px">
</h1>

---
###  Creadores
- María Paula Ospina Zabala
- Alejandro Tello Giraldo
  
 --- 
 ### 👩‍💻 Persona entrevistada
- **Nombre:** Karen Londoño 
- **Cargo:** Gerente de proyectos en una compañía financiera
- **Experiencia relacionada:** Finanzas
- **Fecha de la entrevista:** 08/02/2026

---

### 📖 Descripción del Proyecto
La **Calculadora de Ahorro Programado** es una aplicación diseñada para ayudar a las personas a planificar su ahorro mensual con el fin de alcanzar una meta financiera específica en un periodo de tiempo determinado.
La aplicación permite calcular el valor que se debe ahorrar mensualmente y, además, ofrece la posibilidad de registrar **abonos extra** en cualquier momento y por cualquier cantidad, ajustando el ahorro restante de forma automática.

---
### 🎯 Objetivo
Esta herramienta busca facilitar al usuario una ayuda para alcanzar su meta de ahorro de una manera sencilla, además de brindarle una planificación financiera personal que permita:
-  Definir una meta de ahorro.
-  Establecer un plazo en meses.
-  Calcular el ahorro mensual necesario.
-  Registrar abonos adicionales.
-  Visualizar el progreso del ahorro.
  
---
## ▶️ Funcionamiento

### Prerrequisitos
Antes de ejecutar el proyecto, asegúrese de contar con lo siguiente:
- Tener instalado **Python 3** en su equipo.
- Tener descargado o clonado este repositorio en su computador.

### Ejecución
Ubicado en la carpeta raíz del proyecto (`SUPER-PROYECTO`), ejecute el 
siguiente comando en la terminal o CMD:
```
python src\view\interfaz_consola.py
```

> 💡 En sistemas **Mac** o **Linux**:
> ```
> python3 src/view/interfaz_consola.py
> ```

### Ejecución de pruebas
Para verificar que el programa funciona correctamente, ejecute el siguiente 
comando desde la carpeta raíz del proyecto:
```
/python test/test_ahorro.py
```

> 💡 En sistemas **Mac** o **Linux**:
> ```
>/python test/test_ahorro.py
> ```

> ⚠️ Si no tiene instalado `pytest`, puede instalarlo ejecutando:
> ```
> pip install pytest
> ```

---
## 📥 Entradas del Sistema
El usuario debe ingresar:
- **Meta de ahorro (Meta)**  
- **Tasa de interés mensual (i)**  
- **Plazo en meses (n)**  
- **Abonos extra (opcional y siempre en la última cuota)**
- **Valor del abono**

## ⚙️ Proceso del Sistema
La aplicación utiliza la fórmula financiera de ahorro programado:
**Cuota = Meta × [ i / ((1 + i)^n − 1) ]**
Donde:
- **Meta** = Valor objetivo a alcanzar  
- **i** = Tasa de interés mensual  
- **n** = Número de meses  
- **Cuota** = Valor que debe ahorrarse mensualmente  

❗ **Caso especial:** Si la tasa es 0%, se usa: **Cuota = Meta / n** ❗

## Fórmula de cálculo de cuota

**Cuota mensual (sin abono):**
```
C = meta × (r / ((1 + r)^n - 1))
```

**Cuota mensual (con abono extra):**
```
C = (meta - abono) × (r / ((1 + r)^n - 1))
```

**Donde:**
- `r` = tasa de interés mensual
- `n` = plazo en meses
- `abono` = monto del abono extra (reduce la meta directamente)

**Total de intereses ganados (sin abono):**
```
TI = meta - C × n
```

**Total de intereses ganados (con abono):**
```
TI = (meta - abono) - C × n
```

### Funcionamiento:
1. **Validación:** Se verifican que meta, plazo y tasa sean válidos.
2. **Cálculo inicial:** Se determina la cuota mensual con base en la fórmula.
3. **Simulación mes a mes:** Se proyecta el crecimiento del ahorro aplicando los intereses.
4. **Abonos extras (opcional):**
   - Se suman al capital acumulado en el mes indicado.
   - Empiezan a generar intereses inmediatamente.
   - Se recalcula la cuota para los meses restantes.
5. **Resultado final:** Se muestra la cuota mensual, total de intereses y total ahorrado.

---
## 📤 Salidas del Sistema
El sistema mostrará:
-  **Cuota mensual:** Valor que debe ahorrarse cada mes para alcanzar la meta.
-  **Total de intereses:** Dinero adicional generado durante el periodo de ahorro.
-  **Total ahorrado:** Suma de la meta más los intereses ganados.
-  **Nuevo plan tras abonos:** Si se realizan abonos extras, muestra la cuota recalculada.
-  **Confirmación de meta:** Mensaje cuando la meta sea alcanzada.

### Mensajes de Error
En caso de datos inválidos, el sistema indica qué dato causó el problema y cómo corregirlo:

- ❌ `MetaInvalida`: "ERROR: La meta debe ser mayor que cero. Se recibió meta={valor}. Ingrese un valor positivo."
- ❌ `PlazoInvalido`: "ERROR: El plazo no puede ser cero. Se recibió plazo={valor}. Ingrese un plazo de al menos 1 mes."
- ❌ `PlazoInvalido`: "ERROR: El plazo no puede ser negativo. Se recibió plazo={valor}. Ingrese un plazo de al menos 1 mes."
- ❌ `InteresInvalido`: "ERROR: La tasa de interés no puede ser negativa. Se recibió interes={valor}. Ingrese una tasa mayor o igual a cero."
- ❌ `MesAbonoInvalido`: "ERROR: El mes del abono no es válido. Se recibió mes_abono={valor} con plazo={valor}. El mes debe estar entre 1 y {plazo}."

---

### Descripción carpetas
- **`src/model/`** — Contiene la lógica del sistema. En esta carpeta se 
  encuentra el archivo `logica_ahorro.py`, responsable de ejecutar todos los 
  cálculos financieros del programa: la cuota mensual, los intereses generados 
  y el recálculo del plan ante la presencia de abonos extraordinarios.

- **`src/view/`** — Contiene la presentación del sistema. El archivo 
  `interfaz_consola.py` gestiona la comunicación entre el programa y el usuario, 
  mostrando los mensajes en pantalla, solicitando los datos de entrada y 
  presentando los resultados obtenidos.

- **`test/`** — Contiene las pruebas de validación del sistema. El archivo 
  `test_ahorro.py` agrupa un conjunto de pruebas automatizadas que verifican 
  el correcto funcionamiento de la lógica del programa frente a distintos 
  escenarios de uso.


---
