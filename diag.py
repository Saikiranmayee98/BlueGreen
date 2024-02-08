import plantuml

url = "http://www.plantuml.com/plantuml/img/"

def generate_diagram(plantuml_file, output_format="png"):
    pl = plantuml.PlantUML(url=url)
    pl.processes_file(plantuml_file, f"output.{output_format}")

if __name__ == "__main__":
    plantuml_file = "bluedockerfile_plantuml.puml"
    generate_diagram(plantuml_file)
