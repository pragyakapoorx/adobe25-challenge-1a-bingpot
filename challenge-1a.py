import os
import fitz  # PyMuPDF
import json
import re

INPUT_DIR = "app/input"        #replace with your file location
OUTPUT_DIR = "app/output"

def merge_fragments(text, min_overlap=2):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    merged = []
    for line in lines:
        if not merged:
            merged.append(line)
        else:
            last = merged[-1]
            overlap = 0
            for i in range(min_overlap, min(len(last), len(line)) + 1):
                if last[-i:] == line[:i]:
                    overlap = i
            if overlap:
                merged[-1] = last + line[overlap:]
            else:
                merged.append(line)
    return merged

def detect_headings(lines):
    headings = []
    for i, line in enumerate(lines):
        if len(line) > 120 or len(line) < 3:
            continue

        # Strong candidate: short, mostly capitalized or title case, with no trailing punctuation
        if (line.isupper() or re.match(r'^[A-Z][A-Za-z0-9 ,\-]+$', line)) and not re.match(r'.+[.:;,!?]$', line):
            headings.append((i, line))
    return headings

def classify_heading_level(text, prev_level):
    word_count = len(text.split())
    if word_count <= 3:
        return "H1"
    elif word_count <= 6:
        return "H2"
    else:
        return "H3"

def process_pdf(filepath):
    doc = fitz.open(filepath)
    title = ""
    outline = []

    for page_num, page in enumerate(doc, start=1):
        if page_num > 50:
            break

        raw_text = page.get_text("text", flags=0)
        merged_lines = merge_fragments(raw_text)

        # First non-empty line from page 1 as title candidate
        if page_num == 1 and not title:
            for line in merged_lines:
                if len(line.strip()) >= 5:
                    title = line.strip()
                    break

        page_headings = detect_headings(merged_lines)
        for idx, text in page_headings:
            level = classify_heading_level(text, prev_level=None)
            outline.append({
                "level": level,
                "text": text.strip(),
                "page": page_num
            })

    filename = os.path.splitext(os.path.basename(filepath))[0]
    json_path = os.path.join(OUTPUT_DIR, f"{filename}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "title": title,
            "outline": outline
        }, f, indent=2, ensure_ascii=False)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            process_pdf(os.path.join(INPUT_DIR, filename))

if __name__ == "__main__":
    main()
