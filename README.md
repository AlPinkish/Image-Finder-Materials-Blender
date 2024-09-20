![image](https://github.com/user-attachments/assets/26364713-9e28-4ebe-a372-d04dd9a667d5)


# Image-Finder-Materials-Blender


## Introduction
While Blender provides native tools for file cleanup, this addon makes it more convenient to manage images directly from the Outliner. With just a right-click, you can easily find images used in materials or delete unused images. It's a one-stop solution for lazy users who want to streamline their workflow without jumping through multiple menus.

![image](https://github.com/user-attachments/assets/d5e04606-c19e-434f-b077-3b7c25d33b68)


## Description
This addon for Blender allows you to:
**Find a selected image in all materials' textures**.

  ![image](https://github.com/user-attachments/assets/53199b88-1685-4002-a78a-6ff171c9d7ee)
  
  ![image](https://github.com/user-attachments/assets/13e72faf-4ae5-414c-b16a-b9d4d5807f25)
  
  ![image](https://github.com/user-attachments/assets/cf5054ae-c17e-44a4-a1ae-f667651667d8)
 

**Delete a selected image if it is not associated with any materials**.

![image](https://github.com/user-attachments/assets/ce6fea96-d2ac-41e4-9fbb-33028a36161a)

![image](https://github.com/user-attachments/assets/6b8a240c-805c-40f3-a9f1-0909d6a1237c)


**Delete all unused images** in a single action.

![image](https://github.com/user-attachments/assets/d8934240-571e-4ec8-b20b-dc7871230fa6)

It simplifies the process of managing images directly within the Outliner, making it more accessible from one convenient menu.

## Installation
1. Download the `image_finder.py` file.
2. Open Blender.
3. Go to `Edit` > `Preferences` > `Add-ons`.
4. Click on `Install...` and select the downloaded Python file.
5. Enable the addon by checking the box next to its name.

## Usage
- Open the Outliner and navigate to `Blender File` > `Images`.
- Right-click on the image you want to check or manage.
- You will see the following options in the context menu:
  - **Find Image in Materials**: A notification will appear at the bottom of the screen indicating whether the image is used in any materials.
  - **Delete Image if Unused**: If the image is not used in any materials, it will be deleted, and a confirmation message will be displayed.
  - **Delete All Unused Images**: This option will delete all images not associated with any materials and notify you of the deletions. All deleted images will be listed in the info panel.

## Author
This addon was created by [Alvaro Rosati](https://sites.google.com/view/alvaro-rosati/home-page?authuser=0)

[Support with Paypal](https://www.paypal.com/paypalme/alvarorosati)

[Support with Gumroad](https://alvarobot.gumroad.com/l/imagefinderforblender)
## License
This addon is released under the GPL-3.0-or-later License. See `LICENSE` for more information.
