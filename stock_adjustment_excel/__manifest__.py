
{
    "name": "Import Excel to Update Stock",
    "version": "1.0",
    "category": "Inventory",
    "author": "Toni Guerra",
    "summary": "Update product stock from Excel: import counted quantities and apply inventory adjustments automatically",
    'description': """
📦 Import Excel to Update Stock (Odoo Module)

Actualiza el stock de tus productos directamente desde un archivo Excel (.xlsx). Este módulo te permite exportar productos con su cantidad disponible, cargar nuevos valores de stock y aplicar los ajustes de inventario automáticamente mediante `inventory_quantity` y `action_apply_inventory`. 

🔹 Estructura esperada del archivo Excel:
DEFAULT_CODE | NAME | QUANTITY

✅ Compatible con .xlsx  
✅ Selección de ubicación (stock.location) desde el asistente  
✅ Registro de logs en Odoo para trazabilidad  
✅ Interfaz simple e intuitiva  

💼 Casos de uso: cargas masivas desde conteos físicos, auditorías, hojas de Google exportadas, o sistemas externos.

🧪 Requisitos: el producto debe tener `default_code` y la librería `openpyxl` debe estar instalada.  

📄 Licencia: OPL-1 (uso en una única base de datos, sin redistribución).  
💰 Precio: 49 €
""",
    "website": "",
    "depends": [
        "stock",
    ],
    "data": [
        "views/import_stock_count_wizard_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": True,
    'license': 'OPL-1',
    'price': 9.90,
    'currency': 'EUR',
}
