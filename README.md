# FusionAnimator

## Purpose
If you have ever wanted to make more stylish animations for your objects in your Clickteam Fusion 2.5+ applications then this tool will be of use to you.
Using Blender version 2.79 and above, FusionAnimator + its bundled python script(s) can put animation data right into your games easily.

The included python scripts create json data of a selected Blender object that can be used to transform objects in Clickteam Fusion using the provided FusionAnimated Object.

## How to Setup
1. Own Clickteam Fusion 2.5+
2. Download the required extensions:
   - JSON Object
   - File
   - File Read / Write
If you are missing these extensions then search them by name in the extension manager (**View** > **Extension Manager**)
3. Copy the bundle of objects from the example .mfa file (FusionAnimated Object, JSON Object, File, File Read / Write) to your desired application.
4. _Done!_

Your group of objects should look like this:

![Bundle](https://github.com/Mechlus/FusionAnimator/assets/82886093/4ff8e4ee-f5ed-4a5e-a1cf-c785fcec7926)

## Use
To use FusionAnimator:
1. **Create a FusionAnimated object** in your frame once its contents and required objects are in the same frame.
    - The FusionAnimated Object active is **not** created by default.  
2. **Set the .json file path** in its jsonPath alterable String field.
3. **Set ease speed, animation speed, on-end event and position multiplier**.
    - The on-end event string fires a timer event immediately when the animation is over (and it is not looping) with the name entered in said alterable string.
    - If you would like to reference specific FusionAnimated Objects then you can enter a unique ID in the alterable value **myID** and/or the alterable string **strID**.
    - Certain animation properties, like making an animation loop, are in the animation's .json.
4. _Done!_
_It's best to not modify the FusionAnimated Object active unless you know what you're doing!_

![Example](https://github.com/Mechlus/FusionAnimator/assets/82886093/434ca123-96a6-4deb-afcf-c6ce75be4f6a)


**NOTE**: If you want to reuse the same object but you want to change the animation, simply set the **perform** flag to **FALSE** (0) and repeat steps 2 & 3. If perform is not turned off then the object may run into issues!

There is a simple use case in the .mfa file provided in the repository that the object is stored in. You can ignore that as all of the necessary code is in the **behavior of the FusionAnimated Object active**.
