import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Converts a JSON file to CSV.
    Supports a list of dictionaries [{...}, {...}], and fills missing fields with empty
    strings.
    UTF-8 encoding. Column order can be the same as in the first object or
    alphabetical (specify in the README).
    Args:
        json_path (str): Path to the input JSON file
        csv_path (str): Path to the output CSV file
    """
    J = Path(json_path)  # Create objetc Path for JSON
    C = Path(csv_path)  # Create object Path for CSV
    if J.suffix.lower() != ".json":
        print(f"Caminho a Origem não contém ficheiro .json")
        return False
    try:
        # Try: to open file JSON and read it. The info will be save on "data"
        with J.open("r", newline="", encoding="utf-8") as json_file:
            data = json.load(
                json_file
            )  # Read the file, convert it in Dicty and save in "data"
            if not isinstance(data, list):  # Verify if "data" is a list.
                raise ValueError("JSON data must be a list of objects")
            if not data:
                print("JSON cant be empty")
                return False
            headers = list(
                data[0].keys()
            )  # Lets get the headers of "data" for CSV file.
            for i, pessoa in enumerate(data):
                nome = pessoa.get("name")
                idade_original = pessoa.get("age")
                idade_processada = None
                if idade_original is None or idade_original == None:
                    print(f"Erro no registro {i+1} ({nome}): A idade está vazia.")
                    return False
                try:
                    if isinstance(idade_original, str):
                        idade_processada = int(idade_original)
                    # Se já for inteiro (ou após conversão), verifica se é não negativo
                    elif isinstance(idade_original, int):
                        idade_processada = idade_original
                    else:
                        print(
                            f"Erro no registro {i+1} ({nome}): Formato de Idade incorreto."
                        )
                        return False
                    if idade_processada < 0:
                        print(f"Erro no registro {i+1} ({nome}): Idade negativa!!!")
                        return False
                except ValueError:
                    print(f"Erro no registro {i+1} ({nome}): Idade inválida.")
                    return False
        with C.open("w", newline="", encoding="utf-8") as csv_file:
            # Now lets write it on CSV file:
            # "writer" take info from "csv_file" and organize the headers
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()  # Write the header
            writer.writerows(data)  # Write rows
        print(f"Successfully converted {json_path} to {csv_path}")
        return True
    except FileNotFoundError:
        print(f"Error: File {json_path} not found")
        return False


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Converts CSV to JSON (list of dictionaries).
    Header is required; values ​​are stored as strings.
    json.dump(..., ensure_ascii=False, indent=2)
    A idade DEVE ser um inteiro estrito.
    Interrompe e levanta um ValueError para floats ou inválidos.
    """
    src = Path(csv_path)
    if src.suffix.lower() != ".csv":
        print(f"Caminho a Origem não contém ficheiro .csv")
        return False
    try:  # Try to: Open CVS file to read it and save the content
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)  # Read and save as a Dicty
            data = []
            warnings = []
            # Iterar sobre cada linha do CSV
            for indice, linha in enumerate(reader, start=1):
                nome = linha["name"]
                idade_str = linha["age"]
                idade_final = None
                # --- Lógica de Validação e Conversão da Idade ---
                try:
                    if not idade_str:
                        idade_str = "0"
                        warnings.append(
                            f"Aviso na linha {indice} (Nome: {nome}): O valor da idade estava vazio. Considerado como 0."
                        )
                    idade_final = int(idade_str)
                    if idade_final <= 0:
                        raise ValueError(
                            f"Erro na linha {indice} (Nome: {nome}): Idade inválida '{idade_str}'. valor negativo para Idade."
                        )
                        # return False
                except ValueError:
                    raise ValueError(
                        f"Erro na linha {indice} (Nome: {nome}): Idade inválida '{idade_str}'. Idade deve ser um número inteiro (ex: 25), não um decimal ou texto."
                    )
                linha["age"] = idade_final
                data.append(linha)
            # Retornar os dados em formato JSON e quaisquer avisos gerados
        if not data:
            print("Warning: CSV file is empty or has no data rows")
            return False
        # Making the conversion
        with open(json_path, "w", encoding="utf-8") as json_file:
            # Write "data" to "json_file".Non-ASCII chars written as utf-8.
            # Identation "indent" 2 tabs
            json.dump(data, json_file, ensure_ascii=False, indent=2)
        print(f"Successfully converted {csv_path} to {json_path}")
        print(f"Converted {len(data)} records")
        if warnings:
            print(warnings)
        return True
    except FileNotFoundError:
        print(f"Error: File {csv_path} not found")
        return False
    except csv.Error as e:
        print(f"Error: CSV parsing error - {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    Json_People = "data/samples/people.json"
    CSV_from_JSON = "data/out/people_from_json.csv"
    json_to_csv(Json_People, CSV_from_JSON)

    CSV_People = "data/samples/people.csv"
    JSON_from_CSV = "data/out/people_from_csv.json"
    csv_to_json(CSV_People, JSON_from_CSV)
