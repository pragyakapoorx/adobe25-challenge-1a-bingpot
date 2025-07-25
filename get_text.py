import fitz  # PyMuPDF
import re

def merge_fragments(text, min_overlap=2):

    #Merge repeated fragments based on overlapping content.
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    merged = []
    
    for line in lines:
        if not merged:
            merged.append(line)
        else:
            overlap = 0
            last = merged[-1]
            # Find maximal suffix of last that's prefix of current line
            for i in range(min_overlap, min(len(last), len(line)) + 1):
                if last[-i:] == line[:i]:
                    overlap = i
            if overlap:
                merged[-1] = last + line[overlap:]
            else:
                merged.append(line)
    return " ".join(merged)

def extract_and_clean_text(pdf_path):
    doc = fitz.open(pdf_path)
    raw_text = ""
    for page in doc:
        raw_text += page.get_text("text", flags=0) + "\n"
    
    cleaned_text = merge_fragments(raw_text)
    return cleaned_text

pdf_path = "E:/Academics/Adobe_Hackathon25/GitHub_Adobe-Hackathon25/Challenge_1a/sample_dataset/pdfs/file03.pdf"
final_text = extract_and_clean_text(pdf_path)
print(final_text)
