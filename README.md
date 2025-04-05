# 🚀 **RedditFlow**  
### *A Scalable ETL Pipeline with Airflow, AWS, and Redshift*

**RedditFlow** is a powerful, scalable ETL pipeline built to extract Reddit data, transform it using AWS services, and load it into an Amazon Redshift data warehouse — all orchestrated using Apache Airflow. It's designed for cloud-native data engineering and analytics workflows.


## 📖 Overview
Overview
RedditFlow enables you to:

1. 🔍 **Extract** data from Reddit via its official API  
2. 📦 **Store** raw JSON data in **Amazon S3** using Airflow DAGs  
3. 🔄 **Transform** and catalog data with **AWS Glue** and **Athena**  
4. 🚀 **Load** clean, structured data into **Amazon Redshift** for querying and analytics  

Perfect for data engineers looking to scale Reddit data pipelines in the cloud!

---

## 🏗️ Architecture

![RedditDataEngineering](https://github.com/user-attachments/assets/6f2481c8-8dad-41f1-8e03-798b2714f199)

### 🔧 **Components:**

- **📡 Reddit API** – Source of posts, comments, metadata  
- **🛠️ Apache Airflow + Celery** – Workflow orchestration and task distribution  
- **🐘 PostgreSQL** – Airflow metadata DB and optional staging area  
- **🪣 Amazon S3** – Raw data lake for storing extracted files  
- **🧬 AWS Glue** – ETL and data cataloging engine  
- **📊 Amazon Athena** – Serverless SQL queries on S3 data  
- **🏢 Amazon Redshift** – Scalable, final data warehouse for analysis  

---

## ⚙️ Prerequisites

Before you begin, make sure you have:

- ✅ An AWS Account with permissions for **S3**, **Glue**, **Athena**, and **Redshift**
- ✅ Reddit API credentials (client ID & secret)
- ✅ **Docker** installed
- ✅ **Python 3.9+**

---

## 🧪 System Setup

### 1. 🚀 Clone the repository

```bash
git clone https://github.com/Ajay1812/Reddit_DataEngineering.git
cd RedditDataEngineering
```

### 2. 🐍 Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 4. ⚙️ Configure your environment

Edit `config.conf` and add your credentials and settings:

```ini
[database]
database_host = localhost
database_name = airflow_reddit
database_port = 5432
database_username = postgres
database_password = postgres

[file_paths]
input_path = /opt/airflow/data/input
output_path = /opt/airflow/data/output

[api_keys]
reddit_secret_key = [SECRET KEY HERE]
reddit_client_id = [CLIENT ID HERE]

[aws]
aws_access_key_id = [AWS ACCESS KEY ID]
aws_secret_access_key = [AWS SECRET ACCESS KEY]
aws_session_token = [AWS SESSION TOKEN]
aws_region = [AWS REGION]
aws_bucket_name = [S3 BUCKET NAME]

[etl_settings]
batch_size = 100
error_handling = abort
log_level = info
```

### 5. 🐳 Start Docker containers

```bash
docker-compose up -d
```

### 6. 🌐 Open the Airflow UI

```bash
open http://localhost:8080
```

---

## 📬 Contact

Got questions or want to contribute? Feel free to reach out!

- 📧 **Email**: [a.kumar01c@gmail.com](mailto:a.kumar01c@gmail.com)  
- 🔗 **GitHub**: [Ajay1812](https://github.com/Ajay1812)

---

### 🎉 Happy Data Engineering!

Let the data flow 🚀📈
