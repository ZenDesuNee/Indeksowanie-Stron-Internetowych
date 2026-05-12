#region Import Bibliotek I Danych
import textwrap
import json
#endregion
#region Analiza Danych
def pars_file(file_path="Download_data.json"):
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except json.JSONDecodeError:
        return "Plik Json Jest Pusty/Nieprawidłowy"
            
    headers = existing_data[0]
    data_rows = existing_data[1:]
    
    parsed = [dict(zip(headers, row)) for row in data_rows]
    col_widths = {}
    
    for col in headers:
        max_value_len = max((len(str(item.get(col, ""))) for item in parsed), default=0)
        col_widths[col] = min(max(len(col), max_value_len), 20) + 2

    header_line = ""
    for col in headers:
        header_line += col.ljust(col_widths[col])
        
    print(header_line)
    print("-" *len(header_line))

    for item in parsed:
        wrap_col = []       
        for col in headers:
            value = str(item.get(col, ""))
            wrap = textwrap.wrap(value, width=col_widths[col]-2) or [""]
            wrap_col.append(wrap)
            
        max_lines = max(len(w) for w in wrap_col)

        for i in range(max_lines):
            line = ""
            for col, wrap in zip(headers, wrap_col):
                part = wrap[i] if i < len(wrap) else ""
                line += part.ljust(col_widths[col])

            print(line)
#endregion