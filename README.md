# APO_Softwart

One of my first serious project. It's a simple image processing software, which allow to show histogram, reduce grayscale or stretch histogram.

First of all, I rebuild adding images system. In first version we could make operations in only one image in one window. Now you can add as many images as you can and make operations on all of them.

  ![ezgif com-video-to-gif](https://github.com/JakubKosakowski/APO_Software/assets/67673985/b37b9efc-ae14-43c2-8850-81ecd986e1fd)

The next things are operations. In first version you could show histogram and... Well, you could only show histogram. Now, the application has:
- Two types of histogram

  ![ezgif com-video-to-gif (1)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/4db97233-c6dd-4ace-a81e-ce70496419a9)
- Negation

  ![ezgif com-video-to-gif (2)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/cbb29b62-f3af-4f6e-9e61-49f487b3257b)
- Threshold

  ![ezgif com-video-to-gif (3)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/85eefbe3-2bc2-47c4-a453-f64ae68c2064)
- Go back to default image

  ![ezgif com-video-to-gif (4)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/f648d392-3dda-4919-b681-d6b5c7a0068f)
- Threshold with grayscale

  ![ezgif com-video-to-gif](https://github.com/JakubKosakowski/APO_Software/assets/67673985/8f0d8665-98db-45cf-83ed-c6a782ac04cd)
- Binarization

  ![ezgif com-video-to-gif (1)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/dfcf1344-ef04-4ae5-8bcd-2bc6d1fb3d89)
- Histogram stretching
  
  ![ezgif com-video-to-gif (4)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/28a3bbb3-1b66-4f8f-9743-f562059187db)
- Posterization

  ![ezgif com-video-to-gif (3)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/67553936-9a00-4032-9a95-b83c9adf14df)
- Equalization

  ![ezgif com-video-to-gif (5)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/26748f1d-0537-463e-abb8-f8692eb7c058)
- Blur linear smoothing

  ![ezgif com-video-to-gif (6)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/97b4021b-3cf4-41b1-85d0-1d14033f28ac)
- Gaussian Blur linear smoothing

  ![ezgif com-video-to-gif (7)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/dd3545fa-91ff-42d9-95ee-ea49063847d6)
- Laplacian edge detection

  ![ezgif com-video-to-gif (8)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/10aa187b-6b65-44e1-b1db-1ca074ea5ecc)
- Sobel edge detection

  ![ezgif com-video-to-gif](https://github.com/JakubKosakowski/APO_Software/assets/67673985/63185e10-fba7-4cc9-b616-7ccb2d0afbb1)
- Canny edge detection

  ![ezgif com-video-to-gif (1)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/5e5d5135-4ba7-4787-b227-c1e4cec07b25)
- Linear defuzzification with 3 Laplacian masks

  ![ezgif com-video-to-gif (2)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/9ab9d10b-eea3-44f9-a6be-de1e8146b4cb)
- Directional edge detection with 8 basic Prewitt masks

  ![ezgif com-video-to-gif (3)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/1971d312-f37f-4b5d-a268-b1ae07aaec03)
- Edge detecion with user mask

  ![ezgif com-video-to-gif (4)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/8b9430fd-32db-4db7-b44f-278c577be747)
- Median blur

  ![ezgif com-video-to-gif (6)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/49eb637d-54be-4739-a2c4-655aafeef19d)
- Add, Subtract and Blend two images

  ![ezgif com-video-to-gif](https://github.com/JakubKosakowski/APO_Software/assets/67673985/8340bcdc-c0a6-4b60-bc49-e936b73cf1da)
- Logical operations with two images

  ![ezgif com-video-to-gif (1)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/c039652d-7e5a-4ffb-a4c4-e6d5bf3969f0)
- Morphology operations (ERODE, DILATE, OPEN, CLOSE) with two structure elements (DIAMOND 4X4, SQUARE 8X8)

  ![ezgif com-video-to-gif (2)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/b5a98708-17f1-41ae-840c-4643950f5de9)
- Skeletonize

  ![ezgif com-video-to-gif (3)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/50616360-5383-4e3b-9924-bf2f7ef63520)
- Two stage filter

  ![ezgif com-video-to-gif (4)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/ede030d9-819f-46a2-a4d4-a5609c6b8652)
- Otsu and adaptive thresholding

  ![ezgif com-video-to-gif (5)](https://github.com/JakubKosakowski/APO_Software/assets/67673985/67028387-faa6-41cb-9a9a-531f48ab1a0a)
# How to run APO_Software
```
$ git clone https://github.com/JakubKosakowski/APO_Software.git

$ cd APO_Software

$ python -m venv venv

$ venv\Scripts\activate.bat

$ pip install -r requirements.txt

$ python main_window.py
```
