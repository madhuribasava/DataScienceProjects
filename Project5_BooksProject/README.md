## Introduction
The purpose of this project is to consolidate all the book’s data into records which I can store in the database to 
 serve the customers effectively as all the data will be in one place.
 First, I took the books.csv file downloaded from the internet and applied transformations. I cleaned the data as necessary 
 and saved it in a CSV file. Link to books.csv: https://www.kaggle.com/code/aiswaryarana/7k-books/input?select=books.csv
 Second, I scraped the website for book data and applied transformations to clean the data and format it as necessary.
 Link to website: https://wpdatatables.com/documentation/table-examples/catalog-of-books/
 Third, I called APIs to get the book data based on the ISBN value, applied some transformations to it, and saved it to a CSV file.
 Link to the website to call the API: https://openlibrary.org/dev/docs/api/books
 Fourth, I read all the above three CSV files into individual data frames, connected them to the SQLite database, and saved them
 into three tables.
 Fifth, I combined the three tables into a single table based on the common ISBN, created a data frame from it, 
 and applied visualizations.

## Dataset
The3 datasets used in this project contains information on books.

## Installation
To get a local copy up and running, follow these steps:
1) Clone the repository
2) Create a virtual environment
3) Install dependencies

## Project Contents
This Project Repo consists of toal 6 files:
out of which there are 3 data files:
1) Books_excel.csv taken from the Kaggle website (Link to books.csv: https://www.kaggle.com/code/aiswaryarana/7k-books/input?select=books.csv)
2) Books_website.csv 
	Link to website: https://wpdatatables.com/documentation/table-examples/catalog-of-books/
3) Books_APIs_latest.csv 
	to the website to call the API: https://openlibrary.org/dev/docs/api/books
4) CombinedBooksData_excel.csv: It is the combined dataset of the above 3 data files.
5) BooksProjectSummary.doc: It has the Summary of the Books Project.
6) Books_Project.pdf has the all details of python code for this project.
7) Milestone5.ipynb has the python code file

## Run
Run Milestone5.ipynb file in Jupiter notebook.

## Data
The project uses a dataset containing various metrics such as ISBN, title,
subtile, authors, published year, etc.

## Evaluation
Combined the data from dataset, books website and books api and 
stored in a database to serve as a central storage for the all books.