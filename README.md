# GTPNutriCount Photo Selector Analyzer

[gpt-engineer](https://github.com/gpt-engineer-org/gpt-engineer) generated project, case study, fully operational. gpt-engineer prompts used are in prompt00 and prompt01 files. prompt01 was executed using the `--improve` flag to `gpt-engineer`.

## Description

GPTNutriCount assists users in counting calories and macronutrients based on photos of their meals taken throughout the day.

GPTNutriCount Photo Selector is a component of GPTNutriCount. It is a command-line tool that finds photos in a specified folder, converts them to a supported image format if necessary, and uses OpenAI's GPT-4 Vision model to determine if the photo contains a food or drink item. If the photo does contain a food or drink item, it is kept in the target folder, which folder is also specified via a command line argument.

GPTNutriCount Photo Selector only processes photos in the input folder created on a specific date, which is also provided as a command line argument. If this command line argument is omitted, the tool will find photos created on the current date.

The prompt is specified in the file, which can be replaced to anything, hence allowing for analysing any other properies of photos in the input folder.

## Usage
To use the tool, run the following command in your terminal:

    python -m main ~/Pictures/AllPhotos ~/Pictures/NutriCount --date '2024-01-23' --prompt_file 'nutricount-photo-select-prompt.txt'

## Requirements
- Python 3.11
- Install the required packages using:

    pip install -r requirements.txt