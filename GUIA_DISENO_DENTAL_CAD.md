# Guía completa de diseño dental digital (CAD) para trabajar desde casa

### Curso paso a paso para empezar desde cero: coronas, puentes, férulas de descarga, modelos y más

---

> **Bienvenida a clase.**
>
> Soy tu profesora de diseño dental digital. En esta guía vamos a hacer lo mismo que hago con mis alumnas y alumnos en la universidad: empezar por lo básico, entender *por qué* se hace cada cosa y luego practicar mucho, siempre paso a paso.
>
> Una advertencia desde el primer día: **el programa es la parte fácil**. Lo difícil (y lo que hará que te paguen) es saber de dientes: anatomía, oclusión y materiales. Un botón lo aprende cualquiera en una tarde. Ver que una corona está mal hecha lleva meses de práctica. Por eso esta guía mezcla las dos cosas.
>
> Lee la guía entera una vez, sin prisa, para tener el mapa completo. Después vuelve al principio y ve módulo a módulo haciendo los ejercicios.

---

## Índice

0. [Cómo usar esta guía](#0-cómo-usar-esta-guía)
1. [¿En qué consiste este trabajo?](#1-en-qué-consiste-este-trabajo)
2. [Antes de empezar: titulación, ley y protección de datos (España)](#2-antes-de-empezar-titulación-ley-y-protección-de-datos-españa)
3. [Tu puesto de trabajo en casa: el ordenador](#3-tu-puesto-de-trabajo-en-casa-el-ordenador)
4. [Qué programas aprender (y en qué orden)](#4-qué-programas-aprender-y-en-qué-orden)
5. [Fundamentos dentales que DEBES dominar](#5-fundamentos-dentales-que-debes-dominar)
6. [Fundamentos de 3D: mallas, archivos STL y navegación](#6-fundamentos-de-3d-mallas-archivos-stl-y-navegación)
7. [Primeras prácticas gratis (Meshmixer y Blue Sky Plan)](#7-primeras-prácticas-gratis-meshmixer-y-blue-sky-plan)
8. [exocad: la lógica general de cualquier diseño](#8-exocad-la-lógica-general-de-cualquier-diseño)
9. [Módulo 1 — Corona unitaria paso a paso](#9-módulo-1--corona-unitaria-paso-a-paso)
10. [Módulo 2 — Puentes](#10-módulo-2--puentes)
11. [Módulo 3 — Coronas sobre implantes](#11-módulo-3--coronas-sobre-implantes)
12. [Módulo 4 — Incrustaciones y carillas](#12-módulo-4--incrustaciones-y-carillas)
13. [Módulo 5 — Férula de descarga paso a paso](#13-módulo-5--férula-de-descarga-paso-a-paso)
14. [Módulo 6 — Modelos para imprimir paso a paso](#14-módulo-6--modelos-para-imprimir-paso-a-paso)
15. [Módulo 7 — Encerado diagnóstico, mock-up y provisionales](#15-módulo-7--encerado-diagnóstico-mock-up-y-provisionales)
16. [Módulo 8 — Otros trabajos (visión general)](#16-módulo-8--otros-trabajos-visión-general)
17. [Control de calidad: la lista que revisarás SIEMPRE](#17-control-de-calidad-la-lista-que-revisarás-siempre)
18. [Errores típicos de principiante y cómo arreglarlos](#18-errores-típicos-de-principiante-y-cómo-arreglarlos)
19. [Exportar y entregar un trabajo como una profesional](#19-exportar-y-entregar-un-trabajo-como-una-profesional)
20. [Plan de estudio de 16 semanas](#20-plan-de-estudio-de-16-semanas)
21. [Cómo conseguir clientes y trabajar desde casa](#21-cómo-conseguir-clientes-y-trabajar-desde-casa)
22. [Recursos para seguir aprendiendo](#22-recursos-para-seguir-aprendiendo)
23. [Glosario](#23-glosario)
24. [Chuleta de valores de referencia](#24-chuleta-de-valores-de-referencia)
25. [Autoevaluación final](#25-autoevaluación-final)

---

## 0. Cómo usar esta guía

**Mi método de clase tiene 3 reglas:**

1. **Primero entender, luego hacer.** Antes de cada módulo hay una parte de teoría corta. No te la saltes.
2. **Repetición.** Una corona no se aprende haciendo una; se aprende haciendo cincuenta. Te pondré cantidades mínimas de práctica.
3. **Compararte con la realidad.** Ten siempre abierta una foto o un modelo de un diente natural del mismo tipo que estás diseñando. Tu diseño tiene que parecerse a un diente de verdad, no a un "caramelo".

**Cuaderno de diseño:** abre una libreta (o un documento) y apunta en cada práctica:
- qué diseñaste (diente, material, tipo de trabajo),
- cuánto tardaste,
- qué te salió mal y cómo lo arreglaste.

En 2–3 meses verás tu progreso con números, y eso motiva muchísimo.

**Nota importante sobre los valores numéricos:** todos los grosores, espacios y medidas que te doy son **valores orientativos habituales** para que entiendas los órdenes de magnitud. En el trabajo real **manda siempre**:
1. la ficha técnica del fabricante del material,
2. el protocolo del laboratorio o clínica que te encarga el trabajo,
3. la calibración de su fresadora o impresora.

---

## 1. ¿En qué consiste este trabajo?

### 1.1 El flujo digital completo

Hoy en día muchísimas prótesis dentales ya no se modelan en cera: se **escanean**, se **diseñan en el ordenador** y se **fabrican con máquinas** (fresadora o impresora 3D). Tú vas a ser la pieza del medio: **la diseñadora**.

```
   CLÍNICA                         TÚ (desde casa)                  LABORATORIO
┌──────────────┐   archivos    ┌──────────────────┐   archivos   ┌──────────────────┐
│ Escáner      │  STL / PLY    │  Programa CAD     │   STL final  │ Fresadora o       │
│ intraoral o  │ ───────────►  │  (exocad, 3Shape, │ ──────────►  │ impresora 3D      │
│ de modelos   │  + ficha del  │   etc.)           │              │  (CAM)            │
│ + ficha      │   trabajo     │  Diseñas la pieza │              │ Sinterizado,      │
└──────────────┘               └──────────────────┘              │ maquillaje, etc.  │
                                                                  └────────┬─────────┘
                                                                           │
                                                   El dentista coloca la pieza al paciente
```

- **CAD** = *Computer Aided Design*, diseño asistido por ordenador → **esto es lo tuyo**.
- **CAM** = *Computer Aided Manufacturing*, fabricación asistida → lo hace el laboratorio con la máquina.

### 1.2 ¿Qué trabajos puedes diseñar?

| Trabajo | Dificultad para empezar | Demanda |
|---|---|---|
| Modelos para imprimir (a partir de escaneo intraoral) | ⭐ Fácil | Muy alta |
| Férulas de descarga / protectores nocturnos | ⭐⭐ Fácil-media | Alta |
| Coronas unitarias (dientes posteriores) | ⭐⭐ Media | Muy alta |
| Coronas anteriores (estética) | ⭐⭐⭐ Media-alta | Alta |
| Puentes | ⭐⭐⭐ Media-alta | Alta |
| Coronas sobre implantes, pilares personalizados | ⭐⭐⭐ Media-alta | Alta |
| Incrustaciones (inlays/onlays) y carillas | ⭐⭐⭐ Media-alta | Media |
| Encerados diagnósticos (wax-up) y diseño de sonrisa | ⭐⭐⭐ Media-alta | Media |
| Prótesis completas digitales | ⭐⭐⭐⭐ Alta | Creciente |
| Esqueléticos (prótesis parcial removible metálica) | ⭐⭐⭐⭐ Alta | Media |
| Guías quirúrgicas de implantes | ⭐⭐⭐⭐ Alta (mucha responsabilidad) | Media |
| Alineadores / setups de ortodoncia | ⭐⭐⭐⭐ Alta | Alta |

**Mi recomendación de orden:** Modelos → Férulas → Coronas posteriores → Coronas anteriores → Puentes → Implantes → el resto.
Así empiezas a poder cobrar pronto (modelos y férulas) mientras aprendes lo más difícil.

### 1.3 Qué te van a pedir los clientes

Un laboratorio o clínica que contrata a una diseñadora externa quiere:
1. **Calidad constante** (que no tengan que retocar tu diseño).
2. **Rapidez** (muchos piden entregas en 24 h o el mismo día).
3. **Comunicación clara** (si algo del escaneo está mal, avisar antes de diseñar).
4. **Que respetes su protocolo** (sus parámetros, sus materiales, su forma de nombrar archivos).

---

## 2. Antes de empezar: titulación, ley y protección de datos (España)

> Esto no es asesoría legal (yo te enseño diseño, no derecho), pero es imprescindible que lo conozcas para no llevarte sustos.

### 2.1 Las prótesis dentales son "productos sanitarios a medida"

En la UE (Reglamento de Productos Sanitarios 2017/745) y en España (Real Decreto 192/2023), una corona o una férula hecha para un paciente concreto es un **producto sanitario a medida**. El **fabricante** (el laboratorio) necesita una **licencia sanitaria** de su comunidad autónoma y un **responsable técnico con titulación**.

**¿Qué significa para ti?**
- Lo más habitual y seguro es trabajar **como diseñadora externa (subcontratada) para laboratorios con licencia**. El laboratorio es el fabricante y el responsable legal del producto; tú le entregas el diseño y él lo revisa, fabrica y firma.
- Lo que **no** debes hacer es vender prótesis terminadas directamente a pacientes o a clínicas sin tener la estructura legal de laboratorio.
- **Consulta** al Colegio de Protésicos Dentales de tu comunidad autónoma sobre tu caso concreto.

### 2.2 La titulación que te abre puertas

- **Técnico Superior en Prótesis Dentales** (FP de Grado Superior, 2 cursos). Existe en modalidad presencial y a distancia en muchas comunidades. Con este título puedes ser responsable técnico de un laboratorio y los clientes confían mucho más en ti.
- No es obligatorio para aprender a diseñar ni para empezar como diseñadora subcontratada, pero **te lo recomiendo muchísimo a medio plazo**. Puedes estudiarlo a la vez que practicas con esta guía.
- Además, hay **cursos específicos de exocad y 3Shape** (oficiales y de distribuidores) que dan certificado.

### 2.3 Protección de datos (RGPD)

Los escaneos dentales son **datos de salud** (categoría especial). Reglas de oro:
- Pide a tus clientes que te envíen los casos **sin nombre del paciente** (con un código: `LAB-2026-0153`).
- No guardes archivos en servicios gratuitos poco seguros ni los compartas por WhatsApp.
- Borra los casos cuando ya no los necesites (acuerda el plazo con el laboratorio).
- Firma con cada cliente un **contrato de encargado del tratamiento** (el laboratorio suele tener el modelo).
- Ten el ordenador con contraseña y el disco cifrado (BitLocker en Windows).

---

## 3. Tu puesto de trabajo en casa: el ordenador

### 3.1 Requisitos del ordenador

Los programas profesionales (exocad y 3Shape) funcionan **en Windows**. **No compres un Mac** para esto: no funcionan de forma nativa. Si ya tienes un Mac, puedes empezar a practicar con programas gratuitos que sí tienen versión para Mac (como Blue Sky Plan), pero para trabajar necesitarás un PC con Windows.

| Componente | Mínimo para aprender | Recomendado para trabajar |
|---|---|---|
| Sistema | Windows 10/11 64 bits | Windows 11 64 bits |
| Procesador | Intel i5 / AMD Ryzen 5 recientes | Intel i7 / AMD Ryzen 7 o superior |
| Memoria RAM | 16 GB | 32 GB |
| Tarjeta gráfica | NVIDIA dedicada con 4 GB | NVIDIA RTX con 8 GB o más |
| Disco | SSD 512 GB | SSD NVMe 1 TB + copia de seguridad externa |
| Pantalla | 24" Full HD | 27" QHD, o dos monitores |
| Internet | Fibra estable | Fibra estable (los casos van y vienen por la nube) |

> Antes de comprar, consulta los **requisitos oficiales actualizados** del programa que vayas a usar (exocad y 3Shape los publican en su web); cambian con cada versión y algunos programas exigen tarjetas gráficas concretas.

### 3.2 Periféricos

- **Ratón de 3 botones con rueda** (imprescindible). Todo el diseño 3D se hace girando, desplazando y haciendo zoom.
- **Ratón 3D (tipo SpaceMouse)**: opcional, cuando ya tengas soltura. Muchas diseñadoras rápidas lo usan con la mano izquierda para girar el modelo mientras con la derecha modelan.
- **Tableta gráfica**: opcional; a algunas personas les gusta para esculpir.
- **Silla buena y pantalla a la altura de los ojos.** Vas a pasar muchas horas; tu espalda también es tu herramienta de trabajo.

### 3.3 Organización de carpetas (desde el primer día)

```
📁 DISEÑO_DENTAL
 ├── 📁 01_PRACTICAS          ← tus ejercicios de aprendizaje
 ├── 📁 02_CLIENTES
 │     ├── 📁 LabSonrisa
 │     │     ├── 📁 2026-10-05_LS-0153_corona_36
 │     │     │      ├── 📁 recibido
 │     │     │      └── 📁 entregado
 │     └── 📁 ClinicaNorte
 ├── 📁 03_BIBLIOTECAS         ← librerías de dientes, implantes, etc.
 ├── 📁 04_PORTFOLIO           ← capturas de tus mejores trabajos (anónimos)
 └── 📁 05_ADMINISTRACION      ← facturas, contratos
```

---

## 4. Qué programas aprender (y en qué orden)

### 4.1 El mapa de programas

| Programa | Para qué sirve | Precio aproximado | ¿Lo recomiendo? |
|---|---|---|---|
| **exocad DentalCAD** | El más usado en laboratorios. Coronas, puentes, implantes, férulas, modelos, prótesis completa… (por módulos) | De pago (licencia o suscripción, varios miles de €). Se compra a un distribuidor | ⭐⭐⭐⭐⭐ **Tu programa principal** |
| **3Shape Dental System** | El otro gran estándar de laboratorio | De pago, alto | ⭐⭐⭐⭐ Segundo programa, si tus clientes lo usan |
| **Blue Sky Plan** | Modelos, férulas, guías quirúrgicas, prótesis completas, ortodoncia | **Gratis para diseñar**, pagas una pequeña cantidad por cada exportación | ⭐⭐⭐⭐ **Ideal para practicar gratis** |
| **Autodesk Meshmixer** | Editar y reparar mallas 3D, bases de modelos sencillas | **Gratis** (ya no se actualiza, pero sigue funcionando) | ⭐⭐⭐⭐ Para aprender 3D básico |
| **Blender** (+ complementos dentales) | Modelado 3D general; hay complementos dentales gratuitos | **Gratis** | ⭐⭐⭐ Opcional, curva de aprendizaje alta |
| **Apps de Medit** (Medit Link) | Modelos, férulas y otras apps; algunas gratuitas con cuenta | Algunas gratis, otras de pago | ⭐⭐⭐ Útil si tus clientes usan escáner Medit |
| Software de impresión (PreForm, Chitubox, Asiga Composer…) | Preparar la impresión (orientar, soportes) | Normalmente gratis | ⭐⭐ Solo si vas a preparar impresiones |

### 4.2 Mi recomendación concreta

1. **Semanas 1–4:** Meshmixer (gratis) para perderle el miedo al 3D + Blue Sky Plan (gratis) para tus primeros modelos y férulas.
2. **A partir de la semana 5:** **exocad**. Es el que más trabajo te va a dar como diseñadora externa. Formas de acceder:
   - Pide a un **distribuidor oficial de exocad en España** una **licencia de demostración/prueba** (muchos la ofrecen temporalmente) y un presupuesto.
   - Hazte **un curso oficial** de exocad: suelen incluir licencia temporal para practicar.
   - Si conoces un laboratorio que use exocad, pregunta si puedes practicar allí o hacer prácticas.
   - Pregunta al distribuidor por las **modalidades de suscripción** o pago mensual: suelen abaratar mucho la entrada frente a la licencia completa.
3. **Cuando ya tengas clientes:** compra solo los **módulos** que te pidan (no hace falta comprarlos todos).
4. **3Shape**: apréndelo si tus clientes lo usan. La lógica es muy parecida a la de exocad; si sabes uno, el otro lo aprendes en semanas.

> **Por qué no empiezo directamente por exocad:** porque el primer mes lo vas a dedicar a entender el 3D y la anatomía. No tiene sentido pagar una licencia mientras aprendes a girar un modelo en pantalla.

---

## 5. Fundamentos dentales que DEBES dominar

Esta es la parte que diferencia a una "persona que sabe usar un programa" de una **diseñadora dental**. Dedícale tiempo cada semana, aunque ya estés diseñando.

### 5.1 Numeración de los dientes (sistema FDI)

Es la que se usa en España y Europa. Cada diente tiene **dos cifras**: la primera es el **cuadrante** y la segunda la **posición** contando desde la línea media.

```
                 MAXILAR SUPERIOR
     Derecha del paciente     │     Izquierda del paciente
  18 17 16 15 14 13 12 11     │    21 22 23 24 25 26 27 28
  ────────────────────────────┼────────────────────────────
  48 47 46 45 44 43 42 41     │    31 32 33 34 35 36 37 38
                 MANDÍBULA (INFERIOR)

  Posición:  1 = incisivo central     2 = incisivo lateral
             3 = canino               4 = primer premolar
             5 = segundo premolar     6 = primer molar
             7 = segundo molar        8 = tercer molar (muela del juicio)
```

**Ojo:** en la pantalla ves la boca como si miraras al paciente de frente, así que **su derecha está a tu izquierda**.

Ejemplo: "corona en el **36**" = primer molar inferior izquierdo.

(En Estados Unidos usan el sistema universal, del 1 al 32. Si trabajas para clientes de EE. UU., apréndelo también.)

### 5.2 Caras (superficies) del diente

```
                 VESTIBULAR (hacia labios/mejillas)
                        ┌─────────┐
   MESIAL (hacia la     │         │   DISTAL (alejándose
   línea media)         │ OCLUSAL │   de la línea media)
                        │ (masticatoria en posteriores;
                        │  INCISAL = borde en anteriores)
                        └─────────┘
                 LINGUAL (inferior) / PALATINO (superior)
                 (hacia la lengua / el paladar)
```

- **Vestibular** (también "bucal" en molares, "labial" en anteriores).
- **Lingual** (dientes inferiores) / **palatino** (dientes superiores).
- **Mesial** (mira hacia el centro de la arcada) / **distal** (mira hacia atrás).
- **Oclusal** (cara de masticar de premolares y molares) / **incisal** (borde de incisivos y caninos).
- **Cervical**: zona del "cuello" del diente, junto a la encía.

### 5.3 Anatomía que tienes que saber "dibujar de memoria"

Para cada grupo de dientes aprende: forma general, número de cúspides, surcos principales y cómo se ve desde vestibular, oclusal y proximal.

| Diente | Lo esencial |
|---|---|
| Incisivo central superior (11/21) | El más importante en estética. Borde incisal recto, ángulo mesial más recto que el distal, perfil vestibular con 3 planos |
| Incisivo lateral superior (12/22) | Más pequeño y redondeado, ángulos más curvos |
| Canino (13/23, 33/43) | Una cúspide en punta, el diente más largo. Clave en la **guía canina** |
| Premolares superiores | Dos cúspides (vestibular y palatina) de altura parecida |
| Premolares inferiores | 34/44: cúspide lingual muy pequeña. 35/45: puede tener 2 o 3 cúspides |
| Primer molar superior (16/26) | 4 cúspides (+ a veces tubérculo de Carabelli). Forma romboidal vista desde oclusal |
| Primer molar inferior (36/46) | 5 cúspides (3 vestibulares, 2 linguales). Forma rectangular/pentagonal |
| Segundos molares | Parecidos a los primeros pero más simples (superior 3–4 cúspides, inferior 4) |

**Ejercicio (muy importante):** consigue un libro de anatomía dental (te dejo ideas en la sección 22) y dibuja cada diente en papel desde vestibular y oclusal. Sí, a mano. Tu ojo aprende mucho más rápido así.

### 5.4 Conceptos de anatomía funcional que usarás cada día

- **Punto (área) de contacto:** donde un diente toca al de al lado. En posteriores está en el tercio oclusal y un poco hacia vestibular. Si no hay contacto, se mete comida; si es demasiado fuerte, la corona no entra.
- **Tronera (embrasure):** el espacio en forma de "V" alrededor del punto de contacto (hacia oclusal, vestibular, lingual y hacia la encía). Deben existir para que la encía esté sana y la pieza parezca natural.
- **Altura de contorno:** la zona más abultada de una cara del diente. Protege la encía al masticar.
- **Perfil de emergencia:** cómo "sale" el diente de la encía. Debe ser **plano o ligeramente cóncavo**, nunca abombado (un perfil demasiado abultado inflama la encía).
- **Curva de Spee** (vista lateral) y **curva de Wilson** (vista frontal): las curvas que forman las cúspides de toda la arcada. Tu corona debe **seguir** esas curvas, no salirse de ellas.
- **Plano oclusal:** el plano imaginario donde se encuentran los dientes superiores e inferiores.

### 5.5 Oclusión (cómo muerden los dientes)

Esto es lo que más se equivocan los principiantes. Aprende estos términos:

- **Máxima intercuspidación (MIC):** la posición en la que los dientes encajan con más contactos al cerrar.
- **Cúspides de soporte (céntricas):** las que "pisan" en el diente contrario: **palatinas superiores** y **vestibulares inferiores**.
- **Cúspides de corte (no soporte):** vestibulares superiores y linguales inferiores.
- **Resalte (overjet):** distancia horizontal entre incisivos superiores e inferiores.
- **Sobremordida (overbite):** cuánto tapan verticalmente los incisivos superiores a los inferiores.
- **Guía anterior:** al adelantar la mandíbula, los incisivos guían el movimiento y separan los dientes de atrás.
- **Guía canina:** al mover la mandíbula hacia un lado, solo el canino toca y separa el resto (lo ideal en la mayoría de casos).
- **Función de grupo:** al mover hacia un lado tocan varios dientes a la vez (canino + premolares).
- **Interferencia:** un contacto no deseado durante los movimientos (por ejemplo, un molar que toca al mover la mandíbula hacia un lado). **Tu diseño no debe crear interferencias.**
- **Clases de Angle** (se miden por la posición de los primeros molares; simplificando): clase I (relación normal), clase II (la mandíbula queda atrasada), clase III (la mandíbula queda adelantada).
- **Dimensión vertical:** la altura de la cara con los dientes cerrados. En férulas y rehabilitaciones grandes se modifica a propósito.

**Regla práctica para una corona posterior:** contactos **puntuales** y **ligeros** en las cúspides y fosas, repartidos, en la misma intensidad que los dientes vecinos. **Nunca** una "meseta" plana de contacto y **nunca** contactos en las vertientes que empujen el diente hacia un lado.

### 5.6 Las preparaciones (el diente tallado)

Cuando el dentista va a poner una corona, **talla** (lija) el diente. Ese diente tallado se llama **muñón** o **preparación**. Tu corona se apoya sobre él.

- **Línea de terminación (margen):** el borde donde termina el tallado. **Es la línea más importante de todo el diseño.** Si la marcas mal, la corona no ajusta y entra bacteria.
- **Tipos de terminación:**
  - **Chamfer (chaflán):** borde curvo, muy común en coronas de zirconio y cerámica.
  - **Hombro:** escalón en ángulo recto; típico en cerámica sin metal.
  - **Hombro biselado.**
  - **Filo de cuchillo / preparación vertical:** terminación casi sin escalón; más difícil de marcar.
- **Eje de inserción:** la dirección en la que la corona entra y sale del muñón. Si el muñón tiene zonas que "se esconden" desde esa dirección (**retenciones o socavados**), el programa las rellena en la parte interna de la corona para que pueda entrar.
- **Espacio de cemento:** un hueco finísimo que se deja entre la corona y el muñón para el cemento.

### 5.7 Materiales (y por qué cambian tu diseño)

Cada material necesita un **grosor mínimo** distinto. Si lo diseñas más fino, **se rompe**. Valores orientativos habituales (confirma siempre en la ficha del fabricante):

| Material | Uso típico | Grosor mínimo orientativo | Notas |
|---|---|---|---|
| **Zirconio monolítico** | Coronas y puentes posteriores (y anteriores con zirconios translúcidos) | Oclusal ~0,5–1,0 mm; axial ~0,5 mm | Muy resistente. Distintos tipos de zirconio (más o menos translúcidos) tienen mínimos distintos |
| **Disilicato de litio** (tipo e.max CAD/Press) | Coronas anteriores y posteriores, carillas, incrustaciones | Coronas: oclusal ~1,5 mm, paredes ~1,0–1,5 mm; carillas ~0,3–0,6 mm | Muy estético; puentes solo cortos y con conectores grandes |
| **Estructura de zirconio para estratificar** | Estética alta (el ceramista pone cerámica encima) | Estructura ~0,5 mm | Se diseña "reducida" (cut-back) dejando espacio para la cerámica |
| **Metal (CoCr) para metal-cerámica** | Puentes largos, casos con poco espacio | Estructura ~0,3–0,5 mm | Se fresa o se sinteriza por láser |
| **PMMA / resina de provisionales** | Provisionales | ~1,0–1,5 mm | Menos resistente, se usa temporalmente |
| **Resina de impresión para férulas** | Férulas de descarga | ~1,5–2,0 mm o más | Rígida o termo-flexible según el tipo |
| **Resina de modelos** | Modelos impresos | Paredes ~1,5–2,5 mm si es hueco | — |

### 5.8 Tipos de trabajo, vocabulario rápido

- **Corona completa:** cubre todo el diente.
- **Corona anatómica / reducida:** completa con su forma final / más pequeña para añadir cerámica.
- **Puente:** varias piezas unidas. **Pilares** = dientes (o implantes) que sujetan; **póntico** = diente "falso" que rellena el hueco; **conector** = la unión entre piezas.
- **Incrustación inlay / onlay / overlay:** restauraciones parciales (dentro del diente / cubriendo una o varias cúspides / cubriendo toda la cara oclusal).
- **Carilla:** lámina fina en la cara vestibular.
- **Corona sobre implante atornillada / cementada.**
- **Pilar personalizado:** pieza que une el implante con la corona, diseñada a medida.
- **Férula de descarga (férula oclusal, férula de Michigan):** placa de resina que cubre una arcada para proteger los dientes del bruxismo y relajar la musculatura.

---

## 6. Fundamentos de 3D: mallas, archivos STL y navegación

### 6.1 ¿Qué es una "malla"?

Todo lo que ves en un programa dental 3D es una **superficie hecha de miles de triángulos diminutos**. A esa superficie se le llama **malla** (*mesh*).

```
      Un diente en pantalla = miles de triángulos pegados
            /\  /\  /\
           /__\/__\/__\
           \  /\  /\  /
            \/__\/__\/
```

- Más triángulos = más detalle, pero archivo más pesado.
- **Malla cerrada (estanca / "watertight"):** sin agujeros. **Imprescindible** para imprimir o fresar una pieza.
- **Malla abierta:** tiene bordes sueltos (un escaneo intraoral normalmente es abierto: solo tiene la superficie que vio el escáner).
- **Normales:** cada triángulo tiene una "cara de fuera" y una "cara de dentro". Si están invertidas, el programa se confunde.

### 6.2 Formatos de archivo

| Formato | Qué contiene | Cuándo lo verás |
|---|---|---|
| **STL** | Solo la forma (sin color) | **El más universal**. Casi todo lo recibirás y entregarás en STL |
| **PLY** | Forma + color | Escaneos intraorales en color (útil para ver la encía y el margen) |
| **OBJ** | Forma + color/textura | Menos frecuente en dental |
| **Proyecto de exocad** (`.dentalProject` y archivos asociados) | El caso completo de exocad | Si tu cliente también usa exocad |
| **DCM de 3Shape** | Formato propio de 3Shape (a menudo protegido) | Pide que te lo exporten a STL, o que te envíen el caso por su plataforma |
| **DICOM** | Imágenes de TAC / CBCT (el "escáner" del hueso) | Solo para guías quirúrgicas y planificación de implantes |

### 6.3 Qué suele venir en un caso

Para una corona, lo normal es recibir:
- **Arcada preparada** (la que tiene el muñón) → STL/PLY.
- **Arcada antagonista** (la de enfrente) → STL/PLY.
- **Registro de mordida** o las dos arcadas ya **alineadas en oclusión** (muy importante: si no están alineadas, no puedes diseñar la oclusión).
- A veces: escaneo **preoperatorio** (antes de tallar), fotos, escaneo del provisional.
- **Ficha / orden de trabajo:** diente, tipo de trabajo, material, color, indicaciones.

**Antes de aceptar un caso comprueba siempre:** que el margen se ve claro, que no hay agujeros en el muñón, que la mordida es correcta y que tienes toda la información. Si algo falla, **avisa antes de diseñar**. Esto te hará ganar clientes.

### 6.4 Navegación 3D (practícala hasta que sea automática)

Todos los programas tienen tres movimientos:
- **Girar** (rotar el modelo).
- **Desplazar** (mover el modelo por la pantalla sin girarlo).
- **Zoom** (acercar/alejar, casi siempre con la rueda).

Suele ser: botón derecho para girar, rueda para zoom y botón central (o combinación de botones) para desplazar, pero **cada programa tiene sus combinaciones**: búscalas en el manual o menú de ayuda del tuyo y apúntalas en un pósit pegado al monitor.

**Vistas estándar:** aprende los atajos para ver el modelo desde **oclusal, vestibular, lingual, mesial y distal**. Las diseñadoras rápidas cambian de vista constantemente.

---

## 7. Primeras prácticas gratis (Meshmixer y Blue Sky Plan)

### 7.1 Semana 1–2: Meshmixer para perderle el miedo al 3D

Descarga Autodesk Meshmixer (gratuito). Necesitas modelos de práctica: muchos programas y fabricantes de escáneres ofrecen **casos de ejemplo**, y también puedes pedir a un laboratorio o clínica **escaneos anonimizados** para practicar.

**Ejercicio 1 — Navegar (30 minutos al día durante 3 días)**
1. Importa un STL de una arcada (*Import*).
2. Gira, desplaza y haz zoom hasta verlo desde las 5 vistas (oclusal, vestibular, lingual, mesial, distal).
3. Localiza y nombra en voz alta (sí, en voz alta) cada diente con su número FDI.

**Ejercicio 2 — Analizar y reparar una malla**
1. Abre el escaneo.
2. Usa la herramienta de análisis (*Analysis → Inspector*): marcará agujeros y errores.
3. Repara automáticamente y observa qué ha cambiado.
4. Aprende a **seleccionar** una zona (pincel de selección) y **borrarla** (por ejemplo, restos de escaneo de mejilla o lengua).

**Ejercicio 3 — Convertir un escaneo en un modelo sencillo con base**
1. Recorta el escaneo dejando solo dientes y 3–5 mm de encía.
2. Crea una base plana: cierra el modelo (*Edit → Make Solid*) y corta la parte de abajo con un plano (*Edit → Plane Cut*). Así queda una base recta y cerrada.
3. Haz la malla sólida/cerrada.
4. Comprueba con el inspector que no hay agujeros.
5. Exporta como STL.

¡Enhorabuena! Acabas de hacer tu primer modelo imprimible (sencillo).

### 7.2 Semana 3–4: Blue Sky Plan

Blue Sky Plan es gratuito para diseñar (solo pagas si exportas). Perfecto para aprender el **flujo guiado** que luego verás en exocad.

**Ejercicio 4 — Modelo con base desde escaneo intraoral**
Sigue el asistente de modelos: importar, orientar, recortar, crear base, añadir texto con el código del caso. Hazlo con 5 escaneos distintos.

**Ejercicio 5 — Tu primera férula**
Sigue el asistente de férula/protector nocturno con los pasos que te explico en el [Módulo 5](#13-módulo-5--férula-de-descarga-paso-a-paso). Aunque los botones cambien de nombre, los conceptos son **idénticos**.

> Blue Sky Plan tiene tutoriales oficiales en vídeo. Mira el del módulo que vayas a usar **antes** de empezar el ejercicio.

---

## 8. exocad: la lógica general de cualquier diseño

### 8.1 Las dos partes de exocad

1. **DentalDB (la base de datos / hoja de pedido):** aquí **creas el caso**: nombre (código) del paciente, cliente, diente, tipo de trabajo, material, color, y a qué archivos de escaneo corresponde. Es como rellenar la orden de trabajo.
2. **DentalCAD (el diseño):** aquí diseñas. Funciona con un **asistente (wizard)**: te lleva paso a paso y tú avanzas con "Siguiente". En cada paso puedes ajustar cosas a mano.

### 8.2 Crear el caso en DentalDB (cualquier trabajo)

1. **Nuevo caso** → escribe el código del paciente (¡sin nombre real!) y el cliente.
2. En el **esquema dental**, haz clic en el diente o dientes.
3. Elige el **tipo de restauración** (corona anatómica, reducida, póntico, incrustación, carilla, corona sobre implante…).
4. Elige el **material** (zirconio, disilicato…). Aquí se cargan automáticamente los **parámetros** (grosores, espacio de cemento). *Por eso es tan importante que los materiales estén bien configurados con los valores del laboratorio.*
5. Indica si hay **antagonista** y si quieres usar **articulador virtual**.
6. Asocia los **archivos de escaneo** (preparación, antagonista, preoperatorio…).
7. Guarda y pulsa **Diseñar (Design)**.

### 8.3 El patrón que se repite en casi todos los diseños

```
 1. Cargar escaneos y comprobar la mordida
 2. Marcar el margen (o la zona de trabajo)
 3. Definir el eje de inserción y rellenar retenciones
 4. Ajustar parámetros (espacio de cemento, grosores)
 5. Colocar la anatomía (dientes de biblioteca)
 6. Adaptar: posición, tamaño, contactos, oclusión
 7. Modelar a mano (forma libre)
 8. Revisar grosores mínimos
 9. Unir / cerrar la pieza (merge)
10. Guardar y exportar STL
```

Si entiendes este patrón, entiendes el 80 % de exocad (y de 3Shape).

### 8.4 Herramientas que usarás en todos los trabajos

- **Bibliotecas de dientes:** formas de dientes naturales ya hechas. Tú eliges la que mejor encaje con el paciente (jóvenes → formas marcadas; mayores → más desgastadas).
- **Adaptar a antagonista / a vecinos:** el programa ajusta automáticamente la pieza para que toque (o no) a los dientes de enfrente y de los lados.
- **Mapa de colores de distancia:** colorea la superficie según la distancia al diente contrario o al vecino. **Aprende de memoria la leyenda de colores de tu programa**: es tu mejor amiga para ver contactos y penetraciones.
- **Forma libre (Free-form):** herramientas de "escultura": añadir material, quitar, suavizar, alisar, aplanar. Se controla con el tamaño del pincel y la intensidad.
- **Mediciones de grosor:** te marca en color las zonas por debajo del grosor mínimo del material.
- **Sección (corte):** para ver la pieza "cortada" y comprobar grosores y ajuste interno.
- **Articulador virtual:** simula los movimientos de la mandíbula para ver interferencias.

### 8.5 Recursos oficiales

- exocad tiene un **manual en línea oficial (exocad Wiki)** con cada módulo explicado paso a paso. Úsalo junto con esta guía: cuando un botón no te cuadre, búscalo ahí.
- Tiene también **canal de vídeos** y formaciones oficiales/de distribuidores.

---

## 9. Módulo 1 — Corona unitaria paso a paso

Empezaremos con **una corona de zirconio monolítico en un primer molar inferior (36)**. Es el trabajo más frecuente del mundo; si lo dominas, ya puedes trabajar.

### 9.1 Teoría previa (lee esto antes de abrir el programa)

Una buena corona posterior tiene:
- **Margen perfecto:** ajusta al milímetro en la línea de terminación, sin sobrecontornos ni escalones.
- **Contactos proximales:** toca a los dientes vecinos en el sitio correcto (tercio oclusal, ligeramente hacia vestibular), con la fuerza que indique el protocolo.
- **Perfil de emergencia plano/recto** desde la encía, sin "barrigas".
- **Anatomía coherente con los vecinos:** misma altura de cúspides, mismo tamaño aproximado, surcos definidos pero no exagerados.
- **Oclusión correcta:** contactos puntuales en cúspides de soporte y fosas, sin interferencias.
- **Grosor mínimo respetado** en toda la pieza.

### 9.2 Paso a paso en exocad (flujo de corona)

**Paso 0 — Crear el caso** (sección 8.2): diente 36, *corona anatómica*, material zirconio, con antagonista.

**Paso 1 — Revisar los escaneos**
- Gira el modelo. ¿Está completo el muñón? ¿Se ve el margen? ¿Hay agujeros?
- Revisa la **mordida**: las arcadas deben estar encajadas como en la boca, sin atravesarse exageradamente ni estar separadas.
- Si algo está mal → **para y avisa al cliente.**

**Paso 2 — Marcar el margen (línea de terminación)**
1. El programa propone una detección automática: haz clic sobre el margen y dejará que "corra" alrededor.
2. **Nunca te fíes de la línea automática sin revisarla.** Gira alrededor del muñón con mucho zoom.
3. Corrige los puntos que se hayan ido a la encía o hayan subido por el muñón. Arrastra los puntos o redibuja tramos.
4. Truco: si el escaneo tiene color (PLY), el cambio de color entre diente y encía te ayuda. Mira también desde **abajo**: el margen es el "borde" más externo del tallado.
5. El margen debe ser una **línea cerrada y suave**, sin picos.

> Aquí se ganan o se pierden los clientes. Tómate el tiempo que haga falta. Una corona con el margen mal marcado **no sirve**, por bonita que sea.

**Paso 3 — Eje de inserción**
1. El programa propone una dirección de inserción. Míralo **desde arriba (oclusal) siguiendo ese eje**: el programa colorea las zonas retentivas (socavados).
2. Ajusta el eje para que haya **las mínimas retenciones posibles**, normalmente siguiendo el eje largo del muñón y siendo coherente con los dientes vecinos.
3. Las retenciones que queden se rellenarán en la cara interna de la corona.

**Paso 4 — Parámetros de la parte interna (valores orientativos, usa los del laboratorio)**

| Parámetro | Qué significa | Valor orientativo habitual |
|---|---|---|
| Espacio de cemento (en el margen) | Hueco para cemento cerca del margen | 0–0,02 mm |
| Espacio de cemento adicional (resto) | Hueco en el resto del muñón | 0,03–0,08 mm |
| Distancia al margen | A qué distancia del margen empieza el espacio adicional | 0,5–1,0 mm |
| Compensación de fresa | Para que la fresa de la máquina quepa en las zonas estrechas | Según radio de fresa de la máquina del laboratorio |
| Grosor mínimo | Del material | Ver tabla del apartado 5.7 |

**Paso 5 — Colocar el diente de biblioteca**
1. Elige una biblioteca de dientes adecuada (edad y forma de los vecinos).
2. El programa coloca un 36 "de catálogo" sobre el muñón.
3. Posición grosera: muévelo, gíralo y escálalo hasta que:
   - su tamaño mesio-distal ocupe el hueco entre vecinos,
   - sus cúspides estén a la altura de las de los vecinos (sigue la **curva de Spee**),
   - la cara vestibular esté alineada con la de los vecinos (sigue la **curva de la arcada**).
4. Si el cliente te envió un **escaneo preoperatorio** (el diente antes de tallarlo) y estaba bien, puedes **copiar** su forma: muy útil y rápido.

**Paso 6 — Adaptación automática**
Usa las herramientas de adaptar a **vecinos** (contactos proximales) y a **antagonista** (oclusión). Mira el **mapa de colores**:
- Contactos proximales: deben estar en el sitio correcto y con la intensidad del protocolo del laboratorio (un contacto "ligero", ni abierto ni muy apretado).
- Oclusión: contactos ligeros y repartidos. **Ninguna penetración grande** en el antagonista.

**Paso 7 — Modelado libre (aquí es donde te conviertes en diseñadora)**
Con las herramientas de forma libre:
1. **Contactos oclusales:** quita material donde toca demasiado, añade donde no toca nada (si el protocolo pide contacto).
2. **Surcos y fosas:** defínelos ligeramente. Nada de surcos profundos como cañones (debilitan el material y retienen placa).
3. **Crestas marginales:** a la misma altura que las de los vecinos (si no, se mete comida).
4. **Perfil de emergencia:** míralo desde proximal y desde vestibular; debe salir recto/plano de la encía.
5. **Troneras:** asegúrate de que hay espacio en "V" alrededor del contacto.
6. **Suaviza** al final, con poca intensidad, para eliminar "bultos" de la escultura.

**Paso 8 — Revisar grosores**
- Activa la visualización de grosor mínimo. Si hay zonas por debajo del mínimo:
  - Mejor solución: pedir al dentista más reducción (si la falta es grande).
  - Si es poco: el programa puede **engordar** esas zonas automáticamente. Como engorda la pieza hacia fuera, vuelve a revisar después la oclusión y los contactos.
- Haz un **corte (sección)** en vestibulo-lingual y mesio-distal y mira el grosor real.

**Paso 9 — Articulador virtual (si se usa)**
Simula lateralidades y protrusión. Si la corona toca en los movimientos laterales (interferencia) → quita material de esa vertiente.

**Paso 10 — Unir (merge) y guardar**
El programa une la parte interna (la que ajusta al muñón) con la externa (la anatomía) y genera una pieza **cerrada**. Revisa que el margen haya quedado limpio. Guarda y exporta el STL (sección 19).

### 9.3 Coronas anteriores (lo que cambia)

- La **estética manda**: simetría con el diente homólogo (el 11 con el 21), proporciones, textura, líneas de ángulo, borde incisal.
- Truco profesional: **refleja (espejo)** el diente contralateral sano y ajústalo. Es lo que más rápido da un resultado natural.
- Revisa la **guía anterior**: el borde incisal y la cara palatina deben permitir el movimiento de protrusión sin golpes.
- Si el laboratorio va a estratificar cerámica, diseñas la forma completa y luego un **cut-back** (reducción) dejando espacio para la cerámica (en los mamelones del borde incisal, por ejemplo).

### 9.4 Ejercicios del Módulo 1

- [ ] 10 coronas de primer molar inferior (36/46).
- [ ] 10 coronas de primer molar superior (16/26).
- [ ] 10 coronas de premolares.
- [ ] 5 coronas de incisivo central superior, reflejando el contralateral.
- [ ] Cronometra cada una. Meta de principiante: bajar de 60 a 20 minutos por corona posterior. (Una diseñadora con experiencia tarda unos pocos minutos.)
- [ ] Haz captura de pantalla de cada una desde oclusal, vestibular y proximal, y compárala con una foto de un diente natural.

---

## 10. Módulo 2 — Puentes

### 10.1 Teoría

- **Pilares:** los dientes tallados que sujetan el puente (se diseñan como coronas).
- **Póntico:** el diente que sustituye al ausente. **No tiene muñón** debajo; se apoya sobre la encía.
- **Conectores:** las uniones entre pilares y pónticos. **Son la parte que se rompe** si son demasiado delgados.

**Formas de póntico:**
| Tipo | Apoyo en la encía | Uso |
|---|---|---|
| **Ovoide** | Cóncavo en la encía, entra un poco en ella (la encía se ha preparado) | Zona estética, muy natural |
| **Silla modificada (ridge lap modificado)** | Contacto ligero solo por vestibular | Estética + higiene, muy usado en anteriores y premolares |
| **Higiénico / sanitario** | No toca la encía (deja espacio) | Molares inferiores, poca estética |
| **Cónico** | Punto de contacto mínimo | Zonas posteriores |

**Conectores (valores orientativos):**
- Zirconio: aproximadamente **7–9 mm² en anteriores** y **9–12 mm² en posteriores** (más si el puente es largo).
- Disilicato de litio: conectores mayores (del orden de **12–16 mm²** según zona y fabricante) y solo puentes cortos de 3 piezas, hasta la zona de premolares.
- Siempre: **más alto que ancho** (la altura resiste mucho más que la anchura) y **redondeados** (sin ángulos vivos).
- Deja **troneras** hacia la encía para que el paciente pueda limpiar con cepillo interproximal.

### 10.2 Paso a paso (diferencias con la corona)

1. En DentalDB marca pilares como corona (anatómica o reducida) y el hueco como **póntico**, y márcalos como **puente** (unidos).
2. Marca el margen de **cada** pilar.
3. **Eje de inserción común:** todos los pilares tienen que poder entrar a la vez en la misma dirección. Esto es crítico: si los muñones no son paralelos, busca el mejor eje y acepta más relleno de retenciones en alguno. Si es imposible, avisa al cliente.
4. Coloca los dientes de biblioteca (incluido el póntico).
5. Ajusta el **póntico** a la encía según el tipo elegido.
6. Ajusta los **conectores**: el programa muestra su sección en mm². Súbelos por encima del mínimo del material **sin invadir la encía** (deja tronera gingival) y **sin crear contacto con el antagonista**.
7. Oclusión y forma libre, igual que en coronas.
8. Revisa grosores, conectores otra vez (la escultura puede haberlos adelgazado) y une.

### 10.3 Ejercicios

- [ ] 5 puentes de 3 piezas posteriores (ej. 45-46-47).
- [ ] 5 puentes de 3 piezas anteriores (ej. 11-12-13).
- [ ] 2 puentes largos (4–6 piezas) en zirconio.
- [ ] Para cada puente anota el área de los conectores.

---

## 11. Módulo 3 — Coronas sobre implantes

### 11.1 Teoría

Un **implante** es un tornillo de titanio en el hueso. Encima va la corona, a veces con una pieza intermedia (el **pilar**).

- **Cuerpo de escaneo (scanbody):** una pieza que el dentista enrosca en el implante y escanea. El programa la reconoce y así sabe **exactamente** dónde está el implante y cómo está orientado.
- **Biblioteca de implantes:** archivos del fabricante (o de terceros) con la forma exacta de cada sistema de implante, su scanbody y sus piezas. **Necesitas la biblioteca correcta** para cada marca y modelo; si el cliente no te dice cuál es, **pregunta**.
- **Opciones de restauración:**
  - **Corona atornillada sobre Ti-base (base de titanio):** corona (o pilar híbrido + corona) que se pega a una base de titanio estándar; lleva un **canal para el tornillo**. Muy usada hoy.
  - **Pilar personalizado + corona cementada:** diseñas un pilar a medida (titanio o zirconio sobre Ti-base) y encima una corona como si fuera un muñón.
  - **Canal de tornillo angulado:** algunos sistemas permiten inclinar el canal para que salga por palatino/lingual y no por la cara vestibular.

### 11.2 Paso a paso (resumen)

1. En DentalDB: diente → tipo **implante** → sistema de implante, tipo de conexión, Ti-base o pilar, y tipo de corona.
2. **Alinear el scanbody:** el programa superpone el scanbody de la biblioteca con el escaneado. Revisa que **coincide perfectamente**. Si no coincide bien → el caso no es fiable, avisa.
3. **Perfil de emergencia:** diseña cómo sale la corona/pilar desde el implante hasta la encía. En general **cóncavo/estrecho** en la zona profunda para dar espacio a la encía, y ensanchándose cerca del margen gingival.
4. **Pilar personalizado (si aplica):** margen ligeramente por debajo de la encía (lo que indique el dentista), paredes con buena altura y ligera convergencia, sin ángulos vivos.
5. **Corona:** como en el Módulo 1. Ojo con la **oclusión**: los implantes no tienen la "amortiguación" del diente natural; la oclusión suele diseñarse **más ligera** y sin contactos en lateralidad (sigue el protocolo del cliente).
6. **Canal del tornillo:** comprueba por dónde sale y que el grosor alrededor sea suficiente.
7. Exporta **cada pieza por separado** (pilar, corona) según pida el laboratorio.

### 11.3 Ejercicios

- [ ] 5 coronas atornilladas sobre Ti-base (molares).
- [ ] 5 pilares personalizados + corona cementada.
- [ ] 2 casos anteriores con canal angulado (si tu biblioteca lo permite).

---

## 12. Módulo 4 — Incrustaciones y carillas

### 12.1 Incrustaciones (inlay / onlay / overlay)

- **Margen:** es más complejo porque recorre la cara oclusal y las caras proximales. Márcalo con mucha paciencia y mucho zoom.
- **Eje de inserción:** normalmente desde oclusal.
- **Grosores:** respeta los mínimos del material (en disilicato, del orden de 1–1,5 mm en zonas de carga).
- **Anatomía:** continúa la del diente remanente: los surcos y cúspides deben "seguir" los del diente natural sin escalones.
- **Contactos proximales y oclusión:** igual que en coronas.

### 12.2 Carillas

- **Muy finas** (del orden de 0,3–0,6 mm en disilicato; confirma según material).
- **Estética total:** simetría, proporciones (el central superior suele tener una relación ancho/largo alrededor del 75–80 %), línea de sonrisa, línea media, textura superficial.
- Muchas veces se parte de un **encerado diagnóstico** aprobado por el paciente (Módulo 7) y se "copia" su forma.
- Revisa el **borde incisal** y la **guía anterior**.

### 12.3 Ejercicios

- [ ] 5 onlays en molares.
- [ ] 3 casos de carillas de 13 a 23 (6 dientes), cuidando la simetría.

---

## 13. Módulo 5 — Férula de descarga paso a paso

¡Uno de los trabajos más pedidos y uno de los mejores para empezar a ganar dinero!

### 13.1 Teoría: ¿qué es y cómo debe ser?

Una **férula de descarga** (oclusal, tipo Michigan) es una placa de resina rígida que cubre **todos los dientes de una arcada** (normalmente la superior). Se usa para el bruxismo (apretar o rechinar) y problemas de la articulación temporomandibular (ATM).

**Características de una buena férula tipo Michigan:**
1. **Cubre todos los dientes** de la arcada (al menos hasta los segundos molares).
2. **Superficie oclusal plana y lisa**, sin huellas profundas de los dientes contrarios.
3. **Contactos puntuales, simultáneos y de la misma intensidad** de las cúspides de soporte del antagonista (en férula superior: las vestibulares inferiores y los bordes incisales inferiores) sobre la superficie plana.
4. **Rampa de guía canina:** al mover la mandíbula hacia un lado, **solo el canino** del lado hacia el que se mueve toca la férula y separa el resto de dientes.
5. **Guía anterior:** al adelantar la mandíbula, los incisivos inferiores deslizan por la férula y los dientes de atrás se separan.
6. **Grosor** suficiente para no romperse (del orden de 1,5–2 mm como mínimo en la zona oclusal; muchas quedan más gruesas en posteriores según la apertura).
7. **Retención suficiente** para que no se caiga, pero que se pueda poner y quitar sin forzar.
8. **Bordes redondeados** y cómodos, sin invadir encía de forma molesta.

Otros tipos que te pedirán:
- **Protector nocturno** simple (férula más básica, a veces con impronta).
- **Férula blanda o termo-flexible** (según material).
- **Férula de reposicionamiento mandibular / de avance** (para ronquido o apnea; la prescribe el especialista).
- **Protector deportivo.**

### 13.2 Qué necesitas recibir

- Escaneo de **las dos arcadas**.
- **Registro de mordida** con la **apertura** que quiera el dentista (normalmente se registra con los dientes algo separados), o la indicación de cuántos milímetros abrir.
- Indicación de: arcada (superior/inferior), material, tipo de guía, grosor mínimo, extensión.

### 13.3 Paso a paso (lógica general del módulo de férulas, válido para exocad Bite Splint y para Blue Sky Plan)

**Paso 1 — Cargar y revisar**
Carga ambas arcadas y la mordida. Comprueba que el registro es correcto y que los escaneos cubren todos los dientes (sobre todo los últimos molares: si falta la cara distal del último molar, la férula no ajustará bien).

**Paso 2 — Eje de inserción**
Define la dirección de inserción de la férula (normalmente perpendicular al plano oclusal). Visualiza las retenciones coloreadas.

**Paso 3 — Bloquear retenciones (block-out)**
- El programa rellena las zonas retentivas para que la férula pueda entrar.
- Deja **un poco de retención** controlada para que "clique" (el parámetro depende del material: rígido = muy poca retención; flexible = algo más). Usa el valor del protocolo del laboratorio.
- **Espacio interno / offset:** un hueco mínimo entre dientes y férula para que asiente sin presión (del orden de pocas centésimas a una décima de milímetro, según material e impresora).

**Paso 4 — Dibujar el contorno (borde de la férula)**
- **Vestibular:** normalmente cubre las cúspides y un poco por debajo del ecuador (altura de contorno) de los dientes posteriores para ganar retención; en los anteriores cubre poco (el tercio incisal) por estética y comodidad.
- **Palatino/lingual:** unos milímetros sobre la encía palatina/lingual, lo suficiente para dar rigidez sin molestar a la lengua.
- Haz una línea **suave y continua**, sin picos.

**Paso 5 — Parámetros de grosor**
Define el grosor mínimo de la férula (ej. 1,5–2 mm) y el grosor de las paredes.

**Paso 6 — Superficie oclusal plana**
- Usa la función de **plano oclusal / superficie plana** o de adaptación al antagonista en la posición del registro.
- El objetivo: una superficie **lisa** donde **todas** las cúspides de soporte contrarias toquen a la vez, con la misma intensidad (míralo en el mapa de colores).
- Si usas **articulador virtual**, el programa puede generar la superficie teniendo en cuenta los movimientos de la mandíbula.

**Paso 7 — Guías (canina y anterior)**
- Añade **rampas en la zona de los caninos** para que, en los movimientos laterales, solo el canino toque y los demás dientes se separen.
- Comprueba la **protrusión**: al adelantar, contacto en los incisivos y separación posterior.
- Verifica con el articulador virtual, moviendo en lateralidad derecha, izquierda y protrusión.

**Paso 8 — Modelado final**
Suaviza la superficie, redondea bordes, elimina crestas o bultos. Nada de esquinas afiladas.

**Paso 9 — Revisión y exportación**
- Comprueba grosor mínimo en toda la férula.
- Comprueba que la malla está **cerrada**.
- Añade (si lo pide el laboratorio) un **texto grabado** con el código del caso.
- Exporta STL.

### 13.4 Errores típicos en férulas

| Error | Consecuencia | Solución |
|---|---|---|
| No cubrir bien el último molar | El paciente puede sufrir extrusión (el molar "crece") | Extiende hasta el último diente |
| Superficie oclusal con huellas profundas | Bloquea la mandíbula, no relaja | Superficie plana con contactos puntuales |
| Demasiada retención en material rígido | No entra o se rompe al ponerla | Reduce la retención |
| Poca retención | Se cae | Aumenta cobertura vestibular o retención según material |
| Contactos solo en un lado | Carga desigual, incómoda | Ajusta hasta contactos bilaterales simultáneos |
| Bordes afilados | Heridas en encía o lengua | Redondea y suaviza |

### 13.5 Ejercicios

- [ ] 10 férulas superiores tipo Michigan con guía canina.
- [ ] 5 férulas inferiores.
- [ ] 3 protectores nocturnos sencillos.
- [ ] Anota cuánto tardas. Meta: menos de 30 minutos por férula.

---

## 14. Módulo 6 — Modelos para imprimir paso a paso

Con la odontología digital, el laboratorio muchas veces **no recibe impresiones de silicona**, sino un escaneo intraoral. Para comprobar el ajuste, maquillar la cerámica o hacer alineadores, **hay que imprimir un modelo**. Diseñarlos es un trabajo muy demandado.

### 14.1 Tipos de modelo

| Tipo | Para qué |
|---|---|
| **Modelo de estudio / sólido** | Diagnóstico, ortodoncia, alineadores (termoformar encima) |
| **Modelo hueco** | Igual, pero gastando menos resina (más barato, se imprime más rápido) |
| **Modelo con troquel (muñón) extraíble** | Para coronas y puentes: el técnico saca el muñón para trabajar el margen |
| **Modelo con encía extraíble** | Para coronas sobre implantes: la encía blanda se quita para ver la unión con el implante |
| **Modelo de implantes con análogos** | Lleva un agujero donde se inserta un **análogo** (réplica metálica del implante) |
| **Modelo con placa de articulador** | Con encajes para montarlo en un articulador físico |

### 14.2 Paso a paso (lógica de exocad Model Creator y similares)

**Paso 1 — Importar y orientar**
- Importa las dos arcadas en oclusión.
- Orienta el **plano oclusal horizontal** y la línea media centrada. Una orientación mala = base torcida.

**Paso 2 — Recortar el escaneo**
- Elimina restos (lengua, mejillas, paladar mal escaneado si no se necesita).
- Deja una franja de encía uniforme alrededor de los dientes.

**Paso 3 — Elegir tipo de base**
- Sólida o hueca. Si es hueca: **paredes de ~1,5–2,5 mm** (orientativo) y **agujeros de drenaje** para que salga la resina líquida del interior (si no, el modelo puede agrietarse o deformarse).
- Altura de la base: suficiente para ser manejable, sin gastar resina de más.
- Forma: herradura (sin paladar) o con paladar, según uso.

**Paso 4 — Troqueles (si hay preparaciones)**
1. Marca el margen del muñón (igual que en una corona).
2. El programa crea el **troquel**: una pieza separada con una **espiga** que encaja en el modelo.
3. Revisa el **espacio (holgura) entre troquel y modelo**: debe permitir sacarlo y meterlo sin juego. Este valor depende **mucho de la impresora y la resina**; usa el que te dé el laboratorio.
4. Asegúrate de que el troquel tiene el margen **completamente visible** (el programa "ditchea"/retira material por debajo del margen).

**Paso 5 — Implantes (si los hay)**
- Alinea el scanbody con la biblioteca, igual que en el Módulo 3.
- El programa crea el **alojamiento del análogo** del implante. Usa la biblioteca correcta de análogos para modelo impreso.
- Opcional: **encía extraíble**.

**Paso 6 — Articulador y extras**
- Añade la **placa/encaje de articulador** si el laboratorio lo usa.
- **Texto grabado:** código del caso y "SUP" / "INF". Así nadie mezcla modelos.

**Paso 7 — Exportar**
Comprueba que todo está cerrado y exporta **cada pieza por separado**: modelo superior, inferior, cada troquel, encía, etc.

### 14.3 Ejercicios

- [ ] 10 pares de modelos sólidos de ortodoncia.
- [ ] 10 pares de modelos huecos.
- [ ] 5 modelos con troquel extraíble.
- [ ] 3 modelos de implantes con análogo y encía extraíble.

---

## 15. Módulo 7 — Encerado diagnóstico, mock-up y provisionales

### 15.1 Encerado diagnóstico digital (wax-up)

Es "cómo quedarán los dientes" antes de tocar nada. Sirve para que el dentista y el paciente aprueben el tratamiento.

1. Recibes: escaneos, **fotografías** del paciente (sonriendo, en reposo, de frente y de perfil) y las indicaciones del dentista.
2. Si el programa lo permite (en exocad, el módulo de diseño de sonrisa), **superpones las fotos** al escaneo para diseñar mirando la cara del paciente.
3. Colocas dientes de biblioteca sobre los actuales con las proporciones ideales: línea media, plano incisal paralelo a la línea de las pupilas, proporciones del central, forma coherente con la cara.
4. El resultado se imprime como **modelo encerado**, se usa para hacer una **llave de silicona** y el dentista hace un **mock-up** (prueba en boca con resina provisional).

### 15.2 Provisionales

- Coronas o puentes temporales, normalmente en **PMMA o resina impresa**.
- Diseño parecido a la definitiva, a menudo copiando el encerado o el diente preoperatorio.
- Grosor algo mayor por ser un material menos resistente.

### 15.3 Ejercicios

- [ ] 3 encerados de sector anterior (13 a 23).
- [ ] 3 provisionales de puente de 3 piezas.

---

## 16. Módulo 8 — Otros trabajos (visión general)

Estos son trabajos avanzados. Apréndelos **cuando ya domines coronas, férulas y modelos**. Te doy la idea de cada uno para que sepas qué existe.

### 16.1 Prótesis completa digital (dentadura)
- Se usa cuando el paciente no tiene dientes.
- Se definen: dimensión vertical, línea media, plano oclusal, posición de los dientes de catálogo (dientes de prótesis), y la base de encía rosa.
- Módulo específico (en exocad, *Full Denture*; también Blue Sky Plan).
- Requiere saber mucho de **oclusión balanceada** y del montaje clásico de dientes.

### 16.2 Esqueléticos (prótesis parcial removible)
- Estructura metálica con **retenedores (ganchos)**, **conectores mayores y menores** y **apoyos oclusales**.
- Se diseña sobre el modelo con análisis del **eje de inserción** y retenciones (paralelizado virtual).
- Módulo específico (en exocad, *PartialCAD*).

### 16.3 Guías quirúrgicas de implantes
- Se combinan el escaneo intraoral con el **CBCT (DICOM)**.
- El **dentista planifica** la posición del implante (tú puedes preparar el caso, pero la decisión clínica es suya).
- Se diseña una guía que se apoya en dientes/mucosa con **anillas** por donde pasa la fresa.
- Programas: exoplan (exocad), Blue Sky Plan, coDiagnostiX, entre otros.
- **Mucha responsabilidad:** un error puede dañar un nervio. Solo cuando tengas mucha experiencia y siempre con validación del dentista.

### 16.4 Ortodoncia y alineadores
- **Setup:** segmentar cada diente y moverlo virtualmente a su posición final, paso a paso (etapas).
- Se imprime un modelo por etapa y se termoforma el alineador encima.
- Programas específicos de ortodoncia (hay varios comerciales, y Blue Sky Plan tiene módulo).
- Requiere formación en **biomecánica ortodóncica**; lo aprobará siempre el ortodoncista.

---

## 17. Control de calidad: la lista que revisarás SIEMPRE

Imprime esta lista y pégala junto al monitor. **Antes de entregar cualquier trabajo, repasa cada punto.**

### Para coronas, puentes e incrustaciones
- [ ] Diente, tipo de trabajo y material correctos (según la orden).
- [ ] Margen revisado 360° con zoom. Sin saltos ni picos.
- [ ] Eje de inserción correcto, retenciones rellenas.
- [ ] Parámetros (espacio de cemento, etc.) = los del laboratorio.
- [ ] Contactos proximales en su sitio y con la intensidad correcta.
- [ ] Oclusión: contactos puntuales, sin penetraciones, sin interferencias en movimientos.
- [ ] Crestas marginales a la altura de los vecinos.
- [ ] Perfil de emergencia plano/recto, sin sobrecontorno.
- [ ] Grosor mínimo en toda la pieza (revisado con sección).
- [ ] Conectores (puentes) ≥ mínimo del material, con troneras.
- [ ] Forma natural y coherente con los vecinos (comparada con referencia).
- [ ] Malla cerrada, sin errores.
- [ ] Nombre de archivo según protocolo del cliente.

### Para férulas
- [ ] Cubre todos los dientes de la arcada.
- [ ] Retención adecuada al material.
- [ ] Contactos bilaterales, simultáneos y de igual intensidad.
- [ ] Guía canina y anterior correctas.
- [ ] Grosor mínimo respetado.
- [ ] Bordes redondeados. Malla cerrada.

### Para modelos
- [ ] Orientación correcta (plano oclusal horizontal).
- [ ] Troqueles con margen expuesto y holgura correcta.
- [ ] Análogos con la biblioteca correcta.
- [ ] Agujeros de drenaje si es hueco.
- [ ] Texto identificativo.
- [ ] Todas las piezas exportadas por separado.

---

## 18. Errores típicos de principiante y cómo arreglarlos

| Error | Por qué pasa | Cómo evitarlo |
|---|---|---|
| **Margen mal marcado** | Confiar en la detección automática | Revisar siempre 360° con mucho zoom, desde varias vistas |
| **Coronas "caramelo" (redondas, sin anatomía)** | Suavizar demasiado | Suavizar poco y al final; definir surcos y cúspides |
| **Surcos exageradamente profundos** | Querer "que se note la anatomía" | Surcos suaves; compara con dientes reales |
| **Corona demasiado grande (sobrecontorno)** | Escalar a ojo | Compara con el vecino y el homólogo; mira el perfil de emergencia |
| **Contactos oclusales en "meseta"** | Adaptación automática sin retocar | Contactos puntuales en cúspides y fosas |
| **Olvidar la curva de Spee** | Mirar solo desde oclusal | Mira siempre desde vestibular: las cúspides deben seguir la curva |
| **Grosor insuficiente** | Pieza bonita pero frágil | Revisar el mapa de grosores ANTES de terminar |
| **Conectores finos en puentes** | Priorizar estética | Primero resistencia, después estética |
| **No avisar de un escaneo defectuoso** | Miedo a molestar al cliente | Avisar siempre ANTES: es profesionalidad |
| **Trabajar sin protocolo del cliente** | Usar valores por defecto | Pide sus parámetros por escrito antes del primer caso |
| **Archivos mal nombrados o mezclados** | Prisa | Carpetas por caso y nomenclatura fija (sección 19) |

---

## 19. Exportar y entregar un trabajo como una profesional

### 19.1 Nombres de archivo

Usa siempre el protocolo del cliente. Si no tiene, propón uno claro:

```
[CODIGO-CASO]_[DIENTES]_[TRABAJO]_[MATERIAL]_v[VERSION].stl

LS-0153_36_corona_zirconio_v1.stl
LS-0154_45-47_puente_zirconio_v1.stl
LS-0160_SUP_ferula_v1.stl
LS-0161_SUP_modelo_hueco_v1.stl
LS-0161_SUP_troquel_16_v1.stl
```

### 19.2 Qué entregar

- **STL** de cada pieza a fabricar.
- Si el cliente usa el mismo programa: el **proyecto** (por si quiere retocar).
- **Capturas de pantalla** (oclusal, vestibular, contactos): muchos clientes las agradecen para aprobar rápido.
- **Notas:** cualquier cosa importante ("el grosor mínimo en la cúspide mesiovestibular está justo; recomiendo revisar la reducción", "he tenido que rellenar una retención grande en distal").

### 19.3 Cómo enviar

- Plataformas en la nube profesionales que use el cliente (muchos escáneres y programas tienen su propia plataforma de intercambio de casos) o almacenamiento seguro acordado.
- **Nunca** por redes sociales ni apps de mensajería.

### 19.4 Tiempos de entrega

Acuerda por escrito: hora de corte (ej. "casos recibidos antes de las 12:00 se entregan ese día"), urgencias y qué pasa con las correcciones.

---

## 20. Plan de estudio de 16 semanas

Dedicación recomendada: **2–3 horas al día, 5 días a la semana**. Si tienes menos tiempo, estira el plan, pero **no te saltes fases**.

| Semana | Objetivo | Tareas |
|---|---|---|
| **1** | Anatomía y nomenclatura | Numeración FDI, caras del diente, dibujar a mano incisivos y caninos |
| **2** | Anatomía + 3D básico | Dibujar premolares y molares. Meshmixer: ejercicios 1 y 2 |
| **3** | Oclusión + mallas | Estudiar sección 5.5. Meshmixer: ejercicio 3 (modelo sencillo) |
| **4** | Blue Sky Plan | Ejercicios 4 y 5: modelos y primera férula |
| **5** | exocad: entorno | DentalDB, crear casos, navegar, cargar escaneos, leer el manual oficial |
| **6** | Coronas posteriores I | 10 coronas de molar (cuidando margen y contactos) |
| **7** | Coronas posteriores II | 10 coronas de premolar + 10 de molar superior. Cronometrar |
| **8** | Coronas anteriores | 5 incisivos centrales, 5 laterales, 5 caninos (espejo del contralateral) |
| **9** | Férulas | 10 férulas tipo Michigan con guía canina |
| **10** | Modelos | Modelos sólidos, huecos y con troquel |
| **11** | Puentes | 10 puentes (anteriores y posteriores), cuidar conectores |
| **12** | Implantes I | Coronas atornilladas sobre Ti-base |
| **13** | Implantes II + modelos de implantes | Pilares personalizados, modelos con análogos |
| **14** | Incrustaciones y carillas | 5 onlays, 3 casos de carillas |
| **15** | Velocidad y calidad | Repetir casos cronometrados aplicando la lista de control. Pedir a un técnico con experiencia que revise tus diseños |
| **16** | Portfolio y salida al mercado | Seleccionar tus 20 mejores casos, preparar portfolio y tarifa (sección 21) |

**Después de la semana 16:** sigue practicando a diario y empieza con casos reales sencillos (modelos, férulas, coronas posteriores). Las prótesis completas, esqueléticos, guías y ortodoncia, déjalos para cuando lleves varios meses trabajando.

**Consejo de profesora:** busca un **mentor** (un técnico dental con experiencia en CAD) que revise tus trabajos una vez por semana, aunque le pagues. Es la forma más rápida de mejorar; uno solo en casa repite los mismos errores sin darse cuenta.

---

## 21. Cómo conseguir clientes y trabajar desde casa

### 21.1 Prepara tu portfolio

- 15–25 casos variados (coronas, férulas, modelos, puentes, implantes).
- Capturas limpias, fondo neutro, desde varias vistas, con el mapa de contactos.
- **Nunca** datos de pacientes.
- Una web sencilla o un PDF + perfil de LinkedIn cuidado.

### 21.2 Dónde encontrar clientes

1. **Laboratorios dentales de tu zona** (y de toda España): muchos están saturados y buscan diseñadoras externas. Llama o escribe presentándote, ofrece **un caso de prueba gratuito** para que vean tu calidad.
2. **Clínicas con escáner intraoral** que trabajan con fresadora o impresora propia ("chairside"), sobre todo para modelos y férulas.
3. **Centros de fresado** y **empresas de diseño dental externalizado**, que contratan diseñadores en remoto.
4. **LinkedIn** y **grupos profesionales** de usuarios de exocad y 3Shape.
5. **Plataformas de freelance** (hay mucha competencia en precio; úsalas al principio para coger experiencia).
6. **Distribuidores de exocad/3Shape**: a veces conocen laboratorios que buscan diseñadores.
7. **Mercado hispanohablante**: España y Latinoamérica. Hablar español y atender en tu horario es una ventaja frente a servicios de otros países.

### 21.3 Precios (orientativos)

El precio de diseño por unidad **varía muchísimo** según país, experiencia, urgencia y volumen. Hay competencia internacional muy barata, así que tu valor debe ser **calidad, rapidez, comunicación y cercanía**. Investiga el mercado antes de fijar tarifas preguntando a laboratorios y mirando qué cobran otras diseñadoras.

Orientativamente, el diseño se cobra **por unidad o por caso** (una corona, una férula, un par de modelos…), con suplementos por urgencia o complejidad (implantes, estética, casos grandes), y a menudo con **tarifas por volumen** para clientes que envían muchos casos.

Consejos:
- No compitas solo por precio: la competencia barata siempre existirá.
- Ofrece **correcciones incluidas** (una o dos rondas razonables).
- Cobra aparte los casos muy complejos.

### 21.4 Lo administrativo (España)

- **Alta como autónoma** en Hacienda y Seguridad Social (infórmate de la **tarifa reducida para nuevas autónomas** vigente).
- **Epígrafe de actividad** adecuado: pregúntalo a una gestoría.
- **IVA:** hay exenciones para ciertos servicios sanitarios y de prótesis dental, pero **depende de tu titulación y de cómo se preste el servicio**. No lo decidas tú sola: **consulta con una gestoría** antes de emitir tu primera factura.
- **Contratos:** con cada cliente, un acuerdo sencillo de servicios + el contrato de protección de datos (sección 2.3).
- **Seguro de responsabilidad civil profesional:** muy recomendable.
- **Licencias de software:** asegúrate de tener licencia a tu nombre para uso comercial (una licencia de prueba o educativa **no** sirve para trabajar cobrando).

### 21.5 El futuro: la inteligencia artificial

Ya hay herramientas de IA que proponen coronas automáticamente (tanto dentro de exocad y 3Shape como servicios independientes en la nube). **No te asustes:**
- Las coronas simples serán cada vez más automáticas y baratas.
- El valor estará en **revisar y corregir** lo que propone la IA, en los **casos complejos** (estética, implantes, rehabilitaciones, férulas especiales, prótesis completa) y en la **comunicación con el laboratorio**.
- Aprende a usar esas herramientas: te harán mucho más rápida. Pero sin conocimientos de anatomía y oclusión no sabrás si lo que propone la IA está bien. **Por eso esta guía insiste tanto en los fundamentos.**

---

## 22. Recursos para seguir aprendiendo

### Oficiales (los más fiables)
- **Manual en línea oficial de exocad (exocad Wiki)** y su canal oficial de vídeos.
- **3Shape Academy** (formación en línea de 3Shape).
- **Tutoriales oficiales de Blue Sky Plan** (Blue Sky Bio).
- **Fichas técnicas de los materiales** (zirconio, disilicato, resinas): ahí están los grosores y conectores mínimos reales.

### Formación reglada
- **Ciclo Formativo de Grado Superior en Prótesis Dentales** (presencial o a distancia).
- **Cursos de exocad / 3Shape** impartidos por distribuidores oficiales y centros de formación (pide que sean con práctica y licencia incluida).

### Libros de anatomía y oclusión (busca las ediciones en español)
- *Wheeler: Anatomía, fisiología y oclusión dental* (Nelson).
- *Anatomía odontológica funcional y aplicada* (Figún y Garino).
- *Tratamiento de oclusión y afecciones temporomandibulares* (Okeson) — referencia para oclusión y férulas.

### Práctica
- **Casos de ejemplo** que traen los programas.
- **Escaneos anonimizados** de laboratorios o clínicas con los que contactes.
- **Dientes naturales de referencia**: modelos de anatomía dental (tipodontos) o fotos de calidad.

### Comunidad
- Grupos profesionales de usuarios de exocad y 3Shape (en redes y foros).
- Congresos y ferias del sector dental (en España hay ferias importantes del sector donde exhiben todos los fabricantes de CAD/CAM).

---

## 23. Glosario

| Término | Significado |
|---|---|
| **Análogo** | Réplica metálica de un implante que se coloca en el modelo |
| **Antagonista** | El diente o arcada de enfrente (el que muerde contra el tuyo) |
| **Articulador virtual** | Simulación de los movimientos de la mandíbula en el ordenador |
| **Biblioteca** | Colección de formas prediseñadas (dientes, implantes, pilares) |
| **CAD / CAM** | Diseño / fabricación asistidos por ordenador |
| **CBCT / DICOM** | Tomografía de haz cónico / formato de esas imágenes |
| **Chamfer (chaflán)** | Tipo de terminación del tallado, con borde curvo |
| **Conector** | Unión entre piezas de un puente |
| **Cut-back** | Reducción del diseño para añadir cerámica estratificada |
| **Eje de inserción** | Dirección en la que la pieza entra y sale |
| **Espacio de cemento** | Hueco entre corona y muñón para el cemento |
| **Férula de descarga (Michigan)** | Placa oclusal rígida para bruxismo y ATM |
| **Guía canina / anterior** | Contactos que guían los movimientos laterales / hacia delante |
| **Interferencia** | Contacto indeseado durante los movimientos mandibulares |
| **Malla (mesh)** | Superficie 3D formada por triángulos |
| **Margen / línea de terminación** | Borde del tallado donde termina la corona |
| **Merge (unir)** | Paso final que convierte el diseño en una pieza sólida cerrada |
| **Mock-up** | Prueba estética en boca con resina provisional |
| **Muñón / preparación** | Diente tallado que recibe la corona |
| **Offset** | Separación constante entre dos superficies |
| **Perfil de emergencia** | Forma con la que la corona sale de la encía |
| **Pilar** | Diente o implante que sostiene un puente; o la pieza entre implante y corona |
| **Póntico** | Diente "falso" de un puente, sin muñón debajo |
| **Retención / socavado** | Zona que no se ve desde el eje de inserción e impide que entre la pieza |
| **Scanbody** | Pieza que se atornilla al implante para escanear su posición |
| **STL / PLY** | Formatos de archivo 3D (sin color / con color) |
| **Ti-base** | Base de titanio sobre la que se pega una corona o pilar sobre implante |
| **Tronera** | Espacio en "V" alrededor del punto de contacto |
| **Troquel** | Muñón extraíble del modelo |
| **Wax-up (encerado)** | Propuesta de forma final de los dientes |

---

## 24. Chuleta de valores de referencia

> ⚠️ **Valores orientativos habituales para estudiar.** En el trabajo real, usa SIEMPRE los del fabricante del material y el protocolo del laboratorio.

| Concepto | Valor orientativo |
|---|---|
| Espacio de cemento en el margen | 0–0,02 mm |
| Espacio de cemento adicional | 0,03–0,08 mm |
| Distancia al margen (inicio del espacio adicional) | 0,5–1,0 mm |
| Zirconio monolítico, grosor oclusal | ~0,5–1,0 mm (según tipo de zirconio) |
| Disilicato de litio, corona: oclusal / paredes | ~1,5 mm / ~1,0–1,5 mm |
| Carilla de disilicato | ~0,3–0,6 mm |
| Provisional PMMA | ~1,0–1,5 mm |
| Conector zirconio anterior / posterior | ~7–9 mm² / ~9–12 mm² |
| Conector disilicato (puentes cortos) | ~12–16 mm² |
| Férula de descarga, grosor mínimo | ~1,5–2,0 mm |
| Pared de modelo hueco | ~1,5–2,5 mm (+ agujeros de drenaje) |
| Proporción ancho/largo del incisivo central superior | ~75–80 % |

---

## 25. Autoevaluación final

Cuando puedas responder **sin mirar** a todas estas preguntas, estarás preparada para tus primeros clientes:

1. ¿Qué diente es el 46? ¿Y el 23?
2. ¿Cuáles son las cúspides de soporte en superior y en inferior?
3. ¿Qué es la guía canina y por qué se pone una rampa en la férula?
4. ¿Por qué el perfil de emergencia no debe ser abombado?
5. ¿Qué pasa si marcas mal el margen?
6. ¿Para qué sirve el espacio de cemento? ¿Por qué es menor cerca del margen?
7. ¿Qué diferencia hay entre un póntico ovoide y uno higiénico?
8. ¿Por qué un conector debe ser más alto que ancho?
9. ¿Qué es un scanbody y qué haces si no coincide con la biblioteca?
10. ¿Por qué un modelo hueco necesita agujeros de drenaje?
11. ¿Qué información mínima necesitas para diseñar una férula?
12. ¿Qué debes hacer si recibes un escaneo con el margen invisible?
13. ¿Por qué no debes recibir casos con el nombre del paciente?
14. Nombra 5 puntos de tu lista de control de coronas.
15. ¿Qué diferencia hay entre STL y PLY?

**Examen práctico (hazlo tú misma, cronometrado):**
- 1 corona de molar en menos de 20 minutos, pasando la lista de control completa.
- 1 férula tipo Michigan con guía canina en menos de 30 minutos.
- 1 par de modelos con troquel en menos de 20 minutos.

Si lo consigues con buena calidad y un técnico con experiencia te da el visto bueno: **ya estás lista para empezar a trabajar desde casa.**

---

> **Palabras finales de tu profesora:**
>
> Nadie diseña bien las primeras 50 coronas. Es normal que al principio tardes una hora y el resultado no te guste. Sigue el plan, compárate con dientes reales, pide que te corrijan y **no te saltes la anatomía ni la oclusión**. En unos meses de práctica constante notarás el cambio, y en un año puedes tener una profesión que te permita trabajar desde casa con calidad.
>
> Cuando vayas avanzando, vuelve a preguntarme: podemos profundizar en cualquier módulo (por ejemplo, una clase entera solo de márgenes, de férulas o de implantes), preparar ejercicios concretos o revisar juntas cómo presentar tu portfolio.
>
> ¡Mucho ánimo y a practicar!
