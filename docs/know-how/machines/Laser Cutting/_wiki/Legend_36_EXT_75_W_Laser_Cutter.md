![](/assets/images/IMG_1600.JPG "IMG_1600.JPG")

## Technical specifications

  - Cutting area 900 x 600 millimeters / 35.4" x 23.6" inches
  - Cutting power max. 75 Watt.
  - Maximum Power Consumption:

## Health & Safety

![](/assets/images/Extractor-Compressor-Laser.jpg
"Extractor-Compressor-Laser.jpg")

### 1\. PRECAUTIONS

| Step | Description                                                                                                                                                  |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      |                                                                                                                                                              |
| 1\.  | If you are not going to use the computer in the Fab Lab, install the Epilog drivers in your computer (you can reach the machine inside the Fab Lab network). |
| 2\.  | Turn on the main fume extractor in the big laser cutter switch panel.                                                                                        |
| 3\.  | Turn on the small air compressor on the left hand side of the machine.                                                                                       |
| 4\.  | Turn on the laser cutter (left side of the machine).                                                                                                         |
| 5\.  | Turn on the pc desktop and the monitor of the Lab connected to the laser machine.                                                                            |
| 6\.  | Make sure the material you want to use is in the 'Materials and configuration' list. If it is not there, ask the Fab Lab responsible.                        |
| 7\.  | Measure the size of your material board. If it doesn’t fit into the board of the laser machine ask the Fab Lab responsible for cutting the correct format.   |

### 2\. FILE SETTINGS

| Step | Description                                                                                                                                                                                          |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      |                                                                                                                                                                                                      |
| 1\.  | Open dxf, 3dm, or compatible file with Rhino.                                                                                                                                                        |
| 2\.  | Select the curves and hatches and put them in separate layers.                                                                                                                                       |
| 3\.  | Choose the correct colour for every operation (Cutting, Engraving, Raster E.).                                                                                                                       |
| 4\.  | Select all objects and make sure that they are displayed by layer on properties.                                                                                                                     |
| 5\.  | From your vector editing software, once you are ready for printing and if you already installed the driver, press Ctrl+P or select ‘Print’.                                                          |
| 6\.  | Select ‘Epilog Engraver 75’ from the printer list and go to ‘Printer settings’ or ‘Properties’.                                                                                                      |
| 7\.  | The laser cutter driver interface should appear. Here you can set-up the laser’s power and speed according to how the vector paths in your drawing are organized (you can also print raster images). |

### 3\. PRINT SETTINGS:

| Step | Description                                                                                                                                                                                                                          |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      |                                                                                                                                                                                                                                      |
| 1\.  | For a vector job, In the 'General' tab, under 'Job type' select 'Vector'.                                                                                                                                                            |
| 2\.  | Set the size of the material sheet under 'Piece Size'.                                                                                                                                                                               |
| 3\.  | Set to 'Vector sorting' and 'Optimize'.                                                                                                                                                                                              |
| 4\.  | In the 'Color mapping' tab select the checkbox 'Color mapping'. You must have an organized drawing with lines in different layer colors and sort them depending on the type of job (raster, engraving and cutting).                  |
| 5\.  | Once this is done, you can set the power, speed, and frequency of every color in your drawing. Take a look at the 'Materials and configuration' list above for the right power/speed values according to the material you are using. |
| 6\.  | Send parameters with the double arrow once you set for each color.                                                                                                                                                                   |
| 7\.  | The list order determines the execution sequence of every type of job. You should always engrave first and cut later. You can change the order by selecting a color and pressing the up and down arrows.                             |
| 8\.  | Once you are done with this configuration, press 'OK'.                                                                                                                                                                               |
| 9\.  | For a raster job, In the 'General' tab, under 'Job type' select ‘Raster’. For both jobs select ‘Combined’ and follow the steps from 2 to 8.                                                                                          |
| 10\. | Make sure the Scale is 1:1 (100%) and set the window by moving it to the correct point in the drawing. You should see the parts that you want to cut/engrave fitting the material in the preview.                                    |
| 11\. | Finalize the process with 'Print' and the file will be sent to the laser cutter.                                                                                                                                                     |
|      |                                                                                                                                                                                                                                      |

