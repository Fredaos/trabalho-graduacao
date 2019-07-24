<Qucs Schematic 0.0.18>
<Properties>
  <View=0,0,900,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=circuito_teste4.dat>
  <DataDisplay=circuito_teste4.dpl>
  <OpenDisplay=1>
  <Script=circuito_teste4.m>
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
  <GND * 1 120 330 0 0 0 0>
  <GND * 1 480 380 0 0 0 0>
  <GND * 1 550 120 0 0 0 0>
  <Vac V1 5 120 300 18 -26 0 1 "0.5 V" 1 "10 kHz" 1 "0" 0 "0" 0>
  <C C1 1 270 270 -26 17 0 0 "220 nF" 1 "0" 1 "polar" 0>
  <Vdc V2 5 480 130 -52 -26 0 3 "5 V" 1>
  <R R1 1 480 350 15 -26 0 1 "10 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <R R2 5 480 190 15 -26 0 1 "40 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <GND * 1 670 400 0 0 0 0>
</Components>
<Wires>
  <120 270 240 270 "" 0 0 0 "">
  <480 270 480 320 "" 0 0 0 "">
  <300 270 480 270 "" 0 0 0 "">
  <480 220 480 270 "" 0 0 0 "">
  <480 90 480 100 "" 0 0 0 "">
  <480 90 550 90 "" 0 0 0 "">
  <550 90 550 120 "" 0 0 0 "">
  <730 200 730 270 "" 0 0 0 "">
  <730 430 890 430 "" 0 0 0 "">
  <890 200 890 430 "" 0 0 0 "">
  <730 200 890 200 "" 0 0 0 "">
  <730 270 730 400 "" 0 0 0 "">
  <480 270 730 270 "" 0 0 0 "">
  <730 400 730 430 "" 0 0 0 "">
  <670 400 730 400 "" 0 0 0 "">
  <120 270 120 270 "Vin" 150 240 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
  <Text 740 390 12 #000000 0 "P 01">
  <Text 740 260 12 #000000 0 "P 39">
  <Text 740 210 12 #000000 0 "BeagleBone Black">
</Paintings>
