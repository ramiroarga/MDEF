Work in progress

## Technical Specifications

  - Clamping Area X / Y on grooved panel: 1860 x 1340 mm
  - Length x width x height over all :2180x1800x1420mm
  - Length x width x height of platform :1500x1200x30mm

## Health & Safety

  - Ensure you have been trained in the use of the CNC machine
  - Inspect the equipment to ensure no obvious defects: damaged chuck,
    dull or cracked tools, damaged shields
  - Use appropriate personal protective equipment (PPE)
      - Safety glasses
      - Hearing protection
      - Non-slip shoes
  - Remove rings, bracelets, watches, necklaces before work
  - Tie back and confine long hair
  - Wear tight-fitting clothing and/or roll up sleeves to prevent
    snagging

## CAM

  - **2D and 3D** - RhinoCAM

After creating your milling strategy in RhinoCAM, it has to be
transformed into a format that is readable by the TRex control system.
The piece of software performing this task is called a postprocessor. Be
sure to select the correct postprocessor ("CNC_STEP_BCN") as well as
the expected file extension (.nc) in RhinoCAM when exporting the file
for CNC.

## MCS

  - KinetiC-NC

## Selecting the Right Bit for the Job

**Milling Tools:** A milling bit (also called milling cutter or end
mill) is a tool used in CNC or hand-operated milling machines to remove
material in a controlled manner to obtain the desired shape. This is
usually done by moving the rotating tool sideways (lateral direction)
through the material, thus cutting chips off the workpiece. Most milling
bits can also cut in the direction of the tool axis, like a drilling
bit. Vice-versa, however, a drilling bit is designed to cut only axially
to create cylindrical holes, and cannot be used for milling.

**Bit material:** Router bits are made from a variety of materials. The
most common are solid carbide, carbide-tipped steel, and high-speed
steel. Both solid carbide and carbide- tipped are good choices. We do
not recommend using high-speed steel bits as they dull quickly and must
be re-sharpened.

**Flute type:** There are four basic flute types: Straight, spiral
up-cut, spiral down-cut, and compression. Each type has its own
advantages and disadvantages, which are outlined in the chart below.

![](/assets/images/Schermata_2017-01-13_alle_17.01.41.png
"Schermata_2017-01-13_alle_17.01.41.png")

## Parameters: Feeds and Speeds

A challenge of getting a good CNC cut is in selecting the best bit, best
cutting speed (feed rate) and router/spindle RPM (speed of rotation).
Bits,feeds, and speeds are a critical part of machining and should be
fully understood before deviating from recommended settings. Bits choice
is important in chip load, which is a representation of the size of the
chips produced during cutting. The goal is to get the maximum chip load
possible to increase productivity, reduce heat, and prevent premature
dulling. When chip load is too small, bits will get too hot and dull
quicker. When chip load is too high, the tool will deflect creating a
bad surface finish and, in extreme cases, chip or break the bit.

Optimising feed rates and speeds: =1. Start off using an RPM derived for
the chip load for the material being cut (see charts). 2. Increase the
cutting speed (feed rate) until the quality of the part’s finish starts
to decrease or the part is starting to move from hold downs. Then
decrease speed by 10%. 3. Decrease RPM until finish deteriorates, then
bring RPM back up until finish is acceptable. 4. This optimises RPM and
speed to remove the largest possible chips.

**Feeds and Speed:**

  - PLYWOOD

Flat 6mm, 1 flute

RPM: 13000

Plunge: 1000 mm/min

Travelling clearance plane: 4000 mm/min

Rest of the parameters:2000 mm/min

Step down: 4mm max (always depending on the diameter of the tool)

  - FOAM

Flat 6mm, 1 flute

RPM: 12000

Plunge: 2000 mm/min

Travelling clearance plane: 4000 mm/min

Rest of the parameters:3500 mm/min

Step down: 20mm max (always depending on the diameter of the tool)

  - CHIPBOARD

Flat 6mm, 1 flute

RPM: 12500

Plunge: 1000 mm/min

Travelling clearance plane: 4000 mm/min

Rest of the parameters:2000 mm/min

Step down: 4mm max (always depending on the diameter of the tool)

Parameters are given by ShopBot

![](/assets/images/Schermata_2017-01-13_alle_16.45.07.png
"Schermata_2017-01-13_alle_16.45.07.png")

![](/assets/images/Schermata_2017-01-13_alle_16.51.02.png
"Schermata_2017-01-13_alle_16.51.02.png")

![](/assets/images/Schermata_2017-01-13_alle_16.53.13.png
"Schermata_2017-01-13_alle_16.53.13.png")

![](/assets/images/Schermata_2017-01-13_alle_16.54.38.png
"Schermata_2017-01-13_alle_16.54.38.png")

![](/assets/images/Schermata_2017-01-13_alle_16.55.34.png
"Schermata_2017-01-13_alle_16.55.34.png")

