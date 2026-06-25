import os
from langchain_community.document_loaders.pdf import PyPDFLoader

def load_all_pdfs(folder_path):
    all_docs = []
    num_docs = 0

    try:
        print("Scanning folder:", folder_path)
        files = os.listdir(folder_path)
        print("Files found:", files)

        for filename in files:
            if filename.lower().endswith(".pdf"):

                pdf_path = os.path.join(folder_path, filename)
                print("Loading:", pdf_path)

                loader = PyPDFLoader(pdf_path)
                doc = loader.load()

                print(f"{filename} -> pages loaded:", len(doc))

                # ❗ IMPORTANT CHECK
                if not doc:
                    print(f"WARNING: No content in {filename}")
                    continue

                all_docs.extend(doc)
                num_docs += 1

        print("TOTAL PDFs processed:", num_docs)
        print("TOTAL pages collected:", len(all_docs))

        return all_docs

    except Exception as e:
        print("Error loading PDF:", e)
        print("TOTAL DOCS LOADED (safe):", len(all_docs))
        return []