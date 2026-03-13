import argparse

import llm_clients
import pdf_processor


def save_to_file(content: str, filename: str):
    """Saves the output content to a standard text file."""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Output successfully saved to {filename}")


def main():

    parser = argparse.ArgumentParser(
        description="Convert PDF vocabulary tables to Anki format."
    )

    # Define the REQUIRED provider argument
    # choices enforces strict input validation before programme runs
    parser.add_argument(
        "provider",
        choices=["gemini", "chatgpt", "mistral", "ollama"],
        help="The AI provider to use for processing (gemini, chatgpt, mistral, or ollama)",
    )

    # Define input argument. nargs="?" makes it optional
    parser.add_argument(
        "input_file",
        nargs="?",
        default="input",
        help="The name of the input PDF file (defaults to input.pdf)",
    )

    # Define output argument
    parser.add_argument(
        "output_file",
        nargs="?",
        default="output",
        help="The name of the output text file (defaults to output.txt)",
    )

    args = parser.parse_args()

    pdf_path = args.input_file
    if not pdf_path.lower().endswith(".pdf"):
        pdf_path += ".pdf"

    output_filename = args.output_file
    if not output_filename.lower().endswith(".txt"):
        output_filename += ".txt"

    print(f"Extracting text from {pdf_path}...")

    # Extract text using processor module
    raw_text = pdf_processor.extract_text(pdf_path)

    if not raw_text:
        print("No text extracted. Exiting programme.")
        return

    # get AI provider from parsed arguments
    provider = args.provider

    print(f"Sending text to {provider.capitalize()}...")

    # Route to the correct API client
    if provider == "gemini":
        output_text = llm_clients.call_gemini(raw_text)
    elif provider == "chatgpt":
        output_text = llm_clients.call_chatgpt(raw_text)
    elif provider == "mistral":
        output_text = llm_clients.call_mistral(raw_text)
    elif provider == "ollama":
        output_text = llm_clients.call_ollama(raw_text, "qwen3.5")
    else:
        print("Invalid provider selected.")
        return

    # Save the result
    save_to_file(str(output_text), output_filename)


if __name__ == "__main__":
    main()
