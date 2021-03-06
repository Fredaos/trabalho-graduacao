<Qucs Schematic 0.0.18>
<Properties>
  <View=0,0,951,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=teste7a.dat>
  <DataDisplay=teste7a.dpl>
  <OpenDisplay=1>
  <Script=teste7a.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Título>
  <FrameText1=Desenhado por:>
  <FrameText2=Data:>
  <FrameText3=Revisão:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <GND * 1 400 350 0 0 0 0>
  <GND * 1 470 90 0 0 0 0>
  <GND * 1 730 150 0 0 0 2>
  <C C1 1 320 240 -26 17 0 0 "220 nF" 1 "0" 1 "polar" 0>
  <GND * 1 170 300 0 0 0 0>
  <.TR TR1 1 200 380 0 65 0 0 "lin" 1 "0" 1 "50 ms" 1 "100" 0 "Trapezoidal" 0 "2" 0 "1 ns" 0 "1e-16" 0 "150" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "26.85" 0 "1e-3" 0 "1e-6" 0 "1" 0 "CroutLU" 0 "no" 0 "yes" 0 "0" 0>
  <Vdc V4 5 730 190 -58 -26 0 3 "10 V" 1>
  <Vdc V3 5 730 460 -58 -26 0 3 "10 V" 1>
  <GND * 1 730 490 0 0 0 0>
  <Lib OP1 5 690 280 -20 64 0 0 "OpAmps" 0 "ua741(mod)" 0>
  <Vdc V1 5 400 100 -52 -26 0 3 "2 V" 1>
  <Vac V2 5 170 270 18 -26 0 1 "0.25 V" 1 "10 kHz" 1 "0" 0 "0" 0>
  <R R1 1 400 320 15 -26 0 1 "470 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <R R4 1 530 240 -26 -43 1 0 "5 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <R R3 1 720 70 -26 15 0 0 "10 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <R R2 1 400 160 15 -26 0 1 "470 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <GND * 1 630 410 0 0 0 0>
  <Vdc V5 1 630 370 18 -26 0 1 "1 V" 1>
</Components>
<Wires>
  <400 60 400 70 "" 0 0 0 "">
  <400 60 470 60 "" 0 0 0 "">
  <470 60 470 90 "" 0 0 0 "">
  <400 240 400 290 "" 0 0 0 "">
  <350 240 400 240 "" 0 0 0 "">
  <170 240 290 240 "" 0 0 0 "">
  <730 150 730 160 "" 0 0 0 "">
  <800 280 840 280 "" 0 0 0 "">
  <560 240 620 240 "" 0 0 0 "">
  <400 240 500 240 "" 0 0 0 "">
  <730 320 730 430 "" 0 0 0 "">
  <730 220 730 240 "" 0 0 0 "">
  <620 240 650 240 "" 0 0 0 "">
  <780 280 800 280 "" 0 0 0 "">
  <800 70 800 280 "" 0 0 0 "">
  <750 70 800 70 "" 0 0 0 "">
  <620 70 620 240 "" 0 0 0 "">
  <620 70 690 70 "" 0 0 0 "">
  <400 190 400 240 "" 0 0 0 "">
  <630 400 630 410 "" 0 0 0 "">
  <630 320 650 320 "" 0 0 0 "">
  <630 320 630 340 "" 0 0 0 "">
  <170 240 170 240 "Vin" 200 210 0 "">
  <400 240 400 240 "Vout" 430 210 0 "">
  <840 280 840 280 "Vout2" 870 250 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
