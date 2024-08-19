import pandas as pd
from bs4 import BeautifulSoup

#retrieving high shcool information from html profile files
def extract_high_school(html_content):
    #instantiating beautiful soup object and html parser
    soup = BeautifulSoup(html_content, 'html.parser')
    #locating eductation section in the file
    education_section = soup.find('section', id='education-section')
    #return high school not found if there is no section found
    #profile 3 shows this being tested
    if not education_section:
        return "High School not found"

    #iterating through each list item in the education section
    for entry in education_section.find_all('li'):
        #checking if 'High School' is in the current list item
        if 'High School' in entry.text:
            #extracting the text from the <h3> tag if it exists
            h3_tag = entry.find('h3')
            if h3_tag:
                #return the text concisely
                return h3_tag.text.strip()

    return "High School not found"


def process_profiles(input_csv, output_csv):
    #reading csv to a pandas dataframe for ease of access
    profiles = pd.read_csv(input_csv)
    #list to store output results in
    output_data = []

    #iterating through the dataframe
    for index, row in profiles.iterrows():
        #getting current file name for analysis
        file_name = f"profile{index + 1}.html"

        try:
            #opening file in read mode and closing connection after execution
            with open(file_name, 'r', encoding='utf-8') as file:
                #reading current file into content variable
                html_content = file.read()
                #calling extract_high_school function on current file
                high_school = extract_high_school(html_content)
        #error handling if execptions are encountered
        except FileNotFoundError:
            high_school = "HTML file not found"
        except Exception as e:
            high_school = f"Error processing file: {e}"

        #storing output data from functions in list (linkedin urls and associated high school
        output_data.append([row['LinkedIn URL'], high_school])

    #converting output to a dataframe and writing to a new csv file
    pd.DataFrame(output_data, columns=['LinkedIn URL', 'High School']).to_csv(output_csv, index=False)
    print(f"Output written to {output_csv}")



if __name__ == "__main__":
    process_profiles('input_linkedin_profiles.csv', 'output_high_schools.csv')
