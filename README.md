# Bank Marketing Campaign Prediction with MLOps & CI/CD 🚀

Predict customer responses to bank marketing campaigns using machine learning with **end-to-end MLOps** and **CI/CD deployment** on AWS. Automates model training, testing, and deployment in a scalable, containerized environment.

---

##**Key Features:**
- Developed ML models for customer response prediction.
- Created reusable pipeline with modular components: constants, entities, pipeline, and main file.
- Implemented running environment using Conda and dependency management via `requirements.txt`.
- Deployed models using Docker containers on AWS EC2.
- Stored Docker images in AWS ECR for versioning and management.
- Configured CI/CD pipeline with GitHub Actions for automated deployment.
- Setup self-hosted GitHub runner on EC2 for deployment tasks.


---


  ##**Technologies & Skills:**
- **Programming:** Python 3.8
- **Machine Learning:** Model development, data preprocessing, pipeline creation
- **MLOps & CI/CD:** Docker, GitHub Actions, pipeline automation
- **Cloud & DevOps:** AWS EC2, AWS ECR, IAM, environment variable configuration
- **Version Control:** GitHub
- **Environment Management:** Conda, pip
- **Other Tools:** MongoDB for data storage


---


 ## **Workflow Overview:**
1. Setup project environment using Conda and `requirements.txt`.
2. Implement ML pipeline with modular components.
3. Build Docker image of the project source code.
4. Push Docker image to AWS ECR.
5. Launch EC2 instance and pull Docker image.
6. Run project container on EC2 with environment variables configured.
7. Automated deployment via GitHub Actions.

---

## 📂 Project Structure
- `constants/` → Configuration constants  
- `entity/` → Data and model entities  
- `components/` → Core processing & model modules  
- `pipeline/` → Complete ML workflow  
- `main.py` → Entry point  

---

## ⚙️ Setup & Installation
```bash
# Create environment
conda create -n bank python=3.8 -y
conda activate bank
pip install -r requirements.txt

# Export environment variables
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>"
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

___


#☁️ AWS Deployment Steps

Build Docker image of the project

Push Docker image to AWS ECR

Launch EC2 instance and install Docker

Pull Docker image from ECR and run container

Optional: Set up self-hosted GitHub Actions runner

IAM Policies Needed:

AmazonEC2FullAccess

AmazonEC2ContainerRegistryFullAccess

# 🛠 Skills Applied

Programming & Data: Python, MongoDB, SQL

Machine Learning: Predictive modeling, ML pipelines

MLOps & Deployment: Docker, CI/CD, GitHub Actions, AWS EC2 & ECR

Business Analytics: Marketing campaign analysis, customer response prediction

# 🚀 How It Works

Data is fetched from MongoDB

Preprocessing & feature engineering

Model training and evaluation

Dockerized deployment on AWS EC2

Automated CI/CD with GitHub Actions

# 📈 Outcome

Accurate prediction of customer responses

Fully automated ML workflow and deployment

Scalable solution for future campaigns

