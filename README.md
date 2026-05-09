**FRESHERS JOB AGGREGATOR**

🚀 GETTING STARTED (BACKEND SETUP)			

1. 	CREATE A FOLDER IN YOUR DESKTOP FROM FILE MANAGER OR COMMANDS
   
      OPEN THAT CREATED FOLDER IN VSCODE:
      
       
      EXAMPLE : FOLDER IS test_folder
      
      
      OPEN test_folder in VSCODE  

3. JUST COPY THIS CODE AND PASTE IN TERMINAL  UNTIL STEP 4


3.CLONE REPO :
```bash
git clone https://github.com/RitikM-AiDev/Freshers-Job-Aggregator-backend.git
```

3. CREATE AND ACTIVATE VIRTUAL ENVIRONMENT

i)  WINDOWS:
RUN THIS TO INSTALL ALL REQUIRED LIBRARIES:
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```

ii)
MACOS/LINUX:
RUN THIS TO INSTALL ALL REQUIRED LIBRARIES:
```bash
 python3 -m venv venv
```
```bash
source venv/bin/activate
```
iii)
RUN THIS TO INSTALL ALL REQUIRED LIBRARIES:
```bash
pip install -r requirements.txt
```
```bash
playwright uninstall
```
```bash
playwright install chromium
```

4. START THE FASTAPI SERVER

USE UVICORN TO LAUNCH THE BACKEND:
```bash
uvicorn server:app --reload
```

5.Frontend URL:
PASTE IT IN CHROME BROWSER IN URL SEARCH BAR
```bash
https://freshers-job-aggregator.vercel.app/
```
6. LOCAL ACCESS URLS

ONCE THE TERMINAL SAYS "UVICORN RUNNING," OPEN YOUR BROWSER TO:

LOCAL SERVER:
```bash
http://127.0.0.1:8000
```
