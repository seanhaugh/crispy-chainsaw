# main.py

from serp import get_competitors
from ahrefs_api import get_target_keywords
from gpt_api import generate_meta_title, generate_headings, generate_faq_questions
from headings_processor import consolidate_headings
from utils import display_output

def main():
    # Input keyword/topic
    keyword = input("Enter the canonical topic/keyword: ").strip()
    
    # H1
    h1 = keyword

    # Meta Title
    meta_title = generate_meta_title(keyword)

    # Competitors
    competitors = get_competitors(keyword)

    # Target Keywords
    target_keywords = get_target_keywords(competitors)

    # Suggested Headings
    all_headings = consolidate_headings(competitors)
    suggested_headings = generate_headings(all_headings, keyword)

    # FAQ Questions
    faq_questions = generate_faq_questions(keyword, suggested_headings)

    # Display the output
    display_output(
        h1,
        meta_title,
        competitors,
        target_keywords,
        suggested_headings,
        faq_questions
    )

if __name__ == "__main__":
    main()
