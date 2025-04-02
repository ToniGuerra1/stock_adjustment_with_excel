
{
    "name": "Import Excel to Update Stock",
    "version": "1.0",
    "category": "Inventory",
    "author": "Toni Guerra",
    'description': """
📄 Importa referencias de pago desde Excel y actualiza automáticamente los pedidos de venta en Odoo. Ideal para flujos donde los pagos llegan por separado (contra reembolso, conciliación bancaria, plataformas externas, etc.).

---

🎯 ¿Qué hace este módulo?

✅ Permite cargar un archivo Excel con:
- Nombre del pedido (`sale.order`)
- Referencia de pago personalizada
- Opción de crear facturas automáticamente

✅ Busca los pedidos por nombre y actualiza:
- El campo `payment_reference`
- Las facturas vinculadas (si existen)
- Crea facturas nuevas si marcas “Crear Factura”

---

📂 Estructura del Excel esperada:

| ORDER_NAME | PAYMENT_REF |


| SO1234     | Ref XYZ123  |

| SO5678     | Ref ABC456  |

---

⚙️ Funcionalidades clave:

- Carga masiva desde Excel (.xlsx)
- Interfaz de asistente clara y fácil de usar
- Registro de logs en el backend
- Automatización de facturación opcional

---

💡 Casos de uso:

- Pedidos contra reembolso o transferencia
- Integraciones con sistemas externos que generan Excel
- Contabilidad y conciliación más ágil
- Añadir referencia bancaria a muchas facturas en segundos

---

🧪 Requisitos:
- Formato `.xlsx`
- Campo ORDER_NAME debe coincidir con el nombre del pedido

---

🛡️ Licencia: OPL-1 (uso para 1 base de datos, sin redistribución)
💰 Precio: 9,90 € (pago único)
""",
    "website": "",
    "depends": [
        "stock",
    ],
    "data": [
        "views/import_stock_count_wizard_views.xml",
        "security/ir.model.access.csv",
        "static/description/logo.png",
    ],
    "installable": True,
    "application": True,
    'license': 'OPL-1',
    'price': 9.90,
    'currency': 'EUR',
}
