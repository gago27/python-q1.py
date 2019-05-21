{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "q01.py",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/gago27/python-q1.py/blob/master/q01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2UEepvWnEDHj",
        "colab_type": "code",
        "outputId": "a3dde739-ebd3-4083-a6f2-8632d0ba9942",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "##\n",
        "## Imprima la suma de la segunda columna.\n",
        "##\n",
        "import glob\n",
        "filenames = glob.glob(\"data.csv\")\n",
        "data = open(\"data.csv\",\"r\").readlines()\n",
        "data = [line[:-1] for line in data]\n",
        "data = [line.replace(\"\\t\", \",\") for line in data]\n",
        "data = [line.split(\",\") for line in data]\n",
        "data = [line[1] for line in data]\n",
        "a = 0\n",
        "for row in data:\n",
        "  a= a+ int(row)\n",
        "print(a)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "190\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}