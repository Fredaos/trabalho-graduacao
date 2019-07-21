<Qucs Schematic 0.0.18>
<Properties>
  <View=0,0,870,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=teste3b.dat>
  <DataDisplay=teste3b.dpl>
  <OpenDisplay=1>
  <Script=teste3b.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <GND * 1 290 310 0 0 0 0>
  <GND * 1 650 360 0 0 0 0>
  <.TR TR1 1 230 400 0 65 0 0 "lin" 1 "0" 1 "50 ms" 1 "100" 0 "Trapezoidal" 0 "2" 0 "1 ns" 0 "1e-16" 0 "150" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "26.85" 0 "1e-3" 0 "1e-6" 0 "1" 0 "CroutLU" 0 "no" 0 "yes" 0 "0" 0>
  <GND * 1 720 100 0 0 0 0>
  <Vac V1 5 290 280 18 -26 0 1 "0.5 V" 1 "10 kHz" 1 "0" 0 "0" 0>
  <C C1 1 440 250 -26 17 0 0 "220 nF" 1 "0" 1 "polar" 0>
  <Vdc V2 5 650 110 -52 -26 0 3 "5 V" 1>
  <R R1 1 650 330 15 -26 0 1 "10 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <R R2 5 650 170 15 -26 0 1 "40 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
</Components>
<Wires>
  <290 250 410 250 "" 0 0 0 "">
  <650 250 650 300 "" 0 0 0 "">
  <470 250 650 250 "" 0 0 0 "">
  <650 200 650 250 "" 0 0 0 "">
  <650 70 650 80 "" 0 0 0 "">
  <650 70 720 70 "" 0 0 0 "">
  <720 70 720 100 "" 0 0 0 "">
  <650 250 830 250 "" 0 0 0 "">
  <290 250 290 250 "Vin" 320 220 0 "">
  <830 250 830 250 "Vout" 870 220 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
