package main

deny[msg] {
    input.InstanceType == "t3.xlarge"
    msg := "Instance type not supported within the organisation"
}