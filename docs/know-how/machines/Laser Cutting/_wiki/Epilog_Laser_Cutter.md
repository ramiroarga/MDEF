![](/assets/images/IMG_1600.JPG "IMG_1600.JPG")

## Technical specifications

  - Cutting area 900 x 600 millimeters / 35.4" x 23.6" inches
  - Cutting power max. 50 Watt.
  - Maximum Power Consumption:

## Health & Safety

![](/assets/images/0-plan_p59_laser_cutting_area.jpg
"0-plan_p59_laser_cutting_area.jpg")

### 1\. PRECAUTIONS

![](/assets/images/2-_steps_valves_air_pressure.jpg
"2-_steps_valves_air_pressure.jpg")

| Step | Description                                                                                                                                                                           |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      |                                                                                                                                                                                       |
| 1\.  | If you are not going to use the computer in the Fab Lab, install the Epilog drivers in your computer (you can reach the machine inside the Fab Lab network).                          |
| 2\.  | Turn on the main fume extractor in the big laser cutter switch panel.                                                                                                                 |
| 3\.  | Check that the general compressor of the building is ON.                                                                                                                              |
| 4\.  | Turn ON the laser cutter (left side of the machine).                                                                                                                                  |
| 5\.  | Turn ON the red valve on the left in order to open the general air assistance. (Remember that to open the valve just positioned the RED key aligned along the flow of the air).       |
| 6\.  | Just turn ON the air assistance on the specific machine: Epilog 50w or Epilog 75w.                                                                                                    |
| 7\.  | Turn ON the pc desktop and the monitor of the Lab connected to the laser machine.                                                                                                     |
| 8\.  | Make sure the material you want to use is in the 'Materials and configuration' list. If it is not there, ask the Fab Lab responsible.                                                 |
| 9\.  | Measure the size of your material board. If it doesn’t fit into the board of the laser machine ask the Fab Lab responsible for cutting the correct format.                            |
| 10\. | Please remove all your leftovers pieces after using the machines and remember to **close the valve at the end of your works**. Keep this small area clean and free for others to use. |
| 11\. | The building is already provided by different air outlets.                                                                                                                            |
|      |                                                                                                                                                                                       |

### 2\. FILE SETTINGS

| Step | Description                                                                                                                                                                                          |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      |                                                                                                                                                                                                      |
| 1\.  | Open dxf, 3dm, or compatible file with Rhino.                                                                                                                                                        |
| 2\.  | Select the curves and hatches and put them in separate layers.                                                                                                                                       |
| 3\.  | Choose the correct colour for every operation (Cutting, Engraving, Raster E.).                                                                                                                       |
| 4\.  | Select all objects and make sure that they are displayed by layer on properties.                                                                                                                     |
| 5\.  | From your vector editing software, once you are ready for printing and if you already installed the driver, press Ctrl+P or select ‘Print’.                                                          |
| 6\.  | Select ‘Epilog Engraver 50’ from the printer list and go to ‘Printer settings’ or ‘Properties’.                                                                                                      |
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

## Caution

  - this remark should go on all pages for lasers:

The honeycomb structure of the bed of the machine is very expensive and
it easily gets damaged. The quality of the cuts is only going to be good
if the bed is perfectly flat and undamaged. Take good care of the
honeycomb

## Materials and configurations

### Settings

