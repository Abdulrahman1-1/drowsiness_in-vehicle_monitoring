## Agentic In-Vehicle Monitoring System


1. Install CrewAI  
Follow the official [installation guide](https://docs.crewai.com/installation)

2. Create Your Project  
Use the CLI command below to scaffold your CrewAI project:
```
crewai create crew <your_project_name>
```
Replace `<your_project_name>` with your desired project name.

3. Add Your Files  
Find, copy, and paste the following files into your project's src folder:
- `main.py`
- `crew.py`
- `custom_tool.py`
- `agents.yaml`
- `tasks.yaml`

4. Update Your Main File  
In `main.py`, make sure to import your crew like this:
```
from <your_project_name>.crew import VehicleMonitoringCrew
```
Replace `<your_project_name>` with your actual project name.

5. scenario8  
Make sure to put the folder `scenario8` in the project's root directory.

6. Run  
   Navigate to your project's root directory then type the CLI command: `crewai run`

---

## Drowsiness Detection Comparison

### Setup:
Create a new environment `(python 3.10)` and do:
```
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia
pip install transformers tensorboard
pip install openai
```

Also `pip install` the necessary modules shown in the `files`.

### Trained Models:  
You can download the trained models [from this link](https://mbzuaiac-my.sharepoint.com/:f:/g/personal/abdulrahman_almarzooqi_mbzuai_ac_ae/EvQ8EdsW-5hJssT97RrzPkQBiCz2BvkH3qnCg57zUXIrCQ?e=hLsngV)

### Dataset Source:  
The dataset used was downloaded from [Roboflow](https://universe.roboflow.com/yolo-yvl6h/drowsiness-fatigue_detection/dataset/4)

Format: Multi-Label Classification
