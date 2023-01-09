// Copyright (c) 2023, Neil Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('Inference Images', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Inference Image Result', {
    download: (frm, cdt, cdn) => {
		let row = locals[cdt][cdn];
		var win = window.open(row.result, '_blank');
 		win.focus();
	}
});
