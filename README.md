# Image-Finder-Materials-Blender

## Introduction
While Blender provides native tools for file cleanup, this addon makes it more convenient to manage images directly from the Outliner. With just a right-click, you can easily find images used in materials or delete unused images. It's a one-stop solution for lazy users who want to streamline their workflow without jumping through multiple menus.

## Description
This addon for Blender allows you to:
1. **Find a selected image in all materials' textures**.
2. **Delete a selected image if it is not associated with any materials**.
3. **Delete all unused images** in a single action.

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

Support My Project: [Donate with Paypal](https://www.paypal.com/paypalme/alvarorosati)

## License
This addon is released under the GPL-3.0-or-later License. See `LICENSE` for more information.
