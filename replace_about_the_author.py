from docx import Document
import os

def get_last_two_headings(doc):
    heading1s = [p for p in doc.paragraphs if p.style.name == 'Heading 1']
    last_two_headings = heading1s[-2:]
    return [h.text for h in last_two_headings]

def get_file_list(directory):
    return [file for file in os.listdir(directory) if file.endswith('.docx')]
    

def main():
    directory = r'C:\Users\Dell Latitude 7400\OneDrive\Books\Copies to upload for Pride and Prejudice'
    book_list = get_file_list(directory)

    for filename in book_list:
        doc = Document(filename)
        last_two_headings = get_last_two_headings(doc)
        print(f'Last two headings in {filename}: {last_two_headings}')

if __name__ == "__main__":
    main()
