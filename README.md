# Bank Marketing Campaign Prediction with MLOps & CI/CD 🚀

Predict customer responses to bank marketing campaigns using machine learning with **end-to-end MLOps** and **CI/CD deployment** on AWS. Automates model training, testing, and deployment in a scalable, containerized environment.

---

## 🌟 Project Highlights
- Predictive modeling for bank marketing campaigns  
- CI/CD automation with **GitHub Actions**  
- **Dockerized** application deployment  
- Scalable deployment on **AWS EC2** with **ECR**  
- End-to-end **ML pipeline automation**  

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

---



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

