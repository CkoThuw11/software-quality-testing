# Software Quality Testing

## Project Structure
```
software_testing/
│
├── Jenkinsfile
├── calculator/
│   ├── __init__.py
│   └── operations.py
│
├── tests/
│   ├── __init__.py
│   └── test_operations.py
│
├── requirements.txt
└── README.md
```
## Set up project and run
### Step 1: Run Jenkins in Docker

1. **Create a Docker network**:
```
docker network create jenkins-net
```
2. **Start Jenkins container**:
```
docker run -d --name jenkins \
      -p 8080:8080 -p 50000:50000 \
      --network jenkins-net \
      -v jenkins_home:/var/jenkins_home \
      jenkins/jenkins:lts
```
3. **Access Jenkins at** `http://localhost:8080`
4. **Unlock Jenkins using the password from**:
```
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`
```
After login, Choose Install suggested plugins
    
5. **Install python**

**Access Jenkins container as root**:

```docker exec -u 0 -it jenkins bash```
    
**Install Python and pip**:

```apt update```

```apt install -y python3 python3-pip python3.13-venv```
    
**Verify installation**:

```python3 --version```

```pip3 --version```

6. **Install plugins**
* JUnit 
* HTML Publisher plugin
* Coverage Plugin
### Step 2: Create Jenkins Pipeline Job

1. Go to Jenkins dashboard → “New Item”
2. Name it `PythonDemoPipeline`
3. Choose “Pipeline” → OK
4. In “Pipeline” section:
    - Set “Pipeline script from SCM”
    - Choose “Git”
    - Enter your GitHub repo URL
    - Set branch to `main` `main` `feature` `fix`

### Step 3: Add GitHub Webhook

1. Go to GitHub repo → Settings → Webhooks
2. Add:
    - **Payload URL**: `http://your-public-jenkins-url/github-webhook/` (use ngrok)  
    - **Content type**: `application/json`
    - **Event**: “Just the push event”