### 4\. MACHINE:

| Step | Description                                                                                                                                                             |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      |                                                                                                                                                                         |
| 1\.  | Open the hood and place the material on the metal bed without hitting the cutting head.                                                                                 |
| 2\.  | If the material you use is too thick you should lower the bed switching OFF the X/Y and bring the bed to the desired Z position by pressing the 'up' and 'down' arrows. |
| 3\.  | Turn on the laser pointer 'Puntero’.                                                                                                                                    |
| 4\.  | Set the machine head to the origin by pressing 'Restaur.' and focus the laser by pressing 'Enfocar' and click 'GO/Entra' to run the file.                               |
| 5\.  | Tape the corners for the material and where it is needed, if necessary. Close the hood.                                                                                 |
| 6\.  | After you have sent the job to the machine you will see 'Job:job name' in the display.                                                                                  |
| 7\.  | Pressing the up and down arrows will allow you to select the different jobs stored in the machine.                                                                      |
| 8\.  | Press 'GO/Entra' to start cutting/engraving.                                                                                                                            |
| 9\.  | Press 'STOP/Salir' if something burns inside the machine or the material is not in the right position.                                                                  |
| 10\. | Never leave the machine unattended.                                                                                                                                     |
|      |                                                                                                                                                                         |

## CAM

  - **2D** Printer driver from most CAD or ilustration software
  - From PDF

## Tools

  - Tools here

## Materials and configurations

### Settings

| Material                            | Cut       | Engraving | <u>Raster</u> Engraving - 600 DPI |
| ----------------------------------- | --------- | --------- | --------------------------------- |
|                                     | Speed (%) | Power (%) | Frequency (Hz)                    |
| Polypropylene - White - 0.5mm       | 55        | 50        | 5000                              |
| Polypropylene - Transparent - 0.8mm | 35        | 60        | 5000                              |
| Polypropylene - Black - 1.2mm       | 35        | 80        | 5000                              |
| Wood - Plywood - 4mm                | 20        | 90        | 300                               |
| Wood - MDF - 5mm                    | 15        | 100       | 300                               |
| Paper - Grey - 1.5mm                | 55        | 75        | 500                               |
| Acrylic - Transparent - 2mm         | 30        | 90        | 5000                              |
| Acrylic - Transparent - 3mm         | 20        | 90        | 5000                              |
| Acrylic - Transparent - 4mm         | 15        | 90        | 5000                              |
| Acrylic - Transparent - 5mm         | 15        | 100       | 5000                              |
| Acrylic - Transparent/Matt - 3mm    | 20        | 90        | 5000                              |
| Foam with Textile - Black - 3mm     | 60        | 50        | 250                               |

Laser settings for common materials - Epilog 75W

**Note:** Settings above are a good starting point. Laser cutting
quality is affected by several factors including lens cleanliness,
maintenance and/or aging laser tube. If you are not achieveing a cut,
try to increase the power, decrease the speed or a do combination of
both. Change settings with 5-10% step at a time.

### Suppliers