![](/assets/images/Schermata_2017-01-13_alle_16.56.29.png
"Schermata_2017-01-13_alle_16.56.29.png")

## Use of TRex S-1215

#### Safety Precautions

\-Always wear safety glasses when operating the TRex or observing the
machine when it is in use.

\-Never leave the machine when it is in operation.

\-If you need a bathroom break, the machine can be paused by clicking on
the stop button found when on the program tab of the control
software-KinetiC-NC.

\-Make sure the bed of the machine is clean before use. Inform the
fabrication team if it is not clean.

\-Securely fasten your material to the bed of the machine. Consult us
every time you are faced with a different, challenging or unusual
work-holding scenario.

\-Perform '"Homing routine to establish the true machine home X-0 Y-0
(in the machine coordinates system)

\-Jog X, Y to your personal Work Home coordinates, i.e: the corner of
your material & the X, Y origin of your drawing.

\-Take a photo of the Control PC screen or take note of the machine
[Mesin Cuci Toshiba 1
Tabung](http://www.mesincuci.co/harga-mesin-cuci-toshiba-1-tabung-2017)
coordinates system to your chosen Work Home position. Example: X -
105.499, Y - 145.376 (do not worry about Z yet). Work Home X Y
coordinates are simply offset measurements from the true Home (X-0, Y-0)
of the Machine.

\-Zero work coordinates to X-0 Y-0

\-Install tool in collet/tool holder + install tool/tool holder on the
spindle.

\-Load/Open the NC file, to choose the file you need to launch, you will
see your “G-Code” which you generated in RhinoCam on the screen.

\-Visually check again the machine bed to ensure all tools have been
removed and that material is securely fastened to the bed.

\-Start in KinetiC-NC software, follow prompts.

\-Monitor the machine closely until the machine stops. Laser Cutters and
CNC Routers have a high risk of fire if left unattended.

\-If you need to pause the machine, click the Stop button on the
KinetiC-NC Software. The machine will pause, then continue the work by
clicking on the Play button

\-Emergency stop (E-stop) buttons are located in 2 places: On your
remote, next to the Control PC, and On the end of the Y-Axis gantry. The
Emergency Stop buttons are large, round Red buttons which will
completely shut-down the machine.

\-Remove the tool-holder & tool from the spindle and store it in the
tool-holder rack.

\-Clean the machine and your work area completely after you have removed
your material.

\-Skeletons and scraps created during the process should be cut up &
placed in the recycling cart.

### Interface

![](/assets/images/KinectiC-NC_startup_screen.jpeg
"KinectiC-NC_startup_screen.jpeg")

The image below shows the interface of KinetiC-NC software.

The tabs available in the software are:

#### A. Program

This tab lets you perform the following:

1\. Load the G-Code generated from your RhinoCam.

2\. View and manage the feed rate of the machine while it is running.

3\. View the current coordinates of the machine.

4\. Start and Stop the GCode.

5\. View the tool path on the display window. By default the colour of
the toolpath before running in green. As the file starts and passes the
toolpath the colour changes to light blue which keeps you the track of
the progress of the file.

#### B. Jog Setup

Here you can set the zero of the stock before you start your milling
work.Its really important that you fix your tool well before you set the
zero. You can use the two wrenches of 22mm to fix the milling bit to the
tool head.

![](/assets/images/Setup_screen_Kinetic-nc.JPG
"Setup_screen_Kinetic-nc.JPG")

##### Set X,Y,Z zero

Setting the X,Y and Z is done by eye in the Trex 1215 CNC Machine. To
set the zero please follow these instructions:

1\. To set the X and Y we move the machine towards the zero set in the
stock in RhinoCam.

2\. While setting this, we make sure we place the tool in a way that
half the tool is inside the material and half outside the material. This
makes sure that the center of the tool is at the zero of the stock.

3\. To set the Z we move the bit down slowly in steps until the barely
touches the stock and also we move the tool and make sure it doesn't
drag through the stock leaving a mark. We can use the paper technique by
placing a piece of paper below the bit to set the z.

## External Links

  - [ShopBot wiki](http://shopbotwiki.com/)
  - [Makezine Article on end
    mills](https://makezine.com/2014/09/10/endmills/)

## Rhinocam tutorials

  - <https://mecsoft.com/QuickStartGuides/RhinoCAM2018/MILLQuickStartGuide.pdf>
  - <https://www.youtube.com/watch?v=vrNDFlFOOtE&list=PLx9G05pFm0QKRJoklNlKfvcE1zfFIRXqF&index=1>

## Maintenance

## Downloads

Below here you can find the Post-processor for CNC Trex-1215 and the
library of milling bits

![](/assets/images/Post_processor_&_Milling_bits_library_CNC_Trex_1215.zip
"File:Post_processor_&_Milling_bits_library_CNC_Trex_1215.zip")

[Category:Machines](Category:Machines "wikilink")