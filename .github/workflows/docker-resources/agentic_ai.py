from gemini_coder import generate_flutter_code
from build_flutter import FlutterBuilder
import argparse

def main():
    parser = argparse.ArgumentParser(description="Agentic AI Flutter Builder")
    parser.add_argument("--name", help="App name", default="file_manager")
    parser.add_argument("--prompt", help="App features", default="A File Manager app for Android with dark mode.")
    args = parser.parse_args()

    # Generate code via Gemini
    print("🚀 Generating Flutter code with Gemini...")
    code = generate_flutter_code(args.prompt)

    # Build Flutter project
    print("🛠️  Building Flutter project...")
    builder = FlutterBuilder(args.name)
    builder.create_project()
    builder.add_dependencies()
    builder.write_code(code)
    builder.build_apk()

    print("✅ Done! APK is ready in /build folder.")

if __name__ == "__main__":
    main()


