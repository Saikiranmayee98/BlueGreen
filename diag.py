import subprocess

def generate_diagram(input_file, output_format="png"):
    output_file = f"output.{output_format}"
    try:
        subprocess.run(["plantuml", f"-t{output_format}", f"-o.", input_file], check=True)
        print(f"Diagram generated successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating diagram: {e}")

if __name__ == "__main__":
    input_file = "sequence.puml"
    generate_diagram(input_file)
