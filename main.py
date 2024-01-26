import argparse
import os
from datetime import datetime
from photo_finder import PhotoFinder
from image_processor import ImageProcessor
from openai_client import OpenAIClient
from prompt_loader import PromptLoader

def main(input_folder, target_folder, date, prompt_file):
    # Load the prompt
    prompt = PromptLoader.load_prompt(prompt_file)

    # Initialize the OpenAI client
    openai_client = OpenAIClient(prompt)

    # Find photos
    photo_finder = PhotoFinder(input_folder, date)
    photos = photo_finder.find_photos()
    print(f'All photos found on day {date}: {photos}')

    # Process images
    image_processor = ImageProcessor(target_folder, date)
    image_processor.process_images(photos, openai_client)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GPTNutriCount Photo Selector")
    parser.add_argument("input_folder", help="The folder where photos are located")
    parser.add_argument("target_folder", help="The folder where selected photos will be stored")
    parser.add_argument("--date", help="The date for which to find photos (YYYY-MM-DD). Defaults to today's date.", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--prompt_file", help="The file containing the prompt for OpenAI API", default="nutricount-photo-select-prompt.txt")
    args = parser.parse_args()

    print(f'Input folder: {args.input_folder}')
    print(f'Target folder: {args.target_folder}')
    print(f'Date: {args.date}')
    print(f'Prompt file: {args.prompt_file}')

    main(args.input_folder, args.target_folder, args.date, args.prompt_file)