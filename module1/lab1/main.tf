# Intentionally misconfigured AWS infrastructure
resource "aws_s3_bucket" "data_bucket" {
  bucket = "company-sensitive-data-bucket"
  # Missing: encryption, versioning, public access block
}

resource "aws_security_group" "web_sg" {
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Critical: SSH open to world
  }
}

resource "aws_db_instance" "main_db" {
  allocated_storage = 20
  engine           = "mysql"
  engine_version   = "5.7"
  instance_class   = "db.t3.micro"
  # Missing: encryption_at_rest, backup_retention
  publicly_accessible = true  # Critical vulnerability
}

