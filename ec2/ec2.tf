resource "aws_instance" "neoway_ec2" {
  ami = "ami-08d4ac5b634553e16"
  instance_type = "t2.micro"
  key_name = "aws_key"
  vpc_security_group_ids = [aws_security_group.neoway_sg_allow_http.id, aws_security_group.neoway_sg_allow_ssh.id]

  tags = {
      Name = "neoway_ec2" 
      Terraform   = "true"
  }
}

resource "aws_key_pair" "aws_key" {
  key_name   = "aws_key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqGYdjAtPgtwXtQgdhM3dfgRcB6lT8jJ+AHAPCGCrqwpW/5YpphqNm3s4PPLjAJqEDybx1e6JiNmYFPJ6SlE6uX6KQsLtby1NdcbMaqSjGu9CbRsIseOnv8tyHGjgGysREG5FHCko9y/zCST2nl4EHO6hfL1xRt43noSkC27NCyLkLpuxCpmz5dM/D1HiSu1pMX3QZOJKWdZJOLhmcmTNNtaBibzAvo9ChkIGYPmirlxO9fqRwGGN5WMtSq5eExuY2vsT50y+iBEou5thTDIy3wYeShmfdrJorPK8kYqKUTawAXZ1t1zG+J4uFdybpDzUyQ36o9gPR0J6/9c3Cdhxv rafael.magalhaes@inv001183"
}