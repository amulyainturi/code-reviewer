# code-reviewer

An AI-powered code reviewer that analyzes Python code for bugs, style issues, and best practices.

## Features

- Detects common Python bugs and errors
- - Checks PEP 8 style compliance
  - - Identifies code smells and anti-patterns
    - - Suggests improvements and refactoring tips
      - - Supports multiple review modes (quick, detailed, strict)
       
        - ## Installation
       
        - ```bash
          git clone https://github.com/amulyainturi/code-reviewer.git
          cd code-reviewer
          pip install -r requirements.txt
          ```

          ## Usage

          ```bash
          python reviewer.py --file your_script.py
          python reviewer.py --file your_script.py --mode detailed
          ```

          ## Project Structure

          ```
          code-reviewer/
          ├── reviewer.py          # Main entry point
          ├── rules/
          │   ├── style_rules.py   # PEP 8 style checks
          │   ├── bug_rules.py     # Bug detection rules
          │   └── complexity.py    # Code complexity analyzer
          ├── requirements.txt     # Dependencies
          └── README.md
          ```

          ## License

          MIT
