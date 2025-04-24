# atropos-projects

### The Question

Build an API to manage long running tasks

Implement operations that can at a minimum:

- Create tasks

- Check  task status

- Retrieve task results

Assume tasks may take a significant amount of time to complete (e.g., data processing tasks, report generation, video processing).  

Guidelines

- You're free to choose any language/platform/stack, just be prepared to talk about them.

- Assume that this will be production code that will need to be supported by a separate infrastructure team.

- Provide some information about how to deploy the service locally for our team to be able to review

- Build a basic front-end

[OPTIONAL] - Extra points for using:

- A containerization technology like Docker

- Testing framework

- A more advanced, feature-rich front-end

- Integration with a cloud provider's services that you think can help

#############################################################################
#
# Aaron Cody
# 4/17/2025
#

# REFERENCES
  [FastAPI docs](["fastapi[standard]"](https://fastapi.tiangolo.com/))

  [uvicorn HTTP server](https://www.uvicorn.org/)
# Local DevBox Assumptions
- Clone GitHub repo:
 
      git clone git@github.com:miramar-labs/atropos-projects.git
- Python 3.12.8 virtual environment (pyenv)

        pyenv install 3.12.8
        pyenv virtualenv 3.12.8 atropos
        cd atropos-projects
        pyenv local 3.12.8

        pip install -r requirements.txt

- Evaluation Tools:
  - [Docker](https://www.docker.com/)
  - [Docker Compose](https://docs.docker.com/compose/)
  
- Development Tools [optional]
  - [vscode](https://code.visualstudio.com/)

# Solution - Phase 1