| Material                                               | Cut       | Engraving | <u>Raster</u> Engraving - 600 DPI |
| ------------------------------------------------------ | --------- | --------- | --------------------------------- |
|                                                        | Speed (%) | Power (%) | Frequency (Hz)                    |
| Polypropylene - White - 0.5mm                          | 55        | 50        | 5000                              |
| Polypropylene - Transparent - 0.8mm                    | 35        | 60        | 5000                              |
| Polypropylene - Black 1.2mm                            | 30        | 80        | 5000                              |
| Acrylic - White - 2mm                                  | 25        | 90        | 5000                              |
| Acrylic - White - 3mm                                  | 15        | 88        | 5000                              |
| Acrylic - Transparent - 2mm                            | 25        | 90        | 5000                              |
| Acrylic - Transparent - 3mm                            | 15        | 90        | 5000                              |
| Acrylic - Transparent - 4mm                            | 10        | 95        | 5000                              |
| Acrylic - Transparent - 5mm                            | 10        | 100       | 5000                              |
| Acrylic - Transparent/Matt - 3mm                       | 15        | 90        | 5000                              |
| Acrylic - Transparent/Matt - 6mm                       | 5         | 100       | 5000                              |
| Acrylic - Black/Semi-Transparent - 3mm                 | 15        | 90        | 5000                              |
| EVA Foam (Ethylene-Vinyl Acetate) - Black - 10mm       | 20        | 100       | 1000                              |
| EVA Foam (Ethylene-Vinyl Acetate) - Yellow - 11mm      | 15        | 100       | 1000                              |
| Polyurethane Foam - 10mm                               | 65        | 60        | 500                               |
| Foam with textile - 3mm                                | 60        | 55        | 250                               |
| Felt - Black (5mm) / Fieltro                           | 55        | 55        | 250                               |
| Lycra - White - 0.3mm                                  | 70        | 30        | 500                               |
| Wood - Plywood (4mm) / Madera                          | 20        | 95        | 300                               |
| Wood - Plywood (5mm) / Madera                          | 15        | 90        | 2500                              |
| Wood - MDF (3mm)                                       | 15        | 90        | 500                               |
| Wood - MDF (4mm)                                       | 15        | 100       | 500                               |
| Wood - MDF (5mm)                                       | 8         | 100       | 30                                |
| Wood - Veneer (0.7mm)                                  | 85        | 55        | 500                               |
| Paper - black - 0.4mm                                  | 90        | 35        | 500                               |
| Paper - White - 0.6mm                                  | 80        | 35        | 500                               |
| Paper - Black finish - 1.3mm                           | 70        | 50        | 500                               |
| Paper - Grey - 1.5mm                                   | 55        | 75        | 500                               |
| Paper - White - 1.5mm                                  | 55        | 75        | 500                               |
| Cardboard - Corrugated (4mm/1 layers)                  | 40        | 45        | 500                               |
| Cardboard - Corrugated (5mm/2 layers)                  | 30        | 70        | 500                               |
| Cardboard - Corrugated high res. - white (6mm/1 layer) | 2x 20     | 90        | 500                               |
| Silicone - (less than 0.5 mm)                          | 100       | 80        | 1000                              |

Laser settings for common materials - Epilog 50W

**Note:** Settings above are a good starting point. Laser cutting
quality is affected by several factors including lens cleanliness,
maintenance and/or aging laser tube. If you are not achieveing a cut,
try to increase the power, decrease the speed or a do combination of
both. Change settings with 5-10% step at a time.

### Suppliers

[For a supplier list take a look at this table maintained by de Fab Lab
BARCELONA](http://fablabbcn.org/maquinas/provedores-materiales/)

## Machine work flow

  - If you are not going to use the computer in the Fab Lab, install the
    Epilog drivers in your computer (you can reach the machine inside
    the Fab Lab network).
  - Turn on the main fume extractor in the big laser cutter switch
    panel.
  - Turn on the small air compressor on the left hand side of the
    machine.
  - Turn on the laser cutter (left side of the machine).
  - Make sure the material you want to use is in the 'Materials and
    configuration' list. If it is not there, ask the Fab Lab
    responsible.
  - Measure the size of your material board.
  - From your vector editing software, once you are ready for printing
    and if you already installed the driver, press Ctrl+P or select
    'Print'.
  - Select 'Epilog Engraver' from the printer list and go to 'Printer
    settings' or 'Properties'.
  - The laser cutter driver interface should appear. Here you can set-up
    the laser's power and speed according to how the vector paths in
    your drawing are organized (you can also print raster images).
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