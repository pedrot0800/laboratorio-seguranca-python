from pathlib import Path
from tempfile import mkdtemp

from cryptography.fernet import Fernet


def main():
    # Somente este arquivo fictício será lido.
    arquivo = Path(
        r"C:\Users\Pedro\Documents\Codex\2026-09-29"
        r"\me-x20\outputs\dados_teste\exemplo.txt"
    )

    if not arquivo.is_file():
        print("Arquivo de teste não encontrado.")
        return

    # Cada execução recebe uma pasta nova.
    resultados = arquivo.parent.parent / "resultados"
    resultados.mkdir(exist_ok=True)
    pasta = Path(mkdtemp(prefix="teste-", dir=resultados))

    chave = Fernet.generate_key()
    cifra = Fernet(chave)

    # Salva a chave sem sobrescrever chaves anteriores.
    with (pasta / "chave.key").open("xb") as destino:
        destino.write(chave)

    # Criptografa uma cópia e preserva o arquivo original.
    dados = arquivo.read_bytes()
    with (pasta / "exemplo.txt.fernet").open("xb") as destino:
        destino.write(cifra.encrypt(dados))

    print("Cópia criptografada criada em:", pasta)
    print("O arquivo exemplo.txt original foi preservado.")


if __name__ == "__main__":
    main()
    
