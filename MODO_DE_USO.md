# Guía de Uso - Entorno Odoo 19 Local (Panamá)

Este documento explica cómo utilizar los scripts automatizados para levantar tu entorno local con Colima y Docker, aplicando automáticamente el estándar de configuración de Panamá (impuestos, términos de pago, diarios, etc.).

## Scripts Principales

### 1. Iniciar todo el entorno (`./up.sh`)
Usa este comando para arrancar Colima, Docker y configurar tu base de datos en un solo paso.

**Comando:**
```bash
./up.sh [nombre_de_tu_base_de_datos]
```

*   **Ejemplo:** `./up.sh Digifact`
*   **¿Qué hace?**
    1.  Ejecuta `colima start`.
    2.  Levanta los contenedores con `docker compose up -d`.
    3.  Espera 10 segundos a que Odoo esté listo.
    4.  Si la base de datos no existe, la inicializa automáticamente.
    5.  **Aplica el estándar de Panamá** (impuestos 0%, 7%, 10%, 15%, términos de pago, diarios FE/NC, etc.) a esa base de datos específica.

---

### 2. Apagar todo el entorno (`./down.sh`)
Usa este comando cuando termines de trabajar para liberar recursos de tu Mac.

**Comando:**
```bash
./down.sh
```
*   **¿Qué hace?** Detiene los contenedores de Docker y apaga la máquina virtual de Colima.

---

### 3. Aprovisionar una base de datos existente (`./provision.sh`)
Si ya tienes Odoo corriendo y creas una base de datos nueva desde la interfaz web, puedes aplicarle el estándar de Panamá sin reiniciar todo.

**Comando:**
```bash
./provision.sh [nombre_de_tu_base_de_datos]
```
*   **Ejemplo:** `./provision.sh dental_hospital`

---

### 4. Listar bases de datos (`./ls-db.sh`)
Si no recuerdas cómo se llama tu base de datos, usa este script.

**Comando:**
```bash
./ls-db.sh
```

---

## Qué se configura automáticamente

Al ejecutar `./up.sh` o `./provision.sh`, se aplican los siguientes estándares de Panamá:

1.  **Localización Base**: País (Panamá), Provincias/Estados (PA-01 a PA-13) e Idioma (es_PA).
2.  **Impuestos**:
    *   Exento 0% (Venta y Compra).
    *   ITBMS 7%, 10% y 15% (Venta y Compra).
    *   Retención de Impuestos (configurada como grupo).
3.  **Disposiciones Fiscales**:
    *   "Exento de impuestos" (detección automática).
    *   "Retención de impuestos".
4.  **Métodos de Pago**: Efectivo, Tarjeta, Cheque, Transferencia, y Crédito (30, 60, 90 días).
5.  **Diarios Contables**: Diario de Ventas "FE" (Facturación Electrónica) y "NC" (Notas de Crédito).
6.  **Etiquetas de Contactos**: Etiquetas para segmentar (Persona Natural/Jurídica, Contribuyente, Gobierno, etc.).
7.  **Productos por Defecto**: "Servicio de Acarreo", "Seguro" y "Otros Gastos" (configurados con 0% exento).
8.  **Configuración de Ventas**: Activación de Unidades de Medida y Embalajes.
9.  **Formato de Impresión**: Formato de papel Carta (US Letter) con márgenes de 5mm.
10. **UX**: Vista Kanban por defecto para los contactos.

## Notas Importantes
*   **Base de datos por defecto:** Si ejecutas `./up.sh` sin parámetros, intentará usar una base de datos llamada `postgres`.
*   **Ubicación:** Todos estos comandos deben ejecutarse desde la carpeta `odoo-dev`.
*   **Acceso:** Una vez encendido, puedes acceder a Odoo en: [http://localhost:8069](http://localhost:8069)
