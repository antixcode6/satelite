from jinja2 import Template
from os.path import exists
import subprocess
import click


@click.command()
@click.option('--templates', help='Number of greetings.')
@click.option('--component', help="Declare your file(s) with your components")
#@click.option('--generate', type=bool, default=False, help="Generates a basic Jinja template for this project")
def generate_template(templates, component):
    software_list = []
    with open(component) as software_file:
        for item in software_file.readlines():
            software_list.append(item)
                

    if not exists(templates):
        print(f"file {templates} does not exists please create a valid Jinja template or rerun with the --generate flag")
        return 0

    with open(templates, "r") as f:
        tmpl = Template(f.read())
        tmpl.stream(
            variable='Hubble Software List',
            item_list=software_list,
        ).dump("assets/html/index.html")
