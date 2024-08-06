#!/usr/bin/python3
import os
import sys
import settings

def main():
    if len(sys.argv) != 2:
        print("Error: wrong number of arguments")
        return
    
    template_path = sys.argv[1]
    if not template_path.endswith('.template'):
        print("Error: wrong file extension, (required: .template)")
        return
    
    if not os.path.isfile(template_path):
        print(f"Error: non-existing file... : {template_path}")
        return
    
    try:
        with open(template_path, "r") as f:
            template_content = f.read()
    except Exception as e:
        print(f"Error reading file {template_path}: {e}")
        return

    try:
        rendered_content = template_content.format(
            title=settings.title,
            name=settings.name,
            surname=settings.surname,
            age=settings.age,
            profession=settings.profession
        )
    except Exception as e:
        print(f"Error formatting template: {e}")
        return

    output_path = template_path.replace('.template', '.html')
    try:
        with open(output_path, "w") as f:
            f.write(rendered_content)
    except Exception as e:
        print(f"Error writing to file {output_path}: {e}")
        return
    
    print(f"Rendered HTML saved to {output_path}")

if __name__ == "__main__":
    main()
