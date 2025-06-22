<h1 align="center">Diagnosify</h1>

## 🔍 Overview
This AI agent follows the Model Context Protocol (MCP) to:

 - Process patient symptoms using NLP

 - Extract relevant medical insights from structured & unstructured data

 - Cross-reference with PubMed research for evidence-based diagnostics

 - Generate a ranked list of possible conditions with confidence scores

Built for **doctors, medical researchers, and healthcare AI applications**.


## 🛠️ Features

### 1. Symptom Analysis & Context Extraction
 - NLP-powered symptom parsing

 - Key medical concept extraction (e.g., duration, severity, related conditions)

### 2. AI-Powered Differential Diagnosis
 - GPT-3.5-turbo generates possible conditions based on symptoms

 - Confidence scoring for each potential diagnosis

### 3. PubMed API Integration
 - Real-time medical research lookup

 - Summarization of the latest studies related to symptoms

### 4. Explainable AI (XAI) Output
 - Clear reasoning for each diagnosis

 - Citations from medical literature


## ⚙️ Setup
### Prerequisites
 - Python 3.9+

 - OpenAI API key

 - PubMed API access (optional)

### Installation
```bash
git clone https://github.com/your-repo/medical-diagnosis-ai.git  
cd medical-diagnosis-ai  
pip install -r requirements.txt
```
### Configuration
Add your API keys to `config.yaml`:

```yaml
openai_api_key: "your-api-key"  
pubmed_api_key: "optional-pubmed-key"  
```


