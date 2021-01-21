from jinja2 import Template
from os.path import exists
import click
import yaml


@click.command()
@click.option('--templates', help='Number of greetings.')
@click.option('--component', help="Declare your file(s) with your components")
def generate_template(templates, component):
    software_list = []
    with open(component) as software_file:
        for item in software_file.readlines():
            software_list.append(item)

    if not exists(templates):
        print(f"{templates} does not exists please create a valid template")
        print("To generate a default template run main.py --generate True")
        return 0

    with open(templates, "r") as f:
        tmpl = Template(f.read())
        tmpl.stream(
            variable='Hubble Software List',
            item_list=software_list,
        ).dump("assets/html/index.html")

    generate_pages(software_list)


def generate_pages(component_list: list):
    for component in component_list:
        with open("assets/templates/content.html.jinja", "r") as f:
            with open("config/descriptors.yaml", "r") as stream:
                for data in yaml.safe_load_all(stream):
                    print(data)
                tmpl = Template(f.read())
                tmpl.stream(
                    PageTitle=f'{component.strip()}',
                ).dump(f"assets/html/{component.strip()}.html")


def parse_yaml():
    with open("config/descriptors.yaml", "r") as stream:
        for data in yaml.safe_load_all(stream):
            print(data)
