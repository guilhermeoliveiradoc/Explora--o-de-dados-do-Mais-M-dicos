# The Mais Médicos Programm in Brazil and it's effects on child mortality

## Introduction

The idea of this project was to investigate how did the Mais Médicos programm affect the mortality in childs, and also how it impacted on some crucial health indicators in the county.

After building an API to extract data from IBGE database, I also downloaded a few databases from WEBSITE that added some new perspectives on the analysis.

By the end, I created a few visualizations on Tableau to summ up the ideas that were approached.







## Why is this theme relevant?

During the 2018 elections, the actual president Jair Bolsonaro, while still candidate, made some speaches containing arguments agains the programm, that started during 2013 in Roussef's presidency. After he assumed the office in 2019, Cuba's government called the cubans professionals back to their country, after writing a letter criticising the hostility agains it's citizens.

After the formal end of this endeavor, a lot of cities in Brazil went completly out of basic health assistance by doctors. Some localities in the interior of the county do not count with a body of doctors, that are heavily concentrated in the central regions - according to the data consulted, this proportion is 4x higher in the capitals.

This scenario contributed to a spike on the mortality rates of children that were born in this places, and the number of pregnant woman assisted by qualified professionals also dropped.

In order to explore this subject and reflect about this abrupt change in orientation on our health institucions and policies, I reunited some databases and articles that detail this path and point to the consequences of it.






## Processing the data

The first action was to build an API that could get two databases from IBGE. After that, two Data Frames were created that based the first two visualizations.

After that, I used the Child's Observatory databases that contained more information to elucidate the questions. I downloaded directly from the website, and projected some graphs to make it easier to understand.

A few data clean was necessary, and that is shown in the code.



## Results

The statistics show a large improvement on all the indicators observed after 2013. The number of health appointments, the mortality rate, the proportion of pregnants that could get assessment: all of them had a sharp improvement after 2013.

Even considering that the numbers were already improving, it is clear that not all of this measures and policies had consistent changes before the program.

Some statistics started to drop even before the end of Mais Médicos, probabily because of the loud political campaigns that incited the far-right electors against the cuban doctors - in some cases even with physicall agressions.  This was largelly reported by the press.

After 2019 there were no indicator that did not get worse, according to the data gathered.







## References
1. https://observatoriocrianca.org.br/cenario-infancia/temas/sobrevivencia-infantil-infancia/676-proporcao-de-obitos-de-menores-de-um-ano-de-idade-por-causas-claramente-evitaveis?filters=1,282;4,282
2. https://observatoriocrianca.org.br/cenario-infancia/temas/sobrevivencia-infantil-infancia/615-numero-de-nascidos-vivos?filters=1,229
3. https://observatoriocrianca.org.br/cenario-infancia/temas/sobrevivencia-infantil-infancia/728-numero-de-nascidos-vivos-cujas-maes-fizeram-sete-ou-mais-consultas-de-pre-natal-segundo-anos-de-estudo-da-mae?filters=1,1043;20,1043
4. https://amb.org.br/wp-content/uploads/2018/03/DEMOGRAFIA-M%C3%89DICA.pdf
5. https://www.imb.go.gov.br/files/docs/publicacoes/informes-tecnicos/2018/12-mortes-evitaveis-na-infancia-201810.pdf
6. https://www.poder360.com.br/coronavirus/covid-esta-entre-maiores-causas-de-morte-de-5-a-11-anos/
7. https://www.imb.go.gov.br/files/docs/publicacoes/informes-tecnicos/2018/12-mortes-evitaveis-na-infancia-201810.pdf
8. https://saude.estadao.com.br/noticias/geral,pelo-menos-44-das-mortes-de-criancas-sao-por-doencas-evitaveis-diz-estudo,70003883521
9. https://piaui.folha.uol.com.br/materia/os-pequenos-que-se-foram/
