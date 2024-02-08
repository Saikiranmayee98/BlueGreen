import plantuml

uml_code='''
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

'''
 
#Set the PlantUML server URL (public PlantUML server)
url = "http://www.plantuml.com/plantuml/img/"
 
# Create a PlantUML object with the URL
plantuml_obj = plantuml.PlantUML(url=url)
 
# Generate and save the diagram image
with open("diagram3.png", "wb") as f:
    img = plantuml_obj.processes(uml_code)
    f.write(img)