[For a supplier list take a look at this table maintained by de Fab Lab
BARCELONA](http://fablabbcn.org/maquinas/provedores-materiales/)

## Machine work flow

  - If you are not going to use the computer in the Fab Lab, [Harga AC
    Murah](http://www.buletinac.com/)install the Epilog drivers in your
    computer (you can reach the machine inside the Fab Lab network).
  - Turn on the main fume extractor in the big laser cutter switch
    panel.
  - Turn on the small air compressor on the left hand side of the
    machine.
  - Turn on the laser cutter (left side of the machine).
  - Make sure the material [Harga Ban Motor
    Corsa](http://www.buletinautomotif.com/) you want to use is in the
    'Materials and configuration' list. If it is not there, ask the Fab
    Lab responsible.
  - Measure the size of your material board.
  - From your vector editing software, once you are ready for printing
    and if you already installed the driver, press Ctrl+P or select
    'Print'.
  - Select 'Epilog Engraver' from the printer list and go to 'Printer
    settings' or 'Properties'.
  - The laser cutter driver interface should appear. Here you can set-up
    the laser's power and speed according to how the vector paths in
    your drawing are organized (you can also print raster images).
    [Harga HP Samsung](http://www.buletinsamsung.com/)
  - For a vector job:
      - In the 'General' tab, under 'Job type' select 'Vector'.
      - Set the size of the material sheet under 'Piece Size'.
      - Set to 'Vector sorting' and 'Optimize'.
      - In the 'Color mapping' tab select the check box 'Color mapping'.
        You should have organized your drawing in different colors if
        you need to do different types of jobs (for example engraving
        and cutting).
      - Once this is activated, you can set the power, the speed, and
        other parameters for every single color in your drawing. Take a
        look at the 'Materials and configuration' list above for the
        proper power/speed values according to the material you are
        using.
      - The list order determines the execution sequence of every type
        of job. You should allays engrave first and cut later. You can
        change the order by selecting a color and pressing the up and
        down arrows.
      - Once you are done with this configuration, press 'OK'.
  - For a raster job:
      - You should see the parts that you want to cut/engrave fitting
        the material in the preview. If not, you should scale, move,
        rotate or change the units of the drawing to get it as you want.
      - Finalize the process with 'Print' and the file will be sent to
        the laser cutter.
  - At the machine:
      - Open the hood and place the material on the metal bed without
        hitting the cutting head.
      - If the material you use is to thick (engraving bigger objects),
        you should lower the bed.
          - To lower the bed:
              - Press 'X/Y off' and bring the bed to the desired z
                position by pressing the 'up' and 'down' arrows.
      - Turn on the laser pointer 'Puntero'.
      - Set the machine head to the origin by pressing 'Restaur.' and
        focus the laser by pressing 'Enfocar' and 'GO/Entra'.
          - If you want to change the x/y origin follow this steps:
              - Press 'X/Y off' and bring the laser manually to the
                desire origin.
              - Then press 'Ajuste Inicio' and you should have now a new
                origin point.
  - If you already sent the job to the machine you will see 'Job:job
    name' in the display.
  - Pressing the up and down arrows will allow you to select the
    different jobs stored in the machine.
  - Press 'GO/Entra' to start cutting/engraving.
  - Press 'STOP/Salir' if something burns inside the machine or the
    material moves from its original position.
  - Don't leave the machine unattended.

![](/assets/images/Epilog_legend_md.png "Epilog_legend_md.png")

## Important commands

Structure:
\*<http://issuu.com/fablabbcn/docs/epilog_quick_start?mode=window&backgroundColor=%23222222/>

## External links

  - [program turun berat badan](https://goo.gl/Kh6ih6)
  - [Epilog Legend Series](http://www.epiloglaser.com/legend_series.htm)
  - [tupperware promo](http://www.buletintupperware.com/)
  - ['Laser cutting' in the
    Wikipedia](http://en.wikipedia.org/wiki/Laser_cutting)

## Maintenance

## Downloads

![](/assets/images/IMG_1600.JPG "IMG_1600.JPG")

## Technical specifications

  - Cutting area 900 x 600 millimeters / 35.4" x 23.6" inches
  - Cutting power max. 75 Watt.
  - Maximum Power Consumption:

## Health & Safety

## CAM

  - **2D** Printer driver from most CAD or ilustration software
  - From PDF

## Tools

  - Tools here

## Materials and configurations

### Suppliers

[For a supplier list take a look at this table maintained by de Fab Lab
BARCELONA](http://fablabbcn.org/maquinas/provedores-materiales/)

### Polypropylene (0.5mm) / Polipropileno

CUT:

  - Speed: 60%
  - Power: 60%

ENGRAVE:

  - Speed: 85%
  - Power: 20%

### Polypropylene (1.2mm) / Polipropileno

CUT:

  - Speed: 15%
  - Power: 90%

ENGRAVE:

  - Speed: 60%
  - Power: 40%

### Polypropylene (0.8mm) / Polipropileno

CUT:

  - Speed: 60%
  - Power: 70%

### Poly(methyl methacrylate)(3mm) / Plexiglass

CUT:

  - Speed: 15%
  - Power: 60%

ENGRAVE:

  - Speed: 65%
  - Power: 10%

### Poly(methyl methacrylate)(1mm) / Plexiglass

CUT:

  - Speed: 60%
  - Power: 70%

ENGRAVE:

  - Speed: 90%
  - Power: 15%

### Poly(methyl methacrylate) (5mm) / Plexiglass

CUT:

  - Speed: 10% / 15%
  - Power: 90% / 80%

ENGRAVE:

  - Speed: 65%
  - Power: 10%

### Etilvinilacetato (3mm) / Foami - Eva

CUT:

  - Speed: 40%
  - Power: 60%

### Paper(250gr/3mm) / Papel

CUT:

  - Speed: 60%
  - Power: 30%

ENGRAVE:

  - Speed: 85%
  - Power: 6%

### Paper (0.3mm) / Papel

CUT:

  - Speed: 50%
  - Power: 50%

ENGRAVE:

  - Speed: 95%
  - Power: 3%

### Paper(shine 1 side) / Papel

CUT:

  - Speed: 60%
  - Power: 25%

ENGRAVE:

  - Speed: 95%
  - Power: 4%

### Parchment Paper(for lamp making) / Papel Pergamino (para hacer lamparas)

CUT:

  - Speed: 85%
  - Power: 10%

### Transparent Paper / Papel transparente

CUT:

  - Speed: 75%
  - Power: 20%

### Cardboard Corrugated (5mm/2 layers) / Carton Corrugado

CUT:

  - Speed: 55%
  - Power: 45%

ENGRAVE:

  - Speed: 90%
  - Power: 10%

### Generic Cardboard / Cartulina común

CUT:

  - Speed: 100%
  - Power: 15%

ENGRAVE:

  - Speed: 100%
  - Power: 4%

### Stone Cardboard (3mm) / Carton Piedra

CUT:

  - Speed: 20%
  - Power: 50%

### Plywood (0.6mm) (Rolling roll)/ Madera (Laminada rollo)

CUT:

  - Speed: 40%
  - Power: 10%

ENGRAVE:

  - Speed: 95%
  - Power: 4%

### Plywood (0.6mm) (Plywood)/ Madera (contrachapado Abedul)

CUT:

  - Speed: 50%
  - Power: 50%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (2mm) / Madera

CUT:

  - Speed: 15%
  - Power: 40%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (3mm) / Madera

CUT:

  - Speed: 15%
  - Power: 45%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### MDF (3mm) / Madera DM

CUT:

  - Speed: 15%
  - Power: 65%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (5mm) / Madera

CUT:

  - Speed: 15%
  - Power: 85%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (0.5mm deep)/ Madera RASTER SOLID

ENGRAVE:

  - Speed: 30%
  - Power: 20%

### Felt (3mm) / Fieltro

CUT:

  - Speed: 60%-70%
  - Power: 110%

### Felt (1mm) / Fieltro

CUT:

  - Speed: 90% (70%)
  - Power: 10%

### Grabar sobre piedra/ Raster Image on stone

ENGRAVE:

  - Speed: 90%
  - Power: 20%

### Thin Fabric

CUT:

  - Speed: 80%
  - Power: 30%

## Machine work flow

  - If you are not going to use the computer in the Fab Lab, [Harga AC
    Murah](http://www.buletinac.com/)install the Epilog drivers in your
    computer (you can reach the machine inside the Fab Lab network).
  - Turn on the main fume extractor in the big laser cutter switch
    panel.
  - Turn on the small air compressor on the left hand side of the
    machine.
  - Turn on the laser cutter (left side of the machine).
  - Make sure the material [Harga Ban Motor
    Corsa](http://www.buletinautomotif.com/) you want to use is in the
    'Materials and configuration' list. If it is not there, ask the Fab
    Lab responsible.
  - Measure the size of your material board.
  - From your vector editing software, once you are ready for printing
    and if you already installed the driver, press Ctrl+P or select
    'Print'.
  - Select 'Epilog Engraver' from the printer list and go to 'Printer
    settings' or 'Properties'.
  - The laser cutter driver interface should appear. Here you can set-up
    the laser's power and speed according to how the vector paths in
    your drawing are organized (you can also print raster images).
    [Harga HP Samsung](http://www.buletinsamsung.com/)
  - For a vector job:
      - In the 'General' tab, under 'Job type' select 'Vector'.
      - Set the size of the material sheet under 'Piece Size'.
      - Set to 'Vector sorting' and 'Optimize'.
      - In the 'Color mapping' tab select the check box 'Color mapping'.
        You should have organized your drawing in different colors if
        you need to do different types of jobs (for example engraving
        and cutting).
      - Once this is activated, you can set the power, the speed, and
        other parameters for every single color in your drawing. Take a
        look at the 'Materials and configuration' list above for the
        proper power/speed values according to the material you are
        using.
      - The list order determines the execution sequence of every type
        of job. You should allays engrave first and cut later. You can
        change the order by selecting a color and pressing the up and
        down arrows.
      - Once you are done with this configuration, press 'OK'.
  - For a raster job:
      - You should see the parts that you want to cut/engrave fitting
        the material in the preview. If not, you should scale, move,
        rotate or change the units of the drawing to get it as you want.
      - Finalize the process with 'Print' and the file will be sent to
        the laser cutter.
  - At the machine:
      - Open the hood and place the material on the metal bed without
        hitting the cutting head.
      - If the material you use is to thick (engraving bigger objects),
        you should lower the bed.
          - To lower the bed:
              - Press 'X/Y off' and bring the bed to the desired z
                position by pressing the 'up' and 'down' arrows.
      - Turn on the laser pointer 'Puntero'.
      - Set the machine head to the origin by pressing 'Restaur.' and
        focus the laser by pressing 'Enfocar' and 'GO/Entra'.
          - If you want to change the x/y origin follow this steps:
              - Press 'X/Y off' and bring the laser manually to the
                desire origin.
              - Then press 'Ajuste Inicio' and you should have now a new
                origin point.
  - If you already sent the job to the machine you will see 'Job:job
    name' in the display.
  - Pressing the up and down arrows will allow you to select the
    different jobs stored in the machine.
  - Press 'GO/Entra' to start cutting/engraving.
  - Press 'STOP/Salir' if something burns inside the machine or the
    material moves from its original position.
  - Don't leave the machine unattended.

![](/assets/images/Epilog_legend_md.png "Epilog_legend_md.png")

## Important commands

Structure:
\*<http://issuu.com/fablabbcn/docs/epilog_quick_start?mode=window&backgroundColor=%23222222/>

## External links

  - [program turun berat badan](https://goo.gl/Kh6ih6)
  - [Epilog Legend Series](http://www.epiloglaser.com/legend_series.htm)
  - [tupperware promo](http://www.buletintupperware.com/)
  - ['Laser cutting' in the
    Wikipedia](http://en.wikipedia.org/wiki/Laser_cutting)

## Maintenance

## Downloads

![](/assets/images/IMG_1600.JPG "IMG_1600.JPG")

## Technical specifications

  - Cutting area 900 x 600 millimeters / 35.4" x 23.6" inches
  - Cutting power max. 75 Watt.
  - Maximum Power Consumption:

## Health & Safety

## CAM

  - **2D** Printer driver from most CAD or ilustration software
  - From PDF

## Tools

  - Tools here

## Materials and configurations

### Suppliers

[For a supplier list take a look at this table maintained by de Fab Lab
BARCELONA](http://fablabbcn.org/maquinas/provedores-materiales/)

### Polypropylene (0.5mm) / Polipropileno

CUT:

  - Speed: 60%
  - Power: 60%

ENGRAVE:

  - Speed: 85%
  - Power: 20%

### Polypropylene (1.2mm) / Polipropileno

CUT:

  - Speed: 15%
  - Power: 90%

ENGRAVE:

  - Speed: 60%
  - Power: 40%

### Polypropylene (0.8mm) / Polipropileno

CUT:

  - Speed: 60%
  - Power: 70%

### Poly(methyl methacrylate)(3mm) / Plexiglass

CUT:

  - Speed: 15%
  - Power: 60%

ENGRAVE:

  - Speed: 65%
  - Power: 10%

### Poly(methyl methacrylate)(1mm) / Plexiglass

CUT:

  - Speed: 60%
  - Power: 70%

ENGRAVE:

  - Speed: 90%
  - Power: 15%

### Poly(methyl methacrylate) (5mm) / Plexiglass

CUT:

  - Speed: 10% / 15%
  - Power: 90% / 80%

ENGRAVE:

  - Speed: 65%
  - Power: 10%

### Etilvinilacetato (3mm) / Foami - Eva

CUT:

  - Speed: 40%
  - Power: 60%

### Paper(250gr/3mm) / Papel

CUT:

  - Speed: 60%
  - Power: 30%

ENGRAVE:

  - Speed: 85%
  - Power: 6%

### Paper (0.3mm) / Papel

CUT:

  - Speed: 50%
  - Power: 50%

ENGRAVE:

  - Speed: 95%
  - Power: 3%

### Paper(shine 1 side) / Papel

CUT:

  - Speed: 60%
  - Power: 25%

ENGRAVE:

  - Speed: 95%
  - Power: 4%

### Parchment Paper(for lamp making) / Papel Pergamino (para hacer lamparas)

CUT:

  - Speed: 85%
  - Power: 10%

### Transparent Paper / Papel transparente

CUT:

  - Speed: 75%
  - Power: 20%

### Cardboard Corrugated (5mm/2 layers) / Carton Corrugado

CUT:

  - Speed: 55%
  - Power: 45%

ENGRAVE:

  - Speed: 90%
  - Power: 10%

### Generic Cardboard / Cartulina común

CUT:

  - Speed: 100%
  - Power: 15%

ENGRAVE:

  - Speed: 100%
  - Power: 4%

### Stone Cardboard (3mm) / Carton Piedra

CUT:

  - Speed: 20%
  - Power: 50%

### Plywood (0.6mm) (Rolling roll)/ Madera (Laminada rollo)

CUT:

  - Speed: 40%
  - Power: 10%

ENGRAVE:

  - Speed: 95%
  - Power: 4%

### Plywood (0.6mm) (Plywood)/ Madera (contrachapado Abedul)

CUT:

  - Speed: 50%
  - Power: 50%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (2mm) / Madera

CUT:

  - Speed: 15%
  - Power: 40%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (3mm) / Madera

CUT:

  - Speed: 15%
  - Power: 45%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### MDF (3mm) / Madera DM

CUT:

  - Speed: 15%
  - Power: 65%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (5mm) / Madera

CUT:

  - Speed: 15%
  - Power: 85%

ENGRAVE:

  - Speed: 40%
  - Power: 10%

### Plywood (0.5mm deep)/ Madera RASTER SOLID

ENGRAVE:

  - Speed: 30%
  - Power: 20%

### Felt (3mm) / Fieltro

CUT:

  - Speed: 60%-70%
  - Power: 110%

### Felt (1mm) / Fieltro

CUT:

  - Speed: 90% (70%)
  - Power: 10%

### Grabar sobre piedra/ Raster Image on stone

ENGRAVE:

  - Speed: 90%
  - Power: 20%

### Thin Fabric

CUT:

  - Speed: 80%
  - Power: 30%

## Machine work flow

  - If you are not going to use the computer in the Fab Lab, [Harga AC
    Murah](http://www.buletinac.com/)install the Epilog drivers in your
    computer (you can reach the machine inside the Fab Lab network).
  - Turn on the main fume extractor in the big laser cutter switch
    panel.
  - Turn on the small air compressor on the left hand side of the
    machine.
  - Turn on the laser cutter (left side of the machine).
  - Make sure the material [Harga Ban Motor
    Corsa](http://www.buletinautomotif.com/) you want to use is in the
    'Materials and configuration' list. If it is not there, ask the Fab
    Lab responsible.
  - Measure the size of your material board.
  - From your vector editing software, once you are ready for printing
    and if you already installed the driver, press Ctrl+P or select
    'Print'.
  - Select 'Epilog Engraver' from the printer list and go to 'Printer
    settings' or 'Properties'.
  - The laser cutter driver interface should appear. Here you can set-up
    the laser's power and speed according to how the vector paths in
    your drawing are organized (you can also print raster images).
    [Harga HP Samsung](http://www.buletinsamsung.com/)
  - For a vector job:
      - In the 'General' tab, under 'Job type' select 'Vector'.
      - Set the size of the material sheet under 'Piece Size'.
      - Set to 'Vector sorting' and 'Optimize'.
      - In the 'Color mapping' tab select the check box 'Color mapping'.
        You should have organized your drawing in different colors if
        you need to do different types of jobs (for example engraving
        and cutting).
      - Once this is activated, you can set the power, the speed, and
        other parameters for every single color in your drawing. Take a
        look at the 'Materials and configuration' list above for the
        proper power/speed values according to the material you are
        using.
      - The list order determines the execution sequence of every type
        of job. You should allays engrave first and cut later. You can
        change the order by selecting a color and pressing the up and
        down arrows.
      - Once you are done with this configuration, press 'OK'.
  - For a raster job:
      - You should see the parts that you want to cut/engrave fitting
        the material in the preview. If not, you should scale, move,
        rotate or change the units of the drawing to get it as you want.
      - Finalize the process with 'Print' and the file will be sent to
        the laser cutter.
  - At the machine:
      - Open the hood and place the material on the metal bed without
        hitting the cutting head.
      - If the material you use is to thick (engraving bigger objects),
        you should lower the bed.
          - To lower the bed:
              - Press 'X/Y off' and bring the bed to the desired z
                position by pressing the 'up' and 'down' arrows.
      - Turn on the laser pointer 'Puntero'.
      - Set the machine head to the origin by pressing 'Restaur.' and
        focus the laser by pressing 'Enfocar' and 'GO/Entra'.
          - If you want to change the x/y origin follow this steps:
              - Press 'X/Y off' and bring the laser manually to the
                desire origin.
              - Then press 'Ajuste Inicio' and you should have now a new
                origin point.
  - If you already sent the job to the machine you will see 'Job:job
    name' in the display.
  - Pressing the up and down arrows will allow you to select the
    different jobs stored in the machine.
  - Press 'GO/Entra' to start cutting/engraving.
  - Press 'STOP/Salir' if something burns inside the machine or the
    material moves from its original position.
  - Don't leave the machine unattended.

![](/assets/images/Epilog_legend_md.png "Epilog_legend_md.png")

## Important commands

Structure:
\*<http://issuu.com/fablabbcn/docs/epilog_quick_start?mode=window&backgroundColor=%23222222/>

## External links

  - [Epilog Legend Series](http://www.epiloglaser.com/legend_series.htm)
  - ['Laser cutting' in the
    Wikipedia](http://en.wikipedia.org/wiki/Laser_cutting)

## Maintenance

## Downloads

  - [User
    Manual](https://www.epiloglaser.com/downloads/pdf/ext_4.22.10.pdf)

[Category:Machines](Category:Machines "wikilink") [Category:
Machines](Category:_Machines "wikilink")
[Category:Machines](Category:Machines "wikilink") [Category:
Machines](Category:_Machines "wikilink")
[Category:Machines](Category:Machines "wikilink") [Category:
Machines](Category:_Machines "wikilink")