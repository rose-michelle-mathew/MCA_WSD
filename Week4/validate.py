# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import XMLSchema



from lxml import etree

# Load the XML schema
schema = etree.XMLSchema(file='employee_schema.xsd')
# Parse the XML document
tree = etree.parse('myxml.xml')
# Validate the XML document
if not schema.validate(tree):
    print('The XML document is invalid.')

else:
    print("Valid XML file")
    