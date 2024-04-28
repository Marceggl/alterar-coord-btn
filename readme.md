# Mudar botão de lugar aleatóriamente

## Alterar imagem

Para poder trocar a imagem deste código, é possivel de duas formas:

- Colocar uma imagem nova e renomea-la para:

Neste modo não há necessidade de recompilar o código

```
naoValeEspiar.jpg
```

- Editar a função mostrar_imagem na variavel: image_path

Neste método há necessidade de recompilar o código

```
    # Altere o valor de "NaoValeEspiar.jpg" para outra imagem
    image_path = os.path.join(script_dir, "naoValeEspiar.jpg")
```

## Recompilar o código

1. Instalar o Pyinstaller

```
    pip install pyinstaller
```

2. executar comando no PShell

Deve ser executado na mesma pasta do arquivo main.py

```
    pyinstaller --onefile --windowed main.py
```

## Para executar

Para executar é necessário que a imagem esteja na mesma pasta que main.py

## O botão que altera as coordenadas

Neste código o botão que tem as coordenadas alteradas é "btnEleNao"
