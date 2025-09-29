#!/usr/bin/env python3
"""
PDF Parser Script

A command-line tool that accepts a file path as an argument and processes the file.
Handles both PDF files and regular text files.

Usage:
    python parse_pdf.py <file_path>
    python parse_pdf.py --help

Requirements:
    pip install pypdf

"""

import sys
import os
import argparse
from typing import Tuple, Optional


def extract_pdf_text(file_path: str) -> Tuple[bool, Optional[str]]:
    """
    Extract text content from a PDF file.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        Tuple[bool, Optional[str]]: (success, extracted_text)
    """
    try:
        import pypdf
        
        with open(file_path, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            
            # Extract text from all pages
            full_text = ""
            for page_num, page in enumerate(pdf_reader.pages, 1):
                try:
                    page_text = page.extract_text()
                    full_text += f"\n--- Page {page_num} ---\n{page_text}\n"
                except Exception as e:
                    print(f"Warning: Could not extract text from page {page_num}: {e}")
                    continue
            
            return True, full_text.strip()
            
    except ImportError:
        print("Error: pypdf library not installed.")
        print("Install it with: pip install pypdf")
        return False, None
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return False, None


def read_text_file(file_path: str) -> Tuple[bool, Optional[str]]:
    """
    Read content from a text file.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        Tuple[bool, Optional[str]]: (success, file_content)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return True, content
    except UnicodeDecodeError:
        print(f"Error: Cannot read '{file_path}' as text file. It might be a binary file.")
        return False, None
    except Exception as e:
        print(f"Error reading text file: {e}")
        return False, None


def process_file(file_path: str) -> bool:
    """
    Process a file (PDF or text) and extract its content.
    
    Args:
        file_path (str): Path to the file to process
        
    Returns:
        bool: True if processing was successful, False otherwise
    """
    # Validate file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False
    
    # Validate it's a file (not a directory)
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a file.")
        return False
    
    # Get file extension
    file_extension = os.path.splitext(file_path)[1].lower()
    
    # Process based on file type
    success = False
    content = None
    
    if file_extension == '.pdf':
        success, content = extract_pdf_text(file_path)
    else:
        success, content = read_text_file(file_path)
    
    # Display results
    if success and content:   
        print(content)
        return True
    elif success and not content:
        return True
    else:
        return False


def main():
    """Main function to handle command-line arguments and execute file processing."""
    parser = argparse.ArgumentParser(
        description='Extract and display text content from PDF or text files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python parse_pdf.py document.pdf
  python parse_pdf.py notes.txt
        """
    )
    
    parser.add_argument(
        'file_path',
        help='Path to the file to process (PDF or text file)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='PDF Parser 1.0'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the file
    try:
        success = process_file(args.file_path)
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
