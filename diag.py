import subprocess

def generate_plantuml_diagram(plantuml_code):
    try:
        # Write the PlantUML code to a file
        with open("diagram.puml", "w") as file:
            file.write(plantuml_code)
        
        # Call the PlantUML CLI to generate the diagram
        subprocess.run(["java", "-jar", "plantuml.jar", "bluedockerfile_palntuml.puml"], check=True)
        print("PlantUML diagram generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PlantUML diagram: {e}")

if __name__ == "__main__":
    # PlantUML code to generate the diagram
    plantuml_code = """
    @startuml
    package "Service" {
        [blue-service]
    }

    package "Spec" {
        [type: ClusterIP]
        [selector]
        [ports]
    }

    [blue-service] --> [type: ClusterIP] : spec
    [blue-service] --> [selector] : spec
    [blue-service] --> [ports] : spec

    [ports] --> [protocol: TCP]
    [ports] --> [port: 80]
    [ports] --> [targetPort: 80]
    @enduml
    """

    # Generate the PlantUML diagram
    generate_plantuml_diagram(plantuml_code)
