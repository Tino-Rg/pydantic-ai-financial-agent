from pathlib import Path


def load_prompt(file_name: str) -> str:
    """
    Loads the content of a prompt file from the 'prompts' directory.

    Args:
        file_name (str): The name of the text file containing the prompt 
                         (e.g., 'system_prompt.txt').

    Returns:
        str: The raw text content of the prompt file.

    Raises:
        FileNotFoundError: If the specified prompt file does not exist.
    """

    current_dir = Path(__file__).resolve().parent

    file_path = current_dir.parent / "prompts" / file_name
    
    if not file_path.exists():
        raise FileNotFoundError(f"The prompt file was not found at: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()