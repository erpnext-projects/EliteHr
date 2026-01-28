import frappe

@frappe.whitelist()
def complete_setup(args):
    if isinstance(args, str):
        args = frappe.parse_json(args)
    frappe.db.set_value("Installed Application",{"app_name":"frappe"},"is_setup_complete",1)
    frappe.db.commit()
    frappe.clear_cache()
    
    return "ok"