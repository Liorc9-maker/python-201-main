# type: ignore
import pyjokes
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

# Supported languages and categories
languages = {
    "1": "en",  # English
    "2": "de",  # German
    "3": "es",  # Spanish
    "4": "gl",  # Galician
    "5": "eu",  # Basque
}

categories = {
    "1": "neutral",
    "2": "chuck",
    "3": "all"
}

def choose_language():
    print("\n[bold cyan]Choose a language:[/bold cyan]")
    for key, lang in languages.items():
        print(f"[bold yellow]{key}.[/bold yellow] {lang.upper()}")
    choice = input("Your choice (number): ")
    return languages.get(choice, "en")

def choose_category():
    print("\n[bold cyan]Choose a joke category:[/bold cyan]")
    for key, cat in categories.items():
        print(f"[bold yellow]{key}.[/bold yellow] {cat.title()}")
    choice = input("Your choice (number): ")
    return categories.get(choice, "all")

def main():
    print("[bold magenta]🤣 Welcome to the Multi-language Joke Generator! 🤣[/bold magenta]")

    while True:
        language = choose_language()
        category = choose_category()

        print("\n[bold green]Here's your joke:[/bold green]")
        print("[dim]" + "-" * 40 + "[/dim]")

        try:
            joke = pyjokes.get_joke(language=language, category=category)
            console.print(Panel(joke, style="bold white on blue", expand=False))
        except pyjokes.pyjokes.LanguageNotFoundError:
            print("[red]❌ That language is not supported.[/red]")
        except pyjokes.pyjokes.CategoryNotFoundError:
            print("[red]❌ That category is not available in the selected language.[/red]")

        console.print("\n[bold cyan]Want another joke? (y/n): [/bold cyan]", end="")
        again = input().lower()
        if again != 'y':
            print("[bold green]Thanks for laughing with me! 😄[/bold green]")
            break


if __name__ == "__main__":
    main()
