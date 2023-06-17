---
hide:
    - toc
---

# Digital Prototyping for Design

Here I will be showing some notes, outcomes and reflections of the process of the seminar!

*Basic E&C*

During this task, we acquired knowledge on how to trigger a buzzer in order to generate sound. It proved to be a captivating exercise that further deepened our comprehension of the fundamental principles behind electronics and Arduino programming.

This first class was a general reminder on arduino system, parallel systems and general terms of electronic prototyping. I feel motivated about this seminar, i like playing and learning electronics! We played on making some buzzers melodies to sound with some open-source codes!

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/795018353?h=b476ddf82d&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="IMG_9894.MOV"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*Design Tools*	

In the subsequent task, our objective was twofold: to establish the parameters for a croissant and to generate a 3D design employing algorithmic thinking applied to any object or concept. I hand-sketched a croissant with different sections that were traslated through 2 lines in the space, till the middle and then created the final form by simmetry.

![](../images/croissant.png)

*2D Fabrication*	

For this activity, our assignment entailed developing a parametric model and subsequently fabricating it using the laser cut machine. I decided to use the resources and time to make some laser cuts for the making of a lipid-trap I needed to built for the master project. So I designed the trap (acrylic box) in order to be transparent and could see how the water flowed and lipids and solids were divided by densities. And I laser cutted it and then glue it, the results were so good! Also I didnt choose to make something else for the activity because I have already experience in design and prototypes by laser cutting, so i decided to make something with more sense for the project. Here some images!

![](../images/laser.jpg)
![](../images/lipidd%20built.JPG)


*Inputs / Outpus*

Our assigned task involved designing an Arduino-based system that incorporates an LDR sensor, a button, and an LED to generate a telegram through a combination of inputs and outputs. In this system, pressing the button activates the LED, and releasing it deactivates the LED. Additionally, the LDR sensor detects ambient light. While the initial suggestion was to collaborate in pairs using separate boards, for the sake of efficiency, I opted to design the entire system using a single board and complete the assignment independently.

By leveraging the readings from the LDR sensor, the system aims to distinguish between brief and prolonged exposure to light, representing them as dot (.) or dash (-) signals in Morse code, respectively. To achieve this, I programmed variables corresponding to each letter in Morse code and managed to identify a few letters successfully. However, I encountered a challenge when attempting to concatenate the sensor data to identify all the letters accurately. Thus far, I have only been able to recognize letters E and T, which consist solely of a dot (.) and a dash (-), respectively. Here some videos of the experience.


<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/798407899?h=8e50bbaf11&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="IMG_9959.MOV"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


*Networking*

In this intriguing challenge, our objective entailed establishing a connection between our Feathers and a Wi-Fi network utilizing an MQTT broker and NodeRed. However, an unfortunate oversight on my part led to a lack of documentation during the class session. Moreover, due to the unique MQTT credentials and the utilization of the SmartCitizen broker, I faced challenges in replicating the exercise independently. Nevertheless, I can provide the code file and a selection of Arduino IDE screenshots to shed some light on the process.

Essentially, we successfully set up a sophisticated communication network that facilitated seamless message exchange between devices. This system not only served as a valuable learning experience but also contributed significantly to enhancing the resilience and functionality of our second prototype—the HRV sculpture—which ingeniously harnessed the power of Wi-Fi connectivity.

Although the exercise appeared deceptively simple, its impact proved to be far-reaching, reinforcing the robustness and efficacy of our project. Despite the limitations encountered, the experience garnered from this endeavor was undeniably invaluable. 


*3d softwares*

We reviewed 2d and 3d softwares and made a MIRO board with all the softwares we know how to use. Then we learned about colors, pixels and vectors, PPI/DPI (72PPI normal for monitors and the internet) and image formats (GIF,JPEG,PNG).

Also learned about (TOPoPT) Topology optimization / generative design, mathematical method that optimizes material layout within a given design space. Generative design is not about designing, its about designing the system, we start from nothing, not the other way around.

For the class challenge, I imagined a filtering water system for domestic use, draw a quick sketch and made a 3d model in Rhino, rendered in Vred and finished in Photoshop. Here some images of the process.

![](../images/sketch.jpg)
![](../images/Captura%20de%20pantalla%20(31).png)
![](../images/Captura%20de%20pantalla%20(33).png)


*3d Printing*

In this class we understood how bidimensional fabrication works and its types. We went through laser systems, laser source and focus. Learned specially the lasercut, its functions, how it works and results of it. Also we understood materials that should and not be used in laser cutting.
Best for cutting: cardboard, plywood, mdf, acrylic /polypropylene

Some 3d printing and scanning tasks...

I wanted to print a volcano ashtray as an example for testing the printer and parameters in order to know how it works better for future printings. Here I can show some of the process, the 3d design modelling, print and scanning.


![](../images/IMG_0113.jpg)
![](../images/IMG_0141.jpg)
<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/817798362?h=00a09698c6&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="scan 3d print.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


*Interfaces-Machines Interactions*

Some playing with leds controlling them online!

<div style="padding:177.78% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/806905226?h=74fbd423b9&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="IMG_0068 (Copy)"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


*CNC Manufacturing*

For the CNC task, I 3d modelled a cabinet we had thinked for placing the different water filters we have. The system was thinked and modelled for CNC cutting in 15mm plywood. Then adjust some final settings with the help of Mikel and Adai in RhinoCAM, cutted it and then assembled it!

![](../images/cnc.jpeg)

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/817801542?h=64f045d64e&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="cnc on.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

![](../images/cnc2.jpeg)

