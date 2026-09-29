from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken


def main():
    pasta = Path(
        r"C:\Users\Pedro\Documents\Codex\2026-09-29"
        r"\me-x20\outputs\resultados\teste-43oo88bd"
    )

    arquivo_chave = pasta / "chave.key"
    criptografado = pasta / "exemplo.txt.fernet"
    recuperado = pasta / "exemplo_recuperado.txt"

    if not arquivo_chave.is_file() or not criptografado.is_file():
        print("A chave ou a cópia criptografada não foi encontrada.")
        return

    if recuperado.exists():
        print("O arquivo recuperado já existe. Nada foi sobrescrito.")
        return

    chave = arquivo_chave.read_bytes()
    cifra = Fernet(chave)

    try:
        dados = cifra.decrypt(criptografado.read_bytes())
    except InvalidToken:
        print("Não foi possível recuperar: chave incorreta ou dados alterados.")
        return

    with recuperado.open("xb") as destino:
        destino.write(dados)

    print("Arquivo recuperado criado em:", recuperado)
    print("O original e a cópia criptografada foram preservados.")


if __name__ == "__main__":
    main()
