# backend/services/excel_service.py

import os
import shutil
from openpyxl import load_workbook

def generate_excel_from_template(input_data, template_name, project_name, revision):
    template_path = os.path.join("templates", template_name)
    output_folder = os.path.join("..", "generated_files", "excel")
    os.makedirs(output_folder, exist_ok=True)

    output_file = f"{project_name}-{revision}.xlsx"
    output_path = os.path.join(output_folder, output_file)

    # Copy the template file
    shutil.copy(template_path, output_path)

    # Load workbook
    wb = load_workbook(output_path)
    sheet = wb["trset"]  # Change if the sheet name is different

    for section in input_data:
        for item in input_data[section]:
            cell = item.get("cell_pos")
            value = item.get("value")
            if cell and value is not None:
                sheet[cell] = value

    wb.save(output_path)
    return output_path
