# Python DevOps Automation Repository

This repository contains Python scripts for various DevOps automation tasks including local backups, AWS S3 operations, and Terraform automation.

## 📂 Repository Structure

~~~
python-devops/
├── backup_scripts/
│ ├── local_backup.py
│ └── s3_upload.py
├── terraform_automation/
│ └── terraform_runner.py
└── README.md

~~~

## 🛠️ Scripts Overview

### 1. Local Backup System (`local_backup.py`)
Creates compressed backups of specified directories with date-stamped filenames.

**Features:**
- Creates gzipped tar archives
- Automatically names backups with current date
- Handles Windows file paths correctly

**Usage:**
```python
source = r"C:\path\to\source"
destination = r"C:\path\to\backup\folder"
backup_files(source, destination)


2. AWS S3 Operations (s3_upload.py)
Manages AWS S3 buckets and file uploads using boto3.

Functions:

show_buckets(): Lists all S3 buckets

create_bucket(): Creates new S3 buckets

upload_backup(): Uploads files to S3 with custom keys

Dependencies:

pip install boto3

~~~
s3 = boto3.resource('s3')
bucket_name = "your-bucket-name"
region = "your-region"  # e.g., 'us-west-2'
~~~

3. Terraform Automation (terraform_runner.py)
Executes Terraform commands through Python subprocess.

Features:

Safe command execution with error handling

Directory context management

Output capture and display

Usage Example:

~~~
directory = r"C:\path\to\terraform\configs"
command = f"terraform -chdir={directory} init"
terraform_run(command)
~~~

🚀 Getting Started
Prerequisites:

Python 3.6+

AWS CLI configured (for S3 operations)

Terraform installed (for infrastructure automation)

Install dependencies:

~~~
pip install boto3
~~~

Configuration:

Set correct paths in backup scripts

Configure AWS credentials for S3 access

Update Terraform directory paths

🔧 Common Operations
Creating and Uploading Backups

~~~
# Local backup
backup_files(source_path, backup_destination)

# Upload to S3
upload_backup(s3_client, local_file, bucket_name, s3_key_name)
~~~

Terraform Workflow
~~~
# Initialize
terraform_run("terraform -chdir=path/to/config init")

# Plan
terraform_run("terraform -chdir=path/to/config plan")

# Apply
terraform_run("terraform -chdir=path/to/config apply")
~~~
💡 Best Practices
Always use raw strings (r"") for Windows paths

Store AWS credentials securely using AWS CLI configuration

Use error handling for production deployment

Regularly test backup restoration process

🚀 Future Improvements
Add error handling for backup operations

Implement backup rotation policy

Add S3 bucket policy management

Extend Terraform automation with state management



