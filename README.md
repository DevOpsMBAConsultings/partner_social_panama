# Redes Sociales en Contactos (Panamá)

[![Odoo Version](https://img.shields.io/badge/Odoo-18.0%20%7C%2019.0-875A7B?logo=odoo&logoColor=white)](https://www.odoo.com)
[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)
[![GitHub last commit](https://img.shields.io/github/last-commit/DevOpsMBAConsultings/partner_social)](https://github.com/DevOpsMBAConsultings/partner_social/commits/18.0)
[![GitHub repo size](https://img.shields.io/github/repo-size/DevOpsMBAConsultings/partner_social)](https://github.com/DevOpsMBAConsultings/partner_social)
[![MBA Consultings](https://img.shields.io/badge/Made%20by-MBA%20Consultings-198753?logo=github)](https://mbaconsultings.com)

Módulo para **Odoo 18/19** que añade campos de redes sociales (Facebook, Instagram, LinkedIn) a la ficha de contactos (`res.partner`). Diseñado para empresas en Panamá que necesitan acceso rápido a los perfiles sociales de sus clientes y proveedores.

---

## 📋 Características

- ✅ **3 campos URL nativos** con widget `url` y validación automática
- ✅ **Placeholders intuitivos** (ej. `facebook.com/usuario...`)
- ✅ **Integración nativa** — aparecen justo debajo del campo *Sitio web* en el formulario de contacto
- ✅ **Traducción al español** (`es.po` incluido)
- ✅ **Compatible con Odoo 18 y 19**
- ✅ **Licencia LGPL-3** — uso libre, también comercial

---

## 🖼️ Capturas de pantalla

### Formulario de contacto con campos sociales
![Partner form with social fields](static/description/screenshot_partner_form.png)

> *Los campos aparecen automáticamente tras el campo **Sitio web**.*

---

## 🚀 Instalación

### Desde GitHub (recomendado para desarrollo)

```bash
# Clonar en tu carpeta de addons personalizados
cd /opt/odoo/custom-addons
git clone -b 18.0 https://github.com/DevOpsMBAConsultings/partner_social.git
```

### Desde la interfaz de Odoo (Apps)

1. Activar **Modo desarrollador** (Ajustes → Desarrollador)
2. Ir a **Aplicaciones** → **Actualizar lista de aplicaciones**
3. Buscar *"Redes Sociales en Contactos (Panamá)"*
4. Clic en **Instalar**

> **Nota:** Requiere el módulo base `contacts` (se instala automático como dependencia).

---

## ⚙️ Configuración

No requiere configuración adicional. Al instalar, los campos quedan disponibles en **Contactos → Contactos** (o *Clientes/Proveedores*).

### Para usar:
1. Abre cualquier contacto (o crea uno nuevo)
2. Rellena los campos:
   - **Facebook** → `https://facebook.com/tuempresa`
   - **Instagram** → `https://instagram.com/tuempresa`
   - **LinkedIn** → `https://linkedin.com/company/tuempresa`
3. Guarda — los enlaces son clicables directo desde el formulario

---

## 🏗️ Estructura técnica

```
partner_social/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── res_partner.py          # Herencia de res.partner + 3 campos Char
├── views/
│   └── res_partner_views.xml   # Vista heredada (xpath after website)
└── i18n/
    └── es.po                   # Traducciones al español
```

### Modelo extendido: `res.partner`

| Campo | Tipo | Widget | Descripción |
|-------|------|--------|-------------|
| `social_facebook` | `Char` | `url` | Enlace a página de Facebook |
| `social_instagram` | `Char` | `url` | Enlace a cuenta de Instagram |
| `social_linkedin` | `Char` | `url` | Enlace a perfil de LinkedIn |

### Vista heredada
- **ID**: `view_partner_form_inherit_social_panama`
- **Hereda de**: `base.view_partner_form`
- **Inyección**: `xpath` tras `field[@name='website']`

---

## 🌍 Compatibilidad

| Odoo Version | Estado | Probado |
|--------------|--------|---------|
| 18.0 (CE/EE) | ✅ Soportado | Sí |
| 19.0 (CE/EE) | ✅ Soportado | Sí |
| 17.0 | ⚠️ No probado | No |

---

## 🛠️ Desarrollo

### Requisitos
- Odoo 18.0 o 19.0
- Python 3.10+
- Módulo `contacts` (core)

### Rama de trabajo
- **`18.0`** — rama principal para Odoo 18/19

### Commits y versionado
- Formato versión: `{serie}.{major}.{minor}.{patch}` (ej. `18.0.1.0.0`)
- Cada cambio sube el último dígito (`patch`)

---

## 📄 Licencia

**LGPL-3.0** — Ver [LICENSE](LICENSE) (o [gnu.org/licenses/lgpl-3.0.html](https://www.gnu.org/licenses/lgpl-3.0.html)).

En resumen: puedes usar, modificar y distribuir (incluso comercialmente) manteniendo la misma licencia en derivados.

---

## 👥 Créditos

**Autor**: [MBA Consultings](https://mbaconsultings.com) — [Brooks Gonzalez](https://github.com/BrooksGonzalez)

**Mantenido por**: [DevOpsMBAConsultings](https://github.com/DevOpsMBAConsultings)

---

## 🔗 Enlaces útiles

- [Repositorio GitHub](https://github.com/DevOpsMBAConsultings/partner_social)
- [Issues / Bug reports](https://github.com/DevOpsMBAConsultings/partner_social/issues)
- [MBA Consultings](https://mbaconsultings.com)
- [Documentación Odoo 18](https://www.odoo.com/documentation/18.0/)

---

*¿Encontraste un bug o tienes una mejora? [Abre un issue](https://github.com/DevOpsMBAConsultings/partner_social/issues/new) o haz un PR.*