import subprocess
import os

class FlutterBuilder:
    def __init__(self, app_name: str):
        self.app_name = app_name
        self.project_dir = os.path.abspath(app_name)

    def create_project(self):
        subprocess.run(f"flutter create {self.app_name}", shell=True, check=True)

    def add_dependencies(self):
        pubspec = f"{self.project_dir}/pubspec.yaml"
        with open(pubspec, "a") as f:
            f.write("\ndependencies:\n  file_picker: ^5.3.3\n  path_provider: ^2.1.1\n")

    def setup_firebase(self):
        # Add Firebase dependencies
        with open(f"{self.project_dir}/pubspec.yaml", "a") as f:
            f.write("\ndependencies:\n  firebase_core: ^2.18.0\n  firebase_storage: ^11.7.0\n")

        # Auto-download google-services.json (mock for demo)
        os.makedirs(f"{self.project_dir}/android/app", exist_ok=True)
        with open(f"{self.project_dir}/android/app/google-services.json", "w") as f:
            f.write("""{"project_info": {"project_id": "your-project-id"}}""")

    def write_code(self, code: str):
        lib_dir = f"{self.project_dir}/lib"
        os.makedirs(lib_dir, exist_ok=True)
        with open(f"{lib_dir}/main.dart", "w") as f:
            f.write(code)

    def generate_keystore(self):
        keystore_path = f"{self.project_dir}/android/app/upload-keystore.jks"
        subprocess.run(
            f"keytool -genkey -v -keystore {keystore_path} "
            "-alias uploadkey -keyalg RSA -keysize 2048 -validity 10000 "
            "-storepass android -keypass android -dname 'CN=Android'",
            shell=True, check=True
        )

    def build_apk(self):
        self.generate_keystore()
        subprocess.run(
            f"cd {self.project_dir} && "
            "flutter build apk --release && "
            "cp ./build/app/outputs/flutter-apk/app-release.apk ./file_manager.apk",
            shell=True, check=True
        )
    # def build_app_bundle(self):
    #     subprocess.run(
    #         f"cd {self.project_dir} && "
    #         "flutter build appbundle --release", 
    #         shell=True, check=True
    #     )
