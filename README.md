# Auditcontrole

Dit is een python script geschreven voor de 3e stageperiode als PoC. 
De script controleert de geslecteerde baseline op overtredingen die in de baseline staan geformuleerd.
De eindresultaat is dat het een uitslag presenteert van de audit op de configuratie van de netwerkapparatuur.
Wanneer bij de audit een richtlijn in de baseline is overtreden wordt er een telegram bericht gestuurd naar de beheerder waarin wordt geinformeerd welk netwerkapparaat welke richtlijn heeft overtreden. 

De volgende command zorgt voot de uitvoering van het script: python main.py RouterTestConf.txt baseline.json
RouterTestConf.txt en baseline.json zijn argumenten die kunnen worden gewijzigd.

