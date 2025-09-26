
from Source.Programa import programa_principal
from Source.Logger import logging

if __name__ == "__main__":
    try:
        programa_principal()
    except Exception as error:
        error_msg = f"Error crítico al iniciar el programa: {error}"
        print("\n" + "=" * 55)
        print(f"Error: {error_msg}")
        print("=" * 55)
        logging.critical(error_msg)
        input("Presione Enter para salir...")
