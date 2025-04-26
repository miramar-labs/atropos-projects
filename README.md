
# START HERE
- First, clone GitHub repo:
 
      git clone git@github.com:miramar-labs/atropos-projects.git

- Next, ensure you have the required tools:
  - [Docker](https://www.docker.com/)
  - [Docker Compose v2](https://docs.docker.com/compose/)
  
- Build the Docker containers:

      cd atropos-projects/backend
      docker compose build

- Run the containers:

      cd atropos-projects/backend
      docker compose up

  (you can watch logs from here and when done, stop everything with CTRL-C)

- Load the frontend UI in a browser tab:

      http://localhost:8000

- Load the REST API Swagger in another tab:

      http://localhost/8000/docs


- Configure Development Environment [optional]:
  
- [Install vscode](https://code.visualstudio.com/)

  - Install extensions:
   
    - Docker (microsoft)
    - Python (microsoft)
    - PyLance (microsoft)
    - Python Debugger (microsoft)
  
  
- [Install pyenv](https://github.com/pyenv/pyenv)
  
- Then create a python virtual environment:
  
        pyenv install 3.12.8
        pyenv virtualenv 3.12.8 atropos
        
        cd atropos-projects
        pyenv local 3.12.8

        cd backend
        pip install -r requirements.txt

- Run `vscode` and open the `atropos-projects` folder

# REFERENCES
  [FastAPI docs](https://fastapi.tiangolo.com/)

  [uvicorn HTTP server](https://www.uvicorn.org/)