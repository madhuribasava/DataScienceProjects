## Introduction
This project’s objective is to find which city in the US has the most illnesses
so we can build facilities and provide more services to improve people’s health. 
Big Data Components used for this project are HDFS, Spark, and Yarn. 
The big city health dataset is uploaded into HDFS and seamlessly integrated 
into Spark. PySpark is used for data analysis and machine learning integration.

## Installation
In Google Cloud Console, register a project and spin up an ubantu instance.
Start HDFS, Spark and Yarn as mentioned in google-cloud-deploy.pdf file.


## Folder contents
It consists of 4 files:

1) Big_Cities_Health_Data_Inventory.csv is a dataset related to Big cities health data taken from the Kaggle website 
2) FinalProject.doc is the Project summary file.
3) FinalProject.pdf is the Project summary file in pdf format.
4) google-cloud-deploy.pdf is the doc that can be followed for installation.


## Methodology

The methodology followed here is to store the dataset in 
HDFS (Hadoop Distributed File storage system), process the large data set with Spark, 
analyze the results, and build a Machine Learning model to identify which places 
need more facilities/services to improve people's health.