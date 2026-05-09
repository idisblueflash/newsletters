import argparse
import re
from pathlib import Path


def add_space(text):
    urls = []

    def keep_url(match):
        urls.append(match.group(0))
        return f"\ue000{len(urls) - 1}\ue000"

    text = re.sub(r"https?://.*?[A-Za-z0-9](?=[\u4e00-\u9fff]|$)", keep_url, text)
    text = re.sub(r"([\u4e00-\u9fff])([A-Za-z0-9]+)", r"\1 \2", text)
    text = re.sub(r"([A-Za-z0-9]+)([\u4e00-\u9fff])", r"\1 \2", text)
    text = re.sub(r"([\u4e00-\u9fff])(\([A-Za-z0-9])", r"\1 \2", text)
    text = re.sub(r"([A-Za-z0-9]\))([\u4e00-\u9fff])", r"\1 \2", text)
    for index, url in enumerate(urls):
        text = text.replace(f"\ue000{index}\ue000", f" {url} ")
    return text.strip()


def format_file(input_path, output_path):
    text = Path(input_path).read_text(encoding="utf-8")
    Path(output_path).write_text(add_space(text), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Add spaces between Chinese and halfwidth text in a Markdown file.")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("output", help="Output Markdown file")
    args = parser.parse_args()
    format_file(args.input, args.output)


if __name__ == "__main__":
    main()
