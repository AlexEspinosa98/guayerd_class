from enum import Enum
from typing import Optional

class MenuOption(Enum):
    EXIT = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5

def display_menu() -> None:
    """Display the main menu options."""
    print("\n=== MENU PRINCIPAL ===")
    options = {
        "1": "Primera opción",
        "2": "Segunda opción",
        "3": "Tercera opción",
        "4": "Cuarta opción",
        "5": "Quinta opción",
        "0": "Salir"
    }
    for key, value in options.items():
        print(f"{key}. {value}")

def get_user_choice() -> Optional[MenuOption]:
    """Get and validate user input.
    
    Returns:
        MenuOption if valid choice, None otherwise
    """
    try:
        choice = int(input("\nIngrese una opción: "))
        return MenuOption(choice)
    except (ValueError, KeyError):
        return None

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice is None:
            print("Opción inválida. Por favor intente nuevamente.")
            continue
            
        if choice == MenuOption.EXIT:
            print("¡Hasta luego!")
            break
            
        print(f"Has seleccionado la {choice.name.lower()} opción")

if __name__ == "__main__":
    main()