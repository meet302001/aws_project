# End-to-End Blog Generation Pipeline using AWS Services

## Overview
This project implements an **End-to-End Blog Generation Pipeline** using AWS services. The pipeline leverages **AWS Lambda, S3, and Amazon Bedrock (Llama 3 8B model)** to generate high-quality blogs automatically.

## Features
- **Fully Serverless**: Uses AWS Lambda to handle blog generation.
- **AI-Powered**: Utilizes Amazon Bedrock's Llama 3 8B model for content generation.
- **Cloud Storage**: Stores generated blogs in AWS S3.
- **Event-Driven Execution**: Can be triggered via API Gateway or AWS EventBridge.

## AWS Services Used
- **AWS Lambda**: For executing the blog generation logic.
- **Amazon Bedrock (Llama 3 8B)**: AI model for text generation.
- **Amazon S3**: For storing the generated blog content.
- **API Gateway** (Optional): For exposing an API endpoint.
- **EventBridge** (Optional): For automating blog generation at scheduled intervals.

---

## Setup Guide
### 1. Clone the Repository
```sh
git clone https://github.com/meet302001/aws_project.git
cd aws_project
```

### 2. Create a Virtual Environment

#### **Windows (cmd or PowerShell)**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **Mac/Linux (Terminal)**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

---

## Contribution
Feel free to fork this repository, open issues, or submit pull requests!

## License
MIT License

---

## Author
Meet Bhanushali

