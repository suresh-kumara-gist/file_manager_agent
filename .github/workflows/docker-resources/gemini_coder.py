import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_flutter_code(prompt: str) -> str:
    response = model.generate_content(
        f"""Generate Flutter code for: {prompt}. 
        Include: 
        1. Main Dart file with a File Explorer UI. 
        2. Use 'package:file_picker' and 'path_provider'. 
        3. Add a test case for file listing. 
        Return ONLY CODE, no explanations."""
    )
    return response.text

# def generate_flutter_code(prompt: str) -> str:
#     response = model.generate_content(
#         f"""Generate Flutter code for: {prompt}. 
#         Include:
#         1. Firebase Storage integration for cloud sync.
#         2. File upload/download functionality.
#         3. Provider state management.
#         Return ONLY Dart code."""
#     )
#     return response.text

# "Generate a Flutter file manager with platform-specific behaviors: \
# 1. Android/iOS: Use `path_provider` \
# 2. Windows: Use `dart:io` for direct filesystem access \
# 3. macOS: Support Finder integration"
