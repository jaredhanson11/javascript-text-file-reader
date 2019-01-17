import json
json_data = {'header': None, 'paragraph': None}

with open('./txt/header.txt', 'r') as header:
    header_file_contents = header.read()
    json_data['header'] = header_file_contents

with open('./txt/paragraph.txt', 'r') as paragraph:
    paragraph_file_contents = paragraph.read()
    json_data['paragraph'] = paragraph_file_contents

# To be in javascript format
var_template = 'var %s = %s;'
# variable name to reference in javascript file
var_name = 'item1'
# Writing the dictionary to string in json format
var_value = json.dumps(json_data)
# Replace the %s in the template with the proper values
item_entry = var_template % (var_name, var_value)
# write the line in the json file to be imported to javascript
with open('./data.json', 'w') as data_file:
    data_file.write(item_entry)

