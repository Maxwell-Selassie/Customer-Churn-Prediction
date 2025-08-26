import os
from pathlib import Path

project_name = 'maxMLproejct'
list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data ingestion.py',
    f'src/{project_name}/components/data transformation.py',
    f'src/{project_name}/components/model trainer.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}notebooks/__init__.py',
    f'src/{project_name}/notebooks/eda.ipynb',
    f'src/{project_name}/notebooks/model training.ipynb',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    'params.yaml',
    'schema.yaml',
    'logging.yaml',
    'app.py',
    'main.py',
    'log_setup.py',
    'templates/index.html',
    'Dockerfile'
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0) :
        with open(filepath,'w') as file:
            pass
