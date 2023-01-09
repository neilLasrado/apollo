# -*- coding: utf-8 -*-
# Copyright (c) 2023, Neil Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class InferenceImages(Document):
	def on_submit(self):
		if self.inference_status=="Pending":
			frappe.throw("Please set inference status before submiting.")
