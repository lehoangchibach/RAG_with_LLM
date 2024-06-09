import PyPDF2
import argparse


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


# Example usage
if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file")
    args = parser.parse_args()

    # Extract text from the provided PDF
    extracted_text = extract_text_from_pdf(args.pdf_path)

    file_name = args.pdf_path.split('/')[-1]
    with open(f'./{file_name}.txt', 'w') as f:
      f.write(extracted_text)
    print(extracted_text)
