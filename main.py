import llm_clients
import pdf_processor


def save_to_file(content: str, filename: str):
    """Saves the output content to a standard text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Output successfully saved to {filename}")


def main():
    pdf_path = "Unit 11 Words and Phrases.pdf"
    print(f"Extracting text from {pdf_path}...")

    # Extract text using processor module
    raw_text = pdf_processor.extract_text(pdf_path)

    if not raw_text:
        print("No text extracted. Exiting programme.")
        return

    # Choose the AI provider
    provider = "gemini"  # Options: "gemini", "chatgpt", "mistral", "ollama"

    print(f"Sending text to {provider.capitalize()}...")

    # Route to the correct API client
    if provider == "gemini":
        output_text = llm_clients.call_gemini(raw_text)
    elif provider == "chatgpt":
        output_text = llm_clients.call_chatgpt(raw_text)
    elif provider == "mistral":
        output_text = llm_clients.call_mistral(raw_text)
    elif provider == "ollama":
        output_text = llm_clients.call_ollama(raw_text, "qwen2.5")
    else:
        print("Invalid provider selected.")
        return

    # Save the result
    output_filename = f"Unit_11_{provider}_output.txt"
    save_to_file(str(output_text), output_filename)


if __name__ == "__main__":
    main()
