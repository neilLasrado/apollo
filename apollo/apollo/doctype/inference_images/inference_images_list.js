frappe.listview_settings['Inference Images'] = {
    add_fields: ["inference_status"],

    get_indicator: function(doc) {
        if (doc.inference_status == "Pending") {
            return [__("Pending"), "red ", "inference_status,=,Pending"];
        } else if (doc.inference_status == "Good") {
            return [__("Good"), "green", "inference_status,=,Good"];
        } else if (doc.inference_status == "Not Good") {
            return [__("Not Good"), "orange", "inference_status,=,Not Good"];
        }
    }
};