Hi, 

I have implemented python service using "fastAPI". I decided to use fastAPI to ensure high performance and scalabe server. 

The service have two endpoints:

1. /events – which will get a sentence and counts the number of the occurrence of the following keywords – “checkpoint”, “avanan”, “email” and “security”.
  I used asyncio library to ensure the counting operation will execute async. 
  
2. /stats – which will get time interval (in seconds) and will return a JSON with the number of occurrence of the above keywords in the received interval time.
  
Installation-

1. Clone the project. run "git clone https://github.com/aviranGit/JobMatcher.git"
2. Install app requirements - run "pip install -r requirements.txt"
3. Navigate to src folder. "cd src"
4. In order to run the server - run "uvicorn main:app --reload"

Using CLI commands:

1. Run the following command with your own sentence.   - ' curl -X POST "http://localhost:8000/api/v1/events" -d "YOUR_SENTENCE"  '
   For example - curl -X POST "http://localhost:8000/api/v1/events" -d "Avanan is a leading Enterprise Solution for Cloud Email and Collaboration Security"
   
   
2. Run the following command to recieve the occurrence of the required words - curl -X GET "http://localhost:8000/api/v1/stat/?interval=YOUR_INTERVAL"
   For example, curl -X GET "http://localhost:8000/api/v1/stat/?interval=80" (will recive the occurrence of the words within the 80 last seconds)
   

Docker support:

1. I defined the "DockerFile" to support the service to run in docker/ 
2. To build the image run the following command in the repostory directory:
    2.1 docker build -t myimage .
    2.2 docker run -d --name mycontainer -p 80:80 myimage
 
 
For any questions, feel free to contact me:)
Aviran
