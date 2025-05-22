import os
import glob

# Base directory containing the category folders
base_dir = "data/sample_cv"

def keep_top_20_pdfs(base_dir):
    # Iterate through each category folder
    for category in os.listdir(base_dir):
        category_path = os.path.join(base_dir, category)
        
        # Ensure it's a directory
        if os.path.isdir(category_path):
            # Get all PDF files in the category folder
            pdf_files = glob.glob(os.path.join(category_path, "*.pdf"))
            
            # Extract numeric part from filenames and sort them
            pdf_files_sorted = sorted(pdf_files, key=lambda x: int(os.path.basename(x).split('.')[0]))
            
            # Keep only the top 20 files
            files_to_keep = pdf_files_sorted[:20]
            files_to_delete = pdf_files_sorted[20:]
            
            # Delete the rest of the files
            for file in files_to_delete:
                os.remove(file)
                print(f"Deleted: {file}")

if __name__ == "__main__":
    keep_top_20_pdfs(base_dir)