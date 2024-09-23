def display_output(h1, meta_title, competitors, target_keywords, suggested_headings, faq_questions):
    print("\n--- SEO Brief ---\n")
    print(f"H1:\n{h1}\n")
    print(f"Meta Title:\n{meta_title}\n")
    print("Competitors:")
    for idx, comp in enumerate(competitors, 1):
        print(f"{idx}. {comp}")
    print("\nTarget Keywords:")
    for keyword in target_keywords:
        print(f"- {keyword}")
    print("\nSuggested Headings:")
    for heading in suggested_headings:
        print(f"- {heading}")
    print("\nFAQ Questions:")
    for question in faq_questions:
        print(f"- {question}")
