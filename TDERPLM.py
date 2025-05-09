{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/larissaadames/RPLM/blob/main/TDERPLM.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install truth-table-generator\n"
      ],
      "metadata": {
        "id": "c-Emfq4DSp4f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "22032ca1-4965-4978-d28f-a277af8be7f9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting truth-table-generator\n",
            "  Downloading truth_table_generator-2.0.0-py3-none-any.whl.metadata (15 kB)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (from truth-table-generator) (2.0.2)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (from truth-table-generator) (2.2.2)\n",
            "Collecting PTable (from truth-table-generator)\n",
            "  Downloading PTable-0.9.2.tar.gz (31 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: pyparsing in /usr/local/lib/python3.11/dist-packages (from truth-table-generator) (3.2.3)\n",
            "Requirement already satisfied: tabulate in /usr/local/lib/python3.11/dist-packages (from truth-table-generator) (0.9.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from truth-table-generator) (3.1.6)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->truth-table-generator) (3.0.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas->truth-table-generator) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas->truth-table-generator) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas->truth-table-generator) (2025.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas->truth-table-generator) (1.17.0)\n",
            "Downloading truth_table_generator-2.0.0-py3-none-any.whl (19 kB)\n",
            "Building wheels for collected packages: PTable\n",
            "  Building wheel for PTable (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for PTable: filename=PTable-0.9.2-py3-none-any.whl size=22906 sha256=0e70b05b5c3f2d28520b192eb9acc2f3e9ce4b7fdec4bb388adbb0a0c2402346\n",
            "  Stored in directory: /root/.cache/pip/wheels/5d/5d/31/d7788a512a672caf93d8c13e298f90f3e53e72380c364a5a9a\n",
            "Successfully built PTable\n",
            "Installing collected packages: PTable, truth-table-generator\n",
            "Successfully installed PTable-0.9.2 truth-table-generator-2.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 1 letra a\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['p and q or not(p)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "id": "hQRvaKexWIXO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 1 letra b\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['p=>q = not(q) or p'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2PioPKDGYeVC",
        "outputId": "e3686001-2107-4ef9-edff-151d8f5324b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+----------------------+\n",
            "|   p   |   q   |  p=>q = not(q) or p  |\n",
            "|-------+-------+----------------------|\n",
            "| True  | True  |         True         |\n",
            "| True  | False |        False         |\n",
            "| False | True  |        False         |\n",
            "| False | False |         True         |\n",
            "+-------+-------+----------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 1 letra c\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['(not(p) or not(q)) and p and not(p = q)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5SXssVUZZKAk",
        "outputId": "9ee1558f-0c19-483b-e6b3-5858420b735c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------------------------------------------+\n",
            "|   p   |   q   |  (not(p) or not(q)) and p and not(p = q)  |\n",
            "|-------+-------+-------------------------------------------|\n",
            "| True  | True  |                   False                   |\n",
            "| True  | False |                   True                    |\n",
            "| False | True  |                   False                   |\n",
            "| False | False |                   False                   |\n",
            "+-------+-------+-------------------------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 1 letra d\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['not(p) = not(q) and p = not(p) or not(q)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rS3HmRsuZ9Sg",
        "outputId": "ce7e9060-b8aa-40be-9e48-fbcc006d1081"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+--------------------------------------------+\n",
            "|   p   |   q   |  not(p) = not(q) and p = not(p) or not(q)  |\n",
            "|-------+-------+--------------------------------------------|\n",
            "| True  | True  |                   False                    |\n",
            "| True  | False |                   False                    |\n",
            "| False | True  |                   False                    |\n",
            "| False | False |                   False                    |\n",
            "+-------+-------+--------------------------------------------+\n",
            "Contradiction\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 1 letra e\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['p=((q or q) => not(r))'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PvZ1TWzlbj23",
        "outputId": "e0b31b9e-a3df-4f5c-a43b-79d7e82bcdb6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+--------------------------+\n",
            "|   p   |   q   |   r   |  p=((q or q) => not(r))  |\n",
            "|-------+-------+-------+--------------------------|\n",
            "| True  | True  | True  |          False           |\n",
            "| True  | True  | False |           True           |\n",
            "| True  | False | True  |           True           |\n",
            "| True  | False | False |           True           |\n",
            "| False | True  | True  |           True           |\n",
            "| False | True  | False |          False           |\n",
            "| False | False | True  |          False           |\n",
            "| False | False | False |          False           |\n",
            "+-------+-------+-------+--------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 1 letra f\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['(q and p and not(q)) = (p => not(q))'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RmAIMCWWcNm1",
        "outputId": "f0d5f665-ccbf-4a21-f695-c58dd6787626"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+----------------------------------------+\n",
            "|   p   |   q   |  (q and p and not(q)) = (p => not(q))  |\n",
            "|-------+-------+----------------------------------------|\n",
            "| True  | True  |                  True                  |\n",
            "| True  | False |                 False                  |\n",
            "| False | True  |                 False                  |\n",
            "| False | False |                 False                  |\n",
            "+-------+-------+----------------------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 1 letra g\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['not(p) or q and r => r => not(p) or q'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vdfXqdscdINg",
        "outputId": "de793fc5-cd0a-4df9-dbf0-780ee8cde0ce"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+-----------------------------------------+\n",
            "|   p   |   q   |   r   |  not(p) or q and r => r => not(p) or q  |\n",
            "|-------+-------+-------+-----------------------------------------|\n",
            "| True  | True  | True  |                  True                   |\n",
            "| True  | True  | False |                  True                   |\n",
            "| True  | False | True  |                  False                  |\n",
            "| True  | False | False |                  False                  |\n",
            "| False | True  | True  |                  True                   |\n",
            "| False | True  | False |                  True                   |\n",
            "| False | False | True  |                  True                   |\n",
            "| False | False | False |                  True                   |\n",
            "+-------+-------+-------+-----------------------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2:\n",
        "# a.\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['not(p) or not(q)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())\n"
      ],
      "metadata": {
        "id": "cb7tVu3UggRD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ea696b9b-efbe-4334-e5af-5ff9826f1d3e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+--------------------+\n",
            "|   p   |   q   |  not(p) or not(q)  |\n",
            "|-------+-------+--------------------|\n",
            "| True  | True  |       False        |\n",
            "| True  | False |        True        |\n",
            "| False | True  |        True        |\n",
            "| False | False |        True        |\n",
            "+-------+-------+--------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# b.\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['((p or not(q)) or not(r)) or ((not(p) or q ) or r)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "id": "u46PJ0X3jW6f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5e9816fa-47a3-448a-ab87-66c80cae7332"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+------------------------------------------------------+\n",
            "|   p   |   q   |   r   |  ((p or not(q)) or not(r)) or ((not(p) or q ) or r)  |\n",
            "|-------+-------+-------+------------------------------------------------------|\n",
            "| True  | True  | True  |                         True                         |\n",
            "| True  | True  | False |                         True                         |\n",
            "| True  | False | True  |                         True                         |\n",
            "| True  | False | False |                         True                         |\n",
            "| False | True  | True  |                         True                         |\n",
            "| False | True  | False |                         True                         |\n",
            "| False | False | True  |                         True                         |\n",
            "| False | False | False |                         True                         |\n",
            "+-------+-------+-------+------------------------------------------------------+\n",
            "Tautology\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# c.\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['(p and q ) => (p or q)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JG3vC3HA1jUo",
        "outputId": "1530a395-4377-40ea-d8e9-722695053996"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+--------------------------+\n",
            "|   p   |   q   |  (p and q ) => (p or q)  |\n",
            "|-------+-------+--------------------------|\n",
            "| True  | True  |           True           |\n",
            "| True  | False |           True           |\n",
            "| False | True  |           True           |\n",
            "| False | False |           True           |\n",
            "+-------+-------+--------------------------+\n",
            "Tautology\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# d\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['(p and q) or r'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Dd-8eygpMRoQ",
        "outputId": "3557eea8-333e-4a78-d5e0-b25fcdd16d7e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+------------------+\n",
            "|   p   |   q   |   r   |  (p and q) or r  |\n",
            "|-------+-------+-------+------------------|\n",
            "| True  | True  | True  |       True       |\n",
            "| True  | True  | False |       True       |\n",
            "| True  | False | True  |       True       |\n",
            "| True  | False | False |      False       |\n",
            "| False | True  | True  |       True       |\n",
            "| False | True  | False |      False       |\n",
            "| False | False | True  |       True       |\n",
            "| False | False | False |      False       |\n",
            "+-------+-------+-------+------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# e\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['(p and q) => p'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gmPkoyKPNDUx",
        "outputId": "9a39fc62-7935-4455-a64d-592c56faf8de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+------------------+\n",
            "|   p   |   q   |  (p and q) => p  |\n",
            "|-------+-------+------------------|\n",
            "| True  | True  |       True       |\n",
            "| True  | False |       True       |\n",
            "| False | True  |       True       |\n",
            "| False | False |       True       |\n",
            "+-------+-------+------------------+\n",
            "Tautology\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# f\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['p => (p or q)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HIfUDk9tNP6r",
        "outputId": "def767a8-dc4c-461a-9def-c5c151fc5888"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-----------------+\n",
            "|   p   |   q   |  p => (p or q)  |\n",
            "|-------+-------+-----------------|\n",
            "| True  | True  |      True       |\n",
            "| True  | False |      True       |\n",
            "| False | True  |      True       |\n",
            "| False | False |      True       |\n",
            "+-------+-------+-----------------+\n",
            "Tautology\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# g\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['(p and ( p => q )) => q'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xHsMgTulNfFn",
        "outputId": "21f0f324-d6d1-4e1d-bb74-6ff9ed10725e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+---------------------------+\n",
            "|   p   |   q   |  (p and ( p => q )) => q  |\n",
            "|-------+-------+---------------------------|\n",
            "| True  | True  |           True            |\n",
            "| True  | False |           True            |\n",
            "| False | True  |           True            |\n",
            "| False | False |           True            |\n",
            "+-------+-------+---------------------------+\n",
            "Tautology\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# h\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['((p => q) and not(q)) => not(q)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uS2o4aGnNzAN",
        "outputId": "7e4816c9-f81d-4d1e-905f-7b4936e27d8c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-----------------------------------+\n",
            "|   p   |   q   |  ((p => q) and not(q)) => not(q)  |\n",
            "|-------+-------+-----------------------------------|\n",
            "| True  | True  |               True                |\n",
            "| True  | False |               True                |\n",
            "| False | True  |               True                |\n",
            "| False | False |               True                |\n",
            "+-------+-------+-----------------------------------+\n",
            "Tautology\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# i\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q'],['(p and q) and not(p)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "id": "JwVEynceOCHX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 2\n",
        "# j\n",
        "\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['((p or not(q)) and r) and ((p and q) or not(r))'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0pQ5KhnXOQp7",
        "outputId": "e6c9eafe-372f-4f1a-fbcf-3d3feca8f0bf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+---------------------------------------------------+\n",
            "|   p   |   q   |   r   |  ((p or not(q)) and r) and ((p and q) or not(r))  |\n",
            "|-------+-------+-------+---------------------------------------------------|\n",
            "| True  | True  | True  |                       True                        |\n",
            "| True  | True  | False |                       False                       |\n",
            "| True  | False | True  |                       False                       |\n",
            "| True  | False | False |                       False                       |\n",
            "| False | True  | True  |                       False                       |\n",
            "| False | True  | False |                       False                       |\n",
            "| False | False | True  |                       False                       |\n",
            "| False | False | False |                       False                       |\n",
            "+-------+-------+-------+---------------------------------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 3 letra a\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r','s'],['(p => not(q)) and (not(r)=> s) and q)=> s'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_d0O2Uqrg1Ls",
        "outputId": "6c308e26-5765-42d6-fde9-eb0d3247f3df"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+-------+---------------------------------------------+\n",
            "|   p   |   q   |   r   |   s   |  (p => not(q)) and (not(r)=> s) and q)=> s  |\n",
            "|-------+-------+-------+-------+---------------------------------------------|\n",
            "| True  | True  | True  | True  |                    False                    |\n",
            "| True  | True  | True  | False |                    False                    |\n",
            "| True  | True  | False | True  |                    False                    |\n",
            "| True  | True  | False | False |                    False                    |\n",
            "| True  | False | True  | True  |                    False                    |\n",
            "| True  | False | True  | False |                    False                    |\n",
            "| True  | False | False | True  |                    False                    |\n",
            "| True  | False | False | False |                    False                    |\n",
            "| False | True  | True  | True  |                    True                     |\n",
            "| False | True  | True  | False |                    True                     |\n",
            "| False | True  | False | True  |                    True                     |\n",
            "| False | True  | False | False |                    False                    |\n",
            "| False | False | True  | True  |                    False                    |\n",
            "| False | False | True  | False |                    False                    |\n",
            "| False | False | False | True  |                    False                    |\n",
            "| False | False | False | False |                    False                    |\n",
            "+-------+-------+-------+-------+---------------------------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 3 letra b\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['(not(p) => q) => (not(r or p) => q)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "097PVe4jmdIl",
        "outputId": "872a04e1-7173-480c-b35b-fb45be19dc2a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+---------------------------------------+\n",
            "|   p   |   q   |   r   |  (not(p) => q) => (not(r or p) => q)  |\n",
            "|-------+-------+-------+---------------------------------------|\n",
            "| True  | True  | True  |                 True                  |\n",
            "| True  | True  | False |                 True                  |\n",
            "| True  | False | True  |                 True                  |\n",
            "| True  | False | False |                 True                  |\n",
            "| False | True  | True  |                 True                  |\n",
            "| False | True  | False |                 True                  |\n",
            "| False | False | True  |                 True                  |\n",
            "| False | False | False |                 True                  |\n",
            "+-------+-------+-------+---------------------------------------+\n",
            "Tautology\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##ex 3 letra c\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['((p or q) and not(r)) => q'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LJB5xExwoZ6N",
        "outputId": "a517f0a3-0276-4ae9-c314-26ebe1c79467"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+------------------------------+\n",
            "|   p   |   q   |   r   |  ((p or q) and not(r)) => q  |\n",
            "|-------+-------+-------+------------------------------|\n",
            "| True  | True  | True  |             True             |\n",
            "| True  | True  | False |             True             |\n",
            "| True  | False | True  |             True             |\n",
            "| True  | False | False |            False             |\n",
            "| False | True  | True  |             True             |\n",
            "| False | True  | False |             True             |\n",
            "| False | False | True  |             True             |\n",
            "| False | False | False |             True             |\n",
            "+-------+-------+-------+------------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 3 letra d\n",
        "import ttg\n",
        "x = ttg.Truths(['p','q','r'],['((p => not(q)) and (p or r) and (r and not(q))) => not(p)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kYf7XZtlpSXq",
        "outputId": "ab96d928-5dd3-4e93-8bf3-bf429543cb4b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+-------------------------------------------------------------+\n",
            "|   p   |   q   |   r   |  ((p => not(q)) and (p or r) and (r and not(q))) => not(p)  |\n",
            "|-------+-------+-------+-------------------------------------------------------------|\n",
            "| True  | True  | True  |                            True                             |\n",
            "| True  | True  | False |                            True                             |\n",
            "| True  | False | True  |                            False                            |\n",
            "| True  | False | False |                            True                             |\n",
            "| False | True  | True  |                            True                             |\n",
            "| False | True  | False |                            True                             |\n",
            "| False | False | True  |                            True                             |\n",
            "| False | False | False |                            True                             |\n",
            "+-------+-------+-------+-------------------------------------------------------------+\n",
            "Contingency\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Parte 3\n",
        "# e\n",
        "\n",
        "import ttg\n",
        "\n",
        "x = ttg.Truths(['p','q','r','s','t','u','v'],['(p and q and r) and ((q and p) => (s => (not(t) or u))) and (not(s) and not(v) and not(u)) => not(t)'],ints=False)\n",
        "print(x)\n",
        "print(x.valuation)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1zFrQSYBuLPw",
        "outputId": "dba0f0f9-1bea-477d-d95d-09733562de3a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+-------+-------+-------+-------+-------+-------+--------------------------------------------------------------------------------------------------------+\n",
            "|   p   |   q   |   r   |   s   |   t   |   u   |   v   |  (p and q and r) and ((q and p) => (s => (not(t) or u))) and (not(s) and not(v) and not(u)) => not(t)  |\n",
            "|-------+-------+-------+-------+-------+-------+-------+--------------------------------------------------------------------------------------------------------|\n",
            "| True  | True  | True  | True  | True  | True  | True  |                                                  True                                                  |\n",
            "| True  | True  | True  | True  | True  | True  | False |                                                  True                                                  |\n",
            "| True  | True  | True  | True  | True  | False | True  |                                                 False                                                  |\n",
            "| True  | True  | True  | True  | True  | False | False |                                                 False                                                  |\n",
            "| True  | True  | True  | True  | False | True  | True  |                                                  True                                                  |\n",
            "| True  | True  | True  | True  | False | True  | False |                                                  True                                                  |\n",
            "| True  | True  | True  | True  | False | False | True  |                                                  True                                                  |\n",
            "| True  | True  | True  | True  | False | False | False |                                                  True                                                  |\n",
            "| True  | True  | True  | False | True  | True  | True  |                                                  True                                                  |\n",
            "| True  | True  | True  | False | True  | True  | False |                                                  True                                                  |\n",
            "| True  | True  | True  | False | True  | False | True  |                                                  True                                                  |\n",
            "| True  | True  | True  | False | True  | False | False |                                                 False                                                  |\n",
            "| True  | True  | True  | False | False | True  | True  |                                                  True                                                  |\n",
            "| True  | True  | True  | False | False | True  | False |                                                  True                                                  |\n",
            "| True  | True  | True  | False | False | False | True  |                                                  True                                                  |\n",
            "| True  | True  | True  | False | False | False | False |                                                  True                                                  |\n",
            "| True  | True  | False | True  | True  | True  | True  |                                                 False                                                  |\n",
            "| True  | True  | False | True  | True  | True  | False |                                                 False                                                  |\n",
            "| True  | True  | False | True  | True  | False | True  |                                                 False                                                  |\n",
            "| True  | True  | False | True  | True  | False | False |                                                 False                                                  |\n",
            "| True  | True  | False | True  | False | True  | True  |                                                 False                                                  |\n",
            "| True  | True  | False | True  | False | True  | False |                                                 False                                                  |\n",
            "| True  | True  | False | True  | False | False | True  |                                                 False                                                  |\n",
            "| True  | True  | False | True  | False | False | False |                                                 False                                                  |\n",
            "| True  | True  | False | False | True  | True  | True  |                                                 False                                                  |\n",
            "| True  | True  | False | False | True  | True  | False |                                                 False                                                  |\n",
            "| True  | True  | False | False | True  | False | True  |                                                 False                                                  |\n",
            "| True  | True  | False | False | True  | False | False |                                                 False                                                  |\n",
            "| True  | True  | False | False | False | True  | True  |                                                 False                                                  |\n",
            "| True  | True  | False | False | False | True  | False |                                                 False                                                  |\n",
            "| True  | True  | False | False | False | False | True  |                                                 False                                                  |\n",
            "| True  | True  | False | False | False | False | False |                                                 False                                                  |\n",
            "| True  | False | True  | True  | True  | True  | True  |                                                 False                                                  |\n",
            "| True  | False | True  | True  | True  | True  | False |                                                 False                                                  |\n",
            "| True  | False | True  | True  | True  | False | True  |                                                 False                                                  |\n",
            "| True  | False | True  | True  | True  | False | False |                                                 False                                                  |\n",
            "| True  | False | True  | True  | False | True  | True  |                                                 False                                                  |\n",
            "| True  | False | True  | True  | False | True  | False |                                                 False                                                  |\n",
            "| True  | False | True  | True  | False | False | True  |                                                 False                                                  |\n",
            "| True  | False | True  | True  | False | False | False |                                                 False                                                  |\n",
            "| True  | False | True  | False | True  | True  | True  |                                                 False                                                  |\n",
            "| True  | False | True  | False | True  | True  | False |                                                 False                                                  |\n",
            "| True  | False | True  | False | True  | False | True  |                                                 False                                                  |\n",
            "| True  | False | True  | False | True  | False | False |                                                 False                                                  |\n",
            "| True  | False | True  | False | False | True  | True  |                                                 False                                                  |\n",
            "| True  | False | True  | False | False | True  | False |                                                 False                                                  |\n",
            "| True  | False | True  | False | False | False | True  |                                                 False                                                  |\n",
            "| True  | False | True  | False | False | False | False |                                                 False                                                  |\n",
            "| True  | False | False | True  | True  | True  | True  |                                                 False                                                  |\n",
            "| True  | False | False | True  | True  | True  | False |                                                 False                                                  |\n",
            "| True  | False | False | True  | True  | False | True  |                                                 False                                                  |\n",
            "| True  | False | False | True  | True  | False | False |                                                 False                                                  |\n",
            "| True  | False | False | True  | False | True  | True  |                                                 False                                                  |\n",
            "| True  | False | False | True  | False | True  | False |                                                 False                                                  |\n",
            "| True  | False | False | True  | False | False | True  |                                                 False                                                  |\n",
            "| True  | False | False | True  | False | False | False |                                                 False                                                  |\n",
            "| True  | False | False | False | True  | True  | True  |                                                 False                                                  |\n",
            "| True  | False | False | False | True  | True  | False |                                                 False                                                  |\n",
            "| True  | False | False | False | True  | False | True  |                                                 False                                                  |\n",
            "| True  | False | False | False | True  | False | False |                                                 False                                                  |\n",
            "| True  | False | False | False | False | True  | True  |                                                 False                                                  |\n",
            "| True  | False | False | False | False | True  | False |                                                 False                                                  |\n",
            "| True  | False | False | False | False | False | True  |                                                 False                                                  |\n",
            "| True  | False | False | False | False | False | False |                                                 False                                                  |\n",
            "| False | True  | True  | True  | True  | True  | True  |                                                 False                                                  |\n",
            "| False | True  | True  | True  | True  | True  | False |                                                 False                                                  |\n",
            "| False | True  | True  | True  | True  | False | True  |                                                 False                                                  |\n",
            "| False | True  | True  | True  | True  | False | False |                                                 False                                                  |\n",
            "| False | True  | True  | True  | False | True  | True  |                                                 False                                                  |\n",
            "| False | True  | True  | True  | False | True  | False |                                                 False                                                  |\n",
            "| False | True  | True  | True  | False | False | True  |                                                 False                                                  |\n",
            "| False | True  | True  | True  | False | False | False |                                                 False                                                  |\n",
            "| False | True  | True  | False | True  | True  | True  |                                                 False                                                  |\n",
            "| False | True  | True  | False | True  | True  | False |                                                 False                                                  |\n",
            "| False | True  | True  | False | True  | False | True  |                                                 False                                                  |\n",
            "| False | True  | True  | False | True  | False | False |                                                 False                                                  |\n",
            "| False | True  | True  | False | False | True  | True  |                                                 False                                                  |\n",
            "| False | True  | True  | False | False | True  | False |                                                 False                                                  |\n",
            "| False | True  | True  | False | False | False | True  |                                                 False                                                  |\n",
            "| False | True  | True  | False | False | False | False |                                                 False                                                  |\n",
            "| False | True  | False | True  | True  | True  | True  |                                                 False                                                  |\n",
            "| False | True  | False | True  | True  | True  | False |                                                 False                                                  |\n",
            "| False | True  | False | True  | True  | False | True  |                                                 False                                                  |\n",
            "| False | True  | False | True  | True  | False | False |                                                 False                                                  |\n",
            "| False | True  | False | True  | False | True  | True  |                                                 False                                                  |\n",
            "| False | True  | False | True  | False | True  | False |                                                 False                                                  |\n",
            "| False | True  | False | True  | False | False | True  |                                                 False                                                  |\n",
            "| False | True  | False | True  | False | False | False |                                                 False                                                  |\n",
            "| False | True  | False | False | True  | True  | True  |                                                 False                                                  |\n",
            "| False | True  | False | False | True  | True  | False |                                                 False                                                  |\n",
            "| False | True  | False | False | True  | False | True  |                                                 False                                                  |\n",
            "| False | True  | False | False | True  | False | False |                                                 False                                                  |\n",
            "| False | True  | False | False | False | True  | True  |                                                 False                                                  |\n",
            "| False | True  | False | False | False | True  | False |                                                 False                                                  |\n",
            "| False | True  | False | False | False | False | True  |                                                 False                                                  |\n",
            "| False | True  | False | False | False | False | False |                                                 False                                                  |\n",
            "| False | False | True  | True  | True  | True  | True  |                                                 False                                                  |\n",
            "| False | False | True  | True  | True  | True  | False |                                                 False                                                  |\n",
            "| False | False | True  | True  | True  | False | True  |                                                 False                                                  |\n",
            "| False | False | True  | True  | True  | False | False |                                                 False                                                  |\n",
            "| False | False | True  | True  | False | True  | True  |                                                 False                                                  |\n",
            "| False | False | True  | True  | False | True  | False |                                                 False                                                  |\n",
            "| False | False | True  | True  | False | False | True  |                                                 False                                                  |\n",
            "| False | False | True  | True  | False | False | False |                                                 False                                                  |\n",
            "| False | False | True  | False | True  | True  | True  |                                                 False                                                  |\n",
            "| False | False | True  | False | True  | True  | False |                                                 False                                                  |\n",
            "| False | False | True  | False | True  | False | True  |                                                 False                                                  |\n",
            "| False | False | True  | False | True  | False | False |                                                 False                                                  |\n",
            "| False | False | True  | False | False | True  | True  |                                                 False                                                  |\n",
            "| False | False | True  | False | False | True  | False |                                                 False                                                  |\n",
            "| False | False | True  | False | False | False | True  |                                                 False                                                  |\n",
            "| False | False | True  | False | False | False | False |                                                 False                                                  |\n",
            "| False | False | False | True  | True  | True  | True  |                                                 False                                                  |\n",
            "| False | False | False | True  | True  | True  | False |                                                 False                                                  |\n",
            "| False | False | False | True  | True  | False | True  |                                                 False                                                  |\n",
            "| False | False | False | True  | True  | False | False |                                                 False                                                  |\n",
            "| False | False | False | True  | False | True  | True  |                                                 False                                                  |\n",
            "| False | False | False | True  | False | True  | False |                                                 False                                                  |\n",
            "| False | False | False | True  | False | False | True  |                                                 False                                                  |\n",
            "| False | False | False | True  | False | False | False |                                                 False                                                  |\n",
            "| False | False | False | False | True  | True  | True  |                                                 False                                                  |\n",
            "| False | False | False | False | True  | True  | False |                                                 False                                                  |\n",
            "| False | False | False | False | True  | False | True  |                                                 False                                                  |\n",
            "| False | False | False | False | True  | False | False |                                                 False                                                  |\n",
            "| False | False | False | False | False | True  | True  |                                                 False                                                  |\n",
            "| False | False | False | False | False | True  | False |                                                 False                                                  |\n",
            "| False | False | False | False | False | False | True  |                                                 False                                                  |\n",
            "| False | False | False | False | False | False | False |                                                 False                                                  |\n",
            "+-------+-------+-------+-------+-------+-------+-------+--------------------------------------------------------------------------------------------------------+\n",
            "<bound method Truths.valuation of <ttg.ttg.Truths object at 0x7e203e74a690>>\n"
          ]
        }
      ]
    }
  ]
}