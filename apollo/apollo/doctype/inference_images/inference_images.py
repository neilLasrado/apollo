# -*- coding: utf-8 -*-
# Copyright (c) 2023, Neil Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class InferenceImages(Document):
	def validate(self):
		self.image_file_name = self.image_file[15:]

	def before_submit(self):
		self.inference_status = "Good"
		for result in self.results:
			if not result.inference_status:
				frappe.throw("Please set inference status for result row {0} before submiting.".format(result.idx))
			elif result.inference_status == "Not Good":
				self.inference_status = "Not Good"
