# -*- coding: utf-8 -*-
# Copyright (c) 2022, yashwanth and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class WBSStorageLocation(Document):
	pass

@frappe.whitelist()
def get_attributes(id):
	try:
		print("WBS Settings", id)
		atr_list = frappe.db.sql("""select attribute_level, attribute_name from `tabWBS Attributes`
								where parent=%s""", (id), as_dict=1)
		print(atr_list);
		return {"SC": True, 'attrs': atr_list}
	except Exception as ex:
		return {"EX": ex}
