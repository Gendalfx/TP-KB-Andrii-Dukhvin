def test_string_functions():
    s = "   hello world! welcome to python.   "

    # strip() - Видаляє пробіли з обох боків рядка
    stripped = s.strip()
    print(f"strip():'{stripped}'")  

   # capitalize() - Робить першу літеру великою, а інші маленькими
    capitalized = stripped.capitalize()
    print(f"capitalize():'{capitalized}'")

    # title() - Робить першу літеру кожного слова великою
    titled = s.title()
    print(f"title():'{titled}'")  

    # upper() - Перетворює всі символи в рядку на великі
    uppercased = s.upper()
    print(f"upper():'{uppercased}'")  

    # lower() - Перетворює всі символи в рядку на маленькі
    lowercased = s.lower()
    print(f"lower():'{lowercased}'")  


test_string_functions()
