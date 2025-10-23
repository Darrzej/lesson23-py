from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return{"message":"created successfully", "Developer": developer}

@app.post("/projects/")
def create_projects(project: Project):
    return{"message":"Created Successfully", "Project":project}

@app.get("/projects/")
def get_project():
    sample_project = Project(
        title = "Sample Project",
        description = "This is a description",
        languages = ["Python", "JavaScript"],
        lead_developer = Developer(name="Leon Kastrati", experience=67)

    )
    return {"Project": [sample_project]}