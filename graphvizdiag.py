import subprocess

def generate_plantuml_diagram(plantuml_file):
    try:
        subprocess.run(["plantuml", plantuml_file], check=True)
        print("PlantUML diagram generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PlantUML diagram: {e}")

if __name__ == "__main__":
    plantuml_file = "bluedockerfile_plantuml.puml"
    generate_plantuml_diagram(plantuml_file)
