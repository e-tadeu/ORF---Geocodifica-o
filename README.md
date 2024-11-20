
# ORF24 Geocodificação

Bem-vindo ao **ORF24 Geocodificação**, um plugin desenvolvido para QGIS que geocodifica endereços constantes em arquivo CSV e gera uma camada de pontos em shapefile.

---

## **Pré-requisitos de instalação**

Antes de instalar e utilizar o plugin, siga estas etapas para configurar seu ambiente corretamente.

### **1. Instale o módulo `geocoder`**

No OSGeo4W Shell (Garanta que a versão deste OSGeo4w Shell seja semelhante a versão do QGIS a ser utilizada), execute o seguinte comando para instalar o módulo `geocoder`:

```bash
pip install geocoder
```

### **2. Resolva possíveis problemas de certificação**

Se ocorrerem erros relacionados à certificação durante essa etapa, siga os passos abaixo:

1. Abra o Python e execute os seguintes comandos para localizar o caminho do arquivo de certificação:

    ```python
    import certifi
    print(certifi.where())
    ```

    Será retornado um caminho semelhante a este:

    ```
    C:\Users\seu_usuario\anaconda3\Lib\site-packages\certifi\cacert.pem
    ```

2. Configure o ambiente para usar este caminho como o arquivo de certificação:

    ```bash
    set REQUESTS_CA_BUNDLE=<caminho_do_certifi>
    ```

    Substitua `<caminho_do_certifi>` pelo caminho retornado na etapa anterior.

---

## **Instalação do Plugin no QGIS**

Após configurar o ambiente, siga estas etapas para instalar o plugin no QGIS:

1. Baixe ou clone o repositório do plugin em arquivo ZIP.
2. Abra o QGIS.
3. Vá até **Complementos > Gerenciar e Instalar Complementos**.
4. Clique na aba **Instalar de um arquivo ZIP**.
5. Selecione o arquivo ZIP do plugin ou a pasta onde os arquivos foram extraídos.
6. Clique em **Instalar Complemento**.

---

Com essas etapas concluídas, o plugin estará pronto para uso!

---

## **Orientações de uso**

### **Formato do arquivo CSV**

Para o correto funcionamento do plugin, o arquivo CSV de entrada deve:

1. Usar **vírgulas** como separador de colunas.  
2. Conter uma coluna de endereços no formato padronizado, conforme orientação abaixo.

### **Formato da coluna de endereços**

Durante a execução do plugin, você será solicitado a selecionar a **coluna de endereços**. Esta coluna deve conter os endereços formatados no seguinte padrão:

```
"R. Mal. Bittencourt, 97, Santo Antônio, Manaus, Amazonas"
```

**Exemplo de conteúdo CSV:**

```csv
Locais, endereços, obs
Local 1, "R. Mal. Bittencourt, 97, Santo Antônio, Manaus, Amazonas", 4CGEO
Local 2, "Rua Cleveland, 250, Santa Tereza, Porto Alegre, Rio Grande do Sul", 1CGEO
```

---
