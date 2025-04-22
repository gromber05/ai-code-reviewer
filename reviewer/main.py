from groq import analyze_code_with_groq
from github_api import post_comment
import os
import gc

def get_files(repo_path, extensions=None):
    """
    Obtiene los archivos del repositorio que coincidan con las extensiones especificadas.

    @param repo_path: Ruta del repositorio.
    @param extensions: Lista de extensiones de archivo a incluir (por ejemplo, ['.py', '.js']).
    @return: Lista de rutas de archivos que coinciden con las extensiones.
    """
    if extensions is None:
        extensions = ['.py']

    files = []
    for root, _, files_in_dir in os.walk(repo_path):
        for file in files_in_dir:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) > 10 * 1024 * 1024: 
                    print(f"Skipping large file: {file_path}")
                    continue
                files.append(file_path)
    return files

def clean_console():
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def run_code_review():
    """
    Ejecuta el proceso de revisión de código para los archivos especificados en el repositorio.
    """
    clean_console()
    repo_path = input("Enter the path to the repository (default: current directory): ").strip()
    if not repo_path:
        repo_path = "."

    extensions = input("Enter file extensions to include (comma-separated, e.g., .py,.js,.html): ").strip()
    if not extensions:
        extensions = ".py"  # Valor predeterminado
    extensions = [ext.strip() for ext in extensions.split(",")]

    files_to_review = get_files(repo_path, extensions)

    for file_path in files_to_review:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()

        review = analyze_code_with_groq(code, file_path)
        output_file = f"./output/{os.path.basename(file_path)}_review.md"
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# Code Review for {file_path}\n\n")
            md_file.write(review)
        print(f"Review for {file_path} has been saved to {output_file}")

        post_comment(review)

        del code
        del review
        gc.collect()
        print(f"Memory cleaned after processing")
        print("Finished processing file:", file_path)
        print("--------------------------------------------------")

if __name__ == "__main__":
    run_code_review()