
// Declaracao de variaveis
int analogPin = A0; 
int valor = 0;
float tensao = 0;

void setup() {
  Serial.begin(9600);             // quantidade de bits por segundo 
}

void loop() {
  valor = analogRead(analogPin);  // leitura do sinal analogico
  tensao = valor*(5.0/1023.0);    // conversao do dado bruto para tensao
  delay(1000);                    // espera 1 s
  Serial.print(tensao);           // imprime tensao no serial monitor
  Serial.print(" V\n");           // imprime unidade e pula linha
}
