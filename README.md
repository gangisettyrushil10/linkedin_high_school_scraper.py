This Python script extracts high school information from LinkedIn profiles using pre-scraped HTML files which I simulated by having ChatGPT randomly generate HTML files.
From an input CSV file it reads LinkedIn profile URLs and processes the corresponding local HTML files to output the extracted high school information to a new output CSV file.

The required libraries for running this script are beautifulsoup4 (for HTML parsing) and pandas (for reading in CSV files)

To use the script you must provice an input CSV file with the following format: 

Because Linkedin does not allow scraping as it violates their terms I simulated the profiles and stored them locally

LinkedIn URL,HTML File
https://www.linkedin.com/in/johndoe,human1.html
https://www.linkedin.com/in/janesmith,human2.html
https://www.linkedin.com/in/michaelbrown,human3.html
...

After ensuring the HTML files are in the same directory as the script you can then run the python script to yield an output of the LinkedIn profile and their associated high school

Errors are handled intuitively by printing messages such as "HTML file not found" or "High School not found" for the associated encountered error

