{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0ebb9ba6",
   "metadata": {},
   "source": [
    "## Análise exploratória de dados  com R\n",
    "\n",
    "A Análise Exploratória de Dados (EDA) é uma etapa fundamental no processo de compreensão e extração de insights de conjuntos de dados. Esse notebook realiza uma EDA básica aplicada a dados fictícios da venda de café em um supermercado. Este é um exemplo destinado a usuários iniciantes e tem fins puramente educativos. \n",
    "\n",
    "O objetivo é que, ao final desta experiência, você tenha uma compreensão básica e sólida de como iniciar uma análise de dados. Vamos explorar estatísticas descritivas, gráficos informativos e até mesmo criar algumas variáveis adicionais para ganhar insights mais profundos.\n",
    "\n",
    "O código começa por oferecer uma visão geral dos dados, fornecendo estatísticas descritivas das variáveis presentes no conjunto de dados. Em seguida, prossegue para calcular os desvios padrão das medidas de vendas e preços, proporcionando uma compreensão da dispersão dos valores em torno das médias.\n",
    "\n",
    "A partir daí, o código mergulha na visualização dos dados. Histogramas são criados para ilustrar a distribuição dos preços do café, oferecendo uma representação gráfica da frequência com que os diferentes intervalos de preço ocorrem. Além disso, gráficos de dispersão são utilizados para investigar a relação entre as vendas e os preços do café, incorporando elementos visuais como cores para destacar os dias de promoção.\n",
    "\n",
    "O código também introduz a criação de variáveis derivadas, como aquela que indica se as vendas em determinado dia estão acima ou abaixo da média histórica. Essa variável adicional é usada para construir gráficos de barras e tabelas de contagem, facilitando a análise da distribuição das vendas em relação a essa média.\n",
    "\n",
    "Por fim, o código explora a representação de dados através de boxplots, permitindo identificar padrões de dispersão, mediana e possíveis outliers nas vendas e preços do café. Além disso, realiza comparações entre vendas com e sem promoção, proporcionando uma visão comparativa das distribuições desses dados.\n",
    "\n",
    "No conjunto, esse código de Análise Exploratória de Dados oferece uma jornada informativa e visualmente rica, demonstrando como a combinação de estatísticas e gráficos pode fornecer insights valiosos para tomadas de decisões informadas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "55997dd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Cria o data frame contendo o histórico de vendas do cafe\n",
    "dados <- data.frame(Vendas_Cafe = c(18, 20, 23, 23, 23, 23, 24, 25, 26, 26, 26, 26, 27, 28, 28,\n",
    "                                    29, 29, 30, 30, 31, 31, 33, 34, 35, 38, 39, 41, 44, 44, 46),\n",
    "                    Preco_Cafe = c(4.77, 4.67, 4.75, 4.74, 4.63, 4.56, 4.59, 4.75, 4.75, 4.49,\n",
    "                                   4.41, 4.32, 4.68, 4.66, 4.42, 4.71, 4.66, 4.46, 4.36, 4.47, 4.43,\n",
    "                                   4.4, 4.61, 4.09, 3.73, 3.89, 4.35, 3.84, 3.81, 3.79),\n",
    "                    Promocao = c(\"Nao\", \"Nao\", \"Nao\", \"Nao\", \"Nao\", \"Nao\", \"Nao\", \"Nao\", \"Sim\",\n",
    "                                 \"Nao\", \"Sim\", \"Nao\", \"Nao\", \"Sim\", \"Sim\", \"Nao\", \"Sim\", \"Sim\",\n",
    "                                 \"Sim\", \"Nao\", \"Nao\", \"Sim\", \"Sim\", \"Sim\", \"Nao\", \"Sim\", \"Sim\",\n",
    "                                 \"Sim\", \"Sim\", \"Sim\") )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "8500d516",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>Vendas_Cafe</th><th scope=col>Preco_Cafe</th><th scope=col>Promocao</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>18  </td><td>4.77</td><td>Nao </td></tr>\n",
       "\t<tr><td>20  </td><td>4.67</td><td>Nao </td></tr>\n",
       "\t<tr><td>23  </td><td>4.75</td><td>Nao </td></tr>\n",
       "\t<tr><td>23  </td><td>4.74</td><td>Nao </td></tr>\n",
       "\t<tr><td>23  </td><td>4.63</td><td>Nao </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lll}\n",
       " Vendas\\_Cafe & Preco\\_Cafe & Promocao\\\\\n",
       "\\hline\n",
       "\t 18   & 4.77 & Nao \\\\\n",
       "\t 20   & 4.67 & Nao \\\\\n",
       "\t 23   & 4.75 & Nao \\\\\n",
       "\t 23   & 4.74 & Nao \\\\\n",
       "\t 23   & 4.63 & Nao \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| Vendas_Cafe | Preco_Cafe | Promocao |\n",
       "|---|---|---|\n",
       "| 18   | 4.77 | Nao  |\n",
       "| 20   | 4.67 | Nao  |\n",
       "| 23   | 4.75 | Nao  |\n",
       "| 23   | 4.74 | Nao  |\n",
       "| 23   | 4.63 | Nao  |\n",
       "\n"
      ],
      "text/plain": [
       "  Vendas_Cafe Preco_Cafe Promocao\n",
       "1 18          4.77       Nao     \n",
       "2 20          4.67       Nao     \n",
       "3 23          4.75       Nao     \n",
       "4 23          4.74       Nao     \n",
       "5 23          4.63       Nao     "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizar as 5 primeiras linhas\n",
    "head(dados, 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "089fd087",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quantidade de linhas: 30 \n",
      "Quantidade de colunas: 3 \n"
     ]
    }
   ],
   "source": [
    "# Obtendo a quantidade de linhas\n",
    "quantidade_linhas <- nrow(dados)\n",
    "\n",
    "# Obtendo a quantidade de colunas\n",
    "quantidade_colunas <- ncol(dados)\n",
    "\n",
    "# Imprimindo os resultados\n",
    "cat(\"Quantidade de linhas:\", quantidade_linhas, \"\\n\")\n",
    "cat(\"Quantidade de colunas:\", quantidade_colunas, \"\\n\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24b86370",
   "metadata": {},
   "source": [
    "A seguir são mostradas algumas estatísticas descritivas do conjunto de dados. \n",
    "\n",
    "**Vendas_Cafe:** \n",
    "- A venda mínima de café registrada foi 18 unidades, enquanto a venda máxima foi de 46 unidades.\n",
    "- A mediana (valor do meio quando os dados estão ordenados) das vendas é 28.50, indicando que metade das observações estão abaixo desse valor e metade acima.\n",
    "- A média das vendas é 30.00, sugerindo que, em média, as vendas estão ligeiramente acima da mediana.\n",
    "- O desvio padrão das vendas é aproximadamente 7.31, indicando a dispersão dos valores em relação à média.\n",
    "- O primeiro quartil (25% dos dados) está em 25.25 e o terceiro quartil (75% dos dados) está em 33.75, o que indica a distribuição das vendas no conjunto de dados.\n",
    "\n",
    "**Preco_Cafe:**\n",
    "- O menor preço de café registrado foi 3.730 e o preço máximo foi 4.770.\n",
    "- A mediana dos preços é 4.480, enquanto a média é 4.426. Isso sugere que a distribuição dos preços é relativamente simétrica, com a média próxima da mediana.\n",
    "- O desvio padrão dos preços é aproximadamente 0.322 (30 centavos)\n",
    "- O primeiro quartil está em 4.353 e o terceiro quartil em 4.668, indicando a distribuição dos preços.\n",
    "\n",
    "**Promocao:**\n",
    "- Há um total de 15 registros em que \"Promocao\" é \"Nao\" e 15 registros em que é \"Sim\". Isso sugere um equilíbrio entre as observações de promoção e não promoção."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "76792326",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "  Vendas_Cafe      Preco_Cafe    Promocao\n",
       " Min.   :18.00   Min.   :3.730   Nao:15  \n",
       " 1st Qu.:25.25   1st Qu.:4.353   Sim:15  \n",
       " Median :28.50   Median :4.480           \n",
       " Mean   :30.00   Mean   :4.426           \n",
       " 3rd Qu.:33.75   3rd Qu.:4.668           \n",
       " Max.   :46.00   Max.   :4.770           "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#visualiza a media (mean) e outras estatisticas descritivas das variaveis\n",
    "summary(dados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cd74e95c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "7.31083277486696"
      ],
      "text/latex": [
       "7.31083277486696"
      ],
      "text/markdown": [
       "7.31083277486696"
      ],
      "text/plain": [
       "[1] 7.310833"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "0.322056788024478"
      ],
      "text/latex": [
       "0.322056788024478"
      ],
      "text/markdown": [
       "0.322056788024478"
      ],
      "text/plain": [
       "[1] 0.3220568"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "0.255808162676553"
      ],
      "text/latex": [
       "0.255808162676553"
      ],
      "text/markdown": [
       "0.255808162676553"
      ],
      "text/plain": [
       "[1] 0.2558082"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualiza desvio padrao (standard deviation) das variaveis\n",
    "sd(dados$Vendas_Cafe)\n",
    "sd(dados$Preco_Cafe)\n",
    "sd(dados$Preco_Leite)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b205bb69",
   "metadata": {},
   "source": [
    "O gráfico de histograma abaixo sugere que a distribuição dos dados do preço do café não é simétrica em relação à média, sendo observada uma assimetria negativa, com a maior parte das observações estando entre 4.4 e 4.8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "bddd2dcc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "Plot with title \"Histogram of dados$Preco_Cafe\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualiza atraves de um histograma a distribuicao da variavel Preco_Cafe\n",
    "\n",
    "# Define o tamanho das figuras para o Jupyter Notebook\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "\n",
    "# Cria o histograma\n",
    "hist(dados$Preco_Cafe)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "be24bc33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "Plot with title \"Distribuicao dos Preços Praticados para o Café\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Customizando o histograma\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "hist(dados$Preco_Cafe,\n",
    "     col = 'blue',\n",
    "     main = 'Distribuicao dos Preços Praticados para o Café')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f63a4016",
   "metadata": {},
   "source": [
    "Podemos observar mais de uma variável na mesma figura, isso facilita a análise. Abaixo temos a distribuição das vendas e dos preços. Às vezes parecem ter uma distribuição mais simétrica, com uma leve assimetria positiva"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "6c21470e",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA8AAAAHgCAMAAABdO/S2AAAAM1BMVEUAAAAAAP9NTU1oaGh8\nfHyMjIyampqnp6eysrK9vb3Hx8fQ0NDZ2dnh4eHp6enw8PD////UNI3wAAAACXBIWXMAABJ0\nAAASdAHeZh94AAAgAElEQVR4nO2d2YKjIBAAWY/cifn/r11vQU1EFKEzVQ+7mQwN2G05XjHq\nDQBiUaEnAADuIDCAYBAYQDAIDCAYBAYQDAIDCAaBAQSDwACCQWAAwSAwgGAQGEAwCAwgGAQG\nEAwCAwgGgQEEg8AAgkFgAMEgMIBgEBhAMAgMIBgEBhAMAgMIBoEBBIPAAIJBYADBIDCAYBAY\nQDAIDCAYBAYQDAIDCAaBAQSDwACCQWAAwSAwgGAQGEAwCAwgGAQGEAwCAwgGgQEEg8BieSql\nzqEnAZ6wrS4CiyXH3x/Gtro7C6xasvOrf2Om2WkS9bntqNGGmVm0ypS69z/cy+XYsW/79o9T\nqlSS3+Z+d0mUqtP3DOOv9Aq3LWuS/L7cePd57FtdTwKrToS5pXkkahL1qe2k0YaZWbQqnc37\nHwybt/dt3T7vV7DH5HeX6v1T0yrI31/pFW5bdnjI4bHV9SewerRvzDWafSOG8pZbwPYvy/tV\n5njXvi3bZ1oOn+NfpjPvHYr4Cr9nlmFXjq3u/gJX/xX39Mva/2kJNxbwO5adX4aN8lmpy659\n27Uvt9DJtSi3H1el7w44DrU74iustbx3O6zHzWP36voR+F1vTO7DG8Wl2vLU+/3t1qd59Uor\nX7Tt8zVVyell9DXaehfnsuus3be9VTskaXc4dj9VeyCj3d7XKVHptQ/XI7RZdRTDallWt6jH\nS1RyHqZ0L2NOT5e+J+3nJlwe/CTt4jzTy2vcbR+qT+tI4q+w2WiuDn3L52iaZlaNeSz3Gqa6\n3gS+Nxu35o1X0hY1G5U37d5qg7OZfTOzvF1X9d/Jfn/kof9kbNge7cBtuB6hz6on747tbk1H\nXaNuSufmx6dL36P2sxMu+7+aOdW6HXJnTOtIoq+w2Wi2DsMyjKZpZNWYh0WvYarrTeDyT1na\nv1FuisqNVZFV0zfKq+pfDAVsSfS+zPJ2qas0K3dDsqLOSpWk/uyAkbJk6PU9itBn1XNv5t3/\ngUlGU2o5ufRttp+fcDYchDfo3Q7BxrSOJPYKjxrN1qFfhmczkX6aRlb1edj0Gqa63gQeNm7N\n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\nIYvLPwmxW/45jhL42a6Lz8U191z/PqkWJqtfpjZtl/tN6t/Xa81Sv0PT5W5LiqT5/eJ0h7aL\n/eoNbPoNiJbYhvtQQcuQV/NG8n2l7/LcYJUVM+S8OLFpzNwbCyHLyz8OsVv+WQ4S+Jn0AucL\nLdWpqP5en6ptVPKsIh8WbRf7PVetznWrpX61povdVuTNsi1OV2trkYa+gVW/4dCy1ZKU8y1y\ndbYPOdWN67e/kOsbPLusGCHa6mIdM/vGQsji8k9C7JZ/lmMEvqqsne9VXb43zbtdzGqB7uWr\n2+cIre1iv4kq2qaL/WpNF7utO2qWbXG6WtvFfrUGNv0GRMtWw61eGwuV2Icopf/3gS53DVZZ\nMUNym1FGMXNvLIQsL/8kxGr55zlG4HKReoGvdhGqSni1S7H8R7AR2KrfOqt2/dZNLbp9dRsn\ni277tov9ag1s0xAUbXU9qeeXhrMh7e7k13W+z12DTVZGId24X9f5Scx8J19a2Cz/KMRm+T9w\njMDPPm25up/Kw/WlgEJl1tuluq1dv+daC6t+m6YW3Wbq1fRk0W3fdrFfrcGGzfNhnLUNUqre\nl6TeW7UOubS7kN/+nPa5a7DJyiikoV5dVsTMdvItxGb5RyE2y/+Bw9aKXuCarzl8V3+A7tZr\nbt3Wpt9yt8XWiK7pcrcXdXvbCjy0XexXaxC/wF22GpSqJ//9r4kZ8r5WZ3GSb3slQ+66UfT/\nrELaoep9b+uY+U6+z2xx+SedLi//J44WWJVTfxfnhT3IV5K/bdfcru1yv9c8qbdxFv0OTRe6\nrffhLAU22i70qzWIX+AuWw2qOr1UnL7/OTFDyjW64kuElrtuFP0/q5CaZnWxjpnvZGFmS8s/\n7XRx+T9ytMANxffT/0WSaSHf19y2rVW/1fGJtRGnwa4v3abV1QJLgbW2ltOtG8Qv8NvIVnN9\n6LV43UsLuVZ/jovTl83vJHfLWZmEVBiri0XMbCdLM1ta/knI8vJ/JIzAC2tj1ix7YrPmZkae\nlo+XE8t+jdOIH5ue6v2x5tdL3eptLadbN7CbbmC0bNlucLSQtD4t/WV7Ns3dYlZm0v0ery6L\nMfOdfB9mcfmnIYvL/5kIBX6lWXNBuznR+Pp6Wrdra9Fv38Ci31FfH7tVPcvd6m09TDcww6LY\nXa0xWiyu89PcLWZlJt2T1WUxZq6T5ZmtXpgNO1lHC9xcAvy2Nt77UzuXekt1/3JFfGi72G/X\nIF3uV2u61K1ei6Vu9bbW081t0hAULVsNzXxfX87QTUKaP6dfLp1O1/nFrMy4d186ebqLwIvL\nPw1ZXP4vU14f4kY723O9t3/+fCZQW/DFm220tov91re5FHl1mGF1J1bTdLHbmmbZ7O4Natpa\nTLdvIOFOrCZbDaWYRXVAd7MPKZe2aJf5G7pGllkx/v4uXvyYxsy/sTDM0vJPQiyXf7ab9SFu\ntPMtmrs+P8/0pG2d0vrF56xrbRf7be+/rTtb6ndoutyttmxL3WptF/vVG1j1Gw4tsc3CXRbn\nOwnJrBbR2NO0y4oeoq9a1sOYr6xClpd/EmK3/LPdOMQ40SWh+txF+uVsm7570XxGw77tt37r\nT6+0DZb6HTX93u172DgtdTtq+7XfYsV0AzPMtF24e7Y030mI1SIa67xdVvSQxd3huWHMV3Yh\ny8s/CXEucdSnNgHgOwgMIBgEBhAMAgMIBoEBBIPAAIJBYADBIDCAYBAYQDAIDCAYBAYQDAID\nCAaBAQSDwACCQWAAwSAwgGAQGEAwCAwgGAQGEAwCAwgGgQEEg8AAgkFgAMEgMIBgEBhAMAgM\nIBgEBhAMAgMIBoEBBIPAAIJBYADBIDCAYP6IwH9kMf86f7DMEhd5/gvTP3+N+utUff158X6o\ntH8vVff1Q0x4lj2fph0VJ6Wcvm4dNFzLXDeqSE4v17HlFPYPCPxsy/l+J+rRvveqflw9xJhz\n03M6Xk/y8s2LTQfwBecydwKXPzgaLKiwf0DgTJ0LVZT/vi/95vO8sCG1EviiknIjXVwm64lS\nzpt+6HEuc9eo/WE9kgr7BwSufqHeRbltLvq/u8lCJWwEfnX1PanT+mhYwrnMfaNiYT/rA6IK\nG9+MvnJOyo1qncZ7uTuTnMfvvq+pSq/1m/dMqaw6jElU0S1m1h75PlTWNk7qxuWWNVfJ5fMQ\nfWf6XLq9qSK/6q2b3S+9e1jJxjL3otVSqyJV+dsoR9lT1jg6dKSNLqmwsgTOqgzmVRIvTTbP\n5rvNy9rOa9PgWtUjvbeLeW83qada5LxvXFZItYc3s0MMnRmTeWo/Da27Og/dwzq2ltn4C1zH\nnI1y1OFJYXRkDC+osKIEvqnk+X4mzXb1Vv2szHe7l7dqg/ysfq7OO5/KdJ+a01dJs7zNxl1l\nRXWcdK9+Ll9eq8bzQ2idDZj7U1rrSfewiu1lbsrwyhrtskpVrRy36uWp+p3WkYaowooSOK/P\nIt+HBNevtHfzOqv3auuotAQ/q7OK1V5UuZmuanWrN+m5qgpbVL9QdRdND3NDqLlqzR0QaXXW\nurwWQMIAAAKnSURBVIdVbC9zfxa66Gqrl6Puqf7rrHWkIaqwogRW2t/P9+t+yVq7+ne1l2Ux\n82e/K6Tuab0D/Kxr1ewjdVVWennmhzA7M2fT07fupO+7h1VsL3Orb30duG88qvZkpPH4PVEX\nNo5ZWKLnO+uTOF/Z96U6rO2uA1SnJ+sd4LTcfLYvFwUehjA7a8n7Q6V7YbaOsM6S2F5mPenr\nBRZV2DhmYYmW75NKr/fXt8qW6T+n3WFr/7ururwv6qq1Gl6OetCGMDtruXQnK+s7vPTW+rRg\nNdvLPCvw+J3Z31WIKmxUk1miOWR59DV8tcck/bvdMU1/eFK92VxfaK8JVlvotD6IaRv3zbpj\n4Lkh9FY9/eXCrNog6K21acF6tpd5RmCtHNnkGNg8nBVVWFEC3/XTk4/3szkyuc+enkybk4f1\nJjTvb9GpryC115LqxuWf5FwXeH6IoTOdU33DTnUF+W20brrTuodVbC/zjMBaOa7VaeTz57PQ\nogorSuDmCtypPXlR8zDe1a7r3frfF0lzSqPp4q76E5dN42pra2xfZ4YYOjNoj47qW2b1CTXd\nDd3DOjaXeUZgvRwL14FFFVaWwNUpi/ZmnLKS2aPd+blot+gkxi06tXKvc/8xlXe1q9XfX3dN\nyzViOFPZn6+aDjF0ZnArV6qs3Xxrrdt1pu8eVrK1zHMC6+Wozl23d2Il0zux3pIKK0xgV/7I\nYv51/mCZ/8gi/5HF/Ov8wTL/wUXeghoIPRXYE7GFFTbd0IitM3xHbGGFTRcAdBAYQDAIDCAY\nBAYQDAIDCAaBAQSDwACCQWAAwSAwgGAQGEAwCAwgGAQGEAwCAwgGgQEEg8AAgkFgAMEgMIBg\nEBhAMAgMIBgEBhAMAgMIBoEBBIPAAIJBYADBIDCAYBAYQDAIDCCY/w9B3qBqZ+SzAAAAAElF\nTkSuQmCC",
      "text/plain": [
       "Plot with title \"Distribuicao dos Preços do Café\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualiza o histograma das tres variaveis numericas na mesma pagina\n",
    "#Configura layout para posicionar os graficos em duas linhas e duas colunas\n",
    "options(repr.plot.width = 8, repr.plot.height = 4)\n",
    "par(mfrow=c(1,2)) \n",
    "\n",
    "hist(dados$Vendas_Cafe,\n",
    "     col = 'blue',\n",
    "     main = 'Distribuicao das Vendas do Café')\n",
    "hist(dados$Preco_Cafe,\n",
    "     col = 'blue',\n",
    "     main = 'Distribuicao dos Preços do Café')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b6975601",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<strong>null device:</strong> 1"
      ],
      "text/latex": [
       "\\textbf{null device:} 1"
      ],
      "text/markdown": [
       "**null device:** 1"
      ],
      "text/plain": [
       "null device \n",
       "          1 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#limpa os graficos e volta o layout para configuracao normal\n",
    "dev.off() "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2e98afd",
   "metadata": {},
   "source": [
    "O gráfico de dispersão a seguir indica que a relação entre o preço e as vendas têm boa correlação negativa, ou seja, na medida em que os preços aumentam, as vendas tendem a diminuir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "d6b2cc33",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAtAAAALQCAMAAACOibeuAAAAMFBMVEUAAABNTU1oaGh8fHyM\njIyampqnp6eysrK9vb3Hx8fQ0NDZ2dnh4eHp6enw8PD////QFLu4AAAACXBIWXMAABJ0AAAS\ndAHeZh94AAAZi0lEQVR4nO3d2YKaMABG4bCIiILv/7Y14IKjVcxm/DnfRWuno1Hn1MaAYI6A\nEPPtOwCERNCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQ\nQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQ\nQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQ\nQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQ\nQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQ\nQtCQQtCQQtCQQtCQQtCQQtCQQtCQQtCQkiBoAzhyqC18wF8YApoIGlIIGlIIGlIIGlIIGlII\nGlIIGlIIGlIIGlIIGlIIGlIIGlJkgnbazwpyRIIeayZpyATtdjXI0Qja/Pkdq0XQkELQkKIR\nNHNonKkEzSoHRiJBsw6NiUzQgEXQkJI+6LY0pu6iDoH1Shj0NMmtpuPbNFGGwOqlDroxzXA8\n9o1pYwyB1UsddGEGe3kwZYwhsHqpg74srr1eZCNoOEod9OYSdBFjCKxe0qDrbduZ3eni0Lx+\nV0jQcJQ06OsBfI0phhhDYPVSrkMfDm1b1+Nbw+ZlzwQNV2wphJR8gvY8rwBgfSXot8ESNBwR\nNKR8YZVjwayCoOEoYdD7gqARW8opx1Cbqh9vgSkHIkk7h96ZcUMhQSOWxG8K+8rUA0EjmuSr\nHFtTdASNWNIv2x3K9xtOCBqOvrEOvSFoxJLPpu/EQ0CTYNB/ZjTsGbIqckH/OSgYxwhbGb2g\n72+AoziujFrQ5v73P3+EPIKGFIKGFLWgmUOvnF7QrHKsmlzQrEOvm2DQWDOChhSChhSChhSC\nhhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSChhSC\n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\n7P+y6cUz6Irn4zO3HV8cuqDbCZ6U1YVe4Pha0NMT1gd9PI+jOP3sMwt63Cw01LdpU2Pstvwm\n/DapJFsK70YJ+/P/3yjPvxB4kNMrzmBnt7uoozj97DML+rwvx/iTnx5bdftCUHf/n5WRBrkb\nZRP+tfPJKH8uRRpkm+IJc/rZ5xa03e+tnF6fz49t3OMq/Dh3z9wQaZC7USJMBp6M8udSrEG6\nKv4T5vSzzy5owAdBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpB\nQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBQwpBp8Cz\nnAxP9ceeHx7//wfN7zf2OPTD9E1WsXE+F9bhdFubx1PRDhsT/iw0v4mgP/Zh0IdzxdM3nf/g\nWHQzXb38e3V7ouKwZ0P/WQT9sQ+DrkwzmKEaX0HPZ3SpHF9Ot6Y4vToP24d/EMYEPv/h7yLo\nj30YtP0Lcz7b3vmbHE+72F9C3tiT3y0afH14Jj7RFKfX1rGe7vS//OUETbevHtvycg6vrjKm\nsrNdey7R22kxb78bM5TjuWtP1yna6y2dzzV7u6HZ6JdpxVC387twPbfW7JZWi6A/MJ43r7bt\nTOfpm2YOt6/OTqzXTt/Q2gzL7k/Q4yv0eJ1mmv+eT8Y3Xt2ewv35Gfqq8ZTxF7e7cAm6fnal\ntSHo5XbnE86OL687+2dz/9XLxZ19XT7YP9tTPNsTbm6mk9ROQffVlGFl0+3sb6dZdWe//XRx\nY/9udkMz9xOL2V04/6dxu6UVI+jl6vHcyd2f81vOvlqfzxle2b+6dXWwixP1dIXzKsdgL++n\nG7VZD/bvx1saX71nNzTzbKY8C3p2SytG0MvdneW077bV+QSx16/OLp4arg/XGYLpyvH05fN1\n6Os3X88v+3Am2D8F/w36ehdin6n2l6z70X9mnll1bed50MdtMVtvtqsc5fE+yc+Drq9z6O42\nzyboe+t+9J+ZZbYxZdv1r4I+VdeUY8XH8Vmef+/fW7v/ytO/s7aXVY69vd3ZXXi88fXiSVhu\nmtnur+n256nr9auXqe91Fmu/OC3b3a1DX//uevVR9TCHvp8OX9ehKzt/md2F4+yOrB1BL9fN\nVzn2x0N1Xlx4tspRTmsQ4ytp/WdL4eR8ebzOsbXttnaZovn/KsfppuyWwr4+/+O43oXjbbll\nuqUVI+gPjAu9m/N7vtH+7quz5ePd9e+HYr4vx+3GLper294db9ahr9PmcV+O+V2Ybmt2S+tF\n0J/YXrcJngKu9uc5wXa2pbC421I4Lsz1zWxvu9ttXS+35enfw1ShXRs5byksHrcUnuxO/3qq\n8+v27C6cb2t2S6tF0CnwLCfDU50Cz3IyPNV5Mzffviu/gacpbwT9IZ4mSCFoSCFoSCFoSCFo\nSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFoSCFo\nSCFoSCFoSCFoSCFoSPkHrR8/IgwygNgAAAAASUVORK5CYII=",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualiza relacao entre as vendas do café o preço do café\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "plot(y = dados$Vendas_Cafe,\n",
    "     x = dados$Preco_Cafe)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f0f3fafd",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "Plot with title \"Relação entre o Preço e as Vendas do Café\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Customiza o grafico\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "plot(y = dados$Vendas_Cafe,\n",
    "     x = dados$Preco_Cafe,\n",
    "     pch = 16,\n",
    "     col = 'blue',\n",
    "     xlab = 'Preço',\n",
    "     ylab = 'Quantidade Vendidade',\n",
    "     main = 'Relação entre o Preço e as Vendas do Café')\n",
    "\n",
    "#este comando adiciona linhas de grade ao grafico\n",
    "grid() "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "68881a44",
   "metadata": {},
   "source": [
    "Adicionando as informações sobre a promoção, vemos que as vendas tendem a diminuir mesmo com a promoção, se os preços não estiverem de fato abaixo da média. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "e4661383",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\nSUVORK5CYII=",
      "text/plain": [
       "Plot with title \"Relação entre o Preço e as Vendas do Café\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Colore os pontos em que havia promoção naquele dia\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "plot(y = dados$Vendas_Cafe,\n",
    "     x = dados$Preco_Cafe,\n",
    "     col = factor(dados$Promocao),\n",
    "     pch = 16,\n",
    "     xlab = 'Preço',\n",
    "     ylab = 'Quantidade Vendidade',\n",
    "     main = 'Relação entre o Preço e as Vendas do Café')\n",
    "\n",
    "\n",
    "#adiciona legenda\n",
    "legend(x=4.4,y=45,\n",
    "       c(\"Promoção\",\"Sem_Promoção\"),\n",
    "       col=c(\"red\",\"black\"),\n",
    "       pch=c(16,16))\n",
    "grid()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6da03ff",
   "metadata": {},
   "source": [
    "O gráfico de barras a seguir mostra que a quantidade de unidades vendidas foi maior quando os preços estavam abaixo da média."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1238f60d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Cria uma nova variavel informando se naquele dia vendeu acima ou abaixo da media historica\n",
    "media <- mean(dados$Vendas_Cafe) #armazena a media em uma variavel\n",
    "variavel <- ifelse(dados$Vendas_Cafe > media,\n",
    "                   'Acima_da_media',\n",
    "                   'Abaixo_da_media')\n",
    "\n",
    "variavel <- factor(variavel) #converte nova variavel para factor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "fcade402",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n2LbL5vk9XW6vlh8Xn669XHZvJPB9/1Pq5mK5uPntVra794LZj/114YGnz1wvm+vd28f8eM+Y\np5vZ3Pyy9vj6dR2MaH+2l7s3wPlxwm+/rSMnP2U6LYLexfr9+f1ql2X/Rhi7y9fPb/Cy3V/7\neL9/TLTZPPx8+5df3952f+3VbuQHCw8sy/7628ufn7t6vZnXtcfXr+tgRM9nuxvE8wm//baO\nnPyY6XQI+uG51WX31kRPO3X3eLfZ/Sxadh++7X8o7D7cLNdPw9xf9fIlB35eu7xZeOBpdx6e\nbuT542b3KOvp0sPl7pHWm7XH1q/qcETfdif+ZVfU88m+/bbeP/k50/lMu3LMt/3/3Z//Qn1+\nKH+7XP385EvQTz8obvZXX/34krc/oq/2d0luXwf9+5Z933/8+Xf11b6Oh91NHqw9vn5VhyPa\nn+3Dc7y/f1vPfj35OdP5TLtyzMV+YnfLxePLoJ7/5/72+vI16Pvlzbb9MtL3F/72Ba8fD97i\n9GDt8fWremdEj4cnfPjx+Dc/YTqfaVeOuH8Z3v3byV++vKfu87XbZfvyuT8G/brwty/4V1v2\n7vo1vTeixyNB/+GbnzCdT7Qrx1y/DO/6zfS+LBc3t/dn/IQ+WPjbFxxu2Xtrj69f03sjenw/\n6D998xOm84l25ZiL5cd7MO/+Ql1+3GG7eq348cfFq6f70JePr/ehr97cyvO13182o9yyq9cX\n3n5Z+/76Nb0Z0eUv96F3n/ilxN9Ofs50PtGuHHH3Uublcvf481mO2+e2717vQ+8eF10vN8ee\n5bg9fCz+svDAr1u2v5nH/ePM218fx7+3fkVvR3SzewJi+/osx+76w6DfO/k50/k8u3LM9uVn\nwe3+6fsv+2c995949n0/yIfN8xNX98eeh94/cfplN+iDhQeO3Nnc3L9Ze3z9it6O6NfnoXfX\nv348cvJjpvP5g95sDi8u+1cKr/d/fJrh5fef9z6+/HilcNfxzea9VwqvX14Le1144Lct270W\ntny5f7v2+PoVvR3Rvqmrg1cKH998PHLyU6bz+YOGEwiaUUYHvbw68wsmmzmdRqd6uplb9l+Z\nOZ1Gpwo1QTOKoBlF0IwiaEYRNKMImlEEzSiCZhRBM4qgGUXQjCJoRhE0owiaUQTNKIJmFEEz\niqAZRdCMImhGETSjCJpRBM0ogmYUQTOKoBlF0IwiaEYRNKMImlEEzSiCZhRBM4qgGUXQjCJo\nRhE0owiaUQTNKIJmFEEziqAZRdCMImhGETSjCJpRBM0ogmYUQTOKoBlF0IwiaEYRNKMImlEE\nzSiCZhRBM4qgGUXQjCJoRhE0owiaUQTNKIJmFEEziqAZRdCMImhGETSjCJpRBM0ogmYUQTOK\noBnlH+UJj7nXr0pyAAAAAElFTkSuQmCC",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "plot(variavel) #grafico com a qtde abaixo e acima da media"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a730cae6",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "variavel\n",
       "Abaixo_da_media  Acima_da_media \n",
       "             19              11 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "table(variavel) #visualiza a qtde abaixo e acima da media"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05af1e7e",
   "metadata": {},
   "source": [
    "O gráfico de box-plot abaixo a distribuição dos dados de venda, não indicando a presença de nenhum outlier."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "e76d4d4d",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAtAAAALQCAMAAACOibeuAAAAMFBMVEUAAABNTU1oaGh8fHyM\njIyampqnp6eysrK9vb3Hx8fQ0NDZ2dnh4eHp6enw8PD////QFLu4AAAACXBIWXMAABJ0AAAS\ndAHeZh94AAARfklEQVR4nO3b0XbaWLNF4S0QMsYgv//bdoxjt2+6qgeuvcVamt/NIRcdVZXn\nySCQv70DRtrWAwCVCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpW\nCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpW\nCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpW\nCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpW\nCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpW\nCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWCBpWBgTdgAc9UFt9wBs8Ap4IGlYIGlYIGlYI\nGlYIGlYIGlYIGlYIGlYIGlYIGlYIGlYIGlYIGlYIGlYIGlYIGlYIelPP/D/k0ETQcjhOhKDl\ncJwIQcvhOBGClsNxIgQNKwQNK+ODPh9amy9dH4H9Ghj052ehx8+PRZcuj9gFjhMZHfTSlvX9\n/ba0c49H7ALHiYwOemrrx+u1HXo8Yhc4TmR00F/fwcbfxfIzC3CcyOigT19BTz0esQscJzI0\n6PnlfGmvf16uS/y3Qn5meNDQoL//3Vdr09rjEdi9kZ9DX6/n8zzf/2q4hD0TNB7FN4VyOE7k\neYLe5T9HfwTHiWwSdBosP7MAx4kQtByOE9ngU47/8a6Cn1mA40QGBv02ETR6G/mWY53b8Xb/\nHXjLgU7Gvod+bfcvCgkavQz+S+Ht2OaVoH+F40SGf8rx0qYLQf8Gx4mM/9juesi/OOFnFuA4\nkS0+hz4R9G9wnMjzfPU9+BG6OE6EoGGFoGGFoGGFoOVwnAhBy+E4EYKWw3EiBC2H40QIWg7H\niRA0rBA0rBA0rBC0HI4TIWg5HCdC0HI4ToSg5XCcCEHL4TgRgoYVgoYVgoYVgpbDcSIELYfj\n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\nEYKGFYKGFYKGFYKWw3EiBC2H40QIWg7HiRC0HI4TIWg5HCdC0LBC0LBC0LBC0HI4ToSg5XCc\nCEHL4TgRgpbDcSIELYfjRAgaVggaVggaVghaDseJELQcjhMhaDkcJ0LQcjhOhKDlcJwIQcMK\nQcMKQcMKQcvhOJGhQb+9zO3DvLz1esQOcJzIwKDXQ/vXscsjdoHjRAYGvbTp9Xp/dbtMbenx\niF3gOJGBQU/t+v362qYej9gFjhMZGHRr//WLskdg9/gTGlbGvoe+3O6veA+NXkZ+bHf88SnH\nYe3yiD3gOJGxn0Mv98+hp/mFz6Efx3EifFMoh+NEnifo9lOfR3jgOJGRQa+n1o6Xv78JH9s9\niuNERn71PX3+Q47P34Sg0cPQj+3Of6o+T/d/xkHQ6GLoFyv3/3ObDjeCRicbfPW9Ho8E/Qsc\nJzIw6EP7+jLlcCTox3GcyMCgz+3099WtHQn6YRwnMvJju+W74kvyUTM/swDHiQz9YuU6f726\nnQj6URwn8jzfFA5+BDwRNKwQNKwQtByOEyFoORwnQtByOE6EoOVwnAhBy+E4EYKGFYKGFYKG\nFYKWw3EiBC2H40QIWg7HiRC0HI4TIWg5HCdC0LBC0LBC0LBC0HI4ToSg5XCcCEHL4TgRgpbD\ncSIEvak2zNabjkLQsELQsELQsELQsELQsELQsELQsELQsELQsELQsELQsELQsELQsELQsELQ\nsELQsELQsPKkQQMPeqC2+oCB7RA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0\nrBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0\nrBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0\nrBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0\nrBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0\nrBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0\nrBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0rBA0\nrBA0rPwD+zKbKdSMNGMAAAAASUVORK5CYII=",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Gera boxplot das vendas\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "boxplot(dados$Vendas_Cafe)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c72bbb7a",
   "metadata": {},
   "source": [
    "Já os dados de preço mostram alguns valores discrepantes no limite inferior, possivelmente de promoções."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "99ab7b65",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nOR62w5OguZT9b9s938yf1RA0Z7rGfeg7QX+G5Yx46zuO5YwIOo7ljAg6juWMCDqO5YwImiqC\npoqgqSLoOJYzIug4ljMi6DiWMyLoOJYzIug4ljMiaKoImiqCpoqg41jOiKDjWM6IoONYzoig\n41jOiKDjWM6IoKkiaKoImiqCjmM5I4KOYzkjgo5jOSOCjmM5I4KOYzkjgqaKoKkiaKoIOo7l\njAg6juWMCDqO5YwIOo7ljAg6juWMCJoqgqaKoKki6DiWMyLoOJYzIug4ljMi6DiWMyLoOJYz\nImiqCJoqgqaKoONYzoig41jOiKDjWM6IoONYzoig41jOiKCpImiqCJoqgo5jOSOCjmM5I4KO\nYzkjgo5jOSOCjmM5I4KmiqCpsmvQPx9ut3e39z8v9RJ8czsGfbrZ/na8yEt8C5YzsmPQ99vh\n8fnjs5enw3Z/iZf4FixnZMegD9vzfz5/3g6XeIlvwXJGdgx62/7XPyx7iW/BckZ8hY5jOSP7\nXkM/vXx85hqaS9nztt3xj7scN6eLvATf3b73oe8/7kMfbh/ch+YyvFMYx3JGBB3HckYEHcdy\nRq4VtPvQZ7Ocka8T9PanFS/RynJGXHJQRdBUETRVrhL09BpZ0AOWMyLoOJYzsuvjo//4Rob/\nZgOWM7Jj0D8Pgl7Bckb2vOQ43W7Hj+dHXXJ8huWM7HsN/bhtj6+C5nJ2/qbw5bjdngTNxex+\nl+NhOzwJmkvZ/7bd8838WQ1BD1jOyDXuQ98J+jMsZ8Rb33EsZ0TQcSxnRNBxLGdE0FQRNFUE\nTRVBx7GcEUHHsZwRQcexnBFBx7GcEUHHsZwRQVNF0FQRNFUEHcdyRgQdx3JGBB3HckYEHcdy\nRgQdx3JGBE0VQVNF0FQRdBzLGRF0HMsZEXQcyxkRdBzLGRF0HMsZETRVBE0VQVNF0HEsZ0TQ\ncSxnRNBxLGdE0HEsZ0TQV7Xt5tqT7kXQVBE0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVB\nU0XQVBE0VQRNFUFTRdBUETRVBJ3mG/041TkEneWjZkn/b4LOsv3xkf+HoKNs//Un/03QUQQ9\nI+gogp4RdBbX0BOCzuIux8SeQb/cbYeH19cfN9vh/kIv8Q24Dz20Y9Cnw/vvWPvx8PGr1o4X\neQm+vR2Dvt/evi7fH7a70+vp4/P1L8G3t2PQh49/cdtOH38cLvESfHs7Br1tf3+cfF8jaM50\nha/Q7x9PvkKfyzeFQ1e4hr4//fp8/Uv0c9tuwl2OLN5YmXAfOoq3vme8UxhF0DOCjiLoGUFn\ncQ09ca2g3Yc+j7scE18n6G/5f9U7g+0MueRII+ghQWdxyTEh6Cy+KZy4QtA/DtvNj8u+RC23\n7Wb2DPr5djv8ePXW9ycIembHoJ8/Sr5/f8D/5XYbfo323+t/EPTMjkHffTxt99dzo6ft5hIv\n0c819MT+D/jf/vEPq1+in7scE7sH/fjXtYYH/M/lPvTQrpccd6dfn57uPODPRez8gP/vv2L8\nBVrQnGvX+9D3vzP2gD8X4p1CqgiaKoKmiqCpImiqCJoqgqaKoKkiaKoImiqCpoqgqSJoqgia\nKoKmiqDT+BGsIUFn8UOyE4LO4tcYTAg6il80MyPoKIKeEXQUQc8IOotr6AlBZ3GXY0LQadyH\nHhI0VQRNFUFTRdBUETRVBE0VQVNF0FQRNFUETRVBU0XQVBE0Vb5o0HCmM2pbHzBcj6CpImiq\nCJoqgqaKoKkiaKoImiqCpoqgqSJoqgiaKoKmiqCpImiqCJoqgqaKoKkiaKoImiqCpoqgqSJo\nqgiaKoKmiqCpImiqCJoqgqaKoKkiaKoImiqCpoqgqSJoqgiaKoKmiqCpImiqCJoqgqaKoKki\naKoImiqCpoqgqSJoqgiaKoKmiqCpImiqCJoqgqaKoKkiaKoImiqCpoqgqSJoqgiaKoKmiqCp\nImiqCJoqgqaKoKkiaKoImiqCpoqgqSJoqgiaKoKmiqCpImiqCJoqgqaKoKkiaKoImiqCpoqg\nqSJoqgiaKoKmiqCpImiqCJoqgqaKoKkiaKoImiqCpoqgqSJoqgiaKoKmiqCpImiqCJoqgqaK\noKkiaKoImiqCpoqgqSJoqgiaKoKmiqCpImiqCJoqgqaKoKkiaKoImiqCpoqgqSJoqgiaKoKm\niqCp8n8BmJYSeZ5XVwAAAABJRU5ErkJggg==",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Gera boxplot do preco\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "boxplot(dados$Preco_Cafe)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1d2781b",
   "metadata": {},
   "source": [
    "Se analisarmos os box-plots das vendas para dias com e sem promoção, notamos que a mediana das vendas dos dias com promoção é maior do que as dos dias sem. No entanto, há maior variação nesses casos. Então, para concluirmos com maior segurança essa associação, é interessante a realização de testes de hipóteses para confirmar se essas diferenças são estatisticamente significativas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "db92b007",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\nSPkPCLPGoeuitS0AAAAASUVORK5CYII=",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Gera boxplot comparativo das vendas quando houve promocao e de quando nao houve\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "boxplot(dados$Vendas_Cafe~dados$Promocao)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "35806b01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "Plot with title \"Vendas com promoção vs Vendas sem promoção\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Customizando o boxplot\n",
    "options(repr.plot.width = 6, repr.plot.height = 6)\n",
    "boxplot(dados$Vendas_Cafe~dados$Promocao,\n",
    "        col = 'gray',\n",
    "        pch = 16,\n",
    "        xlab = 'Promoção',\n",
    "        ylab = 'Vendas',\n",
    "        main = 'Vendas com promoção vs Vendas sem promoção')